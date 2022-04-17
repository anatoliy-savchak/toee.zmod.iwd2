import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_npc, const_animate, ctrl_daemon
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_wands
import const_proto_wondrous, const_proto_npc, utils_toee, const_proto_rings, const_proto_wands, module_quests, utils_pc, module_globals, const_proto_scrolls, item_knowstone

THIS_SCRIPT_ID = 14712
def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

PROTOS_WIZARD = [\
	const_proto_scrolls.PROTO_SCROLL_OF_ENLARGE_PERSON \
	, const_proto_scrolls.PROTO_SCROLL_OF_REDUCE_PERSON \
	, const_proto_scrolls.PROTO_SCROLL_OF_SHOCKING_GRASP \
	, const_proto_scrolls.PROTO_SCROLL_OF_GLITTERDUST \
	, const_proto_scrolls.PROTO_SCROLL_OF_GHOUL_TOUCH \
	, const_proto_scrolls.PROTO_SCROLL_OF_HEROISM \
	, const_proto_scrolls.PROTO_SCROLL_OF_VAMPIRIC_TOUCH \
	, const_proto_scrolls.PROTO_SCROLL_OF_DIVINE_FAVOR \
	, const_proto_scrolls.PROTO_SCROLL_OF_CURE_MODERATE_WOUNDS \
	, const_proto_wands.PROTO_WAND_OF_CURE_LIGHT_WOUNDS_USED \
	, const_proto_wands.PROTO_WAND_OF_MAGIC_MISSILES_1ST \
	, const_proto_wands.PROTO_WAND_OF_SLEEP \
	, const_proto_wands.PROTO_WAND_OF_MELFS_ACID_ARROW \
	]

SELL_KNOWSTONE_WIZARD = [
	toee.spell_enlarge,
	toee.spell_reduce,
	toee.spell_shocking_grasp,
	toee.spell_glitterdust,
	toee.spell_ghoul_touch,
	toee.spell_heroism,
	toee.spell_vampiric_touch
	]


class CtrlWizardQuoris(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = THIS_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		if (1):
			npc.feat_add(toee.feat_blind_fight)
			npc.feat_add(toee.feat_combat_reflexes)
			npc.feat_add(toee.feat_dodge)
			npc.feat_add(toee.feat_great_fortitude)
			npc.feat_add(toee.feat_greater_spell_focus_conjuration)
			npc.feat_add(toee.feat_greater_spell_focus_enchantment)
			npc.feat_add(toee.feat_greater_spell_penetration)
			npc.feat_add(toee.feat_greater_weapon_focus_unarmed_strike_medium_sized_being)
			npc.feat_add(toee.feat_improved_counterspell)
			npc.feat_add(toee.feat_improved_critical_unarmed_strike_medium_sized_being)
			#improved precise shot 
			npc.feat_add(toee.feat_lightning_reflexes)
			npc.feat_add(toee.feat_empower_spell)
			npc.feat_add(toee.feat_heighten_spell)
			npc.feat_add(toee.feat_maximize_spell)
			npc.feat_add(toee.feat_silent_spell)
			npc.feat_add(toee.feat_still_spell)
			npc.feat_add(toee.feat_point_blank_shot)
			npc.feat_add(toee.feat_precise_shot)
			npc.feat_add(toee.feat_spell_focus_conjuration)
			npc.feat_add(toee.feat_spell_focus_enchantment)
			npc.feat_add(toee.feat_spell_penetration)
			# superior concentration

			utils_npc.npc_abilities_set(npc, [15, 16, 20-6, 28-6, 13, 12])
			utils_npc.npc_hitdice_set(npc, 0, 0, 0)
			npc.make_class(toee.stat_level_wizard, 20) # 20 is max
			#npc.make_wiz(21)
			#utils_npc.npc_hp_set(npc, 148)
			
			npc.obj_set_int(toee.obj_f_critter_portrait, 8420) # 8700_Prince Zook IV_14701
			npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_GOOD) 
			nameid = utils_toee.make_custom_name("Quoris")
			if (nameid):
				npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
				npc.obj_set_int(const_toee.obj_f_description_correct, nameid)

			hairStyle = utils_npc.HairStyle.from_npc(npc)
			hairStyle.style = const_toee.hair_style_longhair
			hairStyle.color = const_toee.hair_color_white
			hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		utils_item.item_clear_all(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_COAT_LONG_BLACK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		#utils_item.item_create_in_inventory(6048, npc) # Prince Thrommel's Plate Armor
		#utils_item.item_create_in_inventory(6061, npc) # Prince Thrommel's Large Steel Shield
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_MANTLE_OF_SPELL_RESISTANCE_STARS, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_HEALTH_PLUS_6, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_HEADBAND_OF_INTELLECT_PLUS_6, npc)
		utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BRACERS_OF_ARMOR_PLUS_8, npc)
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_PROTECTION_PLUS_5, npc)
		utils_item.item_create_in_inventory(const_proto_rings.PROTO_RING_OF_FIRE_RESISTANCE_MAJOR, npc)
		utils_item.item_create_in_inventory(const_proto_wands.PROTO_WAND_OF_FIREBALL_10TH, npc)
		npc.skill_ranks_set(toee.skill_spot, 10)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		#"Construct_Max_HP"


		box = toee.game.obj_create(const_proto_containers.PROTO_CONTAINER_CHEST_GENERIC, npc.location)
		box.object_flag_set(toee.OF_DONTDRAW)
		box.obj_set_int(toee.obj_f_container_inventory_source, 0)
		npc.substitute_inventory = box

		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if (toee.game.quests[module_quests.QUEST_KEEP_QUORIS_SUMMON_1].state < toee.qs_accepted):
			triggerer.begin_dialog(attachee, 0)
		elif (toee.game.global_vars[module_globals.GVAR_KEEP_QUORIS_SUMMON_1_STATE] == module_globals.GVAL_KEEP_QUORIS_SUMMON_1_STATE_WON):
			triggerer.begin_dialog(attachee, 30)
		else:
			triggerer.begin_dialog(attachee, 40)
		return toee.SKIP_DEFAULT

	def dialog_summon_1_mention(self):
		quest = toee.game.quests[module_quests.QUEST_KEEP_QUORIS_SUMMON_1]
		if (quest.state < toee.qs_mentioned):
			quest.state = toee.qs_mentioned
		return

	def dialog_summon_1_agree(self, npc):
		quest = toee.game.quests[module_quests.QUEST_KEEP_QUORIS_SUMMON_1]
		if (quest.state < toee.qs_accepted):
			quest.state = toee.qs_accepted

		daemon = ctrl_daemon.CtrlDaemon.get_current_daemon()
		if (daemon and "on_quoris_summon_1" in dir(daemon)):
			daemon.on_quoris_summon_1(self)
			npc.scripts[const_toee.sn_heartbeat] = THIS_SCRIPT_ID
		return

	def do_summon_1_killed_all(self, npc):
		npc.scripts[const_toee.sn_heartbeat] = THIS_SCRIPT_ID
		toee.game.global_vars[module_globals.GVAR_KEEP_QUORIS_SUMMON_1_STATE] = module_globals.GVAL_KEEP_QUORIS_SUMMON_1_STATE_WON
		#toee.game.leader.begin_dialog(npc, 30)
		return

	def dialog_quest_summon_1_completed(self, npc):
		toee.game.global_vars[module_globals.GVAR_KEEP_QUORIS_SUMMON_1_STATE] = module_globals.GVAL_KEEP_QUORIS_SUMMON_1_STATE_REACTED
		quest = toee.game.quests[module_quests.QUEST_KEEP_QUORIS_SUMMON_1]
		if (quest.state < toee.qs_completed):
			quest.state = toee.qs_completed
		utils_pc.pc_party_receive_money_and_print(300 * const_toee.gp)
		utils_pc.pc_award_experience_each(150, 1)

		# turn off heartbeat for optimization
		npc.scripts[const_toee.sn_heartbeat] = THIS_SCRIPT_ID

		return

	def dialog_quest_chalice_given(self, npc):
		quest = toee.game.quests[module_quests.QUEST_KEEP_QUORIS_CHALICE]
		if (quest.state < toee.qs_accepted):
			quest.state = toee.qs_accepted
		return

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if (toee.game.global_vars[module_globals.GVAR_KEEP_QUORIS_SUMMON_1_STATE] == module_globals.GVAL_KEEP_QUORIS_SUMMON_1_STATE_WON):
			pc = utils_npc.npc_find_nearest_pc_prefer_leader(attachee)
			if (pc):
				self.dialog(attachee, pc)
		return toee.RUN_DEFAULT

	def dialog_barter(self, npc):
		utils_item.barter_list(npc, PROTOS_WIZARD, 0, item_knowstone.knowstone_create_list(SELL_KNOWSTONE_WIZARD, npc.location))
		return