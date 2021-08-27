import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, utils_toee, ctrl_daemon, const_proto_wondrous

MODULE_ID = 7023

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

class CtrlHobgoblin(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14187

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.condition_add("Base_Attack_Bonus1")
		npc.scripts[const_toee.sn_enter_combat] = MODULE_ID
		utils_npc.npc_generate_hp_random(npc)

		# create inventory
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_JAVELIN, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 10))

		npc.item_wield_best_all()

class CtrlGoblinNaked(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14190

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.condition_add("Base_Attack_Bonus1")
		utils_npc.npc_generate_hp_random(npc)
		#npc.scripts[const_toee.sn_start_combat] = MODULE_ID

		# create inventory
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_JAVELIN, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_JAVELIN, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_JAVELIN, npc)
		#utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR, npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 2))

		npc.item_wield_best_all()
		return

class CtrlGoblin(CtrlGoblinNaked):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlGoblin, self).after_created(npc)

		#npc.scripts[const_toee.sn_start_combat] = MODULE_ID

		# create inventory
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, npc, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc)

		npc.item_wield_best_all()
		return

class CtrlDogAggessive(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14049

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		utils_npc.npc_generate_hp_random(npc)
		return

class CtrlHobgoblinAlubya(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14187

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_ID

		name_id = utils_toee.make_custom_name("Alubya")
		npc.obj_set_int(const_toee.obj_f_description_correct, name_id)
		npc.obj_set_int(toee.obj_f_critter_description_unknown, name_id)

		npc.obj_set_int(toee.obj_f_critter_portrait, 10060) # new, alubya
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_cleric)

		utils_npc.npc_abilities_set(npc, (8, 11, 14, 10, 14, 12))
		#npc.scripts[const_toee.sn_start_combat] = MODULE_ID
		npc.feat_add(toee.feat_combat_casting)
		utils_npc.npc_generate_hp_random(npc)

		# create inventory
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, npc, 1)
		item = utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOAK_GREEN, npc, 1)
		if (item): npc.item_wield(item, toee.item_wear_cloak)
		crossbow = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_MASTERWORK, npc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc)
		if (item): npc.item_wield(item, toee.item_wear_ammo)
		weapon_flags = crossbow.obj_get_int(toee.obj_f_weapon_flags)
		if (not weapon_flags & const_toee.OWF_WEAPON_LOADED):
			weapon_flags |= const_toee.OWF_WEAPON_LOADED
		crossbow.obj_set_int(toee.obj_f_weapon_flags, weapon_flags)


		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc)

		utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_BULLS_STRENGTH, npc)
		utils_item.item_money_create_in_inventory(npc, 0, 65)

		npc.item_wield_best_all()
		return

	def start_combat(self, attachee, triggerer):
		print("{}::{} (round: {})".format(type(self).__name__, "start_combat", toee.game.combat_turn))
		assert isinstance(attachee, toee.PyObjHandle)

		if (not attachee.item_worn_at(toee.item_wear_weapon_primary)):
			attachee.item_wield_best_all()

		weapon = attachee.item_worn_at(toee.item_wear_weapon_primary)
		closest_pc, dist = utils_target_list.find_pc_closest_to_origin(attachee.location)
		print("dist: {}, closest_pc: {}, ".format(dist,closest_pc ))
		#debugg.breakp("start_combat")
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			if (self.spells.get_spell_count(toee.spell_command) and closest_pc and dist <= 25):
				tac.add_target_closest()
				#tac.add_approach()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_command))
				break
			if (self.spells.get_spell_count(toee.spell_inflict_light_wounds) and closest_pc and dist <= 25):
				tac.add_target_closest()
				tac.add_approach()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_inflict_light_wounds))
				break
			if (toee.game.is_ranged_weapon(weapon.get_weapon_type())):
				tac.add_reload()
			tac.add_target_closest()
			tac.add_attack()
			break

		if (tac.count > 0):
			tac.set_strategy(attachee)
		return toee.RUN_DEFAULT

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		stat_class = toee.stat_level_cleric
		caster_level = 1
		# 1
		self.spells.add_spell(toee.spell_command, stat_class, caster_level)
		self.spells.add_spell(toee.spell_inflict_light_wounds, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		attachee.float_text_line("It's Rarkus spies, kill them all!", toee.tf_white)
		return toee.RUN_DEFAULT

class CtrlHobgoblinElite(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14187

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_enter_combat] = MODULE_ID

		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		utils_npc.npc_abilities_set(npc, (14, 12, 16, 11, 8, 10))
		npc.feat_add(toee.feat_weapon_focus_greatsword, 1)
		utils_npc.npc_generate_hp_random(npc)

		# create inventory
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATSWORD_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_potions.PROTO_POTION_OF_BULLS_STRENGTH, npc)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 10))

		npc.item_wield_best_all()

		name_id = 0
		storage = utils_storage.obj_storage_by_id("npc_names")
		if (storage):
			if ("CtrlHobgoblinElite" in storage.data):
				name_id = storage.data["CtrlHobgoblinElite"]

		if (not name_id):
			name_id = utils_toee.make_custom_name("Elite Warrior")
			storage.data["CtrlHobgoblinElite"] = name_id
			storage.data["CtrlHobgoblinElite name"] = "Elite Warrior"

		if (name_id):
			npc.obj_set_int(const_toee.obj_f_description_correct, name_id)
			npc.obj_set_int(toee.obj_f_critter_description_unknown, name_id)
		return

class CtrlDireApe(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14502

class CtrlHobgoblinRarkus(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14187

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_enter_combat] = MODULE_ID
		npc.obj_set_int(toee.obj_f_critter_portrait, 10080) # new, rarkus
		
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_rogue)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_fighter)

		utils_npc.npc_abilities_set(npc, (16, 15, 14, 10, 10, 12))
		#npc.feat_add(toee.feat_weapon_focus_greatsword, 1)
		npc.feat_add(toee.feat_exotic_weapon_proficiency_bastard_sword, 0)
		npc.feat_add(toee.feat_weapon_focus_bastard_sword, 0)
		npc.feat_add(toee.feat_weapon_focus_short_sword, 0)
		npc.feat_add(toee.feat_weapon_specialization_bastard_sword, 0)
		npc.feat_add(toee.feat_two_weapon_fighting, 1)

		#npc.obj_set_int(toee.obj_f_npc_challenge_rating, 4)

		utils_npc.npc_generate_hp_random(npc)

		# create inventory
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, npc, 1)
		weapon_primary = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_1, npc)
		weapon_secondary = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD_MASTERWORK, npc)
		self.vars["weapon_secondary_id"] = weapon_secondary.id
		self.vars["weapon_secondary_proto"] = weapon_secondary.proto

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAINMAIL_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_potions.PROTO_POTION_OF_BULLS_STRENGTH, npc)
		utils_item.item_create_in_inventory(const_proto_potions.PROTO_POTION_OF_CURE_MODERATE_WOUNDS, npc)

		cloak = utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOAK_GREEN, npc, 1)
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(1, 10))

		npc.item_wield_best_all()
		if (weapon_secondary): npc.item_wield(weapon_secondary, toee.item_wear_weapon_secondary)
		if (cloak): npc.item_wield(cloak, toee.item_wear_cloak)

		name_id = utils_toee.make_custom_name("Rarkus")
		if (name_id):
			npc.obj_set_int(const_toee.obj_f_description_correct, name_id)
			npc.obj_set_int(toee.obj_f_critter_description_unknown, name_id)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		# fixed that in T+
		weapon_secondary_proto = self.get_var("weapon_secondary_proto")
		if (weapon_secondary_proto):
			weapon_secondary = attachee.item_find_by_proto(weapon_secondary_proto)
			if (weapon_secondary): 
				print("wielding secondary weapon: {}".format(weapon_secondary))
				attachee.item_wield(weapon_secondary, toee.item_wear_weapon_secondary)
				#debug.breakp("secondary")
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		# todo later
		return None

class CtrlHobgoblinKrebbich(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14187

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_ID

		name_id = utils_toee.make_custom_name("Krebbich")
		npc.obj_set_int(const_toee.obj_f_description_correct, name_id)
		npc.obj_set_int(toee.obj_f_critter_description_unknown, name_id)

		npc.obj_set_int(toee.obj_f_critter_portrait, 10090) # new, hobgoblin_spellscourge
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_cleric)
		#npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 5, toee.stat_level_fighter)

		utils_npc.npc_abilities_set(npc, (13, 12, 14, 14, 14, 10))
		#npc.scripts[const_toee.sn_start_combat] = MODULE_ID
		utils_npc.npc_skill_ensure(npc, toee.skill_concentration, 11)
		npc.feat_add(toee.feat_combat_casting)
		npc.feat_add(toee.feat_toughness, 1)
		utils_npc.npc_generate_hp_random(npc)

		# create inventory
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, npc, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOAK_GREEN, npc, 1, toee.item_wear_cloak)

		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR_MASTERWORK, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_NATURAL_ARMOR_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BROOCH_OF_SHIELDING, npc)

		utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_CURE_SERIOUS_WOUNDS, npc)
		utils_item.item_create_in_inventory(const_proto_scrolls.PROTO_SCROLL_OF_BEARS_ENDURANCE, npc) # todo potion

		utils_item.item_create_in_inventory(const_proto_potions.PROTO_POTION_OF_CURE_MODERATE_WOUNDS, npc)
		utils_item.item_create_in_inventory(const_proto_potions.PROTO_POTION_OF_GLIBNESS, npc)

		utils_item.item_create_in_inventory(const_proto_wands.PROTO_WAND_OF_CURE_LIGHT_WOUNDS, npc)

		utils_item.item_money_create_in_inventory(npc, 0, 65)

		npc.item_wield_best_all()
		return

	def start_combat(self, attachee, triggerer):
		print("{}::{} (round: {})".format(type(self).__name__, "start_combat", toee.game.combat_turn))
		assert isinstance(attachee, toee.PyObjHandle)

		if (not attachee.item_worn_at(toee.item_wear_weapon_primary)):
			attachee.item_wield_best_all()

		leader = attachee.leader_get()
		leader_distance = -1
		leader_near_loc = 0
		leader_hp_current_percent = 0
		if (leader and utils_npc.npc_is_alive(leader)):
			leader_distance = attachee.distance_to(leader)
			leader_hp_current_percent = utils_npc.npc_hp_current_percent(leader)
			#leader_near_loc = utils_npc.npc_find_path_to_target()
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			if (self.spells.get_spell_count(toee.spell_invisibility)):
				tac.add_target_self()
				#tac.add_approach()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_invisibility))
				tac.add_goto(510, 480)
				break
			if (self.spells.get_spell_count(toee.spell_endurance) and leader_hp_current_percent > 0):
				tac.add_target_closest()
				#tac.add_approach()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_endurance))
				break
			if (self.spells.get_spell_count(toee.spell_inflict_light_wounds) and closest_pc and dist <= 25):
				tac.add_target_closest()
				tac.add_approach()
				tac.add_cast_single_code(self.spells.prep_spell(triggerer, toee.spell_inflict_light_wounds))
				break
			if (toee.game.is_ranged_weapon(weapon.get_weapon_type())):
				tac.add_reload()
			tac.add_target_closest()
			tac.add_attack()
			break

		if (tac.count > 0):
			tac.set_strategy(attachee)
		return toee.RUN_DEFAULT

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		stat_class = toee.stat_level_cleric
		caster_level = 3
		# 2
		self.spells.add_spell(toee.spell_invisibility, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_hold_person, stat_class, caster_level)
		self.spells.add_spell(toee.spell_endurance, stat_class, caster_level)

		# 1
		self.spells.add_spell(toee.spell_command, stat_class, caster_level)
		self.spells.add_spell(toee.spell_protection_from_good, stat_class, caster_level)
		self.spells.add_spell(toee.spell_cause_fear, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		return toee.RUN_DEFAULT
