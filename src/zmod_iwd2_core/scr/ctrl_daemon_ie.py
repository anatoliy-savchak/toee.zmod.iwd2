import toee
import ctrl_daemon, ctrl_daemon2
import inf_scripting
import ctrl_behaviour_ie

class CtrlDaemonIE(ctrl_daemon2.CtrlDaemon2, inf_scripting.InfScriptSupportDaemon):

	def create_npc_at(self, npc_loc, ctrl_class, rot, code_name, no_draw = 1, no_kos = 1, no_move = 0):
		npc, ctrl = super(ctrl_daemon2.CtrlDaemon2, self).create_npc_at(npc_loc, ctrl_class, rot, "", code_name, ctrl_class.get_class_faction(), no_draw, no_kos, no_move)

		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(ctrl, ctrl_behaviour_ie.CtrlBehaviourIE)

		ctrl.set_alias(code_name, npc)
		return npc, ctrl
