import toee
import debug
import inspect
import utils_storage

__metaclass__ = type

def get_globals():
	return utils_storage.obj_storage_by_id("globals").data

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
		result = int(self._gnpc().has_met(self._gtriggerer()))
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
		result = not self._gnpc().has_met(self._gtriggerer())
		if num:
			if num > 1: 
				print("{} ({}) -- num is greater than 1, not supported!".format(inspect.stack()[0][3]), num)
				debug.breakp("")
		result = int(result) > num
		return result

class InfScriptSupportDaemon(InfScriptSupport):
	def _get_globals(self, area):
		if area.lower() == "area":
			result = self.vars.get("area_globals")
			if result is None:
				result = dict()
				self.vars["area_globals"] = result
			return result

		return super(InfScriptSupportDaemon, self)._get_globals(area)
