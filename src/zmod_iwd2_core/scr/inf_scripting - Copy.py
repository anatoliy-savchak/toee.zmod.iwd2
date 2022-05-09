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

def strip_quotes(s, notify = False):
	if s and (s[0] == "'" or s[0] == '"'):
		r = s.strip()
		r = r[1:-1]
		if notify:
			return r, s[0]
		else:
			return r
	else:
		if notify:
			return s, None
		else:
			return s
	return

class InfScriptSupport:
	def _gnpc(self):
		return toee.PyObjHandle()

	def _get_globals(self, area):
		area = strip_quotes(area)
		if area.lower() == "global":
			return get_globals()

		raise Exception("globals of {} nof supported!!".format(area))
		return dict()

	def _ensure_global(self, name, area):
		name = strip_quotes(name)
		g = self._get_globals(area)
		v = g.get(name)
		assert isinstance(v, int)
		if v is None:
			g[name] = 0
			v = 0
		return v

	def _set_global(self, name, area, value):
		name = strip_quotes(name)
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

	############# ACTIONS

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

class InfScriptSupportDaemon(InfScriptSupport):
	def _get_globals(self, area):
		if area.lower() == "area":
			result = self.vars.get("area_globals")
			if result is None:
				result = dict()
				self.vars["area_globals"] = result
			return result

		return super(InfScriptSupportDaemon, self)._get_globals(area)

class ScriptBase(object):
	@classmethod
	def execute(cls, self):
		assert isinstance(self, InfScriptSupport)

		cls.do_execute(self)
		return

	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, InfScriptSupport)
		return
