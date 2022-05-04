import toee
import debug
import inspect, itertools
import utils_storage
import utils_inf
import utils_pc
import utils_item
import const_toee

__metaclass__ = type

def get_globals():
	data = utils_storage.obj_storage_by_id("globals").data
	#result = data.get("globals")
	#if result is None:
	#	result = dict()
	#	data["globals"] = result
	return data #result

# from inf_scripting import *
# gv("Hedron_Quest")
def gv(name): return get_globals().get(name, 0)
# gvs("Hedron_Quest", 1)
def gvs(name, value): get_globals()[name] = value

def dump_args(func):
	"This decorator dumps out the arguments passed to a function before calling it"
	argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
	fname = func.func_name

	def echo_func(*args,**kwargs):
		r = "error!"
		try:
			r = func(*args, **kwargs)
		finally:
			line = '{}({})={}'.format(fname, ', '.join('%s=%r' % entry for entry in zip(argnames,args) + kwargs.items()), r)
			print(line)
		return r
	return echo_func

class InfScriptSupport:
	def _gnpc(self):
		return toee.PyObjHandle()

	def _get_globals(self, area):
		if area.lower() == "global":
			return get_globals()

		raise Exception("globals of {} nof supported!!".format(area))
		return dict()

	def _ensure_global(self, name, area):
		g = self._get_globals(area)
		v = g.get(name)
		assert isinstance(v, int)
		if v is None:
			g[name] = 0
			v = 0
		return v

	def _set_global(self, name, area, value):
		g = self._get_globals(area)
		g[name] = value
		return

	def _get_ie_object(self, name):
		# returns (npc, ctrl) if known
		# see object.ids
		_name = name.lower()
		npc = None
		ctrl = None
		if _name == "myself":
			npc = self._gnpc()
			ctrl = self
		elif _name == "protagonist": # not sure, maybe either a leader or first PC TODO
			npc = self._gnpc()
			ctrl = self
		else:
			err = "Unknown objname: {}".format(name)
			print(err)
			debug.breakp("_get_ie_object")
		return (npc, ctrl)

	def _hp(self, obj_name):
		obj, ctrl = self._get_ie_object(obj_name)
		result = 0
		if obj:
			result = obj.stat_level_get(toee.stat_hp_current)
		return result

	def _skill(self, obj_name, skill_name):
		obj, ctrl = self._get_ie_object(obj_name)
		result = 0
		if obj:
			stat = utils_inf.iwd2_skill_convert(skill_name)
			if not stat is None:
				result = obj.stat_level_get(stat)
		return result

	def _get_proto(self, item_name):
		if isinstance(item_name, int):
			return int(item_name)
		err = "Unknown item: {}".format(item_name)
		print(err)
		debug.breakp("_get_proto")
		return None

	############# TRIGGERS

	@dump_args
	def iGlobal(self, name, area, value):
		""" 
		0x400F Global(S:Name*,S:Area*,I:Value*)
		Returns true only if the variable with name 1st parameter of type 2nd parameter has value 3rd parameter.
		"""
		global_value = self._ensure_global(name, area)
		return global_value == value

	@dump_args
	def iGlobalGT(self, name, area, value):
		""" 
		0x4034 GlobalGT(S:Name*,S:Area*,I:Value*)
		See Global(S:Name*,S:Area*,I:Value*) except the variable must be greater than the value specified to be true.
		"""
		global_value = self._ensure_global(name, area)
		return global_value > value

	@dump_args
	def iGlobalLT(self, name, area, value):
		""" 
		0x4035 GlobalLT(S:Name*,S:Area*,I:Value*)
		As above except for less than.
		"""
		global_value = self._ensure_global(name, area)
		return global_value < value

	@dump_args
	def iSetGlobal(self, name, area, value):
		""" 
		30 SetGlobal(S:Name*,S:Area*,I:Value*)
		This action sets a variable (specified by name) in the scope (specified by area) to the value (specified by value).
		"""
		print("setting {} {} = {}".format(area, name, value))
		self._set_global(name, area, value)
		g = self._get_globals(area)
		print("got {} {} = {}".format(area, name, g[name]))
		return


	@dump_args
	def iSubRace(self, obj_name, subrace_names):
		""" 
		0x40CD SubRace(O:Object*,I:SubRace*SubRace)
		"""
		# IMPROVE
		race_name = subrace_names.split("_", 1)[0]
		return self.iRace(obj_name, race_name)

	@dump_args
	def iSubrace(self, obj_name, subrace_names): return self.iSubRace(obj_name, subrace_names)

	@dump_args
	def iRace(self, obj_name, race_names):
		""" 
		0x4017 Race(O:Object*,I:Race*Race)
		Returns true only if the Race of the specified object is the same as that specified by the 2nd parameter.
		"""
		# IMPROVE
		race_id = utils_inf.iwd2_race_convert(race_names)
		if not race_id is None:
			obj, ctrl = self._get_ie_object(obj_name)
			if obj:
				orace = obj.obj_get_int(toee.obj_f_critter_race)
				return race_id == orace
		return False
	
	@dump_args
	def iHP(self, obj_name, hp):
		""" 
		0x4010 HP(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are equal to the 2nd parameter.
		"""
		return self._hp(obj_name) == hp
	
	@dump_args
	def iHPGT(self, obj_name, hp):
		""" 
		00x4011 HPGT(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are greater than the 2nd parameter.
		"""
		return self._hp(obj_name) > hp
	
	@dump_args
	def iHPLT(self, obj_name, hp):
		""" 
		0x4012 HPLT(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are less than the 2nd parameter.
		"""
		return self._hp(obj_name) < hp
	
	@dump_args
	def iClassEx(self, obj_name, classname):
		""" 
		0x4098 ClassEx(O:Object*,I:Class*class*)
		As Class(), except ClassEx() also returns true if the specified object is multi-classed.
		"""
		toee_class = utils_inf.iwd2_classname_to_class(classname)
		npc, ctrl = self._get_ie_object(obj_name)
		if npc:
			cc = npc.get_character_classes()
			if toee_class in cc:
				return True
		return False
	
	@dump_args
	def iCheckStatLT(self, obj_name, value, statname):
		""" 
		0x4046 CheckStatLT(O:Object*,I:Value*,I:StatNum*Stats)
		Returns true only if the specified object has the statistic in the 3rd parameter less than the value of the 2nd parameter.
		"""
		tup = utils_inf.iwd2_stat_convert(statname)
		if tup:
			npc, ctrl = self._get_ie_object(obj_name)
			if npc:
				level = npc.stat_level_get(tup[0])
				return level < value
		return False
	
	@dump_args
	def iCheckStatGT(self, obj_name, value, statname):
		""" 
		0x4045 CheckStatGT(O:Object*,I:Value*,I:StatNum*Stats)
		Returns true only if the specified object has the statistic in the 3rd parameter greater than the value of the 2nd parameter.
		"""
		tup = utils_inf.iwd2_stat_convert(statname)
		if tup:
			npc, ctrl = self._get_ie_object(obj_name)
			if npc:
				level = npc.stat_level_get(tup[0])
				return level > value
		return False

	@dump_args
	def iCheckSkill(self, obj_name, value, statname):
		""" 
		0x40E6 CheckSkill(O:Object*,I:Value*,I:SkillNum*Skills)
		"""
		return self._skill(obj_name, statname) == value

	@dump_args
	def iCheckSkillGT(self, obj_name, value, statname):
		""" 
		0x40E7 CheckSkillGT(O:Object*,I:Value*,I:SkillNum*Skills)
		"""
		return self._skill(obj_name, statname) > value

	@dump_args
	def iCheckSkillLT(self, obj_name, value, statname):
		""" 
		0x40E8 CheckSkillLT(O:Object*,I:Value*,I:SkillNum*Skills)
		"""
		return self._skill(obj_name, statname) < value

	@dump_args
	def iKit(self, obj_name, statname):
		""" 
		0x40BB Kit(O:Object*,I:Kit*KIT)
		NT Returns true only if the specified object is of the kit specified.
		NB. A creature's assigned kit is stored as a dword, however the Kit() trigger only checks the upper word. 
		This, in conjunction with various incorrect values in the game cre files, and an incorrect kits.ids file, 
		means the Kit() trigger can often fail. For optimal usage, the default kit.ids file should be replaced 
		with the updated one listed in the BG2: ToB ids page.
		"""

		result = False
		npc, ctrl = self._get_ie_object(obj_name)
		if npc:
			result = utils_inf.iwd2_kit_has(statname, npc)
		return result

	@dump_args
	def iAlignment(self, obj_name, statname, value):
		""" 
		0x400A Alignment(O:Object*,I:Alignment*Align)
		Returns true only if the alignment of the specified object matches that in the second parameter.
		"""

		result = False
		npc, ctrl = self._get_ie_object(obj_name)
		if npc:
			v = npc.obj_get_int(toee.obj_f_critter_alignment)
			result = utils_inf.iwd2_alignment_equals(statname, npc)
		return result

	@dump_args
	def iPartyHasItem(self, item_name):
		""" 
		0x4042 PartyHasItem(S:Item*)
		Returns true if any of the party members have the specified item in their inventory. This trigger also checks with container items (e.g. Bags of Holding).
		"""

		result = False
		proto = self._get_proto(item_name)
		if not proto is None:
			result = toee.anyone(toee.game.party, "item_find_by_proto", proto)
		return result

	@dump_args
	def iHasItem(self, item_name, obj_name):
		""" 
		0x4061 HasItem(S:ResRef*,O:Object*)
		Returns true only if the specified object has the specified item in its inventory. This trigger also checks with container items (e.g. Bags of Holding).
		"""
		npc, ctrl = self._get_ie_object(obj_name)
		if npc:
			npc = self._gnpc()
			proto = self._get_proto(item_name)
			item = npc.item_find_by_proto(proto)
			return item != None
		return

	############# ACTIONS

	@dump_args
	def iFadeToColor(self, point_str, value):
		""" 
		202 FadeToColor(P:Point*,I:Blue*) Variants: [BG1/BG2/BGEE/IWD1/IWD2] [PST]
		This action will fade the screen. The point parameter is given in [x.y] format with the x coordinate specifying the number of AI 
		updates (which default to 15 per second) to take to complete the fade action.
		"""
		# do nothing
		return

	@dump_args
	def iFadeFromColor(self, point_str, value):
		""" 
		203 FadeFromColor(P:Point*,I:Blue*) Variants: [BG1/BG2/BGEE/IWD1/IWD2] [PST]
		This action will unfade the screen. The point parameter is given in [x.y] format with the x coordinate specifying 
		the number of AI updates (which default to 15 per second) to take to complete the fade action.
		"""
		# do nothing
		return

	@dump_args
	def iAddXpVar(self, difficulty_str, value):
		""" 
		238 AddXPVar(S:VarTableEntry*,I:Strref*) Variants: [IWD1/IWD2] 
		"""
		utils_pc.pc_award_experience_party(value, 1) # TODO verify that it's per party
		return

	@dump_args
	def iRestUntilHealed(self):
		""" 
		258 RestUntilHealed() Variants: [IWD1/IWD2] [BG1/BG2/BGEE/PST]
		This action rests the party until all PCs are fully healed. Healing Spells are cast by the party at the start of each rest period except the first.
		"""
		# TODO TEMPLE+
		return

	@dump_args
	def iGiveItemCreate(self, item_name, obj_name, usage1 = 0, usage2 = 0, usage3 = 0):
		""" 
		140 GiveItemCreate(S:ResRef*,O:Object*,I:Usage1*,I:Usage2*,I:Usage3*)
		This action creates the item specified by the resref parameter on the creature specified by the object parameter, with quantity/charges controlled by the usage parameters. 
		"""
		npc, ctrl = self._get_ie_object(obj_name)
		if npc:
			proto = self._get_proto(item_name)
			#if isinstance(proto, str):
			#	if proto == "Misc07": # gold
			#		utils_pc.pc_party_receive_money_and_print(usage1 * const_toee.gp)
			if not proto is None:
				item_obj = utils_item.item_create_in_inventory2(proto, npc, 0, None)
			#else:
			#	item = utils_item.item_create_in_inventory2(proto, target, 0, None)

		# TODO
		return

	@dump_args
	def iSetCriticalPathObject(self, obj_name, value):
		""" 
		283 SetCriticalPathObject(O:Object*,I:Critical*Boolean) Variants: [IWD2] [BG1/BG2/BGEE/IWD1/PST]
		This action sets the Critical Path flag on the specified objects to the specified value. The game ends if a creature with the Critical Path flag set is killed.
		"""
		npc, ctrl = self._get_ie_object(obj_name)
		if ctrl:
			ctrl.vars["critical_path"] = value
		return

	@dump_args
	def iTakePartyItemNum(self, item_name, num):
		""" 
		204 TakePartyItemNum(S:ResRef*,I:Num*) Variants: [BG1/BG2/BGEE/IWD2] [IWD1/PST]
		This action will remove a number of instances (specified by the Num parameter) of the specified item from the party. 
		The items will be removed from players in order, for example; Player1 has 3 instances of “MYITEM” in their inventory, 
		Player2 has 2 instance of “MYITEM,” and Player3 has 1 instance. If the action TakePartyItemNum(“MYITEM”, 4) is run, 
		all 3 instances of “MYITEM” will be taken from Player1, and 1 instance will be taken from Player2. 
		This leaves Player2 and Player3 each with one instance of “MYITEM.” If the last item of an item type stored in a container 
		STO file is removed by this action, the amount becomes zero. Items with zero quantities cannot be seen in-game, 
		cannot be removed by TakePartyItem, and will not count toward a container’s current item load. 
		If the item to be taken is in a stack, and the stack is in a quickslot, the item will be removed, and the remaining stack will be placed in the inventory. 
		If the inventory is full, the stack item will be dropped on the ground.
		"""

		proto = self._get_proto(item_name)
		if not proto is None:
			for pc in toee.game.party:
				while num:
					item = pc.item_find_by_proto(proto)
					if item:
						item.destroy()
						num = num - 1
				if not num:
					break
		return


class InfScriptSupportNPC(InfScriptSupport):
	def _gtriggerer(self):
		return toee.PyObjHandle()

	def _get_globals(self, area):
		if area.lower() == "locals":
			result = self.vars.get("locals")
			if result is None:
				result = dict()
				self.vars["locals"] = result
			return result

		return super(InfScriptSupportNPC, self)._get_globals(area)

	@dump_args
	def iNumTimesTalkedTo(self, num):
		""" 
		0x4039 NumTimesTalkedTo(I:Num*)

		Returns true only if the player's party has spoken to the active CRE the exact number of times specified.
		NB. NumTimesTalkedTo seems to increment when a PC initiates conversion with an NPC, or an NPC initiates conversation with a PC.
		NumTimesTalkedTo does not seem to increment for force-talks, interactions, interjections and self-talking.
		"""
		#npc = self._gnpc()
		#triggerer = self._gtriggerer()
		#result = npc.has_met(triggerer)
		result = self.has_met()
		if num:
			if num > 1: 
				print("{} ({}) -- num is greater than 1, not supported!".format(inspect.stack()[0][3]), num)
				debug.breakp("")
			result = not result
		return result == num

	@dump_args
	def iNumTimesTalkedToGT(self, num):
		""" 
		0x403A NumTimesTalkedToGT(I:Num*)
		Returns true only if the player's party has spoken to the active CRE more than the number of times specified.
		"""
		#npc = self._gnpc()
		#triggerer = self._gtriggerer()
		#result = npc.has_met(triggerer)
		result = self.has_met()
		#print("has_met = {} for {} to {}".format(result, npc, triggerer))
		if num:
			if num > 1: 
				print("{} ({}) -- num is greater than 1, not supported!".format(inspect.stack()[0][3]), num)
				debug.breakp("")
		result = int(result) > num
		return result

	@dump_args
	def iGiveItem(self, item_name, target_obj_name):
		""" 
		15 GiveItem(S:Object*,O:Target*)
		This action instructs the active creature to give the specified item (parameter 1) to the specified 
		target (parameter 2). The active creature must possess the item to pass it. 
		"""
		target, ctrl = self._get_ie_object(target_obj_name)
		if target:
			npc = self._gnpc()
			proto = self._get_proto(item_name)
			item = npc.item_find_by_proto(proto)
			if item:
				target.item_get(item)
		return

	@dump_args
	def iDestroyItem(self, item_name):
		""" 
		169 DestroyItem(S:ResRef*)
		This action removes a single instance of the specified item from the active creature, unless the item exists in a stack, 
		in which case the entire stack is removed. The example script is from ar1000.bcs.
		"""
		npc = self._gnpc()
		proto = self._get_proto(item_name)
		item = npc.item_find_by_proto(proto)
		if item:
			item.destroy()
		return

class InfScriptSupportDaemon(InfScriptSupport):
	def _get_globals(self, area):
		if area.lower() == "area":
			result = self.vars.get("area_globals")
			if result is None:
				result = dict()
				self.vars["area_globals"] = result
			return result

		return super(InfScriptSupportDaemon, self)._get_globals(area)
