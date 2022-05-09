import toee, debug
import ctrl_behaviour, inf_scripting, ctrl_daemon, utils_storage

__metaclass__ = type

class CtrlBehaviourIE(ctrl_behaviour.CtrlBehaviourAI, inf_scripting.InfScriptSupportNPC):
	def _gnpc(self):
		attachee = self.vars["attachee"]
		assert isinstance(attachee, toee.PyObjHandle)
		return attachee

	def _gtriggerer(self):
		triggerer = self.vars["triggerer"]
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
		
		return toee.SKIP_DEFAULT

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