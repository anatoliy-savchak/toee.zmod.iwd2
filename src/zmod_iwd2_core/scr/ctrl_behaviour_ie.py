import toee, debug
import ctrl_behaviour, inf_scripting, ctrl_daemon, utils_storage

__metaclass__ = type

class CtrlBehaviourIE(ctrl_behaviour.CtrlBehaviourAI, inf_scripting.InfScriptSupportNPC):
	def __init__(self):
		super(CtrlBehaviourIE, self).__init__()

		self.script_vars = dict()
		return

	def __repr__(self):
		repr = self.vars.get("alias")
		if not repr:
			repr = self.id
		if not repr:
			repr = id(self)
		return '{}({})'.format(self.__class__.__name__, repr)

	def __str__(self):
		repr = self.vars.get("alias")
		if not repr:
			repr = self.id
		if not repr:
			repr = id(self)
		return '{}({})'.format(self.__class__.__name__, repr)

	def _gnpc(self):
		attachee = self.vars.get("attachee")
		if attachee is None:
			attachee = self.npc_get()
		assert isinstance(attachee, toee.PyObjHandle)
		return attachee

	def _gtriggerer(self):
		triggerer = self.vars.get("triggerer")
		assert isinstance(triggerer, toee.PyObjHandle)
		return triggerer

	def _get_globals(self, area):
		if area.lower() == "myarea" or area.lower() == "area":
			return ctrl_daemon.CtrlDaemon.get_current_daemon()._get_globals(area)
		return super(CtrlBehaviourIE, self)._get_globals(area)

	def _prepare_scripting(self, attachee = None, triggerer = None):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if attachee is None:
			attachee = self.npc_get()

		self.vars["attachee"] = attachee
		self.vars["triggerer"] = triggerer
		return

	def _unprepare_scripting(self):
		self.vars["attachee"] = None
		self.vars["triggerer"] = None
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		try:
			self._prepare_scripting(attachee, triggerer)
			
			line_id = self.script_dialog(attachee, triggerer)
			if not line_id is None and line_id >= 0:
				self.has_met_inc()
		finally:
			self._unprepare_scripting()
			self.script_vars['last_talked_to_id'] = attachee.id
		
		return toee.SKIP_DEFAULT

	@inf_scripting.dump_args
	def dialog_test(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		try:
			self.vars["attachee"] = npc
			self.vars["triggerer"] = pc
			
			result = self.dialog_test_do(npc, pc, index)
		finally:
			self.vars["attachee"] = None
			self.vars["triggerer"] = None
		
		return result

	@inf_scripting.dump_args
	def Enemy(self):
		self.set_allegiance(255)
		return

	def dialog_action(self, npc, pc, index):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		assert isinstance(index, int)
		
		try:
			self.vars["attachee"] = npc
			self.vars["triggerer"] = pc
			
			result = self.dialog_action_do(npc, pc, index)
		finally:
			self.vars["has_met"] = self.has_met() + 1
			self.vars["attachee"] = None
			self.vars["triggerer"] = None
		
		return result

	def critter_dying(self, attachee, triggerer):
		super(CtrlBehaviourIE, self).critter_dying(attachee, triggerer)
		if self.vars.get("critical_path"):
			# that critter should not die!
			# see iSetCriticalPathObject
			toee.game.moviequeue_play_end_game()
		return

	def has_met(self):
		result = self.vars.get("has_met")
		if result is None:
			result = 0
			self.vars["has_met"] = result
		return result

	def has_met_inc(self):
		result = self.vars.get("has_met")
		if result is None:
			result = 0
		result += 1
		self.vars["has_met"] = result
		return result

	def has_met_set(self, value):
		self.vars["has_met"] = value
		return self.vars["has_met"]

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		return toee.RUN_DEFAULT

	def setup_bcs(self):
		self.vars["bcs_general"] = None
		self.vars["bcs_class"] = None
		self.vars["bcs_combat"] = None
		self.vars["bcs_movement"] = None
		self.vars["bcs_team"] = None
		self.vars["bcs_special_one"] = None
		return

	def setup(self, npc):
		self.setup_bcs()
		super(CtrlBehaviourIE, self).setup(npc)
		return

	def get_dialog_trigger_max_index(self): return None

	def test_dialog_triggers(self, pc = None, specific_trigger_id_else_all = None):
		max_index = self.get_dialog_trigger_max_index()
		if not max_index:
			return 0

		npc = self.npc_get()
		if not specific_trigger_id_else_all is None:
			result = self.dialog_test(npc, toee.game.leader, specific_trigger_id_else_all)
			return 1

		for i in range(1, max_index+1):
			result = self.dialog_test(npc, toee.game.leader, i)

		return max_index

	def get_state_to_line(self, state): return

	def start_dialog_at_state(self, npc, pc, state):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)

		line_id = self.get_state_to_line(state)
		if line_id:
			pc.begin_dialog(npc, line_id)
		else:
			raise Exception('State {} not found as line!'.format(state))
		return

	def hide_creature(self, npc, hidden):
		assert isinstance(npc, toee.PyObjHandle)
		self.vars["hidden"] = hidden
		if npc:
			if hidden:
				npc.object_flag_set(toee.OF_DONTDRAW)
			else:
				npc.object_flag_unset(toee.OF_DONTDRAW)
		return

	def locus_make(self):
		return {'dameon_id': self.vars.get('dameon_id'), 'npc_id': self.id}

	def get_allegiance(self): 
		return self.vars.get('allegiance', self.get_allegiance_default())

	def set_allegiance(self, allegiance): 
		self.vars['allegiance'] = allegiance
		return

	def allegiance_update(self, npc):
		allegiance = self.get_allegiance()
		npc_leader = npc.leader_get()
		if npc_leader:
			lead_ctrl = ctrl_behaviour.get_ctrl(npc_leader.id)
			if lead_ctrl:
				lead_allegiance = lead_ctrl.get_allegiance()
				allegiance = lead_allegiance
				self.set_allegiance(lead_allegiance)
		
		kos = allegiance == 255
		if kos:
			npc.npc_flag_set(toee.ONF_KOS)
		else:
			npc.npc_flag_unset(toee.ONF_KOS)
		return