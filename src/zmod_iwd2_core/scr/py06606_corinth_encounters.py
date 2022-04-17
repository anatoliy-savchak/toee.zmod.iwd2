import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, kots_consts, utils_races, utils_npc_build

MODULE_ID = 6603

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

class CtrlThugBase(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14210

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_start_combat] = MODULE_ID

		npc.make_class(toee.stat_level_fighter, 1)
		npc.obj_set_int(toee.obj_f_critter_portrait, 6830) # Brigand

		# create inventory
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_TAN, npc, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc)

		npc.item_wield_best_all()
		return

	def go_ranged(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#npc.item_wield_best_all()
		#return
		crossbow = npc.item_find_by_proto(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY)
		if (crossbow and npc.item_worn_at(toee.item_wear_weapon_primary) != crossbow):
			npc.item_wield(crossbow, toee.item_wear_weapon_primary)
			weapon_flags = crossbow.obj_get_int(toee.obj_f_weapon_flags)
			if (not weapon_flags & const_toee.OWF_WEAPON_LOADED):
				weapon_flags |= const_toee.OWF_WEAPON_LOADED
			crossbow.obj_set_int(toee.obj_f_weapon_flags, weapon_flags)
		quiver = npc.item_find_by_proto(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER)
		if (quiver and npc.item_worn_at(toee.item_wear_ammo) != quiver):
			npc.item_wield(quiver, toee.item_wear_ammo)
		return

	def go_melee(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		weapon = npc.item_find_by_proto(const_proto_weapon.PROTO_LONGSWORD)
		if (not weapon):
			weapon = npc.item_find_by_proto(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK)
		if (weapon and npc.item_worn_at(toee.item_wear_weapon_primary) != weapon):
			npc.item_wield(weapon, toee.item_wear_weapon_primary)

		shield = npc.item_find_by_proto(const_proto_armor.PROTO_SHIELD_LARGE_STEEL)
		if (shield and npc.item_worn_at(toee.item_wear_shield) != shield):
			npc.item_wield(shield, toee.item_wear_shield)
		return

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		include_melee = 0
		if (toee.game.combat_turn > 1): include_melee = 1
		option = toee.game.random_range(0, 1 + include_melee)

		tac = None
		if (option == 0): #ready vs spell
			print("ready vs spell")
			self.go_ranged(npc)
			tac = utils_tactics.TacticsHelper(self.get_name())
			tac.add_five_foot_step()
			tac.add_ready_vs_spell()
			#npc.float_text_line("ready vs spell")
		elif(option == 1): #shoot low hp
			self.go_ranged(npc)
			target_npc = utils_target_list.AITargetList(npc, 1, 0, utils_target_list.AITargetMeasure.by_hp()).rescan().bottom()
			print("shoot low hp, target: {}".format(target_npc))
			tac = utils_tactics.TacticsHelper(self.get_name())
			if (target_npc):
				tac.add_target_obj(target_npc.id)
			else: tac.add_target_damaged()
			tac.add_five_foot_step()
			tac.add_attack()
			#npc.float_text_line("shoot")
		elif(option == 2): #attack th
			print("attack th")
			self.go_melee(npc)
			tac = utils_tactics.TacticsHelper(self.get_name())
			tac.add_target_closest()
			tac.add_attack_threatened()
			#npc.float_text_line("attack")
		return tac

class CtrlThugLeader(CtrlThugBase):
	def after_created(self, npc):
		super(CtrlThugLeader, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_improved_grapple)
		npc.feat_add(toee.feat_cleave)
		npc.feat_add(toee.feat_weapon_focus_longsword)
		npc.feat_add(toee.feat_rapid_reload)

		utils_npc.npc_abilities_set(npc, [16, 15, 14, 10, 9, 9])
		npc.make_class(toee.stat_level_fighter, 2)
		utils_npc.npc_hp_set(npc, 20)
		npc.obj_set_int(toee.obj_f_critter_portrait, 6800) # Brigand Leader

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc, 1)

		npc.item_wield_best_all()
		return

class CtrlThug2(CtrlThugBase):
	def after_created(self, npc):
		super(CtrlThug2, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_improved_initiative)
		npc.feat_add(toee.feat_rapid_reload)

		utils_npc.npc_abilities_set(npc, [11, 10, 14, 9, 9, 6])
		npc.make_class(toee.stat_level_fighter, 1)
		utils_npc.npc_hp_set(npc, 10)

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc, 1)
		
		npc.item_wield_best_all()
		return

class CtrlThug3(CtrlThugBase):
	def after_created(self, npc):
		super(CtrlThug3, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_improved_initiative)
		npc.feat_add(toee.feat_rapid_reload)
		npc.feat_add(toee.feat_weapon_focus_longsword)

		utils_npc.npc_abilities_set(npc, [14, 15, 12, 9, 11, 8])
		npc.make_class(toee.stat_level_fighter, 1)
		utils_npc.npc_hp_set(npc, 7)

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc, 1)
		
		npc.item_wield_best_all()
		return

class CtrlThug4(CtrlThugBase):
	def after_created(self, npc):
		super(CtrlThug4, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_rapid_reload)

		utils_npc.npc_abilities_set(npc, [13, 11, 13, 10, 11, 6])
		npc.make_class(toee.stat_level_fighter, 1)
		utils_npc.npc_hp_set(npc, 5)

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_GREY, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc, 1)
		
		npc.item_wield_best_all()
		return


class CtrlThug5(CtrlThugBase):
	def after_created(self, npc):
		super(CtrlThug5, self).after_created(npc)
		assert isinstance(npc, toee.PyObjHandle)

		npc.feat_add(toee.feat_iron_will)
		npc.feat_add(toee.feat_toughness)
		npc.feat_add(toee.feat_weapon_focus_longsword)

		utils_npc.npc_abilities_set(npc, [11, 12, 16, 8, 10, 7])
		npc.make_class(toee.stat_level_fighter, 1)
		utils_npc.npc_hp_set(npc, 9-3) #-feat_toughness

		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL, npc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc, 1)
		
		npc.item_wield_best_all()
		return
