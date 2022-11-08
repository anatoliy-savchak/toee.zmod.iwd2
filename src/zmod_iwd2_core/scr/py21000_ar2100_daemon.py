import toee, debug
import module_consts, utils_storage, ctrl_daemon2, ctrl_daemon_ie, ctrl_ambients, inf_scripting, utils_obj
import const_toee, module_difficulty
#### IMPORTS ####
import py21004_ar2100_npc_inst_classes
#### END IMPORTS ####
DAEMON_SCRIPT_ID = 21000
DAEMON_MAP_ID = module_consts.MAP_ID_AR2100
DAEMON_GID = "G_A2369D4F_55CE_4834_94E9_B91AFDC95F9A"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, DAEMON_MAP_ID, CtrlAR2100)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, DAEMON_MAP_ID, CtrlAR2100)

def san_heartbeat(attachee, triggerer): return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_dying(attachee, triggerer): return ctrl_daemon2.do_san_dying(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_use(attachee, triggerer): return ctrl_daemon2.do_san_use(attachee, triggerer, DAEMON_MAP_ID, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): return None
	result = o.data.get(CtrlAR2100.get_name())
	assert isinstance(result, CtrlAR2100)
	return result

class CtrlAR2100(ctrl_daemon_ie.CtrlDaemonIE):
	def created(self, npc):
		self.init_daemon2_fields(DAEMON_MAP_ID, DAEMON_SCRIPT_ID, "daemon_ar2100")
		super(CtrlAR2100, self).created(npc)
		return
	
	def place_encounters_initial(self):
		super(CtrlAR2100, self).place_encounters_initial()
		#toee.game.fade_and_teleport(0, 0, 0, DAEMON_MAP_ID, 457, 499) # verbeeg
		#toee.game.fade_and_teleport(0, 0, 0, DAEMON_MAP_ID, 465, 485) # harpy
		toee.game.fade_and_teleport(0, 0, 0, DAEMON_MAP_ID, 462, 472) # wererats
		return
	
	def place_npcs_auto(self):
		# Gaernat Sharptooth: 21GAERNT (476.8, 479.3) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth,  utils_obj.sec2loc(476, 479)
		if self.authorize_actor(ctrl_class, "Gaernat Sharptooth"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Gaernat Sharptooth", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_01: 21WERRAT (481.3, 478.8) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_01 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_01...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_01,  utils_obj.sec2loc(481, 478)
		if self.authorize_actor(ctrl_class, "GTH01_01"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_01", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_03: 21WERRAT (483.0, 488.6) const_toee.ROT09 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_03 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_03...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_03,  utils_obj.sec2loc(483, 488)
		if self.authorize_actor(ctrl_class, "GTH01_03"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "GTH01_03", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_09: 21WERRAT (494.8, 488.7) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_09 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_09...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_09,  utils_obj.sec2loc(494, 488)
		if self.authorize_actor(ctrl_class, "GTH01_09"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH01_09", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_02: 21WERBGR (480.5, 483.1) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_02 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_02...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_02,  utils_obj.sec2loc(480, 483)
		if self.authorize_actor(ctrl_class, "GTH01_02"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH01_02", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_10: 21WERBGR (496.1, 494.2) const_toee.ROT11 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_10 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_10...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_10,  utils_obj.sec2loc(496, 494)
		if self.authorize_actor(ctrl_class, "GTH01_10"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "GTH01_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_06: 21WERBGR (489.2, 474.7) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_06 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_06...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_06,  utils_obj.sec2loc(489, 474)
		if self.authorize_actor(ctrl_class, "GTH01_06"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH01_06", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_07: 20ORCSHM (490.8, 471.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_07 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_07...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_07,  utils_obj.sec2loc(490, 471)
		if self.authorize_actor(ctrl_class, "GTH01_07"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH01_07", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_08: 20ORCSHM (478.7, 490.2) const_toee.ROT09 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_08 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_08...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_08,  utils_obj.sec2loc(478, 490)
		if self.authorize_actor(ctrl_class, "GTH01_08"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "GTH01_08", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_11: 20ORCSHM (499.6, 488.2) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_11 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_11...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_11,  utils_obj.sec2loc(499, 488)
		if self.authorize_actor(ctrl_class, "GTH01_11"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_11", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_05: 20ORCACH (489.6, 479.4) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_05 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_05...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_05,  utils_obj.sec2loc(489, 479)
		if self.authorize_actor(ctrl_class, "GTH01_05"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_05", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_04: 20ORCACH (490.5, 487.4) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_04 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_04...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_04,  utils_obj.sec2loc(490, 487)
		if self.authorize_actor(ctrl_class, "GTH01_04"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH01_04", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_12: 20ORCACH (496.2, 486.2) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_12 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_12...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_12,  utils_obj.sec2loc(496, 486)
		if self.authorize_actor(ctrl_class, "GTH01_12"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_12", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_10: 21WERRAT (500.2, 465.2) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_10 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_10...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_10,  utils_obj.sec2loc(500, 465)
		if self.authorize_actor(ctrl_class, "GTH02_10"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH02_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_01: 21WERRAT (484.8, 459.7) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_01 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_01...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_01,  utils_obj.sec2loc(484, 459)
		if self.authorize_actor(ctrl_class, "GTH02_01"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_01", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_09: 21WERBGR (500.5, 460.7) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_09 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_09...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_09,  utils_obj.sec2loc(500, 460)
		if self.authorize_actor(ctrl_class, "GTH02_09"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH02_09", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_02: 21WERBGR (488.2, 457.4) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_02 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_02...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_02,  utils_obj.sec2loc(488, 457)
		if self.authorize_actor(ctrl_class, "GTH02_02"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH02_02", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_08: 20ORCSHM (497.3, 458.4) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_08 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_08...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_08,  utils_obj.sec2loc(497, 458)
		if self.authorize_actor(ctrl_class, "GTH02_08"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_08", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_07: 20ORCSHM (491.2, 459.6) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_07 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_07...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_07,  utils_obj.sec2loc(491, 459)
		if self.authorize_actor(ctrl_class, "GTH02_07"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH02_07", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_06: 20ORCACH (480.7, 451.5) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_06 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_06...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_06,  utils_obj.sec2loc(480, 451)
		if self.authorize_actor(ctrl_class, "GTH02_06"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "GTH02_06", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_05: 20ORCACH (485.5, 450.6) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_05 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_05...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_05,  utils_obj.sec2loc(485, 450)
		if self.authorize_actor(ctrl_class, "GTH02_05"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_05", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_03: 20ORCA3 (480.7, 451.5) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_03 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_03...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_03,  utils_obj.sec2loc(480, 451)
		if self.authorize_actor(ctrl_class, "GTH02_03"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "GTH02_03", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_04: 20ORCA3 (485.5, 450.6) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_04 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_04...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_04,  utils_obj.sec2loc(485, 450)
		if self.authorize_actor(ctrl_class, "GTH02_04"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_04", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Ogre: 21OGR (491.2, 449.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21OGR_AR2100_Ogre 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21OGR_AR2100_Ogre...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21OGR_AR2100_Ogre,  utils_obj.sec2loc(491, 449)
		if self.authorize_actor(ctrl_class, "Ogre"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Ogre", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider Queen: 21SPDQN (472.4, 463.9) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDQN_AR2100_Spider_Queen 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDQN_AR2100_Spider_Queen...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDQN_AR2100_Spider_Queen,  utils_obj.sec2loc(472, 463)
		if self.authorize_actor(ctrl_class, "Spider Queen"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider Queen", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider: 21SPDSML (478.6, 463.2) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider,  utils_obj.sec2loc(478, 463)
		if self.authorize_actor(ctrl_class, "Spider"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider 2: 21SPDSML (475.6, 466.8) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_2 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_2...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_2,  utils_obj.sec2loc(475, 466)
		if self.authorize_actor(ctrl_class, "Spider 2"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider 2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider 3: 21SPDSML (475.5, 464.1) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_3 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_3...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_3,  utils_obj.sec2loc(475, 464)
		if self.authorize_actor(ctrl_class, "Spider 3"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider 3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider 4: 21SPDSML (477.2, 465.8) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_4 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_4...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_4,  utils_obj.sec2loc(477, 465)
		if self.authorize_actor(ctrl_class, "Spider 4"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider 4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider 5: 21SPDSML (480.4, 463.4) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_5 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_5...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_5,  utils_obj.sec2loc(480, 463)
		if self.authorize_actor(ctrl_class, "Spider 5"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider 5", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider 6: 21SPDSML (479.5, 467.2) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_6 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_6...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider_6,  utils_obj.sec2loc(479, 467)
		if self.authorize_actor(ctrl_class, "Spider 6"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider 6", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Highland Snake: 21HGHSNK (468.7, 502.7) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake,  utils_obj.sec2loc(468, 502)
		if self.authorize_actor(ctrl_class, "Highland Snake"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Highland Snake", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Highland Snake 2: 21HGHSNK (477.8, 500.9) const_toee.ROT11 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_2 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_2...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_2,  utils_obj.sec2loc(477, 500)
		if self.authorize_actor(ctrl_class, "Highland Snake 2"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Highland Snake 2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Highland Snake 3: 21HGHSNK (460.9, 502.2) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_3 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_3...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_3,  utils_obj.sec2loc(460, 502)
		if self.authorize_actor(ctrl_class, "Highland Snake 3"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Highland Snake 3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy: 21HRP (458.5, 471.2) const_toee.ROT08 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy,  utils_obj.sec2loc(458, 471)
		if self.authorize_actor(ctrl_class, "Harpy"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Harpy", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy 2: 21HRP (462.4, 467.3) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_2 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_2...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_2,  utils_obj.sec2loc(462, 467)
		if self.authorize_actor(ctrl_class, "Harpy 2"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Harpy 2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy 3: 21HRP (466.9, 471.2) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_3 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_3...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_3,  utils_obj.sec2loc(466, 471)
		if self.authorize_actor(ctrl_class, "Harpy 3"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Harpy 3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy 4: 21HRP (461.5, 475.1) const_toee.ROT08 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_4 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_4...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy_4,  utils_obj.sec2loc(461, 475)
		if self.authorize_actor(ctrl_class, "Harpy 4"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Harpy 4", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Verbeeg: 21VERB (448.7, 486.9) const_toee.ROT08 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg,  utils_obj.sec2loc(448, 486)
		if self.authorize_actor(ctrl_class, "Verbeeg"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Verbeeg", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Verbeeg 2: 21VERB (459.1, 485.1) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg_2 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg_2...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg_2,  utils_obj.sec2loc(459, 485)
		if self.authorize_actor(ctrl_class, "Verbeeg 2"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Verbeeg 2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Verbeeg 3: 21VERB (450.9, 482.7) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg_3 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg_3...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg_3,  utils_obj.sec2loc(450, 482)
		if self.authorize_actor(ctrl_class, "Verbeeg 3"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Verbeeg 3", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Wererat_Scripted_Event: 21WERRAT (466.9, 489.6) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event,  utils_obj.sec2loc(466, 489)
		if self.authorize_actor(ctrl_class, "Wererat_Scripted_Event"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Wererat_Scripted_Event", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Emma: 20EMMA (516.9, 476.5) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20EMMA_AR2100_Emma hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20EMMA_AR2100_Emma...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20EMMA_AR2100_Emma,  utils_obj.sec2loc(516, 476)
		if self.authorize_actor(ctrl_class, "Emma"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Emma", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Kristian: 20KRIS (517.2, 474.7) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KRIS_AR2100_Kristian hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KRIS_AR2100_Kristian...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KRIS_AR2100_Kristian,  utils_obj.sec2loc(517, 474)
		if self.authorize_actor(ctrl_class, "Kristian"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Kristian", 0, 1)
			self.actor_created(npc, ctrl)
		
		# WarriorofVirtue1: 20KNTVIR (518.7, 473.2) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue1 hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue1...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue1,  utils_obj.sec2loc(518, 473)
		if self.authorize_actor(ctrl_class, "WarriorofVirtue1"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "WarriorofVirtue1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# WarriorofVirtue2: 20KNTVIR (519.0, 475.1) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue2 hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue2...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue2,  utils_obj.sec2loc(519, 475)
		if self.authorize_actor(ctrl_class, "WarriorofVirtue2"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "WarriorofVirtue2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# WarriorofVirtue3: 20KNTVIR (518.4, 477.1) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue3 hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue3...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue3,  utils_obj.sec2loc(518, 477)
		if self.authorize_actor(ctrl_class, "WarriorofVirtue3"):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "WarriorofVirtue3", 0, 1)
			self.actor_created(npc, ctrl)
		
		return

	def setup_ambients_auto(self):
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(481, 444)
		amb.setup(name="Dstnt rocks falling", flags="Enabled, IgnoreRadius, RandomOrder", frequency=30, frequency_variation=10, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4316, durationf=10.712336, volume=70, title="AR2100\Dstnt rocks falling AM2100B1")
		amb.setup_sound(sound_id=4317, durationf=6.147937, volume=70, title="AR2100\Dstnt rocks falling AM2100B2")
		amb.setup_sound(sound_id=4318, durationf=6.6722, volume=70, title="AR2100\Dstnt rocks falling AM2100B3")
		amb.setup_sound(sound_id=4319, durationf=12.391202, volume=70, title="AR2100\Dstnt rocks falling AM2100B4")
		amb.setup_sound(sound_id=4320, durationf=4.575238, volume=70, title="AR2100\Dstnt rocks falling AM2100B5")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(481, 444)
		amb.setup(name="wind gusts", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4276, durationf=5.042404, volume=80, title="AR2000\wind gusts AM2000A1")
		amb.setup_sound(sound_id=4277, durationf=9.473741, volume=80, title="AR2000\wind gusts AM2000A2")
		amb.setup_sound(sound_id=4278, durationf=9.845261, volume=80, title="AR2000\wind gusts AM2000A3")
		amb.setup_sound(sound_id=4279, durationf=8.916463, volume=80, title="AR2000\wind gusts AM2000A4")
		self.ambients.append(amb)
		
		
		self.ambs_timer_start()
		return

	def actor_created(self, npc, ctrl):
		super(CtrlAR2100, self).actor_created(npc, ctrl)
		# debug only
		#npc.npc_flag_unset(toee.ONF_KOS)
		return

	def authorize_actor(self, ctrl, name = None):
		result = super(CtrlAR2100, self).authorize_actor(ctrl, name)
		if result:
			if name == "Wererat_Scripted_Event": return 0 # skip this for now
			#if issubclass(ctrl, py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake): return 1
			#if issubclass(ctrl, py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_2): return 1
			#if issubclass(ctrl, py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake_3): return 1
			if name == "Gaernat Sharptooth": return 1
			if name.startswith("GTH01"): return 1
			return 0
		return result
