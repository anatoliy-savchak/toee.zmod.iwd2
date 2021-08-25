import toee, debug
import utils_item, const_proto_weapon, const_proto_armor, const_proto_cloth, const_proto_scrolls, const_proto_wands

# import pc_build
# pc_build.b1()
def b1():
	# level 4
	# 1: cleric
	# 2: fighter tank
	# 3: fighter dex
	# 4: wizard

	# fighter tank
	pc = toee.game.party[1]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_MASTERWORK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_LARGE_PLUS_1_STEEL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		utils_item.item_clear_by_proto(pc, const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD)
		pc.item_wield_best_all()

	# fighter dex
	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_RANSEUR_MASTERWORK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_MASTERWORK, pc)
		item = utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		item.obj_set_int(toee.obj_f_ammo_quantity, 100)
		
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)

		utils_item.item_create_in_inventory_buy(const_proto_wands.PROTO_WAND_OF_CURE_LIGHT_WOUNDS, pc)
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		item = utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		item.obj_set_int(toee.obj_f_ammo_quantity, 100)

		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		utils_item.item_create_in_inventory_buy(const_proto_wands.PROTO_WAND_OF_MAGIC_MISSILES_1ST, pc)
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

