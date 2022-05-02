import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals
import ctrl_daemon_ie, ctrl_ambients
#### NPCS IMPORT ####
import py10001_ar1000_npcs
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

		#cabb = toee.game.obj_create(2068, utils_obj.sec2loc(448, 493))
		#ctrl_daemon_ie.global_injector().set_name("cabb", cabb)
		#cabb.obj_set_int(toee.obj_f_sound_effect, 4111)
		#cabb.obj_set_int(toee.obj_f_scenery_flags, const_toee.OSCF_SOUND_EXTRA_LARGE)
		#print("cabb flags: {}, obj: {}", utils_obj.get_scenery_flags_to_str(cabb), cabb)
		#cabb2 = None
		#for obj in toee.game.obj_list_range(utils_obj.sec2loc(495, 454), 50, toee.OLC_SCENERY):
		#	cabb2 = obj
		#	break
		#if cabb2:
		#	print("cabb2 flags: {}, obj: {}", utils_obj.get_scenery_flags_to_str(cabb2), cabb2)
		#	#debug.breakp("cabb")
		#self.iSetGlobal(name='Know_Hedron', area='GLOBAL', value=1)
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
		# Hedron: 10HEDRON (448.9, 493.1) const_toee.ROT09 ctrl: py10001_ar1000_npcs.Ctrl10HEDRON 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10HEDRON,  utils_obj.sec2loc(448, 493)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "Hedron", 0, 1)
		
		# Eldgull: 10ELDGUL (446.7, 499.0) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10ELDGUL 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10ELDGUL,  utils_obj.sec2loc(446, 499)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Eldgull", 0, 1)
		
		# Screed: 10SCREED (459.2, 478.7) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10SCREED 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10SCREED,  utils_obj.sec2loc(459, 478)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Screed", 0, 1)
		
		# Reig: 10REIG (475.4, 466.7) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10REIG 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10REIG,  utils_obj.sec2loc(475, 466)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Reig", 0, 1)
		
		# Jon: 10JON (479.4, 466.8) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10JON 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10JON,  utils_obj.sec2loc(479, 466)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Jon", 0, 1)
		
		# Brogan: 10BROGAN (447.2, 468.5) const_toee.ROT11 ctrl: py10001_ar1000_npcs.Ctrl10BROGAN 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10BROGAN,  utils_obj.sec2loc(447, 468)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Brogan", 0, 1)
		
		# Jorun: 10JORUN (515.5, 466.5) const_toee.ROT11 ctrl: py10001_ar1000_npcs.Ctrl10JORUN 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10JORUN,  utils_obj.sec2loc(515, 466)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Jorun", 0, 1)
		
		# 1000_Goblin_01: 10GOB (493.9, 438.4) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(493, 438)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "1000_Goblin_01", 0, 1)
		
		# Dead_Goblin_0: 10GOBD (500.9, 447.1) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10GOBD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBD,  utils_obj.sec2loc(500, 447)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Dead_Goblin_0", 0, 1)
		
		# Dead_Townsperson_0: 10MALED (501.6, 451.1) const_toee.ROT11 ctrl: py10001_ar1000_npcs.Ctrl10MALED 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10MALED,  utils_obj.sec2loc(501, 451)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "Dead_Townsperson_0", 0, 1)
		
		# Brohn_Dead: 10SOLDRD (477.4, 466.6) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10SOLDRD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10SOLDRD,  utils_obj.sec2loc(477, 466)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Brohn_Dead", 0, 1)
		
		# Dead_Goblin_1: 10GOBD (462.7, 461.9) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10GOBD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBD,  utils_obj.sec2loc(462, 461)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Dead_Goblin_1", 0, 1)
		
		# Dead_Goblin_2: 10GOBD (463.3, 455.5) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10GOBD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBD,  utils_obj.sec2loc(463, 455)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Dead_Goblin_2", 0, 1)
		
		# Dead_Goblin_3: 10GOBD (447.5, 458.8) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10GOBD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBD,  utils_obj.sec2loc(447, 458)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Dead_Goblin_3", 0, 1)
		
		# Dead_Soldier_0: 10SOLDRD (448.5, 456.7) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10SOLDRD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10SOLDRD,  utils_obj.sec2loc(448, 456)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Dead_Soldier_0", 0, 1)
		
		# Dead_Goblin_J1: 10GOBD (515.9, 464.0) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10GOBD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBD,  utils_obj.sec2loc(515, 464)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Dead_Goblin_J1", 0, 1)
		
		# Dead_Goblin_J2: 10GOBD (516.0, 470.9) const_toee.ROT09 ctrl: py10001_ar1000_npcs.Ctrl10GOBD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBD,  utils_obj.sec2loc(516, 470)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "Dead_Goblin_J2", 0, 1)
		
		# Dead_Goblin_6: 10GOBD (519.7, 466.7) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOBD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBD,  utils_obj.sec2loc(519, 466)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "Dead_Goblin_6", 0, 1)
		
		# 1000_Goblin_02: 10GOB (531.8, 481.3) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(531, 481)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_02", 0, 1)
		
		# 1000_Goblin_03: 10GOB (526.3, 480.9) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(526, 480)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "1000_Goblin_03", 0, 1)
		
		# Dead_Townsperson_1: 10MALED (528.8, 480.0) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10MALED 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10MALED,  utils_obj.sec2loc(528, 480)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "Dead_Townsperson_1", 0, 1)
		
		# Dead_Goblin_7: 10GOBARD (506.5, 497.0) const_toee.ROT00 ctrl: py10001_ar1000_npcs.Ctrl10GOBARD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBARD,  utils_obj.sec2loc(506, 497)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT00, "Dead_Goblin_7", 0, 1)
		
		# Dead_Soldier_1: 10SOLDRD (501.4, 490.6) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10SOLDRD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10SOLDRD,  utils_obj.sec2loc(501, 490)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "Dead_Soldier_1", 0, 1)
		
		# Dead_Sailor: 10SAILRD (476.2, 506.8) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10SAILRD 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10SAILRD,  utils_obj.sec2loc(476, 506)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Dead_Sailor", 0, 1)
		
		# 1000_Goblin_04: 10GOB (477.1, 504.7) const_toee.ROT03 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(477, 504)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "1000_Goblin_04", 0, 1)
		
		# 1000_Goblin_05: 10GOB (478.6, 506.9) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(478, 506)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_05", 0, 1)
		
		# 1000_Goblin_06: 10GOB (506.0, 526.9) const_toee.ROT09 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(506, 526)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "1000_Goblin_06", 0, 1)
		
		# 1000_Goblin_Archer_01: 10GOBAR (502.2, 525.9) const_toee.ROT11 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(502, 525)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT11, "1000_Goblin_Archer_01", 0, 1)
		
		# 1000_Goblin_07: 10GOB (502.4, 529.4) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(502, 529)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_07", 0, 1)
		
		# 1000_Goblin_19: 10GOB (506.1, 523.8) const_toee.ROT09 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(506, 523)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "1000_Goblin_19", 0, 1)
		
		# 1000_Goblin_Archer_02: 10GOBAR (505.2, 529.8) const_toee.ROT09 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(505, 529)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "1000_Goblin_Archer_02", 0, 1)
		
		# 1000_Goblin_08: 10GOB (501.1, 533.1) const_toee.ROT03 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(501, 533)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "1000_Goblin_08", 0, 1)
		
		# 1000_Goblin_Archer_03: 10GOBAR (535.5, 476.1) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(535, 476)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_Archer_03", 0, 1)
		
		# 1000_Goblin_09: 10GOB (527.9, 489.2) const_toee.ROT03 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(527, 489)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "1000_Goblin_09", 0, 1)
		
		# 1000_Goblin_10: 10GOB (535.3, 488.0) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(535, 488)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "1000_Goblin_10", 0, 1)
		
		# 1000_Goblin_Archer_04: 10GOBAR (530.7, 485.3) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(530, 485)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_Archer_04", 0, 1)
		
		# 1000_Goblin_11: 10GOB (498.6, 439.4) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(498, 439)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "1000_Goblin_11", 0, 1)
		
		# 1000_Goblin_12: 10GOB (487.9, 442.1) const_toee.ROT03 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(487, 442)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT03, "1000_Goblin_12", 0, 1)
		
		# 1000_Goblin_Archer_05: 10GOBAR (496.6, 433.1) const_toee.ROT05 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(496, 433)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT05, "1000_Goblin_Archer_05", 0, 1)
		
		# 1000_Goblin_Archer_06: 10GOBAR (502.7, 438.4) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(502, 438)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "1000_Goblin_Archer_06", 0, 1)
		
		# 1000_Goblin_Archer_07: 10GOBAR (473.9, 507.2) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(473, 507)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "1000_Goblin_Archer_07", 0, 1)
		
		# 1000_Goblin_Archer_08: 10GOBAR (473.9, 509.6) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(473, 509)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "1000_Goblin_Archer_08", 0, 1)
		
		# 1000_Goblin_13: 10GOB (480.9, 503.7) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(480, 503)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "1000_Goblin_13", 0, 1)
		
		# 1000_Goblin_14: 10GOB (502.3, 479.0) const_toee.ROT09 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(502, 479)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "1000_Goblin_14", 0, 1)
		
		# 1000_Goblin_15: 10GOB (501.0, 485.7) const_toee.ROT06 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(501, 485)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT06, "1000_Goblin_15", 0, 1)
		
		# 1000_Goblin_Archer_09: 10GOBAR (498.7, 481.6) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(498, 481)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "1000_Goblin_Archer_09", 0, 1)
		
		# 1000_Goblin_16: 10GOB (532.2, 501.8) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(532, 501)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_16", 0, 1)
		
		# 1000_Goblin_17: 10GOB (522.8, 505.4) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(522, 505)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "1000_Goblin_17", 0, 1)
		
		# 1000_Goblin_18: 10GOB (524.4, 511.6) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOB 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOB,  utils_obj.sec2loc(524, 511)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_18", 0, 1)
		
		# 1000_Goblin_Archer_10: 10GOBAR (533.9, 505.7) const_toee.ROT02 ctrl: py10001_ar1000_npcs.Ctrl10GOBAR 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10GOBAR,  utils_obj.sec2loc(533, 505)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT02, "1000_Goblin_Archer_10", 0, 1)
		
		# Crandall: 10CRANDA (503.0, 507.4) const_toee.ROT09 ctrl: py10001_ar1000_npcs.Ctrl10CRANDA 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10CRANDA,  utils_obj.sec2loc(503, 507)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT09, "Crandall", 0, 1)
		
		# Swift Thomas (Hidden): 12SWIFTH (503.3, 441.5) const_toee.ROT05 ctrl: None.None hidden
		
		# Dead_Townsperson_2: 10MALED (547.2, 485.7) const_toee.ROT08 ctrl: py10001_ar1000_npcs.Ctrl10MALED 
		ctrl_class, loc = py10001_ar1000_npcs.Ctrl10MALED,  utils_obj.sec2loc(547, 485)
		self.create_npc_at(loc, ctrl_class, const_toee.ROT08, "Dead_Townsperson_2", 0, 1)
		
		# Door_Hint_Text_00: 10HINT (475.3, 443.0) const_toee.ROT06 ctrl: None.None hidden
		
		# Door_Hint_Text_01: 10HINT (442.2, 478.9) const_toee.ROT06 ctrl: None.None hidden
		
		# Firtha Kerdos: 10FIRTHH (529.7, 495.4) const_toee.ROT06 ctrl: None.None hidden
		
		return

	def setup_ambients(self):
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(482, 402)
		npc, ctrl = self.create_ambient(loc, ctrl_class, "Walla")
		ctrl.setup(name="Walla", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, x=482, y=402, schedule="ALL")
		ctrl.setup_sound(sound_id=4109, durationf=1.801814, volume=70, title="AR1000\Walla AM1000D1")
		ctrl.setup_sound(sound_id=4110, durationf=1.668345, volume=70, title="AR1000\Walla AM1000D2")
		ctrl.setup_sound(sound_id=4111, durationf=1.134467, volume=70, title="AR1000\Walla AM1000D3")
		ctrl.setup_sound(sound_id=4112, durationf=2.035374, volume=70, title="AR1000\Walla AM1000D4")
		ctrl.setup_sound(sound_id=4113, durationf=1.801814, volume=70, title="AR1000\Walla AM1000D5")
		ctrl.setup_sound(sound_id=4114, durationf=2.636009, volume=70, title="AR1000\Walla AM1000D6")
		ctrl.setup_sound(sound_id=4115, durationf=3.9039, volume=70, title="AR1000\Walla AM1000D7")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(527, 477)
		npc, ctrl = self.create_ambient(loc, ctrl_class, "Horn_Blow")
		ctrl.setup(name="Horn_Blow", flags="Enabled, IgnoreRadius", frequency=30, frequency_variation=5, radius=100, x=527, y=477, schedule="ALL")
		ctrl.setup_sound(sound_id=4116, durationf=4.331565, volume=90, title="AR1000\Horn_Blow AM1000J")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(481, 419)
		npc, ctrl = self.create_ambient(loc, ctrl_class, "goblin_walla")
		ctrl.setup(name="goblin_walla", flags="Enabled, IgnoreRadius, RandomOrder", frequency=20, frequency_variation=10, radius=500, x=481, y=419, schedule="ALL")
		ctrl.setup_sound(sound_id=4117, durationf=7.282721, volume=75, title="AR1000\goblin_walla AM1000F1")
		ctrl.setup_sound(sound_id=4118, durationf=3.48907, volume=75, title="AR1000\goblin_walla AM1000F2")
		ctrl.setup_sound(sound_id=4119, durationf=4.923673, volume=75, title="AR1000\goblin_walla AM1000F3")
		ctrl.setup_sound(sound_id=4120, durationf=6.028889, volume=75, title="AR1000\goblin_walla AM1000F4")
		ctrl.setup_sound(sound_id=4121, durationf=4.349569, volume=75, title="AR1000\goblin_walla AM1000F5")
		ctrl.setup_sound(sound_id=4122, durationf=4.055918, volume=75, title="AR1000\goblin_walla AM1000F6")
		ctrl.setup_sound(sound_id=4123, durationf=4.761179, volume=75, title="AR1000\goblin_walla AM1000F7")
		ctrl.setup_sound(sound_id=4124, durationf=3.722993, volume=75, title="AR1000\goblin_walla AM1000F8")
		ctrl.setup_sound(sound_id=4125, durationf=4.497143, volume=75, title="AR1000\goblin_walla AM1000F9")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(471, 488)
		npc, ctrl = self.create_ambient(loc, ctrl_class, None)
		ctrl.setup(name="Water laps1", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=1200, x=471, y=488, schedule="ALL")
		ctrl.setup_sound(sound_id=4126, durationf=3.180363, volume=70, title="AR1000\Water laps1 AM1000A1")
		ctrl.setup_sound(sound_id=4127, durationf=2.797007, volume=70, title="AR1000\Water laps1 AM1000A2")
		ctrl.setup_sound(sound_id=4128, durationf=3.360136, volume=70, title="AR1000\Water laps1 AM1000A3")
		ctrl.setup_sound(sound_id=4129, durationf=3.220816, volume=70, title="AR1000\Water laps1 AM1000A4")
		ctrl.setup_sound(sound_id=4130, durationf=3.722585, volume=70, title="AR1000\Water laps1 AM1000A5")
		ctrl.setup_sound(sound_id=4131, durationf=3.123673, volume=70, title="AR1000\Water laps1 AM1000A6")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(460, 492)
		npc, ctrl = self.create_ambient(loc, ctrl_class, None)
		ctrl.setup(name="Dock Creaks1", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=1200, x=460, y=492, schedule="ALL")
		ctrl.setup_sound(sound_id=4132, durationf=2.911156, volume=60, title="AR1000\Dock Creaks1 AM1000B1")
		ctrl.setup_sound(sound_id=4133, durationf=2.328934, volume=60, title="AR1000\Dock Creaks1 AM1000B2")
		ctrl.setup_sound(sound_id=4134, durationf=3.767347, volume=60, title="AR1000\Dock Creaks1 AM1000B3")
		ctrl.setup_sound(sound_id=4135, durationf=4.462993, volume=60, title="AR1000\Dock Creaks1 AM1000B4")
		ctrl.setup_sound(sound_id=4136, durationf=3.065215, volume=60, title="AR1000\Dock Creaks1 AM1000B5")
		ctrl.setup_sound(sound_id=4137, durationf=3.536508, volume=60, title="AR1000\Dock Creaks1 AM1000B6")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(452, 483)
		npc, ctrl = self.create_ambient(loc, ctrl_class, None)
		ctrl.setup(name="Sail Flaps1", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=300, x=452, y=483, schedule="ALL")
		ctrl.setup_sound(sound_id=4138, durationf=3.948345, volume=70, title="AR1000\Sail Flaps1 AM1000M1")
		ctrl.setup_sound(sound_id=4139, durationf=4.373333, volume=70, title="AR1000\Sail Flaps1 AM1000M2")
		ctrl.setup_sound(sound_id=4140, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M3")
		ctrl.setup_sound(sound_id=4141, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M4")
		ctrl.setup_sound(sound_id=4142, durationf=2.998367, volume=70, title="AR1000\Sail Flaps1 AM1000M5")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(470, 518)
		npc, ctrl = self.create_ambient(loc, ctrl_class, None)
		ctrl.setup(name="Sail Flaps2", flags="Enabled, RandomOrder", frequency=5, frequency_variation=0, radius=500, x=470, y=518, schedule="ALL")
		ctrl.setup_sound(sound_id=4138, durationf=3.948345, volume=70, title="AR1000\Sail Flaps1 AM1000M1")
		ctrl.setup_sound(sound_id=4139, durationf=4.373333, volume=70, title="AR1000\Sail Flaps1 AM1000M2")
		ctrl.setup_sound(sound_id=4140, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M3")
		ctrl.setup_sound(sound_id=4141, durationf=3.601678, volume=70, title="AR1000\Sail Flaps1 AM1000M4")
		ctrl.setup_sound(sound_id=4142, durationf=2.998367, volume=70, title="AR1000\Sail Flaps1 AM1000M5")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(534, 494)
		npc, ctrl = self.create_ambient(loc, ctrl_class, "cat_singles_exterior")
		ctrl.setup(name="cat_singles_exterior", flags="Enabled, RandomOrder", frequency=3, frequency_variation=0, radius=800, x=534, y=494, schedule="ALL")
		ctrl.setup_sound(sound_id=4143, durationf=0.940181, volume=100, title="AR1000\cat_singles_exterior AM1000P1")
		ctrl.setup_sound(sound_id=4144, durationf=1.3639, volume=100, title="AR1000\cat_singles_exterior AM1000P2")
		ctrl.setup_sound(sound_id=4145, durationf=1.08585, volume=100, title="AR1000\cat_singles_exterior AM1000P3")
		ctrl.setup_sound(sound_id=4146, durationf=1.092472, volume=100, title="AR1000\cat_singles_exterior AM1000P4")
		ctrl.setup_sound(sound_id=4147, durationf=1.08585, volume=100, title="AR1000\cat_singles_exterior AM1000P5")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(490, 538)
		npc, ctrl = self.create_ambient(loc, ctrl_class, None)
		ctrl.setup(name="lighthouse loop", flags="Enabled, Looping", frequency=0, frequency_variation=0, radius=900, x=490, y=538, schedule="ALL")
		ctrl.setup_sound(sound_id=4148, durationf=9.029478, volume=55, title="AR1000\lighthouse loop AM1000K")
		ctrl.run(npc)
		
		ctrl_class, loc = ctrl_ambients.CtrlAmbient,  utils_obj.sec2loc(512, 482)
		npc, ctrl = self.create_ambient(loc, ctrl_class, None)
		ctrl.setup(name="tavern_walla_ext", flags="Enabled, RandomOrder", frequency=10, frequency_variation=0, radius=900, x=512, y=482, schedule="ALL")
		ctrl.setup_sound(sound_id=4149, durationf=6.027302, volume=60, title="AR1000\tavern_walla_ext AM1000I1")
		ctrl.setup_sound(sound_id=4150, durationf=3.67034, volume=60, title="AR1000\tavern_walla_ext AM1000I2")
		ctrl.setup_sound(sound_id=4151, durationf=4.838186, volume=60, title="AR1000\tavern_walla_ext AM1000I3")
		ctrl.setup_sound(sound_id=4152, durationf=6.64, volume=60, title="AR1000\tavern_walla_ext AM1000I4")
		ctrl.setup_sound(sound_id=4153, durationf=5.138503, volume=60, title="AR1000\tavern_walla_ext AM1000I5")
		ctrl.setup_sound(sound_id=4154, durationf=2.636009, volume=60, title="AR1000\tavern_walla_ext AM1000I6")
		ctrl.setup_sound(sound_id=4155, durationf=6.373061, volume=60, title="AR1000\tavern_walla_ext AM1000I7")
		ctrl.run(npc)
		return
