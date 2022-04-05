import toee, utils_item
from const_proto_weapon import *
from const_proto_armor import *
from const_proto_cloth import *
from const_proto_potions import *
from const_proto_items import *

def san_dialog(attachee, triggerer):
	triggerer.begin_dialog(attachee, 1)
	return toee.SKIP_DEFAULT

def give_default_starting_equipment(x = 0):
	for pc in toee.game.party:
			if pc.stat_level_get(toee.stat_level_barbarian) > 0:
				for item_proto_id in [PROTO_WEAPON_CLUB\
					, PROTO_SHIELD_BUCKLER\
					, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
					, PROTO_ARMOR_HIDE\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
					utils_item.item_create_in_inventory(item_proto_id, pc)
			elif pc.stat_level_get(toee.stat_level_bard) > 0:
				for item_proto_id in [PROTO_RAPIER\
					, PROTO_CLOTH_GARB_VILLAGER_BLUE\
					, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
					, PROTO_WEAPON_CROSSBOW_LIGHT\
					, PROTO_AMMO_BOLT_QUIVER\
					, PROTO_AMMO_BOLT_QUIVER\
					, PROTO_CLOTH_GLOVES_LEATHER_BROWN\
					, PROTO_CLOTH_HAT_JAUNTY\
					, PROTO_INSTRUMENT_MANDOLIN\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
					utils_item.item_create_in_inventory(item_proto_id, pc)

			elif pc.stat_level_get(toee.stat_level_cleric) > 0:
				for item_proto_id in [PROTO_ARMOR_LEATHER_ARMOR_BROWN\
					, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
					, PROTO_CLOTH_GLOVES_LEATHER_BROWN\
					, PROTO_SHIELD_BUCKLER\
					, PROTO_WEAPON_MACE_LIGHT\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
					utils_item.item_create_in_inventory(item_proto_id, pc)

			elif pc.stat_level_get(toee.stat_level_druid) > 0:
				for item_proto_id in [PROTO_ARMOR_HIDE\
					, PROTO_CLOTH_HELM_DRUIDIC\
					, PROTO_WEAPON_SHORTSPEAR\
					, PROTO_WEAPON_SLING\
					, PROTO_AMMO_BULLET_POUCH\
					, PROTO_AMMO_BULLET_POUCH\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
					utils_item.item_create_in_inventory(item_proto_id, pc)

			elif pc.stat_level_get(toee.stat_level_fighter) > 0:
				for item_proto_id in [PROTO_ARMOR_LEATHER_ARMOR_BROWN\
					, PROTO_CLOTH_HELM_LEATHER\
					, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
					, PROTO_CLOTH_GLOVES_LEATHER_BROWN\
					, PROTO_SHIELD_BUCKLER\
					, PROTO_BATTLEAXE\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
					utils_item.item_create_in_inventory(item_proto_id, pc)
	
			elif pc.stat_level_get(toee.stat_level_monk) > 0:
				if pc.stat_level_get(toee.stat_race) in [toee.race_gnome, toee.race_halfling]:
					for item_proto_id in [PROTO_CLOTH_ROBES_MONK_BROWN\
						, PROTO_CLOTH_BOOTS_MONK\
						, PROTO_WEAPON_DAGGER\
						, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]: # dagger (PROTO_WEAPON_DAGGER) instead of quarterstaff
						utils_item.item_create_in_inventory(item_proto_id, pc)

				else:
					for item_proto_id in [PROTO_CLOTH_ROBES_MONK_BROWN\
						, PROTO_CLOTH_BOOTS_MONK\
						, PROTO_WEAPON_QUARTERSTAFF\
						, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
						utils_item.item_create_in_inventory(item_proto_id, pc)

			elif pc.stat_level_get(toee.stat_level_paladin) > 0:
				for item_proto_id in [PROTO_ARMOR_LEATHER_ARMOR_BROWN\
					, PROTO_CLOTH_GLOVES_LEATHER_BROWN\
					, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
					, PROTO_CLOTH_HELM_GENERIC\
					, PROTO_SHIELD_BUCKLER\
					, PROTO_LONGSWORD\
					, PROTO_CLOAK_RED\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
					utils_item.item_create_in_inventory(item_proto_id, pc)

			elif pc.stat_level_get(toee.stat_level_ranger) > 0:
				for item_proto_id in [PROTO_ARMOR_LEATHER_ARMOR_BROWN\
					, PROTO_CLOTH_GLOVES_LEATHER_BROWN\
					, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
					, PROTO_SHIELD_BUCKLER\
					, PROTO_WEAPON_SHORTSWORD\
					, PROTO_WEAPON_SHORTBOW\
					, PROTO_AMMO_ARROW_QUIVER\
					, PROTO_AMMO_ARROW_QUIVER\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS\
					, PROTO_CLOAK_GREEN]:
					utils_item.item_create_in_inventory(item_proto_id, pc)

			elif pc.stat_level_get(toee.stat_level_rogue) > 0:
				for item_proto_id in [PROTO_ARMOR_LEATHER_ARMOR_BLACK\
					, PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK\
					, PROTO_CLOTH_GLOVES_LEATHER_BLACK\
					, PROTO_WEAPON_SHORTSWORD\
					, PROTO_WEAPON_DAGGER\
					, PROTO_CLOAK_BLACK\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS\
					, PROTO_WEAPON_CROSSBOW_LIGHT\
					, PROTO_AMMO_BOLT_QUIVER\
					, PROTO_AMMO_BOLT_QUIVER\
					, PROTO_POTION_OF_CURE_LIGHT_WOUNDS\
					, PROTO_GENERIC_TOOLS_THIEVES]:
					utils_item.item_create_in_inventory(item_proto_id, pc)
				
			elif pc.stat_level_get(toee.stat_level_sorcerer) > 0:
				if pc.stat_level_get(toee.stat_race) in [toee.race_gnome, toee.race_halfling]:
					for item_proto_id in [PROTO_CLOTH_GARB_MYSTIC_TEAL\
						, PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK\
						, PROTO_CLOTH_GLOVES_LEATHER_BLACK\
						, PROTO_CLOAK_RED\
						, PROTO_WEAPON_DAGGER\
						, PROTO_WEAPON_SLING\
						, PROTO_AMMO_BULLET_POUCH\
						, PROTO_AMMO_BULLET_POUCH\
						, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]: # dagger (PROTO_WEAPON_DAGGER) instead of spear
						utils_item.item_create_in_inventory(item_proto_id, pc)

				else:
					for item_proto_id in [PROTO_CLOTH_GARB_MYSTIC_TEAL\
						, PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK\
						, PROTO_CLOTH_GLOVES_LEATHER_BLACK\
						, PROTO_CLOAK_RED\
						, PROTO_WEAPON_SPEAR\
						, PROTO_WEAPON_SLING\
						, PROTO_AMMO_BULLET_POUCH\
						, PROTO_AMMO_BULLET_POUCH\
						, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
						utils_item.item_create_in_inventory(item_proto_id, pc)
				
			elif pc.stat_level_get(toee.stat_level_wizard) > 0:
				if pc.stat_level_get(toee.stat_race) in [toee.race_gnome, toee.race_halfling]:
					for item_proto_id in [PROTO_WEAPON_DAGGER\
						, PROTO_WEAPON_CROSSBOW_LIGHT\
						, PROTO_AMMO_BOLT_QUIVER\
						, PROTO_AMMO_BOLT_QUIVER\
						, PROTO_CLOTH_ROBES_BLUE_LIGHT\
						, PROTO_CLOTH_GARB_FARMER_BLACK\
						, PROTO_CLOTH_HAT_WIZARD_BLACK\
						, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
						, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
						utils_item.item_create_in_inventory(item_proto_id, pc)
		
				else:
					for item_proto_id in [PROTO_WEAPON_QUARTERSTAFF\
						, PROTO_WEAPON_CROSSBOW_LIGHT\
						, PROTO_AMMO_BOLT_QUIVER\
						, PROTO_AMMO_BOLT_QUIVER\
						, PROTO_CLOTH_ROBES_BLUE_LIGHT\
						, PROTO_CLOTH_GARB_FARMER_BLACK\
						, PROTO_CLOTH_HAT_WIZARD_BLACK\
						, PROTO_CLOTH_BOOTS_LEATHER_BROWN\
						, PROTO_POTION_OF_CURE_LIGHT_WOUNDS]:
						utils_item.item_create_in_inventory(item_proto_id, pc)
	return
	
def defalt_equipment_autoequip():	
	for pc in toee.game.party:
		pc.item_wield_best_all()
	return
