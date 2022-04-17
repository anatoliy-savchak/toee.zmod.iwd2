import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals


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

	def place_npcs(self):
		#self.create_lib_foe(utils_obj.sec2loc(491, 480), py06616_orc_fort_encounters.CtrlOrcWarriorShield, const_toee.ROT07, "r03", "orc_melee2", factions_zmod.FACTION_ENEMY, 0, 0)
		return
