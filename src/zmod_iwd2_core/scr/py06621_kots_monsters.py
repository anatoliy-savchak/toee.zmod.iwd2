import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, py14764_npc_portal

MODULE_SCRIPT_ID = 6621

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)

def cs(): return None

class CtrlGiantSpider(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14047

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_enter_combat] = MODULE_SCRIPT_ID
		return

	def setup_char(self, npc):
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([15, 17, 12, 15, 12, 11], utils_npc.stats_random(-2, 2)))

		npc.condition_add("Monster_Sole_Natural")
		npc.condition_add_with_args("Monster DR Magic", 5)
		npc.condition_add_with_args("Monster_Ability_Drain_Su", 0, 0, toee.stat_strength, toee.dice_new("1d3").packed)

		# monster caster level = HD
		# monster DC is based on Wisdom by default

		dc_cha = max(npc.stat_base_get(toee.stat_cha_mod), 1)
		dc_wisdom = npc.stat_base_get(toee.stat_wis_mod)
		# dc default = 10 + spell_level + dc_wisdom
		# dc target = 10 + spell_level + dc_cha
		dc_increase = dc_cha - dc_wisdom
		print("dc_increase: {}".format(dc_increase))
		dc_increase += 2 # for Web
		npc.condition_add_with_args("Spell_DC_Mod", 0, dc_increase)
		self.setup_feats(npc)
		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_weapon_finesse_unarmed_strike_medium_sized_being)
		npc.feat_add(toee.feat_weapon_focus_unarmed_strike_medium_sized_being)
		npc.feat_add(toee.feat_alertness, 1)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(90, 110))
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.domain_special
		caster_level = 2
		# 2
		self.spells.add_spell(toee.spell_web, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_web, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			#if (not utils_npc_spells_tactics.STWeb(npc, self.spells, tac).execute()):
			#	break

			web_spell_tactic = utils_npc_spells_tactics.STWebSingle(npc, self.spells, tac)
			if web_spell_tactic.spells_left() > 0:
				foes_can_los = self._vars_tactics["foes_can_los"]
				if not foes_can_los:
					foes_can_los = self._vars_tactics["foes_can_sense"]
				if web_spell_tactic.pick_target_best(foes_can_los):
					if not web_spell_tactic.execute():
						break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

class CtrlGiantSpiderWar(CtrlGiantSpider):
	def setup_char(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlGiantSpiderWar, self).setup_char(npc)

		character_levels = 4
		npc.make_class(toee.stat_level_fighter, character_levels) # 20 is max

		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 3) # was 2

		#npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 4+2) # natural bab
		
		npc.feat_add(toee.feat_toughness, 1)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(190, 210))
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 2)
		return

class CtrlZombie(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14092

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([16, 10, 10, 1, 10, 1], utils_npc.stats_random(-2, 2)))
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_alertness, 1)

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlSkeleton(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14186

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([14, 14, 10, 1, 10, 1], utils_npc.stats_random(-2, 2)))
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		npc.feat_add(toee.feat_alertness, 1)

		#utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(20, 30))
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		npc.item_wield_best_all()
		return

	def create_weapon_by_proto(self, npc, weapon_proto):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(weapon_proto, int)
		weapon = toee.game.obj_create(weapon_proto, npc.location)
		npc.item_get(weapon)
		npc.item_wield_best_all()
		return weapon

class CtrlCentipede(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14761 

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID

		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([13, 15, 10, 1, 10, 4], utils_npc.stats_random(-2, 2)))
		#utils_npc.npc_hitdice_set(npc, 6, 8, 0)

		npc.feat_add(toee.feat_cleave, 0)
		npc.condition_add_with_args("Monster_Ability_Drain_Su", 0, 0, toee.stat_dexterity, toee.dice_new("1d2").packed)
		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		npc.condition_add("Monster_Sole_Natural")

		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

class CtrlGhoul(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return 14095

	def setup_scripts(self, npc):
		npc.scripts[const_toee.sn_start_combat] = MODULE_SCRIPT_ID
		return

	def setup_char(self, npc):
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_EVIL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum([15, 17, 12, 15, 12, 4], utils_npc.stats_random(-2, 2)))

		atk_index = 0
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, atk_index, const_toee.nwt_bite)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, atk_index, 1) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, atk_index, 1) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, atk_index, toee.dice_new("1d6").packed)

		on_attacks = 1<<(1-1) # on first attack
		npc.condition_add_with_args("Monster_Ability_Drain_Su", 0, 0, toee.stat_constitution, toee.dice_new("1d2").packed, on_attacks)

		atk_index = 1
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, atk_index, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, atk_index, 1-5) # natural bab, second attack
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, atk_index, 2) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, atk_index, toee.dice_new("1d3").packed)

		on_attacks = (1<<(2-1)) + (1<<(3-1)) # on second and third attack
		npc.condition_add("Monster Melee Paralysis Ex", 0, 0, toee.dice_new("1d4").packed, on_attacks) # 0 dc, 1 save, 2 dice, 3 attacks_with_paralysis

		npc.feat_add(toee.feat_weapon_finesse_unarmed_strike_medium_sized_being, 1)
		return

	def setup_end(self, npc):
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_random_first(npc, 0)
		return

class CtrlGnoll(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GNOLL

	def setup_scripts(self, npc):
		return

	def setup_appearance(self, npc):
		return

	def setup_char(self, npc):
		#npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_NEUTRAL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_GNOLL_ARRAY, utils_npc.stats_random(-2, 2)))
		#utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 2)

		#char_levels = 8
		#npc.make_class(toee.stat_level_cleric, char_levels) # 20 is max
		#npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		#npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)
		self.setup_feats(npc)
		return

	def setup_feats(self, npc):
		#npc.feat_add(toee.feat_spell_focus_necromancy)
		#npc.feat_add(toee.feat_cleave, 1)
		return

	def setup_gear(self, npc):
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc, 1)
		self.setup_weapon(npc)
		self.setup_armor(npc)
		return

	def setup_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_GNOLL_1, npc)
		return

	def setup_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_BATTLEAXE_GNOLL, npc)
		return

	def setup_loot(self, npc):
		# usually none
		return

	def setup_end(self, npc):
		npc.item_wield_best_all()
		self.vars["hp_lines"] = utils_npc.npc_generate_hp_avg_first(npc, 1)
		return

class CtrlGnollWarrior2(CtrlGnoll):
	def setup_char(self, npc):
		#npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_NEUTRAL) 
		utils_npc.npc_abilities_set(npc, utils_npc.stats_sum(utils_races.RACE_ABILITY_GNOLL_ARRAY, utils_npc.stats_random(-2, 2)))
		utils_npc.npc_hitdice_set(npc, 1, 8, 0)
		npc.obj_set_int(toee.obj_f_npc_challenge_rating, 0)

		char_levels = 2
		npc.make_class(const_toee.stat_level_npc_warriror, char_levels) # 20 is max
		npc.skill_ranks_set(toee.skill_tumble, 3 + (char_levels-1)*1)
		#npc.skill_ranks_set(toee.skill_concentration, 3 + (char_levels-1)*1)

		self.setup_feats(npc)
		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_weapon_focus_battleaxe)
		npc.feat_add(toee.feat_toughness, 1)
		return

class CtrlGnollWarrior2Leather(CtrlGnollWarrior2):
	def setup_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_GNOLL_1, npc)
		return

	def setup_loot(self, npc):
		utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range(2, 5))
		return

class CtrlGnollWarrior2StuddedFlail(CtrlGnollWarrior2):
	def setup_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc)
		return

	def setup_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_FLAIL_HEAVY, npc)
		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_weapon_focus_heavy_flail)
		npc.feat_add(toee.feat_great_fortitude, 1)
		return

class CtrlGnollWarrior2LeatherScythe(CtrlGnollWarrior2):
	def setup_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)
		return

	def setup_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SCYTHE, npc)
		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_blind_fight)
		npc.feat_add(toee.feat_cleave, 1)
		return

class CtrlGnollWarrior2ScaleScimitar(CtrlGnollWarrior2):
	def setup_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_GNOLL_2, npc)
		return

	def setup_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR, npc)
		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_cleave, 1)
		return

class CtrlGnollWarrior2LeatherLongsword(CtrlGnollWarrior2):
	def setup_armor(self, npc):
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_GNOLL_3, npc)
		return

	def setup_weapon(self, npc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		return

	def setup_feats(self, npc):
		npc.feat_add(toee.feat_weapon_focus_longsword)
		npc.feat_add(toee.feat_toughness, 1)
		return
