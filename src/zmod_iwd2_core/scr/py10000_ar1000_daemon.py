import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals
import ctrl_daemon_ie, ctrl_ambients
#### NPCS IMPORT ####
import py10006_ar1000_scripts
import py10004_ar1000_npc_inst_classes
#### NPCS IMPORT END ####

DAEMON_SCRIPT_ID = 10000
DAEMON_MAP_ID = module_consts.MAP_ID_TARGOS_DOCKS
DAEMON_GID = "G_53D450E2_29FE_401E_BE97_20F806DF94FA"

def san_new_map(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, DAEMON_MAP_ID, CtrlTargosDocks)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, DAEMON_MAP_ID, CtrlTargosDocks)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, DAEMON_MAP_ID, cs())

def san_bust(attachee, triggerer):
	return ctrl_daemon2.do_san_bust(attachee, triggerer, DAEMON_MAP_ID, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): 
		return None
	result = o.data.get(CtrlTargosDocks.get_name())
	assert isinstance(result, CtrlTargosDocks)
	return result

class CtrlTargosDocks(ctrl_daemon_ie.CtrlDaemonIE):
	def created(self, npc):
		self.init_daemon2_fields(DAEMON_MAP_ID, DAEMON_SCRIPT_ID, "targos_docks")
		super(CtrlTargosDocks, self).created(npc)
		return

	def place_encounters_initial(self):
		self.place_portals()
		self.place_doors()
		self.setup_ambients()
		self.place_npcs()

		self.debug_glob_npcs()
		return

	def place_encounters_next(self):
		# TODO = verify that it's triggered only when returning to map, not loading
		return

	# Sleep interface
	def can_sleep(self):
		return toee.SLEEP_IMPOSSIBLE

	def heartbeat(self, npc):
		#print("CtrlTargosDocks heartbeat")
		for handler in self.ambients:
			handler.tick()
		return

	def place_portals(self):
		return

	def place_doors(self):
		return
	
	def place_npcs(self):
		# Hedron: 10HEDRON (448.9, 493.1) const_toee.ROT09 ctrl: py10004_ar1000_npc_inst_classes.Ctrl_10HEDRON_AR1000_Hedron 
		ctrl_class, loc = py10004_ar1000_npc_inst_classes.Ctrl_10HEDRON_AR1000_Hedron,  utils_obj.sec2loc(448, 493)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "Hedron", 0, 1)
		
		return

	def setup_ambients(self):
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(482, 402)
		amb.setup(name="Walla", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4109, durationf=1.801814, volume=70, title="AR1000\Walla AM1000D1")
		amb.setup_sound(sound_id=4110, durationf=1.668345, volume=70, title="AR1000\Walla AM1000D2")
		amb.setup_sound(sound_id=4111, durationf=1.134467, volume=70, title="AR1000\Walla AM1000D3")
		amb.setup_sound(sound_id=4112, durationf=2.035374, volume=70, title="AR1000\Walla AM1000D4")
		amb.setup_sound(sound_id=4113, durationf=1.801814, volume=70, title="AR1000\Walla AM1000D5")
		amb.setup_sound(sound_id=4114, durationf=2.636009, volume=70, title="AR1000\Walla AM1000D6")
		amb.setup_sound(sound_id=4115, durationf=3.9039, volume=70, title="AR1000\Walla AM1000D7")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(483, 403)
		amb.setup(name="Distant fighting", flags="Enabled, IgnoreRadius, RandomOrder", frequency=30, frequency_variation=15, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4116, durationf=5.772426, volume=70, title="AR1000\Distant fighting AM1000E1")
		amb.setup_sound(sound_id=4117, durationf=7.10712, volume=70, title="AR1000\Distant fighting AM1000E2")
		amb.setup_sound(sound_id=4118, durationf=5.505533, volume=70, title="AR1000\Distant fighting AM1000E3")
		amb.setup_sound(sound_id=4119, durationf=4.070748, volume=70, title="AR1000\Distant fighting AM1000E4")
		amb.setup_sound(sound_id=4120, durationf=5.705714, volume=70, title="AR1000\Distant fighting AM1000E5")
		amb.setup_sound(sound_id=4121, durationf=2.669342, volume=70, title="AR1000\Distant fighting AM1000E6")
		amb.setup_sound(sound_id=4122, durationf=6.395646, volume=70, title="AR1000\Distant fighting AM1000E7")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(527, 477)
		amb.setup(name="Horn_Blow", flags="Enabled, IgnoreRadius", frequency=30, frequency_variation=5, radius=100, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4123, durationf=4.331565, volume=90, title="AR1000\Horn_Blow AM1000J")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(484, 405)
		amb.setup(name="Wind Singles", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4124, durationf=10.643991, volume=75, title="AR1000\Wind Singles AM1000O1")
		amb.setup_sound(sound_id=4125, durationf=6.840181, volume=75, title="AR1000\Wind Singles AM1000O2")
		amb.setup_sound(sound_id=4126, durationf=8.675329, volume=75, title="AR1000\Wind Singles AM1000O3")
		amb.setup_sound(sound_id=4127, durationf=7.507528, volume=75, title="AR1000\Wind Singles AM1000O4")
		amb.setup_sound(sound_id=4128, durationf=7.007029, volume=75, title="AR1000\Wind Singles AM1000O5")
		amb.setup_sound(sound_id=4129, durationf=8.508526, volume=75, title="AR1000\Wind Singles AM1000O6")
		amb.setup_sound(sound_id=4130, durationf=12.2122, volume=75, title="AR1000\Wind Singles AM1000O7")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(481, 419)
		amb.setup(name="goblin_walla", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4131, durationf=7.282721, volume=75, title="AR1000\goblin_walla AM1000F1")
		amb.setup_sound(sound_id=4132, durationf=3.48907, volume=75, title="AR1000\goblin_walla AM1000F2")
		amb.setup_sound(sound_id=4133, durationf=4.923673, volume=75, title="AR1000\goblin_walla AM1000F3")
		amb.setup_sound(sound_id=4134, durationf=6.028889, volume=75, title="AR1000\goblin_walla AM1000F4")
		amb.setup_sound(sound_id=4135, durationf=4.349569, volume=75, title="AR1000\goblin_walla AM1000F5")
		amb.setup_sound(sound_id=4136, durationf=4.055918, volume=75, title="AR1000\goblin_walla AM1000F6")
		amb.setup_sound(sound_id=4137, durationf=4.761179, volume=75, title="AR1000\goblin_walla AM1000F7")
		amb.setup_sound(sound_id=4138, durationf=3.722993, volume=75, title="AR1000\goblin_walla AM1000F8")
		amb.setup_sound(sound_id=4139, durationf=4.497143, volume=75, title="AR1000\goblin_walla AM1000F9")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(471, 488)
		amb.setup(name="Water laps1", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=1200, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4140, durationf=3.180363, volume=70, title="AR1000\Water laps1 AM1000A1")
		amb.setup_sound(sound_id=4141, durationf=2.797007, volume=70, title="AR1000\Water laps1 AM1000A2")
		amb.setup_sound(sound_id=4142, durationf=3.360136, volume=70, title="AR1000\Water laps1 AM1000A3")
		amb.setup_sound(sound_id=4143, durationf=3.220816, volume=70, title="AR1000\Water laps1 AM1000A4")
		amb.setup_sound(sound_id=4144, durationf=3.722585, volume=70, title="AR1000\Water laps1 AM1000A5")
		amb.setup_sound(sound_id=4145, durationf=3.123673, volume=70, title="AR1000\Water laps1 AM1000A6")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(460, 492)
		amb.setup(name="Dock Creaks1", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=1200, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4146, durationf=2.911156, volume=60, title="AR1000\Dock Creaks1 AM1000B1")
		amb.setup_sound(sound_id=4147, durationf=2.328934, volume=60, title="AR1000\Dock Creaks1 AM1000B2")
		amb.setup_sound(sound_id=4148, durationf=3.767347, volume=60, title="AR1000\Dock Creaks1 AM1000B3")
		amb.setup_sound(sound_id=4149, durationf=4.462993, volume=60, title="AR1000\Dock Creaks1 AM1000B4")
		amb.setup_sound(sound_id=4150, durationf=3.065215, volume=60, title="AR1000\Dock Creaks1 AM1000B5")
		amb.setup_sound(sound_id=4151, durationf=3.536508, volume=60, title="AR1000\Dock Creaks1 AM1000B6")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(452, 483)
		amb.setup(name="Sail Flaps1", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=300, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4152, durationf=3.948345, volume=70, title="AR1000\Sail Flaps1 AM1000M1")
		amb.setup_sound(sound_id=4153, durationf=4.373333, volume=70, title="AR1000\Sail Flaps1 AM1000M2")
		amb.setup_sound(sound_id=4154, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M3")
		amb.setup_sound(sound_id=4155, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M4")
		amb.setup_sound(sound_id=4156, durationf=2.998367, volume=70, title="AR1000\Sail Flaps1 AM1000M5")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(470, 518)
		amb.setup(name="Sail Flaps2", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=500, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4152, durationf=3.948345, volume=70, title="AR1000\Sail Flaps1 AM1000M1")
		amb.setup_sound(sound_id=4153, durationf=4.373333, volume=70, title="AR1000\Sail Flaps1 AM1000M2")
		amb.setup_sound(sound_id=4154, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M3")
		amb.setup_sound(sound_id=4155, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M4")
		amb.setup_sound(sound_id=4156, durationf=2.998367, volume=70, title="AR1000\Sail Flaps1 AM1000M5")
		self.ambients.append(amb)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(534, 494)
		amb.setup(name="cat_singles_exterior", flags="Enabled, RandomOrder", frequency=3, frequency_variation=0, radius=800, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4157, durationf=0.940181, volume=100, title="AR1000\cat_singles_exterior AM1000P1")
		amb.setup_sound(sound_id=4158, durationf=1.3639, volume=100, title="AR1000\cat_singles_exterior AM1000P2")
		amb.setup_sound(sound_id=4159, durationf=1.08585, volume=100, title="AR1000\cat_singles_exterior AM1000P3")
		amb.setup_sound(sound_id=4160, durationf=1.092472, volume=100, title="AR1000\cat_singles_exterior AM1000P4")
		amb.setup_sound(sound_id=4161, durationf=1.08585, volume=100, title="AR1000\cat_singles_exterior AM1000P5")
		self.ambients.append(amb)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient, utils_obj.sec2loc(490, 538)
		npc, ctrl = self.create_cabbage(loc, ctrl_class, None)
		ctrl.setup(name="lighthouse loop", flags="Enabled, Looping", frequency=0, frequency_variation=0, radius=900, x=490, y=538, schedule="ALL")
		ctrl.setup_sound(sound_id=4162, durationf=9.029478, volume=55, title="AR1000\lighthouse loop AM1000K")
		ctrl.run(npc)
		
		amb = ctrl_ambients.AmbientHanlder()
		loc = utils_obj.sec2loc(512, 482)
		amb.setup(name="tavern_walla_ext", flags="Enabled, RandomOrder", frequency=10, frequency_variation=0, radius=900, loc=loc, schedule="ALL")
		amb.setup_sound(sound_id=4163, durationf=6.027302, volume=60, title="AR1000\tavern_walla_ext AM1000I1")
		amb.setup_sound(sound_id=4164, durationf=3.67034, volume=60, title="AR1000\tavern_walla_ext AM1000I2")
		amb.setup_sound(sound_id=4165, durationf=4.838186, volume=60, title="AR1000\tavern_walla_ext AM1000I3")
		amb.setup_sound(sound_id=4166, durationf=6.64, volume=60, title="AR1000\tavern_walla_ext AM1000I4")
		amb.setup_sound(sound_id=4167, durationf=5.138503, volume=60, title="AR1000\tavern_walla_ext AM1000I5")
		amb.setup_sound(sound_id=4168, durationf=2.636009, volume=60, title="AR1000\tavern_walla_ext AM1000I6")
		amb.setup_sound(sound_id=4169, durationf=6.373061, volume=60, title="AR1000\tavern_walla_ext AM1000I7")
		self.ambients.append(amb)
		
		self.ambs_timer_start()
		return

	def place_bcs(self):
		self.vars["script_area"] = py10006_ar1000_scripts.Script_AR1000
		return
