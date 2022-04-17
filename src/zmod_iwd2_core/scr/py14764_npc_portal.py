import toee
import const_toee
import const_proto_npc
import module_consts
import module_globals
import utils_obj
import ctrl_behaviour

MODULE_SCRIPT_ID = 14764

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)

class CtrlPortalOut(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_PORTAL_DOOR

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = self.get_dialog_script_id(npc)
		npc.obj_set_int(toee.obj_f_critter_flags2, const_toee.OCF2_NIGH_INVULNERABLE)
		npc.condition_add("Non_Combatant")
		#npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID skip this fix for now
		self.rotate_fix(npc)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		self.rotate_fix(attachee)
		line = self.get_dialog_line(attachee)
		print("line: {}, script: {}, class: {}".format(line, attachee.scripts[const_toee.sn_dialog], type(self).__name__))
		if (line):
			triggerer.begin_dialog(attachee, line)
		return toee.SKIP_DEFAULT

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		self.rotate_fix(attachee)
		return toee.RUN_DEFAULT

	def rotate_fix(self, npc):
		if (int(npc.rotation * 10000) != int(const_toee.rotation_0600_oclock * 10000)):
			print("Rotating {} from {} to {}".format(npc, npc.rotation, const_toee.rotation_0600_oclock))
			npc.rotation = const_toee.rotation_0600_oclock
			#npc.critter_flag_set(toee.OCF_STUNNED)
		return

	def get_dialog_line(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return self.get_dialog_line_cls(npc)

	@classmethod
	def get_dialog_line_cls(cls, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return 0

	def get_dialog_script_id(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return self.get_dialog_script_id_cls(npc)

	@classmethod
	def get_dialog_script_id_cls(cls, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return MODULE_SCRIPT_ID

class CtrlPortalOutImmediate(CtrlPortalOut):
	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		print("fade_and_teleport(0, 0, 0, {}, {}, {})...".format(self.get_dest_map(), self.get_dest_location()[0], self.get_dest_location()[1]))
		toee.game.fade_and_teleport(
			0, 0, 0, 
			self.get_dest_map(), 
			self.get_dest_location()[0], 
			self.get_dest_location()[1]
			)
		return toee.SKIP_DEFAULT

	def get_dest_location(self): return 0
	def get_dest_map(self): return 0

class CtrlPortalUp(CtrlPortalOut):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_PORTAL_UP

class CtrlPortalUpImmediate(CtrlPortalOutImmediate):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_PORTAL_UP

class CtrlPortalDown(CtrlPortalOut):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_PORTAL_DOWN

class CtrlPortalDownImmediate(CtrlPortalOutImmediate):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_PORTAL_DOWN

class CtrlPortalLaddersUp(CtrlPortalOut):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_PORTAL_LADDERS_UP
