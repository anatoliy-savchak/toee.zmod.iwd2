import toee, debug
import utils_item, const_proto_weapon, const_proto_armor, const_proto_cloth, const_proto_scrolls, utils_npc

# import pc_build
# pc_build.kots_b1()
def kots_b1():
	# 1: cleric
	# 2: fighter tank
	# 3: fighter dex
	# 4: wizard

	# fighter tank
	pc = toee.game.party[1]
	if (pc):
		#utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BREASTPLATE_GOLD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GOLD_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_LONGSWORD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_2, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	return

def kots_b2():
	# what if all equipment is max out lv1
	# 1: cleric
	# 2: fighter tank
	# 3: fighter dex
	# 4: wizard

	# fighter tank
	pc = toee.game.party[1]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, pc)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		utils_item.item_clear_by_proto(pc, const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_2, pc)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_MASTERWORK, pc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		if (item):
			item.obj_set_int(toee.obj_f_ammo_quantity, 50)

		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MACE_LIGHT_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_STEEL, pc)
		
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, pc)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_MASTERWORK, pc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		if (item):
			item.obj_set_int(toee.obj_f_ammo_quantity, 50)
		
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	return

# import pc_build
# pc_build.kots_b3()
def kots_b3():
	# 1: cleric
	# 2: fighter tank
	# 3: fighter dex
	# 4: wizard

	# instead of cleric armor buy her used acid splash

	# fighter tank
	pc = toee.game.party[1]
	if (pc):
		#utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BREASTPLATE_GOLD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GOLD_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_LONGSWORD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_2, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[0]
	if (pc):
		#utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		#utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		
		#utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		#utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		#utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	return

def kots_b4():
	# 1: cleric
	# 2: fighter tank
	# 3: fighter dex
	# 4: wizard

	# fighter tank
	pc = toee.game.party[1]
	if (pc):
		#utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BREASTPLATE_GOLD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GOLD_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_GUISARME, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)

		utils_item.item_create_in_inventory_buy(const_proto_scrolls.PROTO_SCROLL_OF_ENLARGE_PERSON, pc)
		
		pc.item_wield_best_all()

	return

# import pc_build
# pc_build.kots_c1()

def kots_c1():
	# 1: barbarian
	# 2: fighter dex
	# 3: cleric
	# 4: wizard

	# fighter tank
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_GREATAXE, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BREASTPLATE, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_BUCKLER, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[1]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_GUISARME, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[2]
	if (pc):
		#utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		#utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		if (item):
			item.obj_set_int(toee.obj_f_ammo_quantity, 50)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)

		#utils_item.item_create_in_inventory_buy(const_proto_scrolls.PROTO_SCROLL_OF_ENLARGE_PERSON, pc)
		
		pc.item_wield_best_all()

	return

# import pc_build
# pc_build.kots_l1()

def kots_l1():
	# 1: fighter bastard
	# 2: fighter longsword
	# 3: cleric
	# 4: wizard

	# fighter tank
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[1]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_LONGSWORD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL_2, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		if (item):
			item.obj_set_int(toee.obj_f_ammo_quantity, 50)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)

		#utils_item.item_create_in_inventory_buy(const_proto_scrolls.PROTO_SCROLL_OF_ENLARGE_PERSON, pc)
		
		pc.item_wield_best_all()

	return

# game.leader.stat_base_set(stat_dexterity, 15)

# import pc_build
# pc_build.kots_k2()
def kots_k2():
	# 1: fighter greatsw
	# 2: fighter bastard
	# 3: cleric
	# 4: sorc

	# fighter dmg
	pc = toee.game.party[0]
	if (pc):
		utils_npc.npc_abilities_set(pc, [18, 13, 16, 15, 13, 13])
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_GREATAXE, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.feat_add(toee.feat_combat_reflexes)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[1]
	if (pc):
		utils_npc.npc_abilities_set(pc, [18, 16, 15, 10, 14, 8])
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.feat_add(toee.feat_dodge)
		pc.feat_add(toee.feat_combat_reflexes)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[2]
	if (pc):
		utils_npc.npc_abilities_set(pc, [15, 15, 18, 12, 18, 15])
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# sorc
	pc = toee.game.party[3]
	if (pc):
		utils_npc.npc_abilities_set(pc, [14, 15, 17, 13, 15, 18])
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		if (item):
			item.obj_set_int(toee.obj_f_ammo_quantity, 50)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)

		#utils_item.item_create_in_inventory_buy(const_proto_scrolls.PROTO_SCROLL_OF_ENLARGE_PERSON, pc)
		
		pc.item_wield_best_all()

	return

# game.leader.stat_base_set(stat_dexterity, 15)

# import pc_build
# pc_build.iwd2_caves_prep()
def iwd2_caves_prep():
	# 1: fighter dwarf greatsword
	# 2: cleric female dwarf greatexe
	# 3: cleric Lathander Mace
	# 4: sorc
	# 5: sorc
	# 6: sorc

	# fighter dmg
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_WARHAMMER, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, pc)
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT pc)
		#utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		#pc.feat_add(toee.feat_combat_reflexes)
		pc.item_wield_best_all()

	pc = toee.game.party[1]
	if (pc):
		pc.feat_add(toee.feat_martial_weapon_proficiency_battleaxe, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_BATTLEAXE, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, pc)
		pc.item_wield_best_all()

	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MACE_LIGHT, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, pc)
		pc.item_wield_best_all()

	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTBOW, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, pc)
		pc.item_wield_best_all()

	# sorc
	pc = toee.game.party[4]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		pc.item_wield_best_all()
 
	# sorc
	pc = toee.game.party[5]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		pc.item_wield_best_all()
	return

# import pc_build
# pc_build.iwd2_ar2000_prep()
def iwd2_ar2000_prep():
	# 1: fighter dwarf greatsword
	# 2: cleric female dwarf greataxe
	# 3: cleric Lathander Mace
	# 4: sorc
	# 5: sorc
	# 6: sorc

	# fighter dmg
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATSWORD_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN, pc)
		#utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT pc)
		#utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		#pc.feat_add(toee.feat_combat_reflexes)
		pc.item_wield_best_all()

	pc = toee.game.party[1]
	if (pc):
		pc.feat_add(toee.feat_martial_weapon_proficiency_battleaxe, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_BATTLEAXE_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_2, pc)
		pc.item_wield_best_all()

	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR_MASTERWORK, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, pc)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, pc)
		pc.item_wield_best_all()

	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTBOW, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, pc).obj_set_int(toee.obj_f_ammo_quantity, 100)
		pc.item_wield_best_all()

	# sorc
	pc = toee.game.party[4]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc).obj_set_int(toee.obj_f_ammo_quantity, 100)
		pc.item_wield_best_all()
 
	# sorc
	pc = toee.game.party[5]
	if (pc):
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc).obj_set_int(toee.obj_f_ammo_quantity, 100)
		pc.item_wield_best_all()
	return