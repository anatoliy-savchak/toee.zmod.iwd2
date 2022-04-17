import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_storage
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls
import const_proto_npc, utils_npc, utils_toee, module_globals, module_quests, rumor_control, const_proto_wondrous, const_proto_rings

THIS_SCRIPT_ID = 14714
def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

class CtrlKeepCommander(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = THIS_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = THIS_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		if (1):
			npc.feat_add(toee.feat_blind_fight)
			npc.feat_add(toee.feat_cleave)
			npc.feat_add(toee.feat_combat_reflexes)
			npc.feat_add(toee.feat_exotic_weapon_proficiency_bastard_sword)
			npc.feat_add(toee.feat_great_cleave)
			npc.feat_add(toee.feat_great_fortitude)
			npc.feat_add(toee.feat_greater_weapon_specialization_bastard_sword)
			npc.feat_add(toee.feat_greater_weapon_focus_bastard_sword)
			npc.feat_add(toee.feat_improved_grapple)
			npc.feat_add(toee.feat_improved_critical_bastard_sword)
			npc.feat_add(toee.feat_improved_initiative)
			npc.feat_add(toee.feat_improved_unarmed_strike)
			npc.feat_add(toee.feat_iron_will)
			npc.feat_add(toee.feat_lightning_reflexes)
			npc.feat_add(toee.feat_mobility)
			npc.feat_add(toee.feat_toughness)
			npc.feat_add(toee.feat_weapon_specialization_bastard_sword)
			npc.feat_add(toee.feat_weapon_focus_bastard_sword)

			utils_npc.npc_abilities_set(npc, [30-6, 13, 23-6, 16, 15, 18])
			utils_npc.npc_hitdice_set(npc, 0, 0, 0)
			npc.make_class(toee.stat_level_fighter, 20) # 20 is max
			#utils_npc.npc_hp_set(npc, 278)
			npc.obj_set_int(toee.obj_f_critter_portrait, 8970) # Gregor
			npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) 
			nameid = utils_toee.make_custom_name("Commander Karef")
			if (nameid):
				npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
				npc.obj_set_int(const_toee.obj_f_description_correct, nameid)

			hairStyle = utils_npc.HairStyle.from_npc(npc)
			hairStyle.style = const_toee.hair_style_shorthair
			hairStyle.color = const_toee.hair_color_white
			hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		utils_item.item_clear_all(npc)

		# create inventory
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_COAT_LONG_BLACK, npc, 1, 1)
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		#utils_item.item_create_in_inventory(6048, npc) # Prince Thrommel's Plate Armor
		#utils_item.item_create_in_inventory(6061, npc) # Prince Thrommel's Large Steel Shield
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_ELVEN_BLUE, npc)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc)
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLUE, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_HEALTH_PLUS_6, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BELT_OF_GIANT_STRENGTH_PLUS_6, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_MANTLE_OF_SPELL_RESISTANCE_VIOLET, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BOOTS_OF_SPEED, npc)
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_PROTECTION_PLUS_5, npc)
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_FIRE_RESISTANCE_MAJOR, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_PLUS_5, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_PLUS_4_STEEL, npc)
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if not attachee.has_met(triggerer):
			triggerer.begin_dialog(attachee, 1)
			return toee.SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 100)
		return toee.SKIP_DEFAULT

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)
		# is disabled in dialog_initial_started for optimization!

		# only first time
		if not attachee.has_met(toee.game.leader):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				attachee.turn_towards(pc)
				pc.begin_dialog(attachee, 1)
		return toee.RUN_DEFAULT

	def dialog_initial_started(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_heartbeat] = 0
		quest = toee.game.quests[module_quests.QUEST_KEEP_KAREF_RESOLVE_CORINTH]
		if (quest.state < toee.qs_accepted):
			quest.state = toee.qs_accepted
		return

	def dialog_rumor_swcaves_informed(self, npc):
		if (not rumor_control.is_rumor_given(module_quests.RUMOR_KEEP_KAREF_WEST_CAVES_MENTIONED)):
		#if (not toee.game.global_flags[module_globals.GFLAG_KEEP_KAREF_SW_CAVES_INFORMED]):
			#toee.game.global_flags[module_globals.GFLAG_KEEP_KAREF_SW_CAVES_INFORMED] = 1
			rumor_control.rumor_give(module_quests.RUMOR_KEEP_KAREF_WEST_CAVES_MENTIONED)
		return