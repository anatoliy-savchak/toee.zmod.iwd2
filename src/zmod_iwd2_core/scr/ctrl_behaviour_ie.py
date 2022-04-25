import toee, debug
import ctrl_behaviour, inf_scripting, ctrl_daemon

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
		if area.lower() == "area":
			return ctrl_daemon.CtrlDaemon.get_current_daemon()._get_globals(area)
		return super(CtrlBehaviourIE, self)._get_globals(area)

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		
		try:
			self.vars["attachee"] = attachee
			self.vars["triggerer"] = triggerer
			
			self.script_dialog(attachee, triggerer)
			print("debug after self.script_dialog(attachee, triggerer)")
		finally:
			self.vars["attachee"] = None
			self.vars["triggerer"] = None
		
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
