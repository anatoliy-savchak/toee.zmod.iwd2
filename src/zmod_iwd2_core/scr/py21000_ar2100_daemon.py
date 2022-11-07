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
		return
	
	def place_npcs_auto(self):
		# Gaernat Sharptooth: 21GAERNT (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21GAERNT_AR2100_Gaernat_Sharptooth,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Gaernat Sharptooth", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_01: 21WERRAT (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_01 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_01...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_01,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_01", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_03: 21WERRAT (0.0, 0.0) const_toee.ROT09 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_03 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_03...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_03,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "GTH01_03", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_09: 21WERRAT (0.0, 0.0) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_09 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_09...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH01_09,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH01_09", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_02: 21WERBGR (0.0, 0.0) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_02 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_02...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_02,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH01_02", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_10: 21WERBGR (0.0, 0.0) const_toee.ROT11 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_10 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_10...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_10,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "GTH01_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_06: 21WERBGR (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_06 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_06...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH01_06,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH01_06", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_07: 20ORCSHM (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_07 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_07...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_07,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH01_07", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_08: 20ORCSHM (0.0, 0.0) const_toee.ROT09 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_08 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_08...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_08,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "GTH01_08", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_11: 20ORCSHM (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_11 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_11...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH01_11,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_11", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_05: 20ORCACH (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_05 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_05...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_05,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_05", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_04: 20ORCACH (0.0, 0.0) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_04 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_04...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_04,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH01_04", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH01_12: 20ORCACH (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_12 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_12...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH01_12,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "GTH01_12", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_10: 21WERRAT (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_10 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_10...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_10,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH02_10", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_01: 21WERRAT (0.0, 0.0) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_01 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_01...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_GTH02_01,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_01", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_09: 21WERBGR (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_09 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_09...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_09,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH02_09", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_02: 21WERBGR (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_02 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_02...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERBGR_AR2100_GTH02_02,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "GTH02_02", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_08: 20ORCSHM (0.0, 0.0) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_08 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_08...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_08,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_08", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_07: 20ORCSHM (0.0, 0.0) const_toee.ROT00 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_07 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_07...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCSHM_AR2100_GTH02_07,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "GTH02_07", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_06: 20ORCACH (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_06 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_06...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_06,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "GTH02_06", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_05: 20ORCACH (0.0, 0.0) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_05 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_05...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCACH_AR2100_GTH02_05,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_05", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_03: 20ORCA3 (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_03 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_03...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_03,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "GTH02_03", 0, 1)
			self.actor_created(npc, ctrl)
		
		# GTH02_04: 20ORCA3 (0.0, 0.0) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_04 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_04...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20ORCA3_AR2100_GTH02_04,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "GTH02_04", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Ogre: 21OGR (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21OGR_AR2100_Ogre 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21OGR_AR2100_Ogre...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21OGR_AR2100_Ogre,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Ogre", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider Queen: 21SPDQN (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDQN_AR2100_Spider_Queen 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDQN_AR2100_Spider_Queen...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDQN_AR2100_Spider_Queen,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider Queen", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider: 21SPDSML (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider: 21SPDSML (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider: 21SPDSML (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider: 21SPDSML (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider: 21SPDSML (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Spider: 21SPDSML (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21SPDSML_AR2100_Spider,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Spider", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Highland Snake: 21HGHSNK (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Highland Snake", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Highland Snake: 21HGHSNK (0.0, 0.0) const_toee.ROT11 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Highland Snake", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Highland Snake: 21HGHSNK (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HGHSNK_AR2100_Highland_Snake,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Highland Snake", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy: 21HRP (0.0, 0.0) const_toee.ROT08 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Harpy", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy: 21HRP (0.0, 0.0) const_toee.ROT05 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Harpy", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy: 21HRP (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Harpy", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Harpy: 21HRP (0.0, 0.0) const_toee.ROT08 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21HRP_AR2100_Harpy,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Harpy", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Verbeeg: 21VERB (0.0, 0.0) const_toee.ROT08 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Verbeeg", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Verbeeg: 21VERB (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Verbeeg", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Verbeeg: 21VERB (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21VERB_AR2100_Verbeeg,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Verbeeg", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Wererat_Scripted_Event: 21WERRAT (0.0, 0.0) const_toee.ROT06 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event 
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_21WERRAT_AR2100_Wererat_Scripted_Event,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Wererat_Scripted_Event", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Emma: 20EMMA (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20EMMA_AR2100_Emma hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20EMMA_AR2100_Emma...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20EMMA_AR2100_Emma,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Emma", 0, 1)
			self.actor_created(npc, ctrl)
		
		# Kristian: 20KRIS (0.0, 0.0) const_toee.ROT03 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KRIS_AR2100_Kristian hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KRIS_AR2100_Kristian...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KRIS_AR2100_Kristian,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "Kristian", 0, 1)
			self.actor_created(npc, ctrl)
		
		# WarriorofVirtue1: 20KNTVIR (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue1 hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue1...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue1,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "WarriorofVirtue1", 0, 1)
			self.actor_created(npc, ctrl)
		
		# WarriorofVirtue2: 20KNTVIR (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue2 hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue2...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue2,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "WarriorofVirtue2", 0, 1)
			self.actor_created(npc, ctrl)
		
		# WarriorofVirtue3: 20KNTVIR (0.0, 0.0) const_toee.ROT02 ctrl: py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue3 hidden
		print("Creating py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue3...")
		ctrl_class, loc = py21004_ar2100_npc_inst_classes.Ctrl_20KNTVIR_AR2100_WarriorofVirtue3,  utils_obj.sec2loc(0, 0)
		if self.authorize_actor(ctrl_class):
			npc, ctrl = self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "WarriorofVirtue3", 0, 1)
			self.actor_created(npc, ctrl)
		
		return

	def setup_ambients_auto(self):
		return
