import toee
import ctrl_daemon, ctrl_daemon2
import inf_scripting
import ctrl_behaviour_ie
import monster_info
import sys
import uuid

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

		
def _timed(args):
	map = args["map"]
	if map != toee.game.leader.map:
		return
	ctrl = ctrl_daemon.gdc()
	if not ctrl:
		return
	ctrl.do_timed(args)
	return

class CtrlDaemonIE(ctrl_daemon2.CtrlDaemon2, inf_scripting.InfScriptSupportDaemon):
	def __init__(self):
		super(CtrlDaemonIE, self).__init__()

		self.ambients = list()
		self.timer_context = str(uuid.uuid4())
		self.script_vars = dict()
		return

	def create_npc_at(self, npc_loc, ctrl_class, rot, code_name, no_draw = 1, no_kos = 1, no_move = 0):
		npc, ctrl = super(ctrl_daemon2.CtrlDaemon2, self).create_npc_at(npc_loc, ctrl_class, rot, "", code_name, None, no_draw, no_kos, no_move)

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

	def create_cabbage(self, loc, ctrl_class, alias):
		npc, ctrl = ctrl_class.create_obj_and_class(loc)
		if (npc):
			npc.move(loc)
			if alias:
				ctrl.set_alias(alias, npc)
		return npc, ctrl

	def ambs_timer_start(self): 
		args = {"map": toee.game.leader.map, "timer_context": self.timer_context}
		toee.game.timevent_add(_timed, (args), 1000, 1) # 1000 = 1 second
		return

	def do_timed(self, args):
		if args["timer_context"] != self.timer_context:
			return
		for amb in self.ambients:
			amb.tick()
		self.ambs_timer_start()
		return

	# Storage events
	def storage_data_loaded(self):
		super(CtrlDaemonIE, self).storage_data_loaded()

		self.timer_context = str(uuid.uuid4())
		self.ambs_timer_start()
		return

	def switch_dialog(self, pc, actor_name, state):
		npc, ctrl = self._get_ie_object("'{}'".format(actor_name))
		if npc and ctrl:
			ctrl.start_dialog_at_state(npc, pc, state)
		else:
			raise Exception('Actor {} not found!'.format(actor_name))
		return

	def delete_obsolate_controls(self):
		# this is forbidden in IWD2 game!
		return

	def validate_minfo(self):
		# this is forbidden in IWD2 game!
		return

	def run_daemon_script(self, on_creation = False):
		return

	# Sleep interface
	def can_sleep(self):
		return toee.SLEEP_IMPOSSIBLE

	def place_encounters_initial(self):
		self.setup_ambients()
		self.place_npcs()
		return

	def setup_ambients(self):
		self.setup_ambients_auto()
		return

	def setup_ambients_auto(self):
		return

	def place_npcs(self):
		self.place_npcs_auto()
		return

	def place_npcs_auto(self):
		return

	def ambients_tick(self):
		for handler in self.ambients:
			handler.tick()
		return

	def heartbeat(self, npc):
		#print("CtrlTargosDocks heartbeat")
		return
