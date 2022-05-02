import toee
import ctrl_daemon, ctrl_daemon2
import inf_scripting
import ctrl_behaviour_ie
import monster_info
import sys

class global_injector:
	'''Inject into the *real global namespace*, i.e. "builtins" namespace or "__builtin__" for python2.
	Assigning to variables declared global in a function, injects them only into the module's global namespace.
	>>> Global= sys.modules['__builtin__'].__dict__
	>>> #would need 
	>>> Global['aname'] = 'avalue'
	>>> #With
	>>> Global = global_injector()
	>>> #one can do
	>>> Global.bname = 'bvalue'
	>>> #reading from it is simply
	>>> bname
	bvalue

	'''
	def __init__(self):
		try:
			self.__dict__['builtin'] = sys.modules['__builtin__'].__dict__
		except KeyError:
			self.__dict__['builtin'] = sys.modules['builtins'].__dict__
	def __setattr__(self,name,value):
		self.builtin[name] = value
	def set_name(self, name, value):
		self.builtin[name] = value

class CtrlDaemonIE(ctrl_daemon2.CtrlDaemon2, inf_scripting.InfScriptSupportDaemon):
	def __init__(self):
		super(CtrlDaemonIE, self).__init__()

		self.ambients = list()
		return

	def create_npc_at(self, npc_loc, ctrl_class, rot, code_name, no_draw = 1, no_kos = 1, no_move = 0):
		npc, ctrl = super(ctrl_daemon2.CtrlDaemon2, self).create_npc_at(npc_loc, ctrl_class, rot, "", code_name, ctrl_class.get_class_faction(), no_draw, no_kos, no_move)

		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(ctrl, ctrl_behaviour_ie.CtrlBehaviourIE)

		ctrl.set_alias(code_name, npc)
		return npc, ctrl

	def debug_glob_npcs(self):
		gi = global_injector()
		for m in self.monsters.itervalues():
			assert isinstance(m, monster_info.MonsterInfo)
			npc = m.get_npc()
			if npc:
				global_name = "npc_{}".format(m.name)
				gi.set_name(global_name, npc)
				#exec_line = "global {}\n{} = toee.game.get_obj_by_id('{}')".format(global_name, global_name, m.id)
				#print(exec_line)
				#exec(exec_line)
		return

	def create_ambient(self, loc, ctrl_class, alias):
		npc, ctrl = ctrl_class.create_obj_and_class(loc)
		if (npc):
			npc.move(loc)
			if alias:
				ctrl.set_alias(alias, npc)
		return npc, ctrl
