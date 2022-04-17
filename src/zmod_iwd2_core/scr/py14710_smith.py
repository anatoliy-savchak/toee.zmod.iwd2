import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_npc, const_animate
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_wands, const_proto_items
import const_proto_wondrous, const_proto_npc, utils_toee, const_proto_rings, module_globals, module_quests, rumor_control
import const_proto_list_armor, const_proto_list_weapons_magic

THIS_SCRIPT_ID = 14710
def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)


# masterwork longsword
# defender sword = longsword + 1
# morningstar+
# stormbringer = shock warhammer = PROTO_WEAPON_WARHAMMER_PLUS_1
# red flail = flail + 1
# greatsword+
# longbow+ comp = PROTO_WEAPON_LONGBOW_COMPOSITE_14
# scalemail+1
# Braiser Mail = Plate +1 Fire Resistance, 10650 gp
# grimlock blade = Dagger + 1 Blindness, 32302

PROTOS_WEAPON_SMITH = [\
	const_proto_weapon.PROTO_LONGSWORD_MASTERWORK \
	, const_proto_weapon.PROTO_LONGSWORD_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_MORNINGSTAR_MASTERWORK \
	, const_proto_weapon.PROTO_WEAPON_WARHAMMER_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_SHORTSWORD_MASTERWORK \
	, const_proto_weapon.PROTO_FLAIL_MASTERWORK \
	, const_proto_weapon.PROTO_WEAPON_LONGBOW_COMPOSITE_14 \
	, const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT_MASTERWORK \
	, const_proto_armor.PROTO_ARMOR_SCALE_MAIL_MASTERWORK \
	, const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_DAGGER_PLUS_2 \
	, const_proto_weapon.PROTO_AMMO_ARROW_QUIVER \
	, const_proto_weapon.PROTO_AMMO_BOLT_QUIVER \
	, const_proto_items.PROTO_GENERIC_BACKPACK
	]


class CtrlVillageSmith(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14710

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = THIS_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		if (1):
			npc.feat_add(toee.feat_combat_reflexes)
			npc.feat_add(toee.feat_dodge)
			npc.feat_add(toee.feat_cleave)
			npc.feat_add(toee.feat_great_cleave)
			npc.feat_add(toee.feat_iron_will)
			npc.feat_add(toee.feat_weapon_focus_greatsword)

			utils_npc.npc_abilities_set(npc, [18, 14, 18, 11, 11, 5])
			utils_npc.npc_hitdice_set(npc, 0, 0, 0)
			npc.make_class(toee.stat_level_fighter, 6) # 20 is max
			
			npc.obj_set_int(toee.obj_f_critter_portrait, 6050) # 14016 - Potion of Haste_Ostler Gundigoot_14016
			npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) 
			nameid = utils_toee.make_custom_name("Tenkits")
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

		box = toee.game.obj_create(const_proto_containers.PROTO_CONTAINER_CHEST_GENERIC, npc.location)
		box.object_flag_set(toee.OF_DONTDRAW)
		box.obj_set_int(toee.obj_f_container_inventory_source, 0)
		npc.substitute_inventory = box

		# create inventory
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_COAT_LONG_BLACK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_DWARVEN, npc, 1, 1)
		
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

	def dialog_quest_ring_given(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		quest = toee.game.quests[module_quests.QUEST_KEEP_TENKITS_RING]
		if (quest.state < toee.qs_accepted):
			quest.state = toee.qs_accepted
		return

	def dialog_barter(self, npc):
		utils_item.barter_list(npc, PROTOS_WEAPON_SMITH)
		return