import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_npc, const_animate
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_wands
import const_proto_wondrous, const_proto_npc, utils_toee, const_proto_rings, module_globals, module_quests, rumor_control

THIS_SCRIPT_ID = 14715
def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

class CtrlWizardShania(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFELF_WOMAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = THIS_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		if (1):
			npc.feat_add(toee.feat_augment_summoning)
			npc.feat_add(toee.feat_combat_reflexes)
			npc.feat_add(toee.feat_dodge)
			npc.feat_add(toee.feat_great_fortitude)
			npc.feat_add(toee.feat_silent_spell)
			npc.feat_add(toee.feat_still_spell)
			npc.feat_add(toee.feat_mobility)
			npc.feat_add(toee.feat_point_blank_shot)
			npc.feat_add(toee.feat_spell_focus_conjuration)
			npc.feat_add(toee.feat_spell_focus_necromancy)
			npc.feat_add(toee.feat_weapon_finesse_dagger)
			npc.feat_add(toee.feat_weapon_focus_dagger)

			utils_npc.npc_abilities_set(npc, [7, 24-4, 16-4, 27-4, 11, 18])
			utils_npc.npc_hitdice_set(npc, 0, 0, 0)
			npc.make_class(toee.stat_level_wizard, 13) # 20 is max
			
			npc.obj_set_int(toee.obj_f_critter_portrait, 9350) # Vendor_Vendor_14595; 9440 - Anom_14199
			npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL) 
			nameid = utils_toee.make_custom_name("Shania")
			if (nameid):
				npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
				npc.obj_set_int(const_toee.obj_f_description_correct, nameid)

			hairStyle = utils_npc.HairStyle.from_npc(npc)
			hairStyle.style = const_toee.hair_style_medium
			hairStyle.color = const_toee.hair_color_light_brown
			hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		utils_item.item_clear_all(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_CLOAK_OF_RESISTANCE_PLUS_4_GREEN, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_HEALTH_PLUS_4, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_HEADBAND_OF_INTELLECT_PLUS_4, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_GLOVES_OF_DEXTERITY_PLUS_4, npc)
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_PROTECTION_PLUS_4, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER_PLUS_2_OF_VENOM, npc) # todo frost dagger

		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		#"Construct_Max_HP"
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if not attachee.has_met(triggerer):
			triggerer.begin_dialog(attachee, 0)
			return toee.SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 20) # busy studing
		return toee.SKIP_DEFAULT

	def dialog_can_decipher_informed(self, npc):
		if (not rumor_control.is_rumor_given(module_quests.RUMOR_KEEP_SHANIA_CAN_DECIPHER)):
			rumor_control.rumor_give(module_quests.RUMOR_KEEP_SHANIA_CAN_DECIPHER)
		return