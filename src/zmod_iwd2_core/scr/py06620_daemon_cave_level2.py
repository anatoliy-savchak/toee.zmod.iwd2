import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals
import py06619_cave_encounters, py06123_event_object_fireplace, module_world_travel, module_cheats, py06611_corinth_encounters, py06621_kots_monsters
import const_proto_weapon, item_knowstone, const_proto_wands

DAEMON_SCRIPT_ID = 6620
DAEMON_GID = "G_6D272027_EC82_40FA_882D_CC1E7CAFED1B"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_LEVEL2, CtrlCaveLevel2)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_LEVEL2, CtrlCaveLevel2)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_LEVEL2, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_LEVEL2, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_LEVEL2, cs())

def san_bust(attachee, triggerer):
	return ctrl_daemon2.do_san_bust(attachee, triggerer, module_consts.MAP_ID_ZMOD_CAVE_LEVEL2, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): 
		return None
	result = o.data.get(CtrlCaveLevel2.get_name())
	assert isinstance(result, CtrlCaveLevel2)
	return result

class CtrlCaveLevel2(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(module_consts.MAP_ID_ZMOD_CAVE_LEVEL2, DAEMON_SCRIPT_ID, "cave_level2")
		super(CtrlCaveLevel2, self).created(npc)
		self.vars["foe_ids"] = list()
		return

	def place_encounters_initial(self):
		self.place_doors()
		self.place_portals()
		if 0:
			if not module_cheats.CHEAT_CAVES2_SKIP_CENTEPIDES:
				self.place_encounter_c01()
			else:
				self.place_monsters_c02(toee.game.leader)
		#self.place_monsters_c03()
		#self.place_encounter_c04()
		#self.place_encounter_c05()
		#self.place_monsters_c06()
		#self.place_monsters_c07()
		#self.place_loot_c07()

		#self.place_monsters_c09()
		self.place_monsters_c10()
		return

	def place_encounters_next(self):
		return

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

		return
		if (toee.game.leader.map != self.get_map_default()): return
		radius_feet_int = 10
		fireplace = py06123_event_object_fireplace.fireplace_create(458, 448, radius_feet_int, 5, 5)
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

	def create_lib_foe(self, x, y, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1, no_move = 0, leader = None):
		print("create_lib_foe {} {}".format(encounter, code_name))
		if not faction: faction = faction=factions_zmod.FACTION_ENEMY
		npc_loc = utils_obj.sec2loc(x, y)
		result = self.create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos, no_move)
		self.vars["foe_ids"].append(result[0].id)
		if (module_cheats.CHEAT_GLOBAL_DEBUG_NAMES):
			utils_npc.npc_description_set_new(result[0], code_name)
		if leader:
			if isinstance(leader, toee.PyObjHandle): pass
			elif len(leader) > 1: leader = leader[0]
			result[0].obj_set_obj(toee.obj_f_npc_leader, leader)
		return result

	def critter_dying(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		info = self.get_monsterinfo_by_npc(attachee)
		#print("critter_dying attachee: {}, name: {}".format(attachee, info.monster_code_name))
		if (info and info.encounter_code == "c01"):
			count = int(self.get_var("quest_c01_left"))
			count -= 1
			self.vars["quest_c01_left"] = count
			if (count <= 0):
				self.place_monsters_c02(toee.game.leader)

		super(CtrlCaveLevel2, self).critter_dying(attachee, triggerer)
		return

	def do_san_bust(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("san_bust id: {}, nameid: {}".format(attachee.id, attachee.name))
		# used as a hook from promters

		id = attachee.id
		if (self.vars.get("promter_id_ambush_1") == id):
			self.place_monsters_c01()
		elif (self.vars.get("amenoptes_promter_id") == id):
			self.trigger_encounter_c05(triggerer)
		return toee.RUN_DEFAULT

	def do_san_use(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("do_san_use id: {}, nameid: {}".format(attachee.id, attachee.name))

		id = attachee.id
		if self.vars.get("vampire_doors_id") == id:
			self.trigger_encounter_c08(triggerer)
		return toee.RUN_DEFAULT

	def place_doors(self):
		# C07
		vampire_doors = utils_locks.portal_hook_autodestroy(466, 478)
		if (vampire_doors and vampire_doors[0]):
			utils_locks.portal_setup_dc(vampire_doors[0], 100, module_consts.KEY_CAVES_LV2_VAMPIRE, 100, 100, 100)
			vampire_doors[0].scripts[const_toee.sn_use] = DAEMON_SCRIPT_ID
			self.vars["vampire_doors_id"] = vampire_doors[0].id
			print("self.vars[vampire_doors_id]: {}".format(self.vars["vampire_doors_id"]))
		else:
			print("vampire_doors not found!")
			debug.breakp("vampire_doors")
		return

	def place_portals(self):
		py06619_cave_encounters.CtrlCavesPortalLevel1ToGround.create_obj_at_loc(utils_obj.sec2loc(432, 444))
		return

	def place_encounter_c01(self):
		npc = self.create_promter_at(utils_obj.sec2loc(448, 442), self.get_dialogid_default(), 10, 20, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Centipedes", const_toee.ROT02)
		self.vars["promter_id_ambush_1"] = npc.id
		npc.scripts[const_toee.sn_bust] = DAEMON_SCRIPT_ID
		self.vars["foe_ids"].append(npc.id)
		return

	def place_monsters_c01(self, talker):
		mons = list()
		def prep(npc):
			npc.condition_add_with_args("SurpriseRound2", 1)
			mons.append(npc)
			return npc

		encounter = "c01"
		npc_leader = prep(self.create_lib_foe(445, 435,
				ctrl_class=py06621_kots_monsters.CtrlCentipede, 
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="centipede1",
				no_draw = 0,
				no_kos = 0
			)[0])

		if True:
			prep(self.create_lib_foe(435, 441,
					ctrl_class=py06621_kots_monsters.CtrlCentipede, 
					rot=const_toee.ROT04, 
					encounter=encounter, 
					code_name="centipede2",
					no_draw = 0,
					no_kos = 0,
					leader = npc_leader
				)[0])


			prep(self.create_lib_foe(439, 452,
					ctrl_class=py06621_kots_monsters.CtrlCentipede, 
					rot=const_toee.ROT04, 
					encounter=encounter, 
					code_name="centipede3",
					no_draw = 0,
					no_kos = 0,
					leader = npc_leader
				)[0])

		self.vars["quest_c01_left"] = len(mons)
		if not module_cheats.CHEAT_CAVES2_KILL_CENTEPIDES:
			for pc in toee.game.party:
				#pc.condition_add("TurnWatcher")
				pc.condition_add_with_args("Surprised2", 1)

			for mon in mons:
				mon.attack(talker)
		else:
			for mon in mons:
				mon.critter_kill_by_effect(talker)
		return

	def place_monsters_c02(self, talker):
		def prep(npc): return npc

		encounter = "c02"
		npc_leader = prep(self.create_lib_foe(453, 441,
				ctrl_class=py06619_cave_encounters.CtrlGiantSpiderGuardLeaderC02, 
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="spider_guard1",
				no_draw = 0,
				no_kos = 1
			)[0])

		

		npc = prep(self.create_lib_foe(454, 436,
				ctrl_class=py06619_cave_encounters.CtrlGiantSpiderGuardC02, 
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="spider_guard2",
				no_draw = 0,
				no_kos = 1,
				leader = npc_leader
			)[0])

		utils_npc.npc_approach(npc, talker)
		utils_npc.npc_approach(npc_leader, talker)

		return

	def place_monsters_c03(self):
		def prep(npc): return npc

		encounter = "c03"
		npc_leader = prep(self.create_lib_foe(432, 468,
				ctrl_class=py06621_kots_monsters.CtrlZombie, 
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="zombie1",
				no_draw = 0,
				no_kos = 0
			)[0])
		npc_leader.item_get(toee.game.obj_create(8005, npc_leader.location))
		

		npc = prep(self.create_lib_foe(426, 485,
				ctrl_class=py06621_kots_monsters.CtrlZombie,
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="zombie2",
				no_draw = 0,
				no_kos = 0,
				leader = npc_leader
			)[0])

		return

	def place_encounter_c04(self):
		npc = self.create_promter_at(utils_obj.sec2loc(430, 494), self.get_dialogid_default(), 20, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Skeleton Cave", const_toee.ROT02)
		self.vars["foe_ids"].append(npc.id)
		npc = self.create_promter_at(utils_obj.sec2loc(434, 507), self.get_dialogid_default(), 30, 20, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Skeleton Ambush", const_toee.ROT02)
		self.vars["foe_ids"].append(npc.id)
		return

	def place_monsters_c04(self):
		encounter = "c04"
		if True:
			npc_leader_tup = self.create_lib_foe(447, 511,
					ctrl_class=py06621_kots_monsters.CtrlSkeleton, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="skeleton01",
					no_draw = 0,
					no_kos = 0
				)
			npc_leader_tup[1].create_weapon_by_proto(npc_leader_tup[0], const_proto_weapon.PROTO_LONGSWORD_MASTERWORK)

			npc_tup = self.create_lib_foe(446, 514,
					ctrl_class=py06621_kots_monsters.CtrlSkeleton, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="skeleton02",
					no_draw = 0,
					no_kos = 0,
					leader = npc_leader_tup[0]
				)
			npc_tup[1].create_weapon_by_proto(npc_tup[0], const_proto_weapon.PROTO_LONGSWORD)

			npc_tup = self.create_lib_foe(444, 519,
					ctrl_class=py06621_kots_monsters.CtrlSkeleton, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="skeleton03",
					no_draw = 0,
					no_kos = 0,
					leader = npc_leader_tup[0]
				)
			npc_tup[1].create_weapon_by_proto(npc_tup[0], const_proto_weapon.PROTO_LONGSWORD)

			npc_tup = self.create_lib_foe(443, 523,
					ctrl_class=py06621_kots_monsters.CtrlSkeleton, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="skeleton04",
					no_draw = 0,
					no_kos = 0,
					leader = npc_leader_tup[0]
				)

		npc_leader_tup = self.create_lib_foe(434, 490,
				ctrl_class=py06621_kots_monsters.CtrlGiantSpider, 
				rot=const_toee.ROT05, 
				encounter=encounter, 
				code_name="spider01",
				no_draw = 0,
				no_kos = 0
			)

		if True:
			npc_tup = self.create_lib_foe(425, 495,
					ctrl_class=py06621_kots_monsters.CtrlGiantSpider, 
					rot=const_toee.ROT05, 
					encounter=encounter, 
					code_name="spider02",
					no_draw = 0,
					no_kos = 0,
					leader = npc_leader_tup[0]
				)
		return

	def place_encounter_c05(self):
		npc = self.create_promter_at(utils_obj.sec2loc(467, 511), self.get_dialogid_default(), 0, 15, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_EXEC, "Amenoptes", const_toee.ROT02)
		self.vars["foe_ids"].append(npc.id)
		self.vars["amenoptes_promter_id"] = npc.id
		npc.scripts[const_toee.sn_bust] = DAEMON_SCRIPT_ID

		self.place_monsters_c05()
		return

	def place_monsters_c05(self):
		encounter = "c05"
		npc_leader_tup = self.create_lib_foe(474, 499,
				ctrl_class=py06619_cave_encounters.CtrlAmenoptes,
				rot=const_toee.ROT01, 
				encounter=encounter, 
				code_name="amenoptes",
				no_draw = 1,
				no_kos = 1
			)
		if True:
			npc_tup = self.create_lib_foe(479, 504,
					ctrl_class=py06619_cave_encounters.CtrlQuinox, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="quinox",
					no_draw = 1,
					no_kos = 1,
					leader = npc_leader_tup[0]
				)

			npc_tup = self.create_lib_foe(469, 520,
					ctrl_class=py06621_kots_monsters.CtrlSkeleton, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="skeleton01",
					no_draw = 1,
					no_kos = 1,
					leader = npc_leader_tup[0]
				)
			npc_tup[1].create_weapon_by_proto(npc_tup[0], const_proto_weapon.PROTO_WEAPON_SHORTSWORD)

			npc_tup = self.create_lib_foe(456, 500,
					ctrl_class=py06621_kots_monsters.CtrlSkeleton, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="skeleton02",
					no_draw = 1,
					no_kos = 1,
					leader = npc_leader_tup[0]
				)

			npc_tup = self.create_lib_foe(466, 495,
					ctrl_class=py06621_kots_monsters.CtrlZombie, 
					rot=const_toee.ROT01, 
					encounter=encounter, 
					code_name="zombie",
					no_draw = 1,
					no_kos = 1,
					leader = npc_leader_tup[0]
				)
		return

	def trigger_encounter_c05(self, triggerer):
		self.reveal_monster_list("c05", ["amenoptes", "skeleton01", "skeleton02", "zombie", "quinox"], 1)

		npc = self.get_monster_npc("c05", "amenoptes")
		toee.game.scroll_to(npc)
		triggerer.begin_dialog(npc, 300)
		return

	def trigger_encounter_fight_c05(self, npc, pc):
		mons = self.activate_monster_list("c05", ["amenoptes", "skeleton01", "skeleton02", "zombie", "quinox"], 1, 1, 1)
		for mon_tup in mons:
			if mon_tup and mon_tup[0]:
				mon_tup[0].attack(pc)
		return

	def place_monsters_c06(self):
		encounter = "c06"
		npc_leader = self.create_lib_foe(497, 525,
				ctrl_class=py06621_kots_monsters.CtrlGhoul, 
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="ghoul",
				no_draw = 0,
				no_kos = 0
			)
		utils_locks.key_create_npc(npc_leader[0], module_consts.KEY_CAVES_LV2_VAMPIRE)
		return

	def place_monsters_c07(self):
		encounter = "c07"
		npc_leader = self.create_lib_foe(469, 460,
				ctrl_class=py06619_cave_encounters.CtrlVampire, 
				rot=const_toee.ROT04, 
				encounter=encounter,
				code_name="vampire",
				no_draw = 0,
				no_kos = 0
			)
		return

	def place_loot_c07(self):
		# Arrows of Animal Slaying x3 #TODO!
		# Kukri +1 = Dagger +1
		# Scrolls: Inflict Moderate Wounds, Silence
		# Wand of Chaos (*5), Confusion
		loc = utils_obj.sec2loc(472, 468)
		utils_item.item_create(const_proto_scrolls.PROTO_SCROLL_OF_INFLICT_MODERATE_WOUNDS, loc, 5, 5)
		utils_item.item_created(item_knowstone.knowstone_create(toee.spell_inflict_moderate_wounds, loc=loc, off_x = -5, off_y = -5))

		utils_item.item_create(const_proto_scrolls.PROTO_SCROLL_OF_SILENCE, loc, 5, 5)
		utils_item.item_created(item_knowstone.knowstone_create(toee.spell_silence, loc=loc, off_x = -5, off_y = -5))

		utils_item.wand_created(utils_item.item_create(const_proto_wands.PROTO_WAND_OF_CONFUSION, loc, 2, 6), 5)
		utils_item.item_create(const_proto_weapon.PROTO_WEAPON_DAGGER_PLUS_1, loc, 6, 3)
		return

	def trigger_encounter_c08(self, triggerer):
		# todo - when spider quieen is dead then do not trigger
		self.place_monsters_c08()
		return

	def place_monsters_c08(self):
		encounter = "c08"
		npc_leader = self.create_lib_foe(435, 496,
				ctrl_class=py06621_kots_monsters.CtrlGiantSpider,
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="spider1",
				no_draw = 0,
				no_kos = 0
			)
		npc = self.create_lib_foe(427, 505,
				ctrl_class=py06621_kots_monsters.CtrlGiantSpider,
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="spider2",
				no_draw = 0,
				no_kos = 0,
				leader = npc_leader
			)
		return

	def place_monsters_c09(self):
		encounter = "c09"
		npc_leader = self.create_lib_foe(496, 444,
				ctrl_class=py06621_kots_monsters.CtrlGiantSpiderWar,
				rot=const_toee.ROT04, 
				encounter=encounter, 
				code_name="spider_war1",
				no_draw = 0,
				no_kos = 0
			)
		npc_leader[0].condition_add_with_args("Napping", 0, 20)
		utils_item.item_create_in_inventory(const_proto_items.PROTO_GENERIC_PEARL_WHITE, npc_leader[0])
		utils_item.item_create_in_inventory(const_proto_items.PROTO_GENERIC_PEARL_WHITE, npc_leader[0])
		utils_item.item_create_in_inventory(const_proto_items.PROTO_GENERIC_PEARL_WHITE, npc_leader[0])
		utils_item.item_create_in_inventory(const_proto_items.PROTO_GENERIC_PEARL_WHITE, npc_leader[0])
		return

	def place_monsters_c10(self):
		encounter = "c10"
		npc_leader = self.create_lib_foe(510, 501,
				ctrl_class=py06619_cave_encounters.CtrlGiantSpiderC10Kutula,
				rot=const_toee.ROT10, 
				encounter=encounter, 
				code_name="kutula",
				no_draw = 0,
				no_kos = 0
			)
		npc = self.create_lib_foe(521, 496,
				ctrl_class=py06619_cave_encounters.CtrlGiantSpiderC10Cleric,
				rot=const_toee.ROT10, 
				encounter=encounter, 
				code_name="spider_cleirc2",
				no_draw = 0,
				no_kos = 0,
				leader = npc_leader
			)
		npc = self.create_lib_foe(502, 497,
				ctrl_class=py06619_cave_encounters.CtrlGiantSpiderC10ClericBane,
				rot=const_toee.ROT10, 
				encounter=encounter, 
				code_name="spider_cleirc3",
				no_draw = 0,
				no_kos = 0,
				leader = npc_leader
			)
		npc = self.create_lib_foe(524, 504,
				ctrl_class=py06619_cave_encounters.CtrlGiantSpiderC10,
				rot=const_toee.ROT10, 
				encounter=encounter, 
				code_name="spider4",
				no_draw = 0,
				no_kos = 0,
				leader = npc_leader
			)
		npc = self.create_lib_foe(503, 504,
				ctrl_class=py06619_cave_encounters.CtrlGiantSpiderC10Blindfight,
				rot=const_toee.ROT10, 
				encounter=encounter, 
				code_name="spider5",
				no_draw = 0,
				no_kos = 0,
				leader = npc_leader
			)
		return
