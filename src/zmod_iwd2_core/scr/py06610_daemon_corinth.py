import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts
import py06611_corinth_encounters, py04000_monster_manual1_p1, py06123_event_object_fireplace, module_world_travel, module_cheats, item_knowstone

DAEMON_SCRIPT_ID = 6610
DAEMON_GID = "G_36FB8471_4DAC_4088_BEDB_18600C272035"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_ZMOD_CORINTH, CtrlCorinth)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_CORINTH, CtrlCorinth)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_CORINTH, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_ZMOD_CORINTH, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_ZMOD_CORINTH, cs())

def san_bust(attachee, triggerer):
	return ctrl_daemon2.do_san_bust(attachee, triggerer, module_consts.MAP_ID_ZMOD_CORINTH, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): 
		return None
	result = o.data.get(CtrlCorinth.get_name())
	assert isinstance(result, CtrlCorinth)
	return result

class CtrlCorinth(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(module_consts.MAP_ID_ZMOD_CORINTH, DAEMON_SCRIPT_ID, "corinth")
		super(CtrlCorinth, self).created(npc)
		self.vars["liberate_foe_ids"] = list()
		return

	def place_encounters_initial(self):
		self.place_dead_bodies()
		self.place_doors()
		self.place_portals()
		self.place_general_notices()
		if (not module_cheats.CHEAT_CORINTH_KILL_ALL):
			self.place_encounter_c01()
		else:
			self.place_monsters_c01()
		self.place_encounter_c02()
		self.place_encounter_c03(self.delayed_mode())

		self.place_encounter_c04(self.delayed_mode())
		self.place_encounter_c05(self.delayed_mode())
		if (not module_cheats.CHEAT_CORINTH_KILL_ALL):
			self.place_encounter_c07()
		else:
			self.place_monsters_c07()
		self.place_encounter_c07_loot()
		self.place_encounter_c08(self.delayed_mode())
		self.place_encounter_c08_loot()
		self.place_encounter_garn()
		self.place_encounter_markus()
		self.place_encounter_c09(self.delayed_mode())
		self.place_encounter_c09_loot()
		self.place_encounter_witch()

		if (module_cheats.CHEAT_CORINTH_KILL_ALL):
			self.cheat_kill_all_foes(0)
			self.remove_promters_all()
		return

	def delayed_mode(self):
		return 0

	# Sleep interface
	def can_sleep(self):
		fireplace = self.ensure_fireplace()
		if (fireplace):
			for pc in toee.game.party:
				if (py06123_event_object_fireplace.fireplace_is_in_area(fireplace, pc)):
					return toee.SLEEP_SAFE
		return toee.SLEEP_IMPOSSIBLE

	def ensure_fireplace(self):
		fireplace = self.get_fireplace()
		#print("ensure_fireplace: {}".format(fireplace))
		if (not fireplace):
			#print("ensure_fireplace recreating...")
			fireplace = self.place_fireplace()

		return fireplace

	def place_fireplace(self):
		fireplace = self.get_fireplace()
		if (fireplace):
			fireplace.destroy()
			self.vars["fireplace_id"] = 0

		if (toee.game.leader.map != self.get_map_default()): return
		radius_feet_int = 10
		fireplace = py06123_event_object_fireplace.fireplace_create(module_consts.ZMOD_CORINTH_COORDS_FIREPLACE[0], module_consts.ZMOD_CORINTH_COORDS_FIREPLACE[1], radius_feet_int, -10, -10)
		self.vars["fireplace_id"] = fireplace.id
		return fireplace

	def get_fireplace(self):
		fireplace_id = self.get_var("fireplace_id")
		if (fireplace_id):
			fireplace = toee.game.get_obj_by_id(fireplace_id)
			if (fireplace and fireplace.object_flags_get() & toee.OF_DESTROYED):
				print("no fireplace!")
				return
			return fireplace
		return

	def do_san_bust(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("san_bust id: {}, nameid: {}".format(attachee.id, attachee.name))
		# used as a hook from promters

		id = attachee.id
		if (self.vars.get("promter_id_ambush_1") == id):
			self.place_monsters_c01()
		elif (self.vars.get("promter_id_c02") == id):
			self.place_monsters_c02()
		return toee.RUN_DEFAULT

	def create_lib_foe(self, npc_loc, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1, no_move = 0):
		result = self.create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos, no_move)
		self.vars["liberate_foe_ids"].append(result[0].id)
		return result

	def place_encounter_c01(self):
		npc = self.create_promter_at(utils_obj.sec2loc(427, 427), self.get_dialogid_default(), 0, 20, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_EXEC, "Ambush 1", const_toee.rotation_0100_oclock)
		self.vars["promter_id_ambush_1"] = npc.id
		npc.scripts[const_toee.sn_bust] = DAEMON_SCRIPT_ID
		self.vars["liberate_foe_ids"].append(npc.id)
		return

	def place_monsters_c01(self):
		self.create_lib_foe(utils_obj.sec2loc(424, 430), py06611_corinth_encounters.CtrlThugLeader, const_toee.rotation_0900_oclock, "c01", "thug_leader", factions_zmod.FACTION_ENEMY, 0, 1)
		if (1):
			self.create_lib_foe(utils_obj.sec2loc(424, 417), py06611_corinth_encounters.CtrlThug, const_toee.rotation_0300_oclock, "c01", "thug_1", factions_zmod.FACTION_ENEMY, 0, 1)
			self.create_lib_foe(utils_obj.sec2loc(420, 417), py06611_corinth_encounters.CtrlThug, const_toee.rotation_0300_oclock, "c01", "thug_2", factions_zmod.FACTION_ENEMY, 0, 1)
			self.create_lib_foe(utils_obj.sec2loc(416, 420), py06611_corinth_encounters.CtrlThug, const_toee.rotation_0300_oclock, "c01", "thug_3", factions_zmod.FACTION_ENEMY, 0, 1)
			self.create_lib_foe(utils_obj.sec2loc(419, 430), py06611_corinth_encounters.CtrlThug, const_toee.rotation_0300_oclock, "c01", "thug_4", factions_zmod.FACTION_ENEMY, 0, 1)
		return

	def activate_encounter_c01(self):
		print("activate_encounter_c01")
		self.activate_monster("c01", "thug_leader")
		if (1):
			self.activate_monster("c01", "thug_1")
			self.activate_monster("c01", "thug_2")
			self.activate_monster("c01", "thug_3")
			self.activate_monster("c01", "thug_4")
		return

	def place_general_notices(self):
		npc = self.create_promter_at(utils_obj.sec2loc(434, 447), self.get_dialogid_default(), 10, 20, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Corinth", const_toee.rotation_0900_oclock)
		return

	def place_dead_bodies(self):
		#npc, ctrl = self.create_npc_at(utils_obj.sec2loc(491, 432), py04000_monster_manual1_p1.CtrlCommoner, const_toee.rotation_0300_oclock, "dead_body", "1", factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)
		#npc.obj_set_int(toee.obj_f_hp_damage, npc.obj_get_int(toee.obj_f_hp_pts) + 11)

		dead_body_ids = list()
		dead_body_ids.append(toee.game.obj_create(2112, utils_obj.sec2loc(440, 453)).id)
		self.vars["dead_body_ids"] = dead_body_ids
		return

	def place_portals(self):
		passage = module_world_travel.CtrlWorldPortalCorinth.create_obj_at_loc(utils_obj.sec2loc(416, 415))
		passage = module_world_travel.CtrlWorldPortalCorinth.create_obj_at_loc(utils_obj.sec2loc(539, 490))
		return

	def place_doors(self):
		# C03
		utils_locks.portal_hook_autodestroy(443, 487)

		# C04
		utils_locks.portal_hook_autodestroy(456, 499)
		utils_locks.portal_hook_autodestroy(473, 450)
		utils_locks.portal_hook_autodestroy(460, 489)
		utils_locks.portal_hook_autodestroy(475, 489)
		# C05
		utils_locks.portal_hook_autodestroy(441, 512)
		# C06
		utils_locks.portal_hook_autodestroy(485, 466)

		
		# C09
		utils_locks.portal_hook_autodestroy(483, 521)
		utils_locks.portal_hook_autodestroy(461, 521)
		# Ganr home
		utils_locks.portal_hook_autodestroy(503, 448)

		# Ganr barn
		barns = utils_locks.portal_hook_autodestroy(492, 432)
		if (barns and barns[0]):
			utils_locks.portal_setup_dc(barns[0], 100, module_consts.KEY_CORINTH_BARN, 100, 100, 100)
		else:
			print("barn not found!")
			debug.breakp("barns")

		return

	def place_encounter_c02(self, for_delayed = 0):
		if (for_delayed == self.delayed_mode()):
			self.place_monsters_c02()
		return

	def place_monsters_c02(self):
		npc_leader = self.create_lib_foe(utils_obj.sec2loc(447, 493), py06611_corinth_encounters.CtrlLizardmanLeaderC02, const_toee.rotation_1100_oclock, "c02", "lizard_leader", factions_zmod.FACTION_ENEMY, 0, 1)[0]
		if (1):
			npc = self.create_lib_foe(utils_obj.sec2loc(442, 499), py06611_corinth_encounters.CtrlLizardmanLeaderC02, const_toee.rotation_0500_oclock, "c02", "lizard_1", factions_zmod.FACTION_ENEMY, 0, 1)[0]
			npc.obj_set_obj(toee.obj_f_npc_leader, npc_leader)

			self.create_lib_foe(utils_obj.sec2loc(448, 505), py06611_corinth_encounters.CtrlLizardmanLeaderC02, const_toee.rotation_0600_oclock, "c02", "lizard_2", factions_zmod.FACTION_ENEMY, 0, 1)[0]
			npc.obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		return

	def activate_encounter_c02(self):
		print("activate_encounter_c02")
		self.activate_monster("c02", "lizard_leader")
		if (1):
			self.activate_monster("c02", "lizard_1")
			self.activate_monster("c02", "lizard_2")
		return

	def place_encounter_c03(self, for_delayed = 0):
		if (for_delayed == self.delayed_mode()):
			self.place_monsters_c03()
		return

	def place_monsters_c03(self):
		npc_leader, ctrl = self.create_lib_foe(utils_obj.sec2loc(427, 487), py06611_corinth_encounters.CtrlLizardmanClericC03, const_toee.rotation_0500_oclock, "c03", "lizard_cleric", factions_zmod.FACTION_ENEMY, 0, 0)
		if (module_cheats.CHEAT_CORINTH_DEBUG_NAMES):
			utils_npc.npc_description_set_new(npc_leader, "Lizardman Cleric")

		def add_sub(x, y, num, rot):
			npc, ctrl = self.create_lib_foe(utils_obj.sec2loc(x, y), py06611_corinth_encounters.CtrlLizardman, rot, "c03", "lizard_{}".format(num), factions_zmod.FACTION_ENEMY, 0, 0)
			npc.obj_set_obj(toee.obj_f_npc_leader, npc_leader)
			if (module_cheats.CHEAT_CORINTH_DEBUG_NAMES):
				utils_npc.npc_description_set_new(npc, "Lizardman {}".format(num))
			return npc

		if (1):
			add_sub(429, 477, 1, const_toee.ROT05)
			add_sub(436, 477, 2, const_toee.ROT11)
			add_sub(425, 496, 3, const_toee.ROT05)
			add_sub(438, 487, 4, const_toee.ROT03)
		return

	def place_encounter_c04(self, for_delayed = 0):
		if (for_delayed == self.delayed_mode()):
			self.place_monsters_c04()
		return

	def place_monsters_c04(self):
		npc_leader, ctrl = self.create_lib_foe(utils_obj.sec2loc(455, 478), py06611_corinth_encounters.CtrlLizardmanShamanC04, const_toee.ROT06, "c04", "shaman", factions_zmod.FACTION_ENEMY, 0, 0)
		utils_npc.npc_description_set_new(npc_leader, "Shaman")

		# Loot
		toee.game.obj_create(const_proto_items.PROTO_GENERIC_JASPER_BLUE, utils_obj.sec2loc(462, 482))
		toee.game.obj_create(const_proto_scrolls.PROTO_SCROLL_OF_FALSE_LIFE, utils_obj.sec2loc(462, 482))
		item_knowstone.knowstone_create(toee.spell_false_life, utils_obj.sec2loc(462, 482))
		return

	def place_encounter_c05(self, for_delayed = 0):
		if (for_delayed == self.delayed_mode()):
			self.place_monsters_c05()
		return

	def place_monsters_c05(self):
		self.create_lib_foe(utils_obj.sec2loc(437, 512), py06611_corinth_encounters.CtrlLizardman, const_toee.ROT07, "c05", "lizard_1", factions_zmod.FACTION_ENEMY, 0, 0)
		self.create_lib_foe(utils_obj.sec2loc(433, 515), py06611_corinth_encounters.CtrlLizardman, const_toee.ROT09, "c05", "lizard_2", factions_zmod.FACTION_ENEMY, 0, 0)
		return

	def place_encounter_c07(self):
		npc = self.create_promter_at(utils_obj.sec2loc(489, 485), self.get_dialogid_default(), 20, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Ambush", const_toee.rotation_0200_oclock)
		self.vars["ambush_promter_id"] = npc.id
		self.vars["liberate_foe_ids"].append(npc.id)
		return

	def place_encounter_c07_loot(self):
		toee.game.obj_create(const_proto_items.PROTO_GENERIC_JASPER_BLUE, utils_obj.sec2loc(487, 509))
		toee.game.obj_create(const_proto_items.PROTO_GENERIC_PEARL_WHITE, utils_obj.sec2loc(487, 509))

		toee.game.obj_create(const_proto_items.PROTO_MONEY_GOLD, utils_obj.sec2loc(488, 454)).obj_set_int(toee.obj_f_money_quantity, 283)
		return

	def place_monsters_c07(self):
		npc_leader, ctrl = self.create_lib_foe(utils_obj.sec2loc(491, 479), py06611_corinth_encounters.CtrlLizardmanKing, const_toee.ROT09, "c07", "king", factions_zmod.FACTION_ENEMY, 0, 1)
		self.create_lib_foe(utils_obj.sec2loc(488, 482), py06611_corinth_encounters.CtrlLizardman, const_toee.ROT09, "c07", "lizardmen_1", factions_zmod.FACTION_ENEMY, 0, 1)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		self.create_lib_foe(utils_obj.sec2loc(487, 479), py06611_corinth_encounters.CtrlLizardman, const_toee.ROT09, "c07", "lizardmen_2", factions_zmod.FACTION_ENEMY, 0, 1)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		self.create_lib_foe(utils_obj.sec2loc(490, 492), py06611_corinth_encounters.CtrlLizardmanClericC07, const_toee.ROT09, "c07", "cleric", factions_zmod.FACTION_ENEMY, 0, 1)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		self.create_lib_foe(utils_obj.sec2loc(493, 491), py06611_corinth_encounters.CtrlLizardmanWizardC07, const_toee.ROT09, "c07", "wizard", factions_zmod.FACTION_ENEMY, 0, 1)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		return

	def activate_encounter_c07(self):
		print("activate_encounter_c07")

		self.activate_monster("c07", "king")
		self.activate_monster("c07", "lizardmen_1")
		self.activate_monster("c07", "lizardmen_2")
		self.activate_monster("c07", "cleric")
		self.activate_monster("c07", "wizard")
		return

	def place_encounter_c08(self, for_delayed = 0):
		if (for_delayed == self.delayed_mode()):
			self.place_monsters_c08()
		return

	def place_monsters_c08(self):
		npc_leader, ctrl = self.create_lib_foe(utils_obj.sec2loc(463, 469), py06611_corinth_encounters.CtrlGiantSnake, const_toee.ROT11, "c08", "snake_1", factions_zmod.FACTION_ENEMY, 0, 0)
		npc_leader.obj_set_int(toee.obj_f_hp_pts, 26)
		self.create_lib_foe(utils_obj.sec2loc(468, 467), py06611_corinth_encounters.CtrlGiantSnake, const_toee.ROT09, "c08", "snake_2", factions_zmod.FACTION_ENEMY, 0, 0)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		self.create_lib_foe(utils_obj.sec2loc(463, 473), py06611_corinth_encounters.CtrlGiantSnake, const_toee.ROT09, "c08", "snake_3", factions_zmod.FACTION_ENEMY, 0, 0)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		return

	def place_encounter_c08_loot(self):
		toee.game.obj_create(const_proto_rings.PROTO_RING_OF_PROTECTION_PLUS_1, utils_obj.sec2loc(469, 474))
		toee.game.obj_create(const_proto_items.PROTO_MONEY_GOLD, utils_obj.sec2loc(469, 474)).obj_set_int(toee.obj_f_money_quantity, 388)
		return

	def place_encounter_garn(self):
		npc_leader = self.create_npc_at(utils_obj.sec2loc(513, 446), py06611_corinth_encounters.CtrlCommonerGarn, const_toee.ROT00, "garn", "garn", factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)[0]
		npc = self.create_npc_at(utils_obj.sec2loc(511, 449), py06611_corinth_encounters.CtrlCommonerGarnWife, const_toee.ROT07, "garn", "wife", factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)[0]
		npc.obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		npc.turn_towards(npc_leader)
		npc = self.create_npc_at(utils_obj.sec2loc(512, 443), py06611_corinth_encounters.CtrlCommonerGarnDaughter, const_toee.ROT07, "garn", "daughter", factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)[0]
		npc.obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		npc.turn_towards(npc_leader)
		return

	def quest_evaluate_corinth_liberated(self):
		liberate_foe_ids = self.vars["liberate_foe_ids"]
		assert isinstance(liberate_foe_ids, list)

		if (liberate_foe_ids):
			for id in liberate_foe_ids:
				npc = toee.game.get_obj_by_id(id)
				if not utils_npc.npc_is_dead_or_destroyed(npc):
					print("quest_evaluate_corinth_liberated = False, npc: {} {} found by id: {}".format(npc, npc.description, id))
					return False

		print("quest_evaluate_corinth_liberated = True")
		return True

	def place_encounter_markus(self):
		npc_leader = self.create_npc_at(utils_obj.sec2loc(456, 520), py06611_corinth_encounters.CtrlCommonerMarkus, const_toee.ROT07, "markus", "markus", factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)[0]

		npc = self.create_npc_at(utils_obj.sec2loc(455, 524), py06611_corinth_encounters.CtrlCommonerMarkusBodyguard, const_toee.ROT08, "markus", "bodyguard", factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)[0]
		npc.obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		npc.turn_towards(npc_leader)
		return

	def place_encounter_c09(self, for_delayed = 0):
		if (for_delayed == self.delayed_mode()):
			self.place_monsters_c09()
		return

	def place_monsters_c09(self):
		npc_leader, ctrl = self.create_lib_foe(utils_obj.sec2loc(478, 532), py06611_corinth_encounters.CtrlGiantSnake, const_toee.ROT07, "c09", "snake_1", factions_zmod.FACTION_ENEMY, 0, 0)
		npc_leader.obj_set_int(toee.obj_f_hp_pts, 26)
		self.create_lib_foe(utils_obj.sec2loc(475, 535), py06611_corinth_encounters.CtrlGiantSnake, const_toee.ROT09, "c09", "snake_2", factions_zmod.FACTION_ENEMY, 0, 0)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		self.create_lib_foe(utils_obj.sec2loc(479, 536), py06611_corinth_encounters.CtrlGiantSnake, const_toee.ROT09, "c09", "snake_3", factions_zmod.FACTION_ENEMY, 0, 0)[0].obj_set_obj(toee.obj_f_npc_leader, npc_leader)
		return

	def place_encounter_c09_loot(self):
		toee.game.obj_create(const_proto_items.PROTO_MONEY_GOLD, utils_obj.sec2loc(485, 531)).obj_set_int(toee.obj_f_money_quantity, 133)
		return

	def place_encounter_witch(self):
		self.create_npc_at(utils_obj.sec2loc(528, 508), py06611_corinth_encounters.CtrlWitch, const_toee.ROT08, "witch", "witch", factions_zmod.FACTION_NEUTRAL_NPC, 0, 1)[0]
		return
