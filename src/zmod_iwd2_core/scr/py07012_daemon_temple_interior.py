import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import startup_zmod, utils_sneak, monster_info, copy, rttoee_consts, const_animate, const_sceneries
import const_proto_items, const_proto_cloth, const_proto_rings, py07023_npc_temple_tower, const_proto_containers, const_proto_potions, utils_locks, tpdp

TEMPLE_INTERIOR = 7012
TEMPLE_INTERIOR_DAEMON_ID = "G_A3BFADF8_E76D_4254_AD0A_4ECF00BBFEF9"
TEMPLE_INTERIOR_DAEMON_DIALOG = 7012

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_INTERIOR, CtrlTempleInterior)

def san_first_heartbeat(attachee, triggerer):
	#print(attachee.id)
	#debug.breakp("")
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_INTERIOR, CtrlTempleInterior)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_INTERIOR, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_INTERIOR, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, rttoee_consts.MAP_ID_TEMPLE_INTERIOR, cs())

def cs():
	o = utils_storage.obj_storage_by_id(TEMPLE_INTERIOR_DAEMON_ID)
	if (not o): return None
	if (CtrlTempleInterior.get_name() in o.data):
		result = o.data[CtrlTempleInterior.get_name()]
	else: return None
	assert isinstance(result, CtrlTempleInterior)
	return result

class CtrlTempleInterior(ctrl_daemon2.CtrlDaemon2):
	def __init__(self):
		super(CtrlTempleInterior, self).__init__()
		self.init_daemon2_fields(rttoee_consts.MAP_ID_TEMPLE_INTERIOR, TEMPLE_INTERIOR, "temple_interior")
		return

	def place_encounters_initial(self):
		self.place_monsters()
		#toee.game.fade_and_teleport(0, 0, 0, self.get_map_default(), 489, 420) #leader
		return

	def place_monsters(self):
		# 8. Camp (EL 5)
		if (1):
			self.create_npc_at(utils_obj.sec2loc(463, 488), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "01", None, 0, 0)
		if (0):
			self.create_npc_at(utils_obj.sec2loc(463-2, 488+2), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "02", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(463-4, 488+4), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "03", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(463-6, 488+5), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "04", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(463-8, 488+8), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "05", None, 0, 0)

			self.create_npc_at(utils_obj.sec2loc(468, 491), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "06", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(468-2, 491+2), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "07", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(468-4, 491+4), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "08", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(468-6, 491+5), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "09", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(468-8, 491+8), py07023_npc_temple_tower.CtrlHobgoblin, const_toee.rotation_0500_oclock, "temple_08", "10", None, 0, 0)

		# 10. Elite Warriors (EL 4)
		if (0):
			self.create_npc_at(utils_obj.sec2loc(488, 491), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0300_oclock, "temple_10", "01", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(488+2, 491+2), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0300_oclock, "temple_10", "02", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(488+4, 491+4), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0300_oclock, "temple_10", "03", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(488-2, 491+5), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0300_oclock, "temple_10", "04", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(488-4, 491+8), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0300_oclock, "temple_10", "05", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(488-6, 491+10), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0300_oclock, "temple_10", "06", None, 0, 0)

		# 13. Grand Staircase (EL 3)
		if (0):
			self.create_npc_at(utils_obj.sec2loc(489, 458), py07023_npc_temple_tower.CtrlDireApe, const_toee.rotation_0300_oclock, "temple_13", "ape", None, 0, 0)

		# 16. Throne (EL 5)
		if (1):
			#self.create_npc_at(utils_obj.sec2loc(494, 406), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0500_oclock, "temple_16", "01", None, 0, 0)
			#self.create_npc_at(utils_obj.sec2loc(484, 407), py07023_npc_temple_tower.CtrlHobgoblinElite, const_toee.rotation_0500_oclock, "temple_16", "02", None, 0, 0)
			self.create_npc_at(utils_obj.sec2loc(489, 405), py07023_npc_temple_tower.CtrlHobgoblinRarkus, const_toee.rotation_0500_oclock, "temple_16", "rarkus", None, 0, 0)
		return

	@staticmethod
	def pc_entered_combat_post(self, initiator):
		assert isinstance(initiator, toee.PyObjHandle)
		print("pc_entered_combat_post post")
		#debug.breakp("pc_entered_combat_post post")
		npcs = self.get_alive_monster_npcs("temple_")
		if (npcs):
			assert isinstance(locf, tpdp.LocAndOffsets)
			for name, baddy in npcs.items():
				if (not "temple_08" in name and not "temple_10" in name and not "temple_13" in name and not "temple_16" in name): continue
				assert isinstance(baddy, toee.PyObjHandle)
				if (baddy.is_active_combatant()): continue
				print("adding to combat: {}".format(baddy))
				locs = utils_npc.npc_find_path_to_target(baddy, toee.game.leader)
				loc = 0
				if (locs):loc = locs[0]
				else: loc = utils_obj.sec2loc(475 + toee.game.random_range(-5, 5), 483 + toee.game.random_range(-5, 5))
				if (loc):
					baddy.standpoint_set(toee.STANDPOINT_DAY, -1, loc)
					baddy.standpoint_set(toee.STANDPOINT_NIGHT, -1, loc)

				baddy.attack(toee.game.leader)
				baddy.add_to_initiative()
				if (not baddy.is_active_combatant()): 
					print("failed to add combatant: {}".format(baddy))
		toee.game.update_combat_ui()
		#debug.breakp("pc_entered_combat_post end")
		return

	def combat_start(self, initiator):
		assert isinstance(initiator, toee.PyObjHandle)
		print("combat_start")
		toee.game.timevent_add(CtrlTempleInterior.pc_entered_combat_post, (self, initiator), 1, 1)
		return

	def create_npc_at(self, npc_loc, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1):
		npc, ctrl = super(CtrlTempleInterior, self).create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos)
		# dev
		if (npc):
			utils_npc.npc_description_set_new(npc, encounter + code_name)
		return npc, ctrl

	def consider_target_not_too_far(self, attacker, target, distance_direct_ft):
		assert isinstance(attacker, toee.PyObjHandle)
		assert isinstance(target, toee.PyObjHandle)
		assert isinstance(distance_direct_ft, float)

		return 1