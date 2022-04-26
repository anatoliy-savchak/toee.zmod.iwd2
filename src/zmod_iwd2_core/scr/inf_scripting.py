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
		return (npc, ctrl)

	def _hp(self, obj_name):
		obj, ctrl = self._get_ie_object(obj_name)
		result = 0
		if obj:
			result = obj.stat_level_get(toee.stat_hp_current)
		return result

	def iGlobal(self, name, area, value):
		""" 
		0x400F Global(S:Name*,S:Area*,I:Value*)
		Returns true only if the variable with name 1st parameter of type 2nd parameter has value 3rd parameter.
		"""
		global_value = self._ensure_global(name, area)
		return global_value == value

	def iGlobalGT(self, name, area, value):
		""" 
		0x4034 GlobalGT(S:Name*,S:Area*,I:Value*)
		See Global(S:Name*,S:Area*,I:Value*) except the variable must be greater than the value specified to be true.
		"""
		global_value = self._ensure_global(name, area)
		return global_value > value

	def iGlobalLT(self, name, area, value):
		""" 
		0x4035 GlobalLT(S:Name*,S:Area*,I:Value*)
		As above except for less than.
		"""
		global_value = self._ensure_global(name, area)
		return global_value < value

	#@dump_args
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


	def iSubrace(self, obj_name, subrace_names):
		""" 
		0x40CD SubRace(O:Object*,I:SubRace*SubRace)
		"""
		# TODO
		return False

	def iRace(self, obj_name, subrace_names):
		""" 
		0x4017 Race(O:Object*,I:Race*Race)
		Returns true only if the Race of the specified object is the same as that specified by the 2nd parameter.
		"""
		# TODO
		return False
	
	def iHP(self, obj_name, hp):
		""" 
		0x4010 HP(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are equal to the 2nd parameter.
		"""
		return self._hp(obj_name) == hp
	
	def iHPGT(self, obj_name, hp):
		""" 
		00x4011 HPGT(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are greater than the 2nd parameter.
		"""
		return self._hp(obj_name) > hp
	
	def iHPLT(self, obj_name, hp):
		""" 
		0x4012 HPLT(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are less than the 2nd parameter.
		"""
		return self._hp(obj_name) < hp
	
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

	def iFadeToColor(self, point_str, value):
		""" 
		202 FadeToColor(P:Point*,I:Blue*) Variants: [BG1/BG2/BGEE/IWD1/IWD2] [PST]
		This action will fade the screen. The point parameter is given in [x.y] format with the x coordinate specifying the number of AI 
		updates (which default to 15 per second) to take to complete the fade action.
		"""
		# do nothing
		return

	def iFadeFromColor(self, point_str, value):
		""" 
		203 FadeFromColor(P:Point*,I:Blue*) Variants: [BG1/BG2/BGEE/IWD1/IWD2] [PST]
		This action will unfade the screen. The point parameter is given in [x.y] format with the x coordinate specifying 
		the number of AI updates (which default to 15 per second) to take to complete the fade action.
		"""
		# do nothing
		return

	def iAddXpVar(self, difficulty_str, value):
		""" 
		238 AddXPVar(S:VarTableEntry*,I:Strref*) Variants: [IWD1/IWD2] 
		"""
		utils_pc.pc_award_experience_party(value, 1) # TODO verify that it's per party
		return

	def iRestUntilHealed(self):
		""" 
		258 RestUntilHealed() Variants: [IWD1/IWD2] [BG1/BG2/BGEE/PST]
		This action rests the party until all PCs are fully healed. Healing Spells are cast by the party at the start of each rest period except the first.
		"""
		# TODO TEMPLE+
		return

	def iGiveItemCreate(self, proto, target_obj_name, usage1 = 0, usage2 = 0, usage3 = 0):
		""" 
		140 GiveItemCreate(S:ResRef*,O:Object*,I:Usage1*,I:Usage2*,I:Usage3*)
		This action creates the item specified by the resref parameter on the creature specified by the object parameter, with quantity/charges controlled by the usage parameters. 
		"""
		target, ctrl = self._get_ie_object(target_obj_name)
		if target:
			if isinstance(proto, str):
				if proto == "Misc07": # gold
					utils_pc.pc_party_receive_money_and_print(usage1 * const_toee.gp)
			else:
				item = utils_item.item_create_in_inventory2(proto, target, 0, None)

		# TODO
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

	def iNumTimesTalkedTo(self, num):
		""" 
		0x4039 NumTimesTalkedTo(I:Num*)

		Returns true only if the player's party has spoken to the active CRE the exact number of times specified.
		NB. NumTimesTalkedTo seems to increment when a PC initiates conversion with an NPC, or an NPC initiates conversation with a PC.
		NumTimesTalkedTo does not seem to increment for force-talks, interactions, interjections and self-talking.
		"""
		npc = self._gnpc()
		triggerer = self._gtriggerer()
		result = npc.has_met(triggerer)
		print("has_met = {} for {} to {}".format(result, npc, triggerer))
		if num:
			if num > 1: 
				print("{} ({}) -- num is greater than 1, not supported!".format(inspect.stack()[0][3]), num)
				debug.breakp("")
			result = not result
		return result == num

	def iNumTimesTalkedToGT(self, num):
		""" 
		0x403A NumTimesTalkedToGT(I:Num*)
		Returns true only if the player's party has spoken to the active CRE more than the number of times specified.
		"""
		npc = self._gnpc()
		triggerer = self._gtriggerer()
		result = npc.has_met(triggerer)
		print("has_met = {} for {} to {}".format(result, npc, triggerer))
		if num:
			if num > 1: 
				print("{} ({}) -- num is greater than 1, not supported!".format(inspect.stack()[0][3]), num)
				debug.breakp("")
		result = int(result) > num
		return result

	def iGiveItem(self, proto, target_obj_name):
		""" 
		15 GiveItem(S:Object*,O:Target*)
		This action instructs the active creature to give the specified item (parameter 1) to the specified 
		target (parameter 2). The active creature must possess the item to pass it. 
		"""
		target, ctrl = self._get_ie_object(target_obj_name)
		if target:
			npc = self._gnpc()
			item = npc.item_find_by_proto(proto)
			if item:
				target.item_get(item)
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
