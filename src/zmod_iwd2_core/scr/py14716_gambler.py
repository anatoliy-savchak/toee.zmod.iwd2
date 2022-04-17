import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_storage, tpdp
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls
import const_proto_npc, utils_npc, utils_toee, module_globals, module_quests, rumor_control, const_proto_wondrous, const_proto_rings, module_cheats

THIS_SCRIPT_ID = 14716
def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

class CtrlKeepGabler(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = THIS_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = THIS_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		if (1):
			npc.feat_add(toee.feat_dodge)

			utils_npc.npc_abilities_set(npc, [11, 13, 12, 10, 8, 9])
			utils_npc.npc_hitdice_set(npc, 0, 0, 0)
			npc.make_class(toee.stat_level_fighter, 1) # 20 is max
			npc.obj_set_int(toee.obj_f_critter_portrait, 7330) # Elixir of Vision_Deggum_14227
			npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_GOOD) 
			nameid = utils_toee.make_custom_name("Jack")
			if (nameid):
				npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
				npc.obj_set_int(const_toee.obj_f_description_correct, nameid)

			hairStyle = utils_npc.HairStyle.from_npc(npc)
			hairStyle.style = const_toee.hair_style_shorthair
			hairStyle.color = const_toee.hair_color_brown
			hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		utils_item.item_clear_all(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CLOTH_ARMOR, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)

		#npc.money_adj(200 * const_toee.gp)
		self.vars["money_left"] = 2000

		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if (self.dialog_critter_have_play_money(attachee)):
			triggerer.begin_dialog(attachee, 1)
		else:
			attachee.float_line(140, triggerer)
		return toee.SKIP_DEFAULT

	def dialog_play(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		pc_dice = toee.dice_new("1d20")
		npc_dice = toee.dice_new("1d20")

		pc_roll = pc_dice.roll()
		npc_roll = pc_dice.roll()
		success = 0
		if (pc_roll >= npc_roll): 
			success = 1

		success_code = 102 if (success) else 103
		won_text = "won" if (success) else "lost"
		money_mod = 1 if (success) else -1
		money_mod_npc = -1 if (success) else 1
		pc.money_adj(money_mod * 50 * const_toee.gp)
		self.vars["money_left"] = int(self.vars["money_left"]) + money_mod_npc * 50
		text = "{} {} 50 gp (net: {} gp)\n\n".format(pc.description, won_text, pc.money_get() // const_toee.gp)

		hist_id = tpdp.create_history_type6_opposed_check(pc, npc, pc_roll, npc_roll, tpdp.BonusList(), tpdp.BonusList(), 5127, success_code, 1)
		toee.game.create_history_from_id(hist_id)
		toee.game.create_history_freeform(text)

		if (success):
			if (self.dialog_critter_have_play_money(npc)):
				pc.begin_dialog(npc, 100)
			else:
				pc.begin_dialog(npc, 120)
		else:
			if (self.dialog_critter_have_play_money(npc)):
				pc.begin_dialog(npc, 110)
			else:
				pc.begin_dialog(npc, 130)
		return

	def dialog_critter_have_play_money(self, critter):
		assert isinstance(critter, toee.PyObjHandle)
		gp_left = critter.money_get() // const_toee.gp if (critter in toee.game.party) else int(self.vars["money_left"])
		print("{} left for {}".format(gp_left, critter))
		return gp_left >= 50

	def dialog_give_all_money(self, npc, pc):
		assert isinstance(npc, toee.PyObjHandle)
		assert isinstance(pc, toee.PyObjHandle)
		money_left = self.vars["money_left"]
		if (money_left> 0):
			pc.money_adj(money_left * const_toee.gp)
			text = "{} {} {} gp (net: {} gp)\n\n".format(pc.description, "won", money_left, pc.money_get() // const_toee.gp)
			toee.game.create_history_freeform(text)
			self.vars["money_left"] = 0
		return

class CtrlKeepGablerBystander(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = THIS_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = THIS_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		if (1):
			npc.feat_add(toee.feat_dodge)

			utils_npc.npc_abilities_set(npc, [11, 13, 12, 10, 8, 9])
			utils_npc.npc_hitdice_set(npc, 0, 0, 0)
			npc.make_class(toee.stat_level_fighter, 1) # 20 is max
			npc.obj_set_int(toee.obj_f_critter_portrait, 6040) # 8048_Rannos Davl_14018
			npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_GOOD) 
			nameid = utils_toee.make_custom_name("Donel")
			if (nameid):
				npc.obj_set_int(toee.obj_f_critter_description_unknown, nameid)
				npc.obj_set_int(const_toee.obj_f_description_correct, nameid)

			hairStyle = utils_npc.HairStyle.from_npc(npc)
			hairStyle.style = const_toee.hair_style_shorthair
			hairStyle.color = const_toee.hair_color_red
			hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		utils_item.item_clear_all(npc)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GARB_FARMER_BROWN, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)

		#npc.money_adj(200 * const_toee.gp)
		self.vars["money_left"] = 200

		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.float_line(150, triggerer)
		return toee.SKIP_DEFAULT
