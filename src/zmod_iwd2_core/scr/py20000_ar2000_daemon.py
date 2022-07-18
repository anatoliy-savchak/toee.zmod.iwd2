import toee, debug
import module_consts, utils_storage, ctrl_daemon2, ctrl_daemon_ie, ctrl_ambients, inf_scripting, utils_obj
import const_toee
#### IMPORTS ####
import py20004_ar2000_npc_inst_classes
#### END IMPORTS ####
DAEMON_SCRIPT_ID = 20000
DAEMON_MAP_ID = module_consts.MAP_ID_AR2000
DAEMON_GID = "G_DB928653_5F39_4A0E_B1DB_28631799B8D7"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, DAEMON_MAP_ID, CtrlAR2000)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, DAEMON_MAP_ID, CtrlAR2000)

def san_heartbeat(attachee, triggerer): return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_dying(attachee, triggerer): return ctrl_daemon2.do_san_dying(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_use(attachee, triggerer): return ctrl_daemon2.do_san_use(attachee, triggerer, DAEMON_MAP_ID, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): return None
	result = o.data.get(CtrlAR2000.get_name())
	assert isinstance(result, CtrlAR2000)
	return result

class CtrlAR2000(ctrl_daemon_ie.CtrlDaemonIE):
	def created(self, npc):
		self.init_daemon2_fields(DAEMON_MAP_ID, DAEMON_SCRIPT_ID, "daemon_ar2000")
		super(CtrlAR2000, self).created(npc)
		return
	
	def place_encounters_initial(self):
		super(CtrlAR2000, self).place_encounters_initial()
		return

	def authorize_actor(self, ctrl):
		if ctrl == py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak1: return False
		if ctrl == py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak2: return False
		if ctrl == py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak3: return False
		if ctrl == py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak4: return False

		result = super(CtrlAR2000, self).authorize_actor(ctrl)
		return result
	
	def place_npcs_auto(self):
		# T1_Arch_1: 20ORCACH (524.4, 499.5) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_1,  utils_obj.sec2loc(524, 499)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Arch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_2: 20ORCACH (521.5, 500.2) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_2,  utils_obj.sec2loc(521, 500)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Arch_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_3: 20ORCACH (514.1, 506.2) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_3,  utils_obj.sec2loc(514, 506)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T1_Arch_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_4: 20ORCACH (514.5, 508.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T1_Arch_4,  utils_obj.sec2loc(514, 508)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T1_Arch_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Orc_1: 20ORCWAR (514.8, 498.3) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_1,  utils_obj.sec2loc(514, 498)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Orc_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Orc_2: 20ORCWAR (515.8, 501.3) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_2,  utils_obj.sec2loc(515, 501)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Orc_3: 20ORCWAR (512.6, 501.3) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T1_Orc_3,  utils_obj.sec2loc(512, 501)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Shaman_1: 20ORCSHM (515.6, 493.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T1_Shaman_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T1_Shaman_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T1_Shaman_1,  utils_obj.sec2loc(515, 493)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Shaman_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_5: 20ORCA3 (524.4, 499.5) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_5,  utils_obj.sec2loc(524, 499)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Arch_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_6: 20ORCA3 (521.5, 500.2) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_6,  utils_obj.sec2loc(521, 500)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Arch_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_7: 20ORCA3 (514.1, 506.2) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_7,  utils_obj.sec2loc(514, 506)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T1_Arch_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_8: 20ORCA3 (514.5, 508.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T1_Arch_8,  utils_obj.sec2loc(514, 508)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T1_Arch_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Orc_4: 20ORCW3 (515.8, 501.3) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T1_Orc_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T1_Orc_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T1_Orc_4,  utils_obj.sec2loc(515, 501)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Orc_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Shaman_2: 20ORCSHM (507.0, 500.2) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T1_Shaman_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T1_Shaman_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T1_Shaman_2,  utils_obj.sec2loc(507, 500)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T1_Shaman_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_9: 20ORCA4 (524.4, 499.5) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_9,  utils_obj.sec2loc(524, 499)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Arch_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_10: 20ORCA4 (521.5, 500.2) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_10 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_10...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_10,  utils_obj.sec2loc(521, 500)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Arch_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_11: 20ORCA4 (514.1, 506.2) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_11 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_11...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_11,  utils_obj.sec2loc(514, 506)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T1_Arch_11", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Arch_12: 20ORCA4 (514.5, 508.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_12 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_12...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T1_Arch_12,  utils_obj.sec2loc(514, 508)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T1_Arch_12", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Orc_5: 20ORCW4 (515.8, 501.3) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_5,  utils_obj.sec2loc(515, 501)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Orc_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Orc_6: 20ORCW4 (514.8, 498.3) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_6,  utils_obj.sec2loc(514, 498)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Orc_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T1_Orc_7: 20ORCW4 (512.6, 501.3) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T1_Orc_7,  utils_obj.sec2loc(512, 501)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T1_Orc_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_1: 20ORCACH (520.2, 534.4) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_1,  utils_obj.sec2loc(520, 534)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_2: 20ORCACH (523.2, 537.1) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_2,  utils_obj.sec2loc(523, 537)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_3: 20ORCACH (520.8, 538.3) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T2_Arch_3,  utils_obj.sec2loc(520, 538)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Orch_1: 20ORCW3 (502.4, 515.2) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orch_1,  utils_obj.sec2loc(502, 515)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T2_Orch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Orc_2: 20ORCW3 (498.2, 516.3) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orc_2,  utils_obj.sec2loc(498, 516)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T2_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Orc_3: 20ORCW3 (498.9, 512.4) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T2_Orc_3,  utils_obj.sec2loc(498, 512)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T2_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_4: 20ORCA3 (520.1, 534.3) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_4,  utils_obj.sec2loc(520, 534)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_5: 20ORCA3 (523.1, 537.0) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_5,  utils_obj.sec2loc(523, 537)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_6: 20ORCA3 (520.8, 538.3) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T2_Arch_6,  utils_obj.sec2loc(520, 538)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_7: 20ORCA4 (520.1, 534.3) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_7,  utils_obj.sec2loc(520, 534)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_8: 20ORCA4 (523.0, 537.0) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_8,  utils_obj.sec2loc(523, 537)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Arch_9: 20ORCA4 (520.8, 538.3) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T2_Arch_9,  utils_obj.sec2loc(520, 538)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T2_Arch_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Orc_4: 20ORCW4 (498.9, 512.4) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_4,  utils_obj.sec2loc(498, 512)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T2_Orc_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Orc_5: 20ORCW4 (502.4, 515.2) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_5,  utils_obj.sec2loc(502, 515)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T2_Orc_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T2_Orc_6: 20ORCW4 (498.2, 516.3) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T2_Orc_6,  utils_obj.sec2loc(498, 516)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T2_Orc_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_1: 20ORCACH (462.1, 479.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_1,  utils_obj.sec2loc(462, 479)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Arch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_2: 20ORCACH (466.0, 478.9) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_2,  utils_obj.sec2loc(466, 478)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Arch_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_3: 20ORCACH (481.9, 485.2) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_3,  utils_obj.sec2loc(481, 485)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T3_Arch_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_4: 20ORCACH (481.9, 478.3) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T3_Arch_4,  utils_obj.sec2loc(481, 478)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T3_Arch_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_1: 20ORCWAR (462.5, 473.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_1,  utils_obj.sec2loc(462, 473)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Orc_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_2: 20ORCWAR (463.0, 476.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_2,  utils_obj.sec2loc(463, 476)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T3_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_3: 20ORCWAR (466.7, 477.0) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T3_Orc_3,  utils_obj.sec2loc(466, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T3_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Shaman_1: 20ORCSHM (472.3, 472.5) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T3_Shaman_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T3_Shaman_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T3_Shaman_1,  utils_obj.sec2loc(472, 472)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T3_Shaman_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_5: 20ORCA3 (462.1, 479.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_5,  utils_obj.sec2loc(462, 479)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Arch_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_6: 20ORCA3 (466.0, 478.9) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_6,  utils_obj.sec2loc(466, 478)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Arch_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_7: 20ORCA3 (481.9, 478.3) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_7,  utils_obj.sec2loc(481, 478)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T3_Arch_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_8: 20ORCA3 (481.9, 485.2) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T3_Arch_8,  utils_obj.sec2loc(481, 485)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T3_Arch_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_4: 20ORCW3 (462.5, 473.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_4,  utils_obj.sec2loc(462, 473)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Orc_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_5: 20ORCW3 (463.0, 476.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_5,  utils_obj.sec2loc(463, 476)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T3_Orc_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_6: 20ORCW3 (466.7, 477.0) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T3_Orc_6,  utils_obj.sec2loc(466, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T3_Orc_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_9: 20ORCA4 (462.1, 479.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_9,  utils_obj.sec2loc(462, 479)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Arch_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_10: 20ORCA4 (466.0, 478.9) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_10 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_10...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_10,  utils_obj.sec2loc(466, 478)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Arch_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_11: 20ORCA4 (481.9, 478.3) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_11 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_11...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_11,  utils_obj.sec2loc(481, 478)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T3_Arch_11", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Arch_12: 20ORCA4 (481.9, 485.2) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_12 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_12...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T3_Arch_12,  utils_obj.sec2loc(481, 485)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T3_Arch_12", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_7: 20ORCW4 (462.5, 473.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_7,  utils_obj.sec2loc(462, 473)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Orc_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_8: 20ORCW4 (463.0, 476.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_8,  utils_obj.sec2loc(463, 476)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T3_Orc_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Orc_9: 20ORCW4 (466.7, 477.0) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T3_Orc_9,  utils_obj.sec2loc(466, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T3_Orc_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Shaman_2: 20ORCSHM (459.9, 467.4) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T3_Shaman_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T3_Shaman_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T3_Shaman_2,  utils_obj.sec2loc(459, 467)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T3_Shaman_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T3_Firestarter_1: 20ORCFIR (483.8, 484.9) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T3_Firestarter_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T3_Firestarter_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T3_Firestarter_1,  utils_obj.sec2loc(483, 484)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T3_Firestarter_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Arch_1: 20ORCA3 (470.5, 513.6) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_1,  utils_obj.sec2loc(470, 513)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T4_Arch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Arch_2: 20ORCA3 (465.2, 516.2) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_2,  utils_obj.sec2loc(465, 516)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T4_Arch_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Arch_3: 20ORCA3 (460.8, 516.9) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T4_Arch_3,  utils_obj.sec2loc(460, 516)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T4_Arch_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Shaman_1: 20ORCSHM (460.4, 512.3) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T4_Shaman_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T4_Shaman_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T4_Shaman_1,  utils_obj.sec2loc(460, 512)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T4_Shaman_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Orc_1: 20ORCW3 (467.7, 508.2) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T4_Orc_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T4_Orc_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T4_Orc_1,  utils_obj.sec2loc(467, 508)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T4_Orc_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Orc_2: 20ORCW4 (462.6, 510.4) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_2,  utils_obj.sec2loc(462, 510)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T4_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Orc_3: 20ORCW4 (466.0, 512.1) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_3,  utils_obj.sec2loc(466, 512)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T4_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Arch_4: 20ORCA4 (470.5, 513.6) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_4,  utils_obj.sec2loc(470, 513)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T4_Arch_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Arch_5: 20ORCA4 (465.2, 516.2) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_5,  utils_obj.sec2loc(465, 516)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T4_Arch_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Arch_6: 20ORCA4 (460.8, 516.9) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T4_Arch_6,  utils_obj.sec2loc(460, 516)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T4_Arch_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Orc_4: 20ORCW4 (467.7, 508.2) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_4,  utils_obj.sec2loc(467, 508)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T4_Orc_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T4_Orc_5: 20ORCW4 (470.5, 509.4) const_toee.ROT00 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T4_Orc_5,  utils_obj.sec2loc(470, 509)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "T4_Orc_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Arch_1: 20ORCACH (487.8, 445.6) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T5_Arch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T5_Arch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T5_Arch_1,  utils_obj.sec2loc(487, 445)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T5_Arch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Arch_2: 20ORCACH (487.4, 451.1) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T5_Arch_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T5_Arch_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T5_Arch_2,  utils_obj.sec2loc(487, 451)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T5_Arch_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Shaman_1: 20ORCSHM (484.6, 448.4) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T5_Shaman_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T5_Shaman_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T5_Shaman_1,  utils_obj.sec2loc(484, 448)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T5_Shaman_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_1: 20ORCWAR (489.8, 448.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_1,  utils_obj.sec2loc(489, 448)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T5_Orc_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_2: 20ORCWAR (500.8, 443.0) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_2,  utils_obj.sec2loc(500, 443)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_3: 20ORCWAR (505.4, 445.7) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_3,  utils_obj.sec2loc(505, 445)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T5_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_4: 20ORCWAR (504.2, 442.4) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T5_Orc_4,  utils_obj.sec2loc(504, 442)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Orc_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Shaman_2: 20ORCSHM (510.5, 434.7) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T5_Shaman_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T5_Shaman_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T5_Shaman_2,  utils_obj.sec2loc(510, 434)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T5_Shaman_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_5: 20ORCW3 (505.4, 445.7) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_5,  utils_obj.sec2loc(505, 445)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T5_Orc_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_6: 20ORCW3 (500.8, 443.0) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_6,  utils_obj.sec2loc(500, 443)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Orc_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_7: 20ORCW3 (504.2, 442.4) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T5_Orc_7,  utils_obj.sec2loc(504, 442)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Orc_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Arch_3: 20ORCA3 (505.5, 432.3) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_3,  utils_obj.sec2loc(505, 432)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Arch_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Arch_4: 20ORCA3 (501.3, 433.3) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_4,  utils_obj.sec2loc(501, 433)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Arch_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Arch_5: 20ORCA3 (487.8, 445.6) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_5,  utils_obj.sec2loc(487, 445)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T5_Arch_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Arch_6: 20ORCA3 (487.4, 451.1) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T5_Arch_6,  utils_obj.sec2loc(487, 451)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T5_Arch_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_8: 20ORCW4 (489.8, 448.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_8,  utils_obj.sec2loc(489, 448)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T5_Orc_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_9: 20ORCW4 (505.4, 445.7) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_9,  utils_obj.sec2loc(505, 445)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T5_Orc_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_10: 20ORCW4 (500.8, 443.0) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_10 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_10...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_10,  utils_obj.sec2loc(500, 443)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Orc_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Orc_11: 20ORCW4 (504.2, 442.4) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_11 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_11...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T5_Orc_11,  utils_obj.sec2loc(504, 442)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Orc_11", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T5_Firestarter_1: 20ORCFIR (496.9, 455.6) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T5_Firestarter_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T5_Firestarter_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T5_Firestarter_1,  utils_obj.sec2loc(496, 455)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T5_Firestarter_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Firestarter_1: 20ORCFIR (538.1, 467.0) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T9_Firestarter_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T9_Firestarter_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T9_Firestarter_1,  utils_obj.sec2loc(538, 467)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T9_Firestarter_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Runner_1: 20ORCRUN (539.4, 468.4) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T9_Runner_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T9_Runner_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T9_Runner_1,  utils_obj.sec2loc(539, 468)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T9_Runner_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_1: 20ORCACH (522.7, 473.4) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_1,  utils_obj.sec2loc(522, 473)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T9_Archer_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_2: 20ORCACH (527.9, 474.0) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_2,  utils_obj.sec2loc(527, 474)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T9_Archer_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_3: 20ORCACH (523.0, 477.8) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T9_Archer_3,  utils_obj.sec2loc(523, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T9_Archer_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_4: 20ORCA3 (522.7, 473.4) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_4,  utils_obj.sec2loc(522, 473)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T9_Archer_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_5: 20ORCA3 (523.0, 477.8) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_5,  utils_obj.sec2loc(523, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T9_Archer_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_6: 20ORCA3 (527.9, 474.0) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T9_Archer_6,  utils_obj.sec2loc(527, 474)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T9_Archer_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_7: 20ORCA4 (527.9, 474.0) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_7,  utils_obj.sec2loc(527, 474)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T9_Archer_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_8: 20ORCA4 (522.7, 473.4) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_8,  utils_obj.sec2loc(522, 473)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T9_Archer_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T9_Archer_9: 20ORCA4 (523.0, 477.8) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T9_Archer_9,  utils_obj.sec2loc(523, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T9_Archer_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_1: 20ORCWAR (425.6, 496.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_1,  utils_obj.sec2loc(425, 496)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_2: 20ORCWAR (423.5, 491.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_2,  utils_obj.sec2loc(423, 491)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_3: 20ORCWAR (420.8, 493.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T6_Orc_3,  utils_obj.sec2loc(420, 493)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_1: 20ORCACH (431.0, 507.4) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_1,  utils_obj.sec2loc(431, 507)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T6_Arch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_2: 20ORCACH (429.6, 505.5) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_2,  utils_obj.sec2loc(429, 505)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T6_Arch_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Shaman_1: 20ORCSHM (419.7, 489.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T6_Shaman_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T6_Shaman_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T6_Shaman_1,  utils_obj.sec2loc(419, 489)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Shaman_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_3: 20ORCACH (416.8, 483.9) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_3,  utils_obj.sec2loc(416, 483)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Arch_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_4: 20ORCACH (417.1, 481.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T6_Arch_4,  utils_obj.sec2loc(417, 481)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Arch_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_4: 20ORCW3 (425.6, 496.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_4,  utils_obj.sec2loc(425, 496)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_5: 20ORCW3 (423.5, 491.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_5,  utils_obj.sec2loc(423, 491)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_6: 20ORCW3 (420.8, 493.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T6_Orc_6,  utils_obj.sec2loc(420, 493)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_5: 20ORCA3 (429.6, 505.5) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T6_Arch_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T6_Arch_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T6_Arch_5,  utils_obj.sec2loc(429, 505)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T6_Arch_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_6: 20ORCA3 (431.0, 507.4) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T6_Arch_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T6_Arch_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA3_AR2000_T6_Arch_6,  utils_obj.sec2loc(431, 507)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T6_Arch_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_7: 20ORCW4 (425.6, 496.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_7,  utils_obj.sec2loc(425, 496)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_8: 20ORCW4 (423.5, 491.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_8,  utils_obj.sec2loc(423, 491)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Orc_9: 20ORCW4 (420.8, 493.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T6_Orc_9,  utils_obj.sec2loc(420, 493)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Orc_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_7: 20ORCA4 (431.0, 507.4) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_7,  utils_obj.sec2loc(431, 507)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T6_Arch_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_8: 20ORCA4 (429.6, 505.5) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_8,  utils_obj.sec2loc(429, 505)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T6_Arch_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_9: 20ORCA4 (417.1, 481.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_9,  utils_obj.sec2loc(417, 481)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Arch_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Arch_10: 20ORCA4 (416.8, 483.9) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_10 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_10...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T6_Arch_10,  utils_obj.sec2loc(416, 483)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T6_Arch_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Firestarter_1: 20ORCFIR (431.1, 490.2) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T6_Firestarter_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T6_Firestarter_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T6_Firestarter_1,  utils_obj.sec2loc(431, 490)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T6_Firestarter_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T6_Runner_1: 20ORCRUN (431.0, 491.9) const_toee.ROT05 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T6_Runner_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T6_Runner_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T6_Runner_1,  utils_obj.sec2loc(431, 491)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "T6_Runner_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Firestarter_1: 20ORCFIR (443.9, 453.0) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T7_Firestarter_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T7_Firestarter_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T7_Firestarter_1,  utils_obj.sec2loc(443, 453)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T7_Firestarter_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Firestarter_2: 20ORCFIR (444.7, 454.7) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T7_Firestarter_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T7_Firestarter_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T7_Firestarter_2,  utils_obj.sec2loc(444, 454)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T7_Firestarter_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Shaman_1: 20ORCSHM (440.3, 456.0) const_toee.ROT09 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T7_Shaman_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T7_Shaman_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T7_Shaman_1,  utils_obj.sec2loc(440, 456)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "T7_Shaman_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_1: 20ORCW4 (434.3, 459.5) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_1,  utils_obj.sec2loc(434, 459)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T7_Orc_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_2: 20ORCW4 (437.5, 467.6) const_toee.ROT02 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_2,  utils_obj.sec2loc(437, 467)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "T7_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_3: 20ORCW4 (430.3, 463.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_3,  utils_obj.sec2loc(430, 463)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T7_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_4: 20ORCW4 (426.6, 469.0) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_4,  utils_obj.sec2loc(426, 469)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T7_Orc_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_5: 20ORCW4 (433.6, 469.1) const_toee.ROT11 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_5 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_5...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T7_Orc_5,  utils_obj.sec2loc(433, 469)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "T7_Orc_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_1: 20ORCW3 (441.4, 433.4) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_1,  utils_obj.sec2loc(441, 433)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Orc_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_2: 20ORCW3 (438.3, 435.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_2,  utils_obj.sec2loc(438, 435)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Orc_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_3: 20ORCW3 (443.4, 430.2) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_3,  utils_obj.sec2loc(443, 430)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Orc_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Arch_1: 20ORCACH (439.2, 429.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T8_Arch_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T8_Arch_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T8_Arch_1,  utils_obj.sec2loc(439, 429)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Arch_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Arch_2: 20ORCACH (436.9, 431.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T8_Arch_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T8_Arch_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCACH_AR2000_T8_Arch_2,  utils_obj.sec2loc(436, 431)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Arch_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Arch_3: 20ORCA4 (439.2, 429.1) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T8_Arch_3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T8_Arch_3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T8_Arch_3,  utils_obj.sec2loc(439, 429)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Arch_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Arch_4: 20ORCA4 (436.9, 431.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T8_Arch_4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T8_Arch_4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCA4_AR2000_T8_Arch_4,  utils_obj.sec2loc(436, 431)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Arch_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Shaman_1: 20ORCSHM (432.5, 433.6) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T8_Shaman_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T8_Shaman_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T8_Shaman_1,  utils_obj.sec2loc(432, 433)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T8_Shaman_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_6: 20ORCW3 (433.8, 437.0) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW3_AR2000_T8_Orc_6,  utils_obj.sec2loc(433, 437)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T8_Orc_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_7: 20ORCW4 (443.4, 430.2) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_7,  utils_obj.sec2loc(443, 430)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Orc_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_8: 20ORCW4 (441.4, 433.4) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_8,  utils_obj.sec2loc(441, 433)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Orc_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_9: 20ORCW4 (438.3, 435.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_9 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_9...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_9,  utils_obj.sec2loc(438, 435)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Orc_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Orc_10: 20ORCW4 (433.8, 437.0) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_10 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_10...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCW4_AR2000_T8_Orc_10,  utils_obj.sec2loc(433, 437)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T8_Orc_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Shaman_2: 20ORCSHM (434.0, 429.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T8_Shaman_2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T8_Shaman_2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCSHM_AR2000_T8_Shaman_2,  utils_obj.sec2loc(434, 429)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "T8_Shaman_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Firestarter_1: 20ORCFIR (465.3, 448.8) const_toee.ROT02 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T8_Firestarter_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T8_Firestarter_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCFIR_AR2000_T8_Firestarter_1,  utils_obj.sec2loc(465, 448)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "T8_Firestarter_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T8_Runner_1: 20ORCRUN (464.4, 451.1) const_toee.ROT02 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T8_Runner_1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T8_Runner_1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCRUN_AR2000_T8_Runner_1,  utils_obj.sec2loc(464, 451)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "T8_Runner_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_6: 20ORCWAR (434.3, 459.5) const_toee.ROT03 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_6 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_6...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_6,  utils_obj.sec2loc(434, 459)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "T7_Orc_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_7: 20ORCWAR (437.5, 467.6) const_toee.ROT02 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_7 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_7...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_7,  utils_obj.sec2loc(437, 467)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "T7_Orc_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# T7_Orc_8: 20ORCWAR (430.3, 463.9) const_toee.ROT08 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_8 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_8...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCWAR_AR2000_T7_Orc_8,  utils_obj.sec2loc(430, 463)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "T7_Orc_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Torak1: 20ORCCHF (523.5, 505.8) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak1 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak1...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak1,  utils_obj.sec2loc(523, 505)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Torak1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Torak2: 20ORCCHF (466.8, 486.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak2 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak2...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak2,  utils_obj.sec2loc(466, 486)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Torak2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Torak3: 20ORCCHF (452.3, 449.6) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak3 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak3...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak3,  utils_obj.sec2loc(452, 449)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Torak3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Torak4: 20ORCCHF (439.1, 431.7) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak4 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak4...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20ORCCHF_AR2000_Torak4,  utils_obj.sec2loc(439, 431)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Torak4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Dereth: 20DERETH (454.3, 471.9) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20DERETH_AR2000_Dereth 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20DERETH_AR2000_Dereth...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20DERETH_AR2000_Dereth,  utils_obj.sec2loc(454, 471)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Dereth", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Sabrina: 20SABRIN (495.4, 424.2) const_toee.ROT06 ctrl: py20004_ar2000_npc_inst_classes.Ctrl_20SABRIN_AR2000_Sabrina 
		print("Creating py20004_ar2000_npc_inst_classes.Ctrl_20SABRIN_AR2000_Sabrina...")
		ctrl_class, loc = py20004_ar2000_npc_inst_classes.Ctrl_20SABRIN_AR2000_Sabrina,  utils_obj.sec2loc(495, 424)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Sabrina", 0, 1)
			self.actor_created(npc, ctrl)
		
		return
	
	def place_bcs_auto(self):
		return

	def setup_ambients_auto(self):
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(472, 407)
		amb.setup(name="wind gusts", flags="Enabled, IgnoreRadius, RandomOrder", frequency=15, frequency_variation=5, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4276, durationf=5.042404, volume=80, title="AR2000\wind gusts AM2000A1")
		amb.setup_sound(sound_id=4277, durationf=9.473741, volume=80, title="AR2000\wind gusts AM2000A2")
		amb.setup_sound(sound_id=4278, durationf=9.845261, volume=80, title="AR2000\wind gusts AM2000A3")
		amb.setup_sound(sound_id=4279, durationf=8.916463, volume=80, title="AR2000\wind gusts AM2000A4")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(472, 407)
		amb.setup(name="birds", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, loc=loc, schedule="From_0530_to_0629, From_0630_to_0729, From_0730_to_0829, From_0830_to_0929, From_0930_to_1029, From_1030_to_1129, From_1130_to_1229, From_1230_to_1329, From_1330_to_1429, From_1430_to_1529, From_1530_to_1629, From_1630_to_1729")
		amb.setup_sound(sound_id=4280, durationf=2.98059, volume=70, title="AR2000\birds AM2000B1")
		amb.setup_sound(sound_id=4281, durationf=3.02576, volume=70, title="AR2000\birds AM2000B2")
		amb.setup_sound(sound_id=4282, durationf=4.922494, volume=70, title="AR2000\birds AM2000B3")
		amb.setup_sound(sound_id=4283, durationf=4.33542, volume=70, title="AR2000\birds AM2000B4")
		amb.setup_sound(sound_id=4284, durationf=3.341859, volume=70, title="AR2000\birds AM2000B5")
		amb.setup_sound(sound_id=4285, durationf=3.477324, volume=70, title="AR2000\birds AM2000B6")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(474, 409)
		amb.setup(name="wolfs", flags="Enabled, IgnoreRadius, RandomOrder", frequency=10, frequency_variation=0, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4286, durationf=2.24644, volume=100, title="AR2000\wolfs AM2000C1")
		amb.setup_sound(sound_id=4287, durationf=2.755782, volume=100, title="AR2000\wolfs AM2000C2")
		amb.setup_sound(sound_id=4288, durationf=6.097415, volume=100, title="AR2000\wolfs AM2000C3")
		amb.setup_sound(sound_id=4289, durationf=7.509116, volume=100, title="AR2000\wolfs AM2000C4")
		amb.setup_sound(sound_id=4290, durationf=6.3839, volume=100, title="AR2000\wolfs AM2000C5")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(440, 447)
		amb.setup(name="ice cracking", flags="Enabled, RandomOrder", frequency=10, frequency_variation=0, radius=800, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4291, durationf=2.409433, volume=65, title="AR2000\ice cracking AM6200B1")
		amb.setup_sound(sound_id=4292, durationf=3.943673, volume=65, title="AR2000\ice cracking AM6200B2")
		amb.setup_sound(sound_id=4293, durationf=4.96263, volume=65, title="AR2000\ice cracking AM6200B3")
		amb.setup_sound(sound_id=4294, durationf=4.358821, volume=65, title="AR2000\ice cracking AM6200B4")
		amb.setup_sound(sound_id=4295, durationf=5.966168, volume=65, title="AR2000\ice cracking AM6200B5")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(518, 527)
		amb.setup(name="ice cracking 2", flags="Enabled, RandomOrder", frequency=20, frequency_variation=5, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4295, durationf=5.966168, volume=65, title="AR2000\ice cracking AM6200B5")
		amb.setup_sound(sound_id=4291, durationf=2.409433, volume=65, title="AR2000\ice cracking AM6200B1")
		amb.setup_sound(sound_id=4292, durationf=3.943673, volume=65, title="AR2000\ice cracking AM6200B2")
		amb.setup_sound(sound_id=4293, durationf=4.96263, volume=65, title="AR2000\ice cracking AM6200B3")
		amb.setup_sound(sound_id=4294, durationf=4.358821, volume=65, title="AR2000\ice cracking AM6200B4")
		self.ambients.append(amb)
		
		
		self.ambs_timer_start()
		return
