import toee, debug, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals
import py06616_orc_fort_encounters, py04000_monster_manual1_p1, py06123_event_object_fireplace, module_world_travel, module_cheats
import py06611_corinth_encounters, utils_pc, const_proto_weapon, py06621_kots_monsters, rumor_control, py06214_doors_autodestroy, const_proto_armor

DAEMON_SCRIPT_ID = 6615
DAEMON_GID = "G_9ABF8614_F234_4C53_B183_309013B23108"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_ZMOD_ORC_FORT, CtrlOrcFort)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_ORC_FORT, CtrlOrcFort)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_ZMOD_ORC_FORT, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_ZMOD_ORC_FORT, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_ZMOD_ORC_FORT, cs())

def san_bust(attachee, triggerer):
	return ctrl_daemon2.do_san_bust(attachee, triggerer, module_consts.MAP_ID_ZMOD_ORC_FORT, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): 
		return None
	result = o.data.get(CtrlOrcFort.get_name())
	assert isinstance(result, CtrlOrcFort)
	return result

class CtrlOrcFort(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(module_consts.MAP_ID_ZMOD_ORC_FORT, DAEMON_SCRIPT_ID, "orc_fort")
		super(CtrlOrcFort, self).created(npc)
		self.vars["foe_ids"] = list()
		return

	def place_encounters_initial(self):
		self.place_doors()
		#self.place_encounter_rope()
		self.place_portals()
		#self.place_encounter_r01()
		#self.place_monsters_r01()
		#self.place_monsters_r02()
		#self.place_encounter_r03()
		#self.place_monsters_r04()
		#self.place_monsters_r05()

		#self.place_encounter_r06()
		self.place_encounter_r07() # inform
		#self.place_monsters_r08()
		#self.place_ecnounter_loot_r09()
		#self.place_encounter_r10()
		#self.place_encounter_r11()
		#self.place_monsters_r11()
		#self.place_encounter_r12()
		#self.place_monsters_r13()
		#self.place_monsters_r15()
		#self.place_encounter_r16()
		#self.place_monsters_r17()
		#self.place_monsters_r18()
		#self.place_encounter_r19()
		#self.place_monsters_r19()
		#self.place_monsters_r19_allies()
		#self.place_monsters_r20()
		#self.place_monsters_r21()
		self.place_monsters_r21()

		#rumor_control.rumor_give(module_quests.RUMOR_ORC_FORT_LIUTENENT_ARROWS)
		return

	def place_encounters_next(self):
		self.rope_update()
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

		return #todo
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
		if (self.vars.get("assault_promter_id") == id):
			if (not toee.game.global_flags[module_globals.GFLAG_ORC_FORT_SKIP_ASSAULT]):
				toee.game.global_flags[module_globals.GFLAG_ORC_FORT_SKIP_ASSAULT] = 1
				self.place_monsters_assault()
				self.deactivate_encounter_assault()
				self.trigger_orc_leader_talk_r01(triggerer)
			attachee.destroy()
		#elif (self.vars.get("unwelcome_promter_id") == id):
		#	self.place_monsters_unwelcome()
		#	attachee.destroy()
			
		return toee.RUN_DEFAULT

	def do_san_use(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("do_san_use id: {}, nameid: {}".format(attachee.id, attachee.name))
		id = attachee.id

		doors_r11_ids = self.vars.get("doors_r11_ids")
		if doors_r11_ids and id in doors_r11_ids:
			for iid in doors_r11_ids:
				door = toee.game.get_obj_by_id(iid)
				if door:
					door.scripts[const_toee.sn_use] = 0
			# find promter
			promter_info = next((x for x in self.promters_info if x.monster_code_name == "Alarm Doors"), None)
			if promter_info:
				promter = toee.game.get_obj_by_id(promter_info.id)
				if promter:
					triggerer.begin_dialog(promter, promter.obj_get_int(py06122_cormyr_prompter.PROMTER_PARAM_FIELD_LINEID))
					return toee.SKIP_DEFAULT
			
		return toee.RUN_DEFAULT

	def create_lib_foe(self, npc_loc, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1, no_move = 0, leader = None):
		result = self.create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos, no_move)
		self.vars["foe_ids"].append(result[0].id)
		if (module_cheats.CHEAT_ORC_FORT_DEBUG_NAMES):
			utils_npc.npc_description_set_new(result[0], code_name)
		if leader:
			if isinstance(leader, toee.PyObjHandle): pass
			elif len(leader) > 1: leader = leader[0]
			result[0].obj_set_obj(toee.obj_f_npc_leader, leader)
		return result

	def create_lib_foe2(self, x, y, ctrl_class, rot, encounter, code_name, no_draw = 1, no_kos = 1, no_move = 0, leader = None):
		return self.create_lib_foe(utils_obj.sec2loc(x, y), ctrl_class, rot, encounter, code_name, factions_zmod.FACTION_ENEMY, no_draw, no_kos, no_move, leader)

	def place_portals(self):
		module_world_travel.CtrlWorldPortalOrcFort.create_obj_at_loc(utils_obj.sec2loc(529, 478))
		py06616_orc_fort_encounters.CtrlOrcFortPortalGroundToTowersSE.create_obj_at_loc(utils_obj.sec2loc(498, 493))
		py06616_orc_fort_encounters.CtrlOrcFortPortalGroundToTowersSW.create_obj_at_loc(utils_obj.sec2loc(502, 469))
		return

	def place_doors(self):
		# r01
		doors = utils_locks.portal_hook_autodestroy(503, 474)
		# r04
		doors = utils_locks.portal_hook_autodestroy(465, 462)
		# r06
		doors = utils_locks.portal_hook_autodestroy(442, 474)
		doors = utils_locks.portal_hook_autodestroy(439, 489)
		# r08
		doors = utils_locks.portal_hook_autodestroy(442, 498)
		# r09
		doors = utils_locks.portal_hook_autodestroy(449, 511)
		# r10
		doors = utils_locks.portal_hook_autodestroy(440, 511)
		# r11
		doors = utils_locks.portal_hook_autodestroy(431, 521)
		if doors:
			doors_r11_ids = list()
			for door in doors: 
				doors_r11_ids.append(door.id)
				door.scripts[const_toee.sn_use] = DAEMON_SCRIPT_ID
			self.vars["doors_r11_ids"] = doors_r11_ids
		# r12
		doors = utils_locks.portal_hook_autodestroy(428, 510)
		doors = utils_locks.portal_hook_autodestroy(434, 510)
		# r13
		doors = utils_locks.portal_hook_autodestroy(433, 502)
		# r16
		utils_locks.portal_hook_autodestroy(439, 458)
		# r17
		utils_locks.portal_hook_autodestroy(450, 452)
		utils_locks.portal_hook_autodestroy(445, 444)
		utils_locks.portal_hook_autodestroy(444, 435)
		utils_locks.portal_hook_autodestroy(444, 427)
		# r19
		utils_locks.portal_hook_autodestroy(429, 475)
		# r20
		utils_locks.portal_hook_autodestroy(423, 459)
		# r21
		utils_locks.portal_hook_autodestroy(423, 451)
		return

	def place_encounter_r01(self):
		npc = self.create_promter_at(utils_obj.sec2loc(497, 474), self.get_dialogid_default(), 10, 40, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_EXEC, "Assault", const_toee.rotation_0800_oclock)
		self.vars["assault_promter_id"] = npc.id
		npc.scripts[const_toee.sn_bust] = DAEMON_SCRIPT_ID
		return

	def place_monsters_r01(self):
		self.create_lib_foe(utils_obj.sec2loc(495, 469), py06616_orc_fort_encounters.CtrlOrcCleric1, const_toee.ROT07, "r01", "orc_cleric8", factions_zmod.FACTION_ENEMY, 0, 1)

		if (1):
			self.create_lib_foe(utils_obj.sec2loc(496, 478), py06616_orc_fort_encounters.CtrlOrcWarriorCrossbow, const_toee.ROT07, "r01", "orc_crossbow1", factions_zmod.FACTION_ENEMY, 0, 1)
			self.create_lib_foe(utils_obj.sec2loc(498, 478), py06616_orc_fort_encounters.CtrlOrcWarriorCrossbow, const_toee.ROT07, "r01", "orc_crossbow2", factions_zmod.FACTION_ENEMY, 0, 1)
			self.create_lib_foe(utils_obj.sec2loc(496, 481), py06616_orc_fort_encounters.CtrlOrcWarriorShield, const_toee.ROT07, "r01", "orc_shield3", factions_zmod.FACTION_ENEMY, 0, 1)

			self.create_lib_foe(utils_obj.sec2loc(502, 465), py06616_orc_fort_encounters.CtrlOrcWarriorScaleMail, const_toee.ROT07, "r01", "orc_melee4", factions_zmod.FACTION_ENEMY, 0, 1)
			self.create_lib_foe(utils_obj.sec2loc(494, 466), py06616_orc_fort_encounters.CtrlOrcWarriorShield, const_toee.ROT07, "r01", "orc_melee5", factions_zmod.FACTION_ENEMY, 0, 1)
		return

	def place_monsters_assault(self):
		self.create_lib_foe(utils_obj.sec2loc(489, 476), py06616_orc_fort_encounters.CtrlOrcLeader, const_toee.ROT07, "ass", "orc_leader", factions_zmod.FACTION_ENEMY, 0, 1)

		self.create_lib_foe(utils_obj.sec2loc(493, 476), py06616_orc_fort_encounters.CtrlOrcWarriorGuard, const_toee.ROT07, "ass", "orc_melee6", factions_zmod.FACTION_ENEMY, 0, 1)
		self.create_lib_foe(utils_obj.sec2loc(493, 474), py06616_orc_fort_encounters.CtrlOrcWarriorGuardHeavy, const_toee.ROT07, "ass", "orc_melee7", factions_zmod.FACTION_ENEMY, 0, 1)

		self.create_lib_foe(utils_obj.sec2loc(489, 473), py06616_orc_fort_encounters.CtrlOrcWizard1, const_toee.ROT07, "ass", "orc_wizard9", factions_zmod.FACTION_ENEMY, 0, 1)
		return

	def get_names_monsters_assault(self, skip_second_pack = 0):
		result = list()
		result.append(("ass", "orc_leader"))

		result.append(("r01", "orc_crossbow1"))
		result.append(("r01", "orc_crossbow2"))
		result.append(("r01", "orc_shield3"))
		result.append(("r01", "orc_melee4"))
		result.append(("r01", "orc_melee5"))

		if (not skip_second_pack):
			result.append(("ass", "orc_melee6"))
			result.append(("ass", "orc_melee7"))
			result.append(("ass", "orc_wizard9"))
		return result

	def activate_encounter_assault(self, skip_second_pack = 0):
		print("activate_encounter_assault")

		result = list()
		for name_tup in self.get_names_monsters_assault(skip_second_pack):
			result.append(self.activate_monster(name_tup[0], name_tup[1], 1, 1, 1))
		return result

	def deactivate_encounter_assault(self, skip_second_pack = 0):
		print("deactivate_encounter_assault")

		for name_tup in self.get_names_monsters_assault(skip_second_pack):
			npc = self.get_monster_npc(name_tup[0], name_tup[1])
			if (npc):
				npc.npc_flag_unset(toee.ONF_KOS)
		return

	def trigger_orc_leader_talk_r01(self, talker):
		assert isinstance(talker, toee.PyObjHandle)

		py06611_corinth_encounters.CtrlWitch.dialog_quest_help_complete_omitted()

		leader = self.get_monster_npc("ass", "orc_leader")
		if (leader):
			talker.begin_dialog(leader, 10)
		else:
			print("leader not found!")
			debug.breakp("leader not found!")
		return

	def combat_start_r01(self, leader, talker):
		assert isinstance(leader, toee.PyObjHandle)
		assert isinstance(talker, toee.PyObjHandle)

		tups = self.activate_encounter_assault() #[[npc, info]]
		for tup in tups:
			npc, info = tup
			assert isinstance(npc, toee.PyObjHandle)
			if (npc != leader):
				npc.obj_set_obj(toee.obj_f_npc_leader, leader)
			npc.turn_towards(talker)
			npc.attack(talker)

		#leader.attack(talker)
		return

	def place_monsters_r02(self):
		self.create_lib_foe(utils_obj.sec2loc(494, 506), py06616_orc_fort_encounters.CtrlTiger, const_toee.ROT07, "r02", "tiger", factions_zmod.FACTION_ENEMY, 0, 0)
		return

	def place_encounter_rope(self):
		rope = py06616_orc_fort_encounters.CtrlRope.create_obj_at_loc(utils_obj.sec2loc(503, 496))
		self.vars["rope_id"] = rope.id
		self.rope_update()
		return

	def rope_update(self):
		rope_id = self.vars.get("rope_id")
		if (rope_id):
			rope = toee.game.get_obj_by_id(rope_id)
			if rope and not utils_npc.npc_is_dead_or_destroyed(rope):
				quest_state = toee.game.quests[module_quests.QUEST_CORINTH_WITCH_HELP].state
				if (quest_state == toee.qs_accepted):
					rope.object_flag_unset(toee.OF_OFF)
				else:
					rope.object_flag_set(toee.OF_OFF)
		return

	def place_encounter_r03(self):
		npc = self.create_promter_at(utils_obj.sec2loc(470, 474), self.get_dialogid_default(), 10, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Unwelcome", const_toee.rotation_0800_oclock)
		self.vars["unwelcome_promter_id"] = npc.id
		#npc.scripts[const_toee.sn_bust] = DAEMON_SCRIPT_ID
		return

	def place_monsters_r03(self):
		print("place_monsters_r03")
		kos = 1
		npc_leader = self.create_lib_foe(utils_obj.sec2loc(472, 489), py06616_orc_fort_encounters.CtrlOrcSergeant, const_toee.ROT07, "r03", "sergeant", factions_zmod.FACTION_ENEMY, 0, kos)[0]
		if (1):
			self.create_lib_foe(utils_obj.sec2loc(464, 474), py06616_orc_fort_encounters.CtrlTroll, const_toee.ROT07, "r03", "troll1", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
		if (1):
			self.create_lib_foe(utils_obj.sec2loc(461, 472), py06616_orc_fort_encounters.CtrlTroll, const_toee.ROT07, "r03", "troll2", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(469, 481), py06616_orc_fort_encounters.CtrlOrcWarriorGreataxeCB, const_toee.ROT07, "r03", "warrior3", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(472, 481), py06616_orc_fort_encounters.CtrlOrcWarriorGuardCB, const_toee.ROT07, "r03", "warrior4", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(472, 483), py06616_orc_fort_encounters.CtrlOrcWarriorGuardHeavy, const_toee.ROT07, "r03", "warrior5", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(475, 485), py06616_orc_fort_encounters.CtrlOrcWarriorGuardCB, const_toee.ROT07, "r03", "warrior6", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(475, 487), py06616_orc_fort_encounters.CtrlOrcWarriorGreataxeCB, const_toee.ROT07, "r03", "warrior7", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)

			self.create_lib_foe(utils_obj.sec2loc(464, 476), py06616_orc_fort_encounters.CtrlOrcWarriorGuardCB, const_toee.ROT07, "r03", "warrior8", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(462, 476), py06616_orc_fort_encounters.CtrlOrcWarriorGuardCB, const_toee.ROT07, "r03", "warrior9", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(464, 478), py06616_orc_fort_encounters.CtrlOrcWarriorGuardHeavyGreataxe, const_toee.ROT07, "r03", "warrior10", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(462, 478), py06616_orc_fort_encounters.CtrlOrcSergeantJunior, const_toee.ROT07, "r03", "junior11", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(460, 479), py06616_orc_fort_encounters.CtrlOrcWarriorGuardCB, const_toee.ROT07, "r03", "warrior12", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
			self.create_lib_foe(utils_obj.sec2loc(469, 486), py06616_orc_fort_encounters.CtrlOrcWizard2, const_toee.ROT07, "r03", "wizard13", factions_zmod.FACTION_ENEMY, 0, kos, 0, npc_leader)
		return

	def activate_encounter_r03(self, talker):
		print("activate_encounter_r03")
		monster_npc_infos = self.activate_monster_list("r03", [
			"sergeant",
			"troll1",
			"troll2",
			"warrior3",
			"warrior4",
			"warrior5",
			"warrior6",
			"warrior7",
			"warrior8",
			"warrior9",
			"warrior10",
			"junior11",
			"warrior12",
			"warrior13"
			], 1, 1, 1)
		for tup in monster_npc_infos:
			if tup and tup[0]:
				#tup[0].condition_add("TurnWatcher")
				tup[0].condition_add_with_args("SurpriseRound2", 1)
		for pc in toee.game.party:
			#pc.condition_add("TurnWatcher")
			pc.condition_add_with_args("Surprised2", 1)
		self.monsters_attack(monster_npc_infos, talker)
		return

	def place_monsters_r04(self):
		print("place_monsters_r04")
		npc_leader = self.create_lib_foe(utils_obj.sec2loc(470, 464), py06616_orc_fort_encounters.CtrlOrcWarrior, const_toee.ROT07, "r04", "orc1", factions_zmod.FACTION_ENEMY, 0, 0)[0]
		if (1):
			self.create_lib_foe(utils_obj.sec2loc(471, 468), py06616_orc_fort_encounters.CtrlOrcWarrior, const_toee.ROT07, "r03", "orc2", factions_zmod.FACTION_ENEMY, 0, 0, 0, npc_leader)

		return

	def place_monsters_r05(self):
		print("place_monsters_r04")
		npc_leader = self.create_lib_foe(utils_obj.sec2loc(456, 447), py06616_orc_fort_encounters.CtrlOrcWarrior, const_toee.ROT07, "r04", "orc1", factions_zmod.FACTION_ENEMY, 0, 0)[0]
		npc_leader.obj_set_int(toee.obj_f_npc_challenge_rating, -1)
		if (1):
			npc = self.create_lib_foe(utils_obj.sec2loc(458, 447), py06616_orc_fort_encounters.CtrlOrcWarrior, const_toee.ROT07, "r03", "orc2", factions_zmod.FACTION_ENEMY, 0, 0, 0, npc_leader)[0]
			npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1)
			npc = self.create_lib_foe(utils_obj.sec2loc(460, 447), py06616_orc_fort_encounters.CtrlOrcWarrior, const_toee.ROT07, "r03", "orc2", factions_zmod.FACTION_ENEMY, 0, 0, 0, npc_leader)[0]
			npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1)
			npc = self.create_lib_foe(utils_obj.sec2loc(462, 447), py06616_orc_fort_encounters.CtrlOrcWarrior, const_toee.ROT07, "r03", "orc2", factions_zmod.FACTION_ENEMY, 0, 0, 0, npc_leader)[0]
			npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1)

		return

	def place_encounter_r06(self):
		npc = self.create_promter_at(utils_obj.sec2loc(446, 475), self.get_dialogid_default(), 30, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Archers", const_toee.rotation_0800_oclock)
		self.vars["archers_promter_id"] = npc.id
		#npc.scripts[const_toee.sn_bust] = DAEMON_SCRIPT_ID
		return

	def place_blockade(self):
		blockade_ids = list()

		def place_block(x, y, ox, oy):
			block = toee.game.obj_create(2040, utils_obj.sec2loc(x, y), ox, oy) # mirror
			block.move(utils_obj.sec2loc(x, y), ox, oy)
			block.rotation = 2.3561945
			block.object_flag_unset(toee.OF_SEE_THROUGH)
			block.object_flag_unset(toee.OF_SHOOT_THROUGH)
			block.object_flag_unset(toee.OF_CLICK_THROUGH)
			blockade_ids.append(block.id)
			return block

		place_block(455, 472, -4.242641, 7.071068)
		place_block(455, 475, -2.82842684, 2.82842779)
		place_block(455, 478, -5.65685368, -2.82842684)
		self.vars["blockade_ids"] = blockade_ids
		return

	def place_monsters_r06(self):
		encounter = "r06"
		print("place_monsters_{}".format(encounter))

		#TODO: High grass cover
		mons = list()
		npc_leader_tup = self.create_lib_foe2(449, 486, py06616_orc_fort_encounters.CtrlOrcSergeantR06, const_toee.ROT07, encounter, "sergant", 0, 0)
		mons.append(npc_leader_tup)
		mons.append(self.create_lib_foe2(451, 488, py06616_orc_fort_encounters.CtrlOrcWarriorArcherR06Leather, const_toee.ROT07, encounter, "orc2", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(443, 482, py06616_orc_fort_encounters.CtrlOrcWarriorArcherR06HalberdStudded, const_toee.ROT07, encounter, "orc3", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(445, 481, py06616_orc_fort_encounters.CtrlOrcWarriorArcherR06HalberdScale, const_toee.ROT07, encounter, "orc4", 0, 0, 0, npc_leader_tup))

		mons.append(self.create_lib_foe2(451, 461, py06616_orc_fort_encounters.CtrlOrcWarriorArcherR06Leather, const_toee.ROT07, encounter, "orc5", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(443, 462, py06616_orc_fort_encounters.CtrlOrcWarriorArcherR06Studded, const_toee.ROT07, encounter, "orc6", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(443, 464, py06616_orc_fort_encounters.CtrlOrcWarriorArcherR06HalberdScale, const_toee.ROT07, encounter, "orc7", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(443, 466, py06616_orc_fort_encounters.CtrlOrcWarriorArcherR06HalberdStudded, const_toee.ROT07, encounter, "orc8", 0, 0, 0, npc_leader_tup))

		for tup in mons:
			if tup and tup[0]:
				#tup[0].condition_add("TurnWatcher")
				tup[0].condition_add_with_args("SurpriseRound2", 1)
		for pc in toee.game.party:
			#pc.condition_add("TurnWatcher")
			pc.condition_add_with_args("Surprised2", 1)
		self.monsters_attack(monster_npc_infos, toee.game.leader)
		return

	def dialog_archers_place(self, npc, pc):
		utils_pc.pc_move_party(447, 475)
		self.place_blockade()
		self.place_monsters_r06()
		return

	def dialog_archers_attack(self, npc, pc):
		return

	def place_encounter_r07(self):
		npc = self.create_promter_at(utils_obj.sec2loc(439, 475), self.get_dialogid_default(), 40, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_FLOAT_DIALOG_LINE, "Tracks", const_toee.ROT08)
		self.vars["archers_promter_id"] = npc.id
		#npc.scripts[const_toee.sn_bust] = DAEMON_SCRIPT_ID
		return

	def place_monsters_r08(self):
		encounter = "r08"
		print("place_monsters_{}".format(encounter))

		mons = list()
		npc_leader_tup = self.create_lib_foe2(444, 499, py06616_orc_fort_encounters.CtrlOrcWarriorR08, const_toee.ROT11, encounter, "orc1", 0, 0)
		mons.append(npc_leader_tup)
		mons.append(self.create_lib_foe2(447, 500, py06616_orc_fort_encounters.CtrlOrcWarriorR08, const_toee.ROT11, encounter, "orc2", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(450, 500, py06616_orc_fort_encounters.CtrlOrcWarriorR08, const_toee.ROT11, encounter, "orc3", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(448, 493, py06616_orc_fort_encounters.CtrlOrcWarriorR08, const_toee.ROT02, encounter, "orc4", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(444, 494, py06616_orc_fort_encounters.CtrlOrcWarriorR08, const_toee.ROT02, encounter, "orc5", 0, 0, 0, npc_leader_tup))
		mons.append(self.create_lib_foe2(450, 493, py06616_orc_fort_encounters.CtrlOrcWarriorR08, const_toee.ROT02, encounter, "orc6", 0, 0, 0, npc_leader_tup))
		return

	def place_ecnounter_loot_r09(self):
		loc = utils_obj.sec2loc(451, 517)
		utils_item.item_create(const_proto_weapon.PROTO_WEAPON_GREATSWORD_MASTERWORK, loc, 5, 5)
		utils_item.item_create(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, loc, 1, 1)

		loc = utils_obj.sec2loc(449, 521)
		toee.game.obj_create(const_proto_items.PROTO_MONEY_GOLD, loc).obj_set_int(toee.obj_f_money_quantity, 892)
		toee.game.obj_create(const_proto_items.PROTO_GENERIC_JASPER_BLUE, loc, 2, 2)
		# humanoid slaying arrow TODO
		return

	def place_encounter_r10(self):
		encounter = "r10"
		print("place_monsters_{}".format(encounter))

		npc_leader_tup = self.create_lib_foe2(441, 520, py06616_orc_fort_encounters.CtrlLiutenentR10, const_toee.ROT11, encounter, "liutenant", 0, 1)
		return

	def dialog_liutenant_attack(self, npc_leader, pc):
		utils_pc.pc_move_party(440, 515)
		encounter = "r10"
		print("place_monsters_{}".format(encounter))

		mons = list()
		mons.append(npc_leader)
		mons.append(self.create_lib_foe2(436, 521, py06616_orc_fort_encounters.CtrlGuardHumanR10, const_toee.ROT07, encounter, "guard2", 0, 0, 0, npc_leader)[0])
		mons.append(self.create_lib_foe2(434, 521, py06616_orc_fort_encounters.CtrlGuardHumanR10Chainmail, const_toee.ROT07, encounter, "guard3", 0, 0, 0, npc_leader)[0])
		mons.append(self.create_lib_foe2(434, 523, py06616_orc_fort_encounters.CtrlGuardHumanR10Longbow, const_toee.ROT07, encounter, "guard4", 0, 0, 0, npc_leader)[0])
		mons.append(self.create_lib_foe2(436, 523, py06616_orc_fort_encounters.CtrlGuardDwarfR10Greataxe, const_toee.ROT07, encounter, "guard5", 0, 0, 0, npc_leader)[0])

		mons.append(self.create_lib_foe2(440, 507, py06616_orc_fort_encounters.CtrlGuardHumanR10Flail, const_toee.ROT01, encounter, "guard6", 0, 0, 0, npc_leader)[0])
		mons.append(self.create_lib_foe2(442, 507, py06616_orc_fort_encounters.CtrlGuardDwarfR10Falchion, const_toee.ROT01, encounter, "guard7", 0, 0, 0, npc_leader)[0])
		mons.append(self.create_lib_foe2(440, 505, py06616_orc_fort_encounters.CtrlGuardElfR10Longbow, const_toee.ROT01, encounter, "guard8", 0, 0, 0, npc_leader)[0])
		mons.append(self.create_lib_foe2(442, 505, py06616_orc_fort_encounters.CtrlGuardHumanR10Warhammer, const_toee.ROT01, encounter, "guard9", 0, 0, 0, npc_leader)[0])

		for m in mons:
			m.attack(pc)
		return

	def place_encounter_r11(self):
		self.create_promter_at(utils_obj.sec2loc(429, 522), self.get_dialogid_default(), 80, 1, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Alarm Doors", const_toee.ROT08)
		return

	def place_monsters_r11(self):
		encounter = "r11"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(420, 506, py06616_orc_fort_encounters.CtrlWizardHumanR11Lv5Leader, const_toee.ROT04, encounter, "wizard_lv5_1", 0, 0, 0)
		self.create_lib_foe2(422, 506, py06616_orc_fort_encounters.CtrlWizardHumanR11Lv5, const_toee.ROT04, encounter, "wizard_lv5_2", 0, 0, 0, npc_leader)
		self.create_lib_foe2(424, 506, py06616_orc_fort_encounters.CtrlWizardHumanR11Necro3, const_toee.ROT04, encounter, "wizard_lv3_necro_3", 0, 0, 0, npc_leader)
		self.create_lib_foe2(420, 508, py06616_orc_fort_encounters.CtrlWizardHumanR11Conj3, const_toee.ROT04, encounter, "wizard_lv3_conj_4", 0, 0, 0, npc_leader)
		self.create_lib_foe2(422, 508, py06616_orc_fort_encounters.CtrlWizardHumanR11Ench3, const_toee.ROT04, encounter, "wizard_lv3_ench_5", 0, 0, 0, npc_leader)
		return

	def dialog_encounter_11_activate(self, npc, pc, suprised):
		prepared = False
		lot = self.get_monsterinfos_and_npc_and_ctrl_by_encounter("r11")
		for info, obj, ctrl in lot:
			assert isinstance(obj, toee.PyObjHandle)
			if obj and ctrl and "dialog_prepare" in dir(ctrl):
				ctrl.dialog_prepare(obj, suprised)
				prepared = True

		if prepared:
			for pc in toee.game.party:
				#pc.condition_add("TurnWatcher")
				pc.condition_add_with_args("SurpriseRound2", 1)
		return

	def dialog_encounter_11_open_doors(self, npc, pc, force):
		#force: 0 - slowly, 1 - normal, 2 - force
		doors_r11_ids = self.vars.get("doors_r11_ids")
		if doors_r11_ids:
			for iid in doors_r11_ids:
				door = toee.game.get_obj_by_id(iid)
				if door:
					door.portal_toggle_open()
					py06214_doors_autodestroy.san_use(door, None)
					if force < 2:
						toee.game.sound_local_obj(4057, door) # sound of door open
					#else:
					#	toee.game.sound_local_obj(4081, door) # sound of door smash - does not work
					if force:
						toee.game.sound_local_obj(4080, door) # door bells
		if rumor_control.is_rumor_given(module_quests.RUMOR_ORC_FORT_LIUTENENT_HELP):
			self.place_encounter_r14()
		return

	def place_encounter_r12(self):
		self.create_promter_at(utils_obj.sec2loc(428, 516), self.get_dialogid_default(), 60, 5, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Barrels", const_toee.ROT10)
		return

	def place_monsters_r12(self):
		encounter = "r12"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(426, 512, py06621_kots_monsters.CtrlCentipede, const_toee.ROT04, encounter, "centipede", 0, 0, 0)
		return
	
	def place_monsters_r13(self):
		encounter = "r13"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(431, 492, py06616_orc_fort_encounters.CtrlDragonGreenLarge, const_toee.ROT01, encounter, "dragon", 0, 0, 0)
		return

	def place_encounter_r14(self):
		self.create_promter_at(utils_obj.sec2loc(433, 515), self.get_dialogid_default(), 120, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Pool", const_toee.ROT10)
		return

	def dialog_encounter_14_give(self, npc, pc):
		utils_pc.pc_award_experience_each(400, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER_OF_DRAGON_SLAYING_ARROW, pc, 3)
		return

	def place_monsters_r15(self):
		encounter = "r15"
		print("place_monsters_{}".format(encounter))

		loct = (421, 494)

		def place(x, y, c, r, n):
			npc_tup = self.create_lib_foe2(loct[0] + x, loct[1] + y, c, r, encounter, n, 0, 1, 0)
			npc = npc_tup[0]
			assert isinstance(npc, toee.PyObjHandle)
			npc.npc_flag_set(toee.ONF_NO_ATTACK)
			npc.critter_flag_set(toee.OCF_MUTE)
			npc.object_flag_set(toee.OF_INVULNERABLE)
			return npc_tup

		npc_tup = place(0, 0, py06616_orc_fort_encounters.CtrlSlaveInStuporElf, const_toee.ROT07, "slave1")
		npc_tup = place(0, -2, py06616_orc_fort_encounters.CtrlSlaveInStuporElf, const_toee.ROT07, "slave2")
		npc_tup = place(0, -4, py06616_orc_fort_encounters.CtrlSlaveInStupor, const_toee.ROT07, "slave3")
		npc_tup = place(0, -6, py06616_orc_fort_encounters.CtrlSlaveInStuporWoman, const_toee.ROT07, "slave4")
		npc_tup = place(0, -8, py06616_orc_fort_encounters.CtrlSlaveInStuporDwarf, const_toee.ROT07, "slave5")
		npc_tup = place(0, -10, py06616_orc_fort_encounters.CtrlSlaveInStuporWomanBlue, const_toee.ROT07, "slave6")

		npc_tup = place(2, 0, py06616_orc_fort_encounters.CtrlSlaveInStuporWomanBlue, const_toee.ROT07, "slave7")
		npc_tup = place(2, -2, py06616_orc_fort_encounters.CtrlSlaveInStupor, const_toee.ROT07, "slave8")
		npc_tup = place(2, -4, py06616_orc_fort_encounters.CtrlSlaveInStupor, const_toee.ROT07, "slave9")
		npc_tup = place(2, -6, py06616_orc_fort_encounters.CtrlSlaveInStuporWoman, const_toee.ROT07, "slave10")
		npc_tup = place(2, -8, py06616_orc_fort_encounters.CtrlSlaveInStuporElf, const_toee.ROT07, "slave11")
		npc_tup = place(2, -10, py06616_orc_fort_encounters.CtrlSlaveInStuporWomanBlue, const_toee.ROT07, "slave12")
		return

	def place_encounter_r16(self):
		npc = self.create_promter_at(utils_obj.sec2loc(446, 454), self.get_dialogid_default(), 140, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_FLOAT_DIALOG_LINE, "Smelly room", const_toee.ROT01)
		return

	def place_monsters_r17(self):
		encounter = "r17"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(447, 444, py06621_kots_monsters.CtrlSkeleton, const_toee.ROT04, encounter, "skeleton01", 0, 0, 0)
		npc_leader[1].create_weapon_by_proto(npc_leader[0], const_proto_weapon.PROTO_LONGSWORD)
		npc_leader[1].create_weapon_by_proto(npc_leader[0], const_proto_armor.PROTO_SHIELD_SMALL_STEEL)

		npc_tup = self.create_lib_foe2(451, 443, py06621_kots_monsters.CtrlSkeleton, const_toee.ROT04, encounter, "skeleton02", 0, 0, 0, npc_leader)
		npc_tup[1].create_weapon_by_proto(npc_tup[0], const_proto_weapon.PROTO_WEAPON_FALCHION)

		npc_tup = self.create_lib_foe2(451, 430, py06621_kots_monsters.CtrlSkeleton, const_toee.ROT04, encounter, "skeleton03", 0, 0, 0, npc_leader)
		npc_tup[1].create_weapon_by_proto(npc_tup[0], const_proto_weapon.PROTO_LONGSWORD)
		npc_tup[1].create_weapon_by_proto(npc_tup[0], const_proto_armor.PROTO_SHIELD_SMALL_STEEL)

		self.create_lib_foe2(447, 434, py06621_kots_monsters.CtrlZombie, const_toee.ROT04, encounter, "zombie04", 0, 0, 0, npc_leader)
		self.create_lib_foe2(450, 433, py06621_kots_monsters.CtrlZombie, const_toee.ROT04, encounter, "zombie05", 0, 0, 0, npc_leader)
		self.create_lib_foe2(448, 431, py06621_kots_monsters.CtrlZombie, const_toee.ROT04, encounter, "zombie06", 0, 0, 0, npc_leader)
		# 450 xp for 4xlv6
		loc = utils_obj.sec2loc(439, 444)
		toee.game.obj_create(const_proto_items.PROTO_MONEY_GOLD, loc).obj_set_int(toee.obj_f_money_quantity, 892)
		return

	def place_monsters_r18(self):
		encounter = "r18"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(440, 438, py06616_orc_fort_encounters.CtrlTronen, const_toee.ROT08, encounter, "tronen", 0, 1, 0)
		npc_tup = self.create_lib_foe2(439, 430, py06616_orc_fort_encounters.CtrlExSlave, const_toee.ROT08, encounter, "ex_slave1", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(441, 427, py06616_orc_fort_encounters.CtrlExSlaveW, const_toee.ROT08, encounter, "ex_slave2", 0, 1, 0, npc_leader)
		return

	def place_encounter_r19(self):
		npc = self.create_promter_at(utils_obj.sec2loc(430, 473), self.get_dialogid_default(), 150, 10, py06122_cormyr_prompter.PROMTER_DIALOG_METHOD_DIALOG, "Smelly room", const_toee.ROT04)
		return

	def place_monsters_r19(self):
		encounter = "r19"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(428, 473, py06621_kots_monsters.CtrlGnollWarrior2, const_toee.ROT11, encounter, "gnoll1", 0, 1, 0)
		npc_tup = self.create_lib_foe2(426, 473, py06621_kots_monsters.CtrlGnollWarrior2Leather, const_toee.ROT11, encounter, "gnoll2", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(424, 473, py06621_kots_monsters.CtrlGnollWarrior2StuddedFlail, const_toee.ROT11, encounter, "gnoll3", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(428, 471, py06621_kots_monsters.CtrlGnollWarrior2LeatherScythe, const_toee.ROT11, encounter, "gnoll4", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(430, 471, py06621_kots_monsters.CtrlGnollWarrior2ScaleScimitar, const_toee.ROT11, encounter, "gnoll5", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(430, 469, py06621_kots_monsters.CtrlGnollWarrior2StuddedFlail, const_toee.ROT01, encounter, "gnoll6", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(429, 467, py06621_kots_monsters.CtrlGnollWarrior2, const_toee.ROT01, encounter, "gnoll7", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(431, 467, py06621_kots_monsters.CtrlGnollWarrior2LeatherLongsword, const_toee.ROT01, encounter, "gnoll8", 0, 1, 0, npc_leader)
		return

	def place_monsters_r19_allies(self):
		encounter = "r19"
		print("place_monsters_{}_allies".format(encounter))

		self.create_npc_at(utils_obj.sec2loc(424, 467), py06616_orc_fort_encounters.CtrlSlaveR19, const_toee.ROT05, encounter, "slave", factions_zmod.FACTION_ALLY_NPC, 0, 1, 0)
		return

	def dialog_r19_attack(self, npc, pc, surprised):
		prepared = False
		lot = self.get_monsterinfos_and_npc_and_ctrl_by_encounter("r19")
		slave = None
		gnoll1 = None
		pc_leader = toee.game.party[0]
		for info, obj, ctrl in lot:
			assert isinstance(obj, toee.PyObjHandle)
			if info.monster_code_name == "slave":
				#obj.condition_add_with_args("SurpriseRound2", 1)
				pc_leader.ai_follower_add(obj)
			else:
				obj.condition_add_with_args("Surprised2", 1)
				obj.attack(pc_leader)
				if info.monster_code_name == "gnoll1":
					gnoll1 = obj
			
		if slave and gnoll1:
			slave.attack(gnoll1)

		for pc in toee.game.party:
			pc.condition_add_with_args("SurpriseRound2", 1)
		return

	def place_monsters_r20(self):
		encounter = "r20"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(433, 457, py06616_orc_fort_encounters.CtrlTandek, const_toee.ROT01, encounter, "tandek", 0, 1, 0)
		npc_tup = self.create_lib_foe2(426, 462, py06616_orc_fort_encounters.CtrlTandekBodyguard, const_toee.ROT11, encounter, "bodyguard1", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(431, 461, py06616_orc_fort_encounters.CtrlTandekBodyguard2, const_toee.ROT08, encounter, "bodyguard2", 0, 1, 0, npc_leader)
		return

	def place_monsters_r21(self):
		encounter = "r21"
		print("place_monsters_{}".format(encounter))

		npc_leader = self.create_lib_foe2(432, 451, py06616_orc_fort_encounters.CtrlExecutioner, const_toee.ROT01, encounter, "executioner", 0, 1, 0)
		return

	def place_monsters_r21(self):
		encounter = "r21"
		print("place_monsters_{}".format(encounter))
		# xp 2025 for 4x6 + 130 gp
		# For defeating the minor Slaver Lord Icarus, each party member gains an additional 1,000 experience points!

		npc_leader = self.create_lib_foe2(424, 429, py06616_orc_fort_encounters.CtrlIcarus, const_toee.ROT03, encounter, "icarus", 0, 1, 0)
		npc_tup = self.create_lib_foe2(420, 430, py06616_orc_fort_encounters.CtrlOrcWarrior3, const_toee.ROT05, encounter, "orc1", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(420, 428, py06616_orc_fort_encounters.CtrlOrcWarrior3Crossbow, const_toee.ROT05, encounter, "orc2", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(422, 427, py06616_orc_fort_encounters.CtrlOrcWizard3, const_toee.ROT04, encounter, "orc_wizard3", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(426, 427, py06616_orc_fort_encounters.CtrlOrcWarrior3Crossbow, const_toee.ROT04, encounter, "orc4", 0, 1, 0, npc_leader)

		npc_tup = self.create_lib_foe2(428, 433, py06616_orc_fort_encounters.CtrlOrcWarrior3Crossbow, const_toee.ROT04, encounter, "orc4", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(428, 435, py06616_orc_fort_encounters.CtrlOrcWarrior3, const_toee.ROT03, encounter, "orc5", 0, 1, 0, npc_leader)
		npc_tup = self.create_lib_foe2(428, 440, py06616_orc_fort_encounters.CtrlOrcWarrior3Crossbow, const_toee.ROT02, encounter, "orc6", 0, 1, 0, npc_leader)
		return
