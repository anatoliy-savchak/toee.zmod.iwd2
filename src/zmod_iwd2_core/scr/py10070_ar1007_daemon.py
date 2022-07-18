import toee, debug
import module_consts, utils_storage, ctrl_daemon2, ctrl_daemon_ie, ctrl_ambients, inf_scripting, utils_obj
import const_toee
#### IMPORTS ####
import py10074_ar1007_npc_inst_classes
from bcs import scr_ar1007
#### END IMPORTS ####
DAEMON_SCRIPT_ID = 10070
DAEMON_MAP_ID = module_consts.MAP_ID_AR1007
DAEMON_GID = "G_F8B1914F_1608_4C3C_AD21_9AB736DCFF57"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, DAEMON_MAP_ID, CtrlAR1007)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, DAEMON_MAP_ID, CtrlAR1007)

def san_heartbeat(attachee, triggerer): return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_dying(attachee, triggerer): return ctrl_daemon2.do_san_dying(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_use(attachee, triggerer): return ctrl_daemon2.do_san_use(attachee, triggerer, DAEMON_MAP_ID, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): return None
	result = o.data.get(CtrlAR1007.get_name())
	assert isinstance(result, CtrlAR1007)
	return result

class CtrlAR1007(ctrl_daemon_ie.CtrlDaemonIE):
	def created(self, npc):
		self.init_daemon2_fields(DAEMON_MAP_ID, DAEMON_SCRIPT_ID, "daemon_ar1007")
		super(CtrlAR1007, self).created(npc)
		return
	
	def place_encounters_initial(self):
		super(CtrlAR1007, self).place_encounters_initial()
		return
	
	def place_npcs_auto(self):
		# Goblin_1: 10GOBC (457.7, 512.8) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_1 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_1...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_1,  utils_obj.sec2loc(457, 512)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Goblin_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_2: 10GOBC (455.3, 499.3) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_2 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_2...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_2,  utils_obj.sec2loc(455, 499)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_3: 10GOBC (462.2, 503.3) const_toee.ROT00 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_3 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_3...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_3,  utils_obj.sec2loc(462, 503)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "Goblin_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_4: 10GOBC (480.0, 497.6) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_4 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_4...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_4,  utils_obj.sec2loc(480, 497)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_5: 10GOBC (479.5, 501.2) const_toee.ROT11 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_5 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_5...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_5,  utils_obj.sec2loc(479, 501)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Goblin_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_1: 10GOBSC (477.1, 470.8) const_toee.ROT11 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_1 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_1...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_1,  utils_obj.sec2loc(477, 470)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Goblin_Sapper_1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_2: 10GOBSC (482.5, 465.0) const_toee.ROT00 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_2 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_2...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_2,  utils_obj.sec2loc(482, 465)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "Goblin_Sapper_2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_3: 10GOBSC (482.1, 477.8) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_3 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_3...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_3,  utils_obj.sec2loc(482, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_Sapper_3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_6: 10GOBC (466.0, 480.8) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_6 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_6...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_6,  utils_obj.sec2loc(466, 480)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_7: 10GOBC (473.1, 488.5) const_toee.ROT02 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_7 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_7...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_7,  utils_obj.sec2loc(473, 488)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Goblin_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_8: 10GOBC (493.2, 481.1) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_8 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_8...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_8,  utils_obj.sec2loc(493, 481)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_9: 10GOBC (497.0, 453.5) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_9 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_9...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_9,  utils_obj.sec2loc(497, 453)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_10: 10GOBC (501.8, 454.0) const_toee.ROT08 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_10 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_10...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_10,  utils_obj.sec2loc(501, 454)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Goblin_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_11: 10GOBC (498.5, 464.4) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_11 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_11...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_11,  utils_obj.sec2loc(498, 464)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_11", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_4: 10GOBSC (510.3, 454.8) const_toee.ROT08 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_4 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_4...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_4,  utils_obj.sec2loc(510, 454)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Goblin_Sapper_4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_5: 10GOBSC (495.6, 460.0) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_5 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_5...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_5,  utils_obj.sec2loc(495, 460)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_Sapper_5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_6: 10GOBSC (506.2, 459.6) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_6 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_6...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_6,  utils_obj.sec2loc(506, 459)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Goblin_Sapper_6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Dead Goblin: 10GOBD (478.9, 469.8) const_toee.ROT11 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBD_AR1007_Dead_Goblin 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBD_AR1007_Dead_Goblin...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBD_AR1007_Dead_Goblin,  utils_obj.sec2loc(478, 469)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Dead Goblin", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Dead Goblin: 10GOBD (478.9, 469.8) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBD_AR1007_Dead_Goblin 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBD_AR1007_Dead_Goblin...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBD_AR1007_Dead_Goblin,  utils_obj.sec2loc(478, 469)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Dead Goblin", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_12: 10GOBC (457.9, 497.7) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_12 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_12...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_12,  utils_obj.sec2loc(457, 497)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_12", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_13: 10GOBC (464.9, 505.1) const_toee.ROT00 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_13 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_13...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_13,  utils_obj.sec2loc(464, 505)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "Goblin_13", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_14: 10GOBC (459.8, 496.0) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_14 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_14...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_14,  utils_obj.sec2loc(459, 496)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_14", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_15: 10GOBC (458.8, 502.1) const_toee.ROT02 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_15 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_15...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_15,  utils_obj.sec2loc(458, 502)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Goblin_15", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_16: 10GOBC (477.4, 499.5) const_toee.ROT08 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_16 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_16...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_16,  utils_obj.sec2loc(477, 499)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Goblin_16", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_17: 10GOBC (482.9, 499.2) const_toee.ROT02 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_17 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_17...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_17,  utils_obj.sec2loc(482, 499)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Goblin_17", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_18: 10GOBC (473.8, 502.7) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_18 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_18...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_18,  utils_obj.sec2loc(473, 502)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_18", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_19: 10GOBC (481.7, 500.8) const_toee.ROT00 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_19 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_19...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_19,  utils_obj.sec2loc(481, 500)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "Goblin_19", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_20: 10GOBC (466.4, 485.0) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_20 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_20...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_20,  utils_obj.sec2loc(466, 485)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_20", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_21: 10GOBC (470.8, 489.9) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_21 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_21...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_21,  utils_obj.sec2loc(470, 489)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_21", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_22: 10GOBC (467.2, 488.0) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_22 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_22...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_22,  utils_obj.sec2loc(467, 488)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_22", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_23: 10GOBC (477.8, 487.8) const_toee.ROT02 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_23 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_23...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_23,  utils_obj.sec2loc(477, 487)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Goblin_23", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_24: 10GOBC (483.4, 475.9) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_24 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_24...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_24,  utils_obj.sec2loc(483, 475)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Goblin_24", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_25: 10GOBC (484.6, 482.0) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_25 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_25...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_25,  utils_obj.sec2loc(484, 482)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_25", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_26: 10GOBC (495.2, 477.2) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_26 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_26...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_26,  utils_obj.sec2loc(495, 477)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_26", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_27: 10GOBC (493.1, 484.4) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_27 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_27...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_27,  utils_obj.sec2loc(493, 484)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_27", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_7: 10GOBSC (486.9, 464.6) const_toee.ROT02 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_7 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_7...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_7,  utils_obj.sec2loc(486, 464)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Goblin_Sapper_7", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_8: 10GOBSC (478.6, 474.4) const_toee.ROT11 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_8 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_8...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_8,  utils_obj.sec2loc(478, 474)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Goblin_Sapper_8", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_9: 10GOBSC (495.0, 456.8) const_toee.ROT05 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_9 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_9...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_9,  utils_obj.sec2loc(495, 456)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Goblin_Sapper_9", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_28: 10GOBC (502.0, 464.5) const_toee.ROT02 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_28 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_28...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_28,  utils_obj.sec2loc(502, 464)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Goblin_28", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_29: 10GOBC (500.3, 462.1) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_29 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_29...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_29,  utils_obj.sec2loc(500, 462)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_29", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_30: 10GOBC (497.3, 457.3) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_30 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_30...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_30,  utils_obj.sec2loc(497, 457)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Goblin_30", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_10: 10GOBSC (509.3, 457.9) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_10 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_10...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_10,  utils_obj.sec2loc(509, 457)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Goblin_Sapper_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_11: 10GOBSC (510.6, 452.1) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_11 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_11...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_11,  utils_obj.sec2loc(510, 452)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Goblin_Sapper_11", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_Sapper_12: 10GOBSC (507.7, 454.7) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_12 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_12...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBSC_AR1007_Goblin_Sapper_12,  utils_obj.sec2loc(507, 454)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Goblin_Sapper_12", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_31: 10GOBC (500.4, 455.0) const_toee.ROT08 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_31 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_31...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_31,  utils_obj.sec2loc(500, 455)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Goblin_31", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_32: 10GOBC (503.5, 460.6) const_toee.ROT09 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_32 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_32...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_32,  utils_obj.sec2loc(503, 460)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "Goblin_32", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Goblin_33: 10GOBC (504.2, 452.4) const_toee.ROT06 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_33 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_33...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10GOBC_AR1007_Goblin_33,  utils_obj.sec2loc(504, 452)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Goblin_33", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Rukwurm: 10RUKWU (502.6, 456.6) const_toee.ROT08 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10RUKWU_AR1007_Rukwurm 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10RUKWU_AR1007_Rukwurm...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10RUKWU_AR1007_Rukwurm,  utils_obj.sec2loc(502, 456)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Rukwurm", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Ulek: 10ULEK (499.4, 459.2) const_toee.ROT03 ctrl: py10074_ar1007_npc_inst_classes.Ctrl_10ULEK_AR1007_Ulek 
		print("Creating py10074_ar1007_npc_inst_classes.Ctrl_10ULEK_AR1007_Ulek...")
		ctrl_class, loc = py10074_ar1007_npc_inst_classes.Ctrl_10ULEK_AR1007_Ulek,  utils_obj.sec2loc(499, 459)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Ulek", 0, 1)
			self.actor_created(npc, ctrl)
		
		return
	
	def place_bcs_auto(self):
		self.vars["script_area"] = scr_ar1007.Script_AR1007
		return

	def setup_ambients_auto(self):
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(498, 443)
		amb.setup(name="Dripping Water Singles", flags="Enabled, IgnoreRadius, RandomOrder", frequency=10, frequency_variation=0, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4196, durationf=3.09102, volume=75, title="AR1007\Dripping Water Singles AM1007A1")
		amb.setup_sound(sound_id=4197, durationf=4.663039, volume=75, title="AR1007\Dripping Water Singles AM1007A2")
		amb.setup_sound(sound_id=4198, durationf=6.744399, volume=75, title="AR1007\Dripping Water Singles AM1007A3")
		amb.setup_sound(sound_id=4199, durationf=6.224127, volume=75, title="AR1007\Dripping Water Singles AM1007A4")
		amb.setup_sound(sound_id=4200, durationf=4.708118, volume=75, title="AR1007\Dripping Water Singles AM1007A5")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(498, 443)
		amb.setup(name="dstnt axes", flags="Enabled, IgnoreRadius, RandomOrder", frequency=15, frequency_variation=10, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4201, durationf=2.29093, volume=80, title="AR1007\dstnt axes AM1007B1")
		amb.setup_sound(sound_id=4202, durationf=1.513968, volume=80, title="AR1007\dstnt axes AM1007B2")
		amb.setup_sound(sound_id=4203, durationf=2.834649, volume=80, title="AR1007\dstnt axes AM1007B3")
		amb.setup_sound(sound_id=4204, durationf=2.339592, volume=80, title="AR1007\dstnt axes AM1007B4")
		amb.setup_sound(sound_id=4205, durationf=3.800998, volume=80, title="AR1007\dstnt axes AM1007B5")
		amb.setup_sound(sound_id=4206, durationf=2.524626, volume=80, title="AR1007\dstnt axes AM1007B6")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(498, 443)
		amb.setup(name="goblins", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4207, durationf=3.032063, volume=75, title="AR1007\goblins AM1007C1")
		amb.setup_sound(sound_id=4208, durationf=6.15483, volume=75, title="AR1007\goblins AM1007C2")
		amb.setup_sound(sound_id=4209, durationf=3.091837, volume=75, title="AR1007\goblins AM1007C3")
		amb.setup_sound(sound_id=4210, durationf=3.678231, volume=75, title="AR1007\goblins AM1007C4")
		amb.setup_sound(sound_id=4211, durationf=3.677732, volume=75, title="AR1007\goblins AM1007C5")
		self.ambients.append(amb)
		
		
		self.ambs_timer_start()
		return
