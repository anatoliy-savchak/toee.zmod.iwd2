import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals
import py01001_targos_docks_encounters


DAEMON_SCRIPT_ID = 1000
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

class CtrlTargosDocks(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(DAEMON_MAP_ID, DAEMON_SCRIPT_ID, "targos_docks")
		super(CtrlTargosDocks, self).created(npc)
		return

	def place_encounters_initial(self):
		self.place_portals()
		self.place_doors()
		self.place_npcs()
		return

	def place_encounters_next(self):
		self.update_witch()
		return

	# Sleep interface
	def can_sleep(self):
		return toee.SLEEP_IMPOSSIBLE


	def create_lib_foe(self, npc_loc, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1, no_move = 0):
		result = self.create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos, no_move)
		return result

	def place_portals(self):
		return

	def place_doors(self):
		return

	def place_npcs2(self):
		self.create_lib_foe(utils_obj.sec2loc(448, 492), py01001_targos_docks_encounters.Ctrl10HEDRON, const_toee.ROT09, "r01", py01001_targos_docks_encounters.Ctrl10HEDRON.get_name(), factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)
		self.create_lib_foe(utils_obj.sec2loc(446, 499), py01001_targos_docks_encounters.Ctrl10ELDGUL, const_toee.ROT04, "r01", py01001_targos_docks_encounters.Ctrl10ELDGUL.get_name(), factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)
		return

	
	def place_npcs(self):
		# Hedron: 10HEDRON (448.9, 493.1) const_toee.ROT09 ctrl: py01001_targos_docks_encounters.Ctrl10HEDRON 
		ctrl_class, loc = py01001_targos_docks_encounters.Ctrl10HEDRON,  utils_obj.sec2loc(448, 493)
		self.create_lib_foe(loc, ctrl_class, const_toee.ROT09, "", "Hedron", ctrl_class.get_class_faction(), 0, 1)
		
		# Eldgull: 10ELDGUL (446.7, 499.0) const_toee.ROT05 ctrl: py01001_targos_docks_encounters.Ctrl10ELDGUL 
		ctrl_class, loc = py01001_targos_docks_encounters.Ctrl10ELDGUL,  utils_obj.sec2loc(446, 499)
		self.create_lib_foe(loc, ctrl_class, const_toee.ROT05, "", "Eldgull", ctrl_class.get_class_faction(), 0, 1)
		
		# Screed: 10SCREED (459.2, 478.7) const_toee.ROT06 ctrl: None.None 
		
		# Reig: 10REIG (475.4, 466.7) const_toee.ROT06 ctrl: None.None 
		
		# Jon: 10JON (479.4, 466.8) const_toee.ROT02 ctrl: None.None 
		
		# Brogan: 10BROGAN (447.2, 468.5) const_toee.ROT11 ctrl: None.None 
		
		# Jorun: 10JORUN (515.5, 466.5) const_toee.ROT11 ctrl: None.None 
		
		# 1000_Goblin_01: 10GOB (493.9, 438.4) const_toee.ROT05 ctrl: None.None 
		
		# Dead_Goblin_0: 10GOBD (500.9, 447.1) const_toee.ROT05 ctrl: None.None 
		
		# Dead_Townsperson_0: 10MALED (501.6, 451.1) const_toee.ROT11 ctrl: None.None 
		
		# Brohn_Dead: 10SOLDRD (477.4, 466.6) const_toee.ROT05 ctrl: None.None 
		
		# Dead_Goblin_1: 10GOBD (462.7, 461.9) const_toee.ROT08 ctrl: None.None 
		
		# Dead_Goblin_2: 10GOBD (463.3, 455.5) const_toee.ROT05 ctrl: None.None 
		
		# Dead_Goblin_3: 10GOBD (447.5, 458.8) const_toee.ROT08 ctrl: None.None 
		
		# Dead_Soldier_0: 10SOLDRD (448.5, 456.7) const_toee.ROT05 ctrl: None.None 
		
		# Dead_Goblin_J1: 10GOBD (515.9, 464.0) const_toee.ROT05 ctrl: None.None 
		
		# Dead_Goblin_J2: 10GOBD (516.0, 470.9) const_toee.ROT09 ctrl: None.None 
		
		# Dead_Goblin_6: 10GOBD (519.7, 466.7) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_02: 10GOB (531.8, 481.3) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_03: 10GOB (526.3, 480.9) const_toee.ROT08 ctrl: None.None 
		
		# Dead_Townsperson_1: 10MALED (528.8, 480.0) const_toee.ROT05 ctrl: None.None 
		
		# Dead_Goblin_7: 10GOBARD (506.5, 497.0) const_toee.ROT00 ctrl: None.None 
		
		# Dead_Soldier_1: 10SOLDRD (501.4, 490.6) const_toee.ROT06 ctrl: None.None 
		
		# Dead_Sailor: 10SAILRD (476.2, 506.8) const_toee.ROT08 ctrl: None.None 
		
		# 1000_Goblin_04: 10GOB (477.1, 504.7) const_toee.ROT03 ctrl: None.None 
		
		# 1000_Goblin_05: 10GOB (478.6, 506.9) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_06: 10GOB (506.0, 526.9) const_toee.ROT09 ctrl: None.None 
		
		# 1000_Goblin_Archer_01: 10GOBAR (502.2, 525.9) const_toee.ROT11 ctrl: None.None 
		
		# 1000_Goblin_07: 10GOB (502.4, 529.4) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_19: 10GOB (506.1, 523.8) const_toee.ROT09 ctrl: None.None 
		
		# 1000_Goblin_Archer_02: 10GOBAR (505.2, 529.8) const_toee.ROT09 ctrl: None.None 
		
		# 1000_Goblin_08: 10GOB (501.1, 533.1) const_toee.ROT03 ctrl: None.None 
		
		# 1000_Goblin_Archer_03: 10GOBAR (535.5, 476.1) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_09: 10GOB (527.9, 489.2) const_toee.ROT03 ctrl: None.None 
		
		# 1000_Goblin_10: 10GOB (535.3, 488.0) const_toee.ROT06 ctrl: None.None 
		
		# 1000_Goblin_Archer_04: 10GOBAR (530.7, 485.3) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_11: 10GOB (498.6, 439.4) const_toee.ROT06 ctrl: None.None 
		
		# 1000_Goblin_12: 10GOB (487.9, 442.1) const_toee.ROT03 ctrl: None.None 
		
		# 1000_Goblin_Archer_05: 10GOBAR (496.6, 433.1) const_toee.ROT05 ctrl: None.None 
		
		# 1000_Goblin_Archer_06: 10GOBAR (502.7, 438.4) const_toee.ROT06 ctrl: None.None 
		
		# 1000_Goblin_Archer_07: 10GOBAR (473.9, 507.2) const_toee.ROT08 ctrl: None.None 
		
		# 1000_Goblin_Archer_08: 10GOBAR (473.9, 509.6) const_toee.ROT08 ctrl: None.None 
		
		# 1000_Goblin_13: 10GOB (480.9, 503.7) const_toee.ROT06 ctrl: None.None 
		
		# 1000_Goblin_14: 10GOB (502.3, 479.0) const_toee.ROT09 ctrl: None.None 
		
		# 1000_Goblin_15: 10GOB (501.0, 485.7) const_toee.ROT06 ctrl: None.None 
		
		# 1000_Goblin_Archer_09: 10GOBAR (498.7, 481.6) const_toee.ROT08 ctrl: None.None 
		
		# 1000_Goblin_16: 10GOB (532.2, 501.8) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_17: 10GOB (522.8, 505.4) const_toee.ROT08 ctrl: None.None 
		
		# 1000_Goblin_18: 10GOB (524.4, 511.6) const_toee.ROT02 ctrl: None.None 
		
		# 1000_Goblin_Archer_10: 10GOBAR (533.9, 505.7) const_toee.ROT02 ctrl: None.None 
		
		# Crandall: 10CRANDA (503.0, 507.4) const_toee.ROT09 ctrl: None.None 
		
		# Swift Thomas (Hidden): 12SWIFTH (503.3, 441.5) const_toee.ROT05 ctrl: None.None hidden
		
		# Dead_Townsperson_2: 10MALED (547.2, 485.7) const_toee.ROT08 ctrl: None.None 
		
		# Door_Hint_Text_00: 10HINT (475.3, 443.0) const_toee.ROT06 ctrl: None.None hidden
		
		# Door_Hint_Text_01: 10HINT (442.2, 478.9) const_toee.ROT06 ctrl: None.None hidden
		
		# Firtha Kerdos: 10FIRTHH (529.7, 495.4) const_toee.ROT06 ctrl: None.None hidden
		
		return

