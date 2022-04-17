import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_npc, const_animate
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_wands
import const_proto_wondrous, const_proto_npc, utils_toee, const_proto_rings, module_globals, module_quests, rumor_control
import const_proto_list_armor, const_proto_list_weapons_magic, const_proto_scrolls, const_proto_wands, const_proto_wondrous

THIS_SCRIPT_ID = 14713
def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

PROTOS_GIMRID_VANILLA = [\
	const_proto_scrolls.PROTO_SCROLL_OF_CURE_LIGHT_WOUNDS \
	, const_proto_scrolls.PROTO_SCROLL_OF_CURE_MODERATE_WOUNDS \
	, const_proto_scrolls.PROTO_SCROLL_OF_RESTORATION_LESSER \
	, const_proto_scrolls.PROTO_SCROLL_OF_RESTORATION \
	, const_proto_wands.PROTO_WAND_OF_CURE_LIGHT_WOUNDS \
	, const_proto_wands.PROTO_WAND_OF_CURE_MODERATE_WOUNDS \
	, const_proto_wands.PROTO_WAND_OF_CURE_SERIOUS_WOUNDS \
	, const_proto_wands.PROTO_WAND_OF_CURE_CRITICAL_WOUNDS \
	, const_proto_wands.PROTO_WAND_OF_INFLICT_SERIOUS_WOUNDS \
	, const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_HEALTH_PLUS_2 \
	, const_proto_wondrous.PROTO_WONDROUS_CLOAK_OF_ARACHNIDA \
	]



class CtrlGimrid(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14710

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = THIS_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		if (1):
			npc.feat_add(toee.feat_great_fortitude)
			npc.feat_add(toee.feat_silent_spell)
			npc.feat_add(toee.feat_heighten_spell)
			npc.feat_add(toee.feat_combat_casting)

			utils_npc.npc_abilities_set(npc, [14, 11, 20-2, 12, 19, 13])
			utils_npc.npc_hitdice_set(npc, 0, 0, 0)
			npc.make_class(toee.stat_level_cleric, 9) # 20 is max
			
			npc.obj_set_int(toee.obj_f_critter_portrait, 6050) # 14016 - Potion of Haste_Ostler Gundigoot_14016
			npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) 
			nameid = utils_toee.make_custom_name("Gimrid")
			if (nameid):
				npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
				npc.obj_set_int(const_toee.obj_f_description_correct, nameid)

			hairStyle = utils_npc.HairStyle.from_npc(npc)
			hairStyle.style = const_toee.hair_style_medium
			hairStyle.color = const_toee.hair_color_brown
			hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		utils_item.item_clear_all(npc)

		# create inventory
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_COAT_LONG_BLACK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_CLOAK_OF_RESISTANCE_PLUS_2_GREEN, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_DWARVEN, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_PROTECTION_PLUS_1, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_HEALTH_PLUS_2, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MACE_LIGHT_PLUS_1, npc)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		#self.stop_walking(attachee)
		attachee.turn_towards(triggerer)
		if not attachee.has_met(triggerer):
			triggerer.begin_dialog(attachee, 1)
			return toee.SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 10)
		return toee.SKIP_DEFAULT

	def stop_walking(self, npc):
		loc = npc.location
		npc.npc_flag_unset(toee.ONF_WAYPOINTS_DAY)
		npc.npc_flag_unset(toee.ONF_WAYPOINTS_NIGHT)
		npc.move(loc)
		return

	def restart_walking(self, npc):
		npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
		npc.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)
		return
