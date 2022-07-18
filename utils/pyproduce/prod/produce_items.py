#import produce_npc
import sys
import inspect

class ItemBase(object):
    def __init__(self, item_entry: dict, parent):
        self.item_entry = item_entry
        self.parent = parent

        self.item_file_name = self.item_entry["Item"]["Filename"]
        self.item_type = self.item_entry["ItemTypeEval"]
        self.slot_name = self.item_entry["SlotCode"]
        self.item_name = self.item_entry["ItemNameEval"]
        self.droppable = bool(self.item_entry["ItemDroppableEval"])
        self.no_loot = not self.droppable
        return

    @classmethod
    def get_category(cls): return ""

    @classmethod
    def get_item_codes(cls): return ()

    @classmethod
    def is_default(cls): return False

    @classmethod
    def get_proto_const(cls): return None

    @staticmethod
    def pick(item_entry: dict, parent):
        item_type = item_entry["ItemTypeEval"]

        category_classes = [cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ItemBase) and cls.get_category() == item_type]
        if not category_classes:
            return None

        item_file_name = item_entry["Item"]["Filename"]
        # cls = None
        # for c in category_classes:
        #      if item_file_name in c.get_item_codes():
        #          cls = c
        #          break
        item_file_name_lo = item_file_name.lower()
        cls = next((cls for cls in category_classes for item_code in cls.get_item_codes() if item_code and item_file_name_lo == item_code.lower()), None)
        if not cls:
            cls = next((cls for cls in category_classes if cls.is_default()), None)
        if not cls:
            return None

        result = cls(item_entry, parent)
        return result

    @classmethod
    def give_item_create_line(cls, item_file_name: str, charges1: int = None):
        return None
        
    @staticmethod
    def find_item_class(item_file_name: str):
        item_file_name_l = item_file_name.lower()
        #cls = next((cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ItemBase) and item_file_name in cls.get_item_codes()), None)
        for cls in [cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ItemBase)]:
            for code in cls.get_item_codes():
                if item_file_name_l == code.lower():
                    return cls
        return None

    def get_wear(self):
        wear = None
        if self.slot_name == 'SLOT_WEAPON1':
            wear = "toee.item_wear_weapon_primary"
        # actually this is not secondary, but second option for combat
        #elif self.slot_name == 'SLOT_WEAPON2':
        #    wear = "toee.item_wear_weapon_secondary"
        elif self.slot_name == 'SLOT_HELMET':
            wear = "toee.item_wear_helmet"
        elif self.slot_name == 'SLOT_ARMOR':
            wear = "toee.item_wear_armor"
        elif self.slot_name == 'SLOT_SHIELD':
            wear = "toee.item_wear_shield"
        elif self.slot_name == 'SLOT_GAUNTLETS':
            wear = "toee.item_wear_gloves"
        elif self.slot_name == 'SLOT_RING_LEFT':
            wear = "toee.item_wear_ring_primary"
        elif self.slot_name == 'SLOT_RING_RIGHT':
            wear = "toee.item_wear_ring_secondary"
        elif self.slot_name == 'SLOT_AMULET':
            wear = "toee.item_wear_necklace"
        elif self.slot_name == 'SLOT_BELT':
            wear = "toee.item_wear_lockpicks"
        elif self.slot_name == 'SLOT_BOOTS':
            wear = "toee.item_wear_boots"
        elif self.slot_name == 'SLOT_AMMO1':
            wear = "toee.item_wear_ammo"
        elif self.slot_name == 'SLOT_CLOAK':
            wear = "toee.item_wear_cloak"
        return wear

    def process_item(self):
        item_const_full_name = self.get_proto_const()
        if not item_const_full_name: return False

        wear = self.get_wear()
        self._add_line(self._get_item_create_prefix() + f'utils_item.item_create_in_inventory2({item_const_full_name}, npc, no_loot = {self.no_loot}, wear_on = {wear}) # {self.item_name} ({self.item_file_name}) at {self.slot_name} {"OK" if self.item_file_name in self.get_item_codes() else "default TODO ITEM" if self.is_default() else "base! TODO ITEM"}')

        self.log_item(item_const_full_name, wear)
        return True

    def process_char(self):
        return


    def log_item(self, item_const, wear):
        if item_const:
            self.parent.items.append(item_const)
            if wear:
                self.parent.wears[wear] = item_const
        return

    def _add_line(self, line):
        self.parent.writeline(line)
        return

    def _get_item_create_prefix(self):
        return ""

########## WEAPONS

class ItemWeapons(ItemBase):
    pass

########## WEAPONS / SPEARS
class ItemSpears(ItemBase):
    @classmethod
    def get_category(cls): return "Spears"

class ItemSpearDefault(ItemSpears):
    @classmethod
    def get_item_codes(cls): return ("00SPER01",)

    @classmethod
    def is_default(cls): return True

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_SHORTSPEAR"

########## WEAPONS / DAGGERS
class ItemDaggers(ItemBase):
    @classmethod
    def get_category(cls): return "Daggers"

class ItemDaggerDefault(ItemDaggers):
    @classmethod
    def is_default(cls): return True

    @classmethod
    def get_item_codes(cls): return ("00DAGG01",)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_DAGGER"    

########## WEAPONS / CLUB
class ItemClubs(ItemBase):
    @classmethod
    def get_category(cls): return "Club"

class ItemClubDefault(ItemClubs):
    @classmethod
    def is_default(cls): return True

    @classmethod
    def get_item_codes(cls): return ("00CLUB01",)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_CLUB"    

########## WEAPONS / AXES
class ItemAxes(ItemBase):
    @classmethod
    def get_category(cls): return "Axes"

class ItemThrowingAxe(ItemAxes):
    @classmethod
    def get_item_codes(cls): return ("00AX1H05",)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_HANDAXE"    

class ItemHandaxe(ItemAxes):
    @classmethod
    def get_item_codes(cls): return ("00AX1H11",)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_HANDAXE"    

class ItemBattleaxe(ItemAxes):
    @classmethod
    def get_item_codes(cls): return ("00AX1H01", "00CWAXEA", "00CWAXEE", "00CWRDE1")

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_BATTLEAXE"    

class ItemBattleaxePlus1(ItemAxes):
    @classmethod
    def get_item_codes(cls): return ("00AX1H03", )

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_BATTLEAXE_PLUS_1"

class ItemGreataxe(ItemAxes):
    @classmethod
    def get_item_codes(cls): return ("00CWAXED", "00AX2H01")

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_GREATAXE"    

########## WEAPONS / HAMMERS
class ItemHammers(ItemBase):
    @classmethod
    def get_category(cls): return "Hammers"

class ItemThrowingHammer(ItemHammers):
    @classmethod
    def get_item_codes(cls): 
        return ("00HAMT01" # used by half orcs
            ,)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_HAMMER_LIGHT"    

class ItemWarhammer(ItemHammers):
    @classmethod
    def get_item_codes(cls): 
        return ("00CWHAMA" # used by half orcs
            #,"00CWHAMD" # That one is 10d3 and Invisibility detection.
            ,"00HAMM01" # very common
            ,"00HAMM05")

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_WARHAMMER"    

########## WEAPONS / BOWS
class ItemBows(ItemBase):
    @classmethod
    def get_category(cls): return "Bows"

class ItemGoblinsShortbow(ItemBows):
    @classmethod
    def get_item_codes(cls): 
        return ("00CWBOWK" # used by goblins
            ,)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_SHORTBOW"    

    def _get_item_create_prefix(self): return "weapon = "

    def process_item(self):
        result = super().process_item()
        if result:
            self._add_line('weapon.obj_set_int(toee.obj_f_weapon_damage_dice, toee.dice_new("1d6-4").packed)')
        return result 

class ItemLongbow(ItemBows):
    @classmethod
    def get_item_codes(cls): 
        return ("00CWBOWG" # used by orcs
            ,)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_LONGBOW"    

########## WEAPONS / ARROWS
class ItemArrows(ItemBase):
    @classmethod
    def get_category(cls): return "Arrows"

    def _get_item_create_prefix(self): return "quiver = "

class ItemQuiver1(ItemArrows):
    @classmethod
    def get_item_codes(cls): 
        return ("00AROW01" # used by goblins
            ,)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_AMMO_ARROW_QUIVER"

    def process_item(self):
        result = super().process_item()
        if result:
            q = int(self.item_entry["Item"]["Charges1"])
            if q:
                self._add_line(f"quiver.obj_set_int(toee.obj_f_ammo_quantity, {q})")

        return result 

class ItemQuiverOfFlame(ItemArrows):
    @classmethod
    def get_item_codes(cls): 
        return ("00CWARWB" # used by Fire Orcs, TODO
            ,)

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_AMMO_ARROW_QUIVER"

########## ARMORS
class ItemArmors(ItemBase):
    def process_item(self):
        result = super().process_item()

        if result:
            boots_proto_const = self.get_boots_proto_const()
            if boots_proto_const:
                # already = None
                # for item in self.parent.cre["Items"]:
                #     if item["SlotCode"] == "SLOT_BOOTS":
                #         already = item
                #         break
                already = next((item for item in self.parent.cre["Items"] if item["SlotCode"] == "SLOT_BOOTS"), None)
                if not already:
                    already = self.parent.wears.get("toee.item_wear_boots")
                if not already:
                    self._add_line(f'utils_item.item_create_in_inventory2({boots_proto_const}'
                        + f', npc, no_loot = {self.no_loot}, wear_on = toee.item_wear_boots) # boots for {self.item_name} ({self.item_file_name}) {"OK" if self.item_file_name in self.get_item_codes() else "default"}')
                    
                    self.log_item(boots_proto_const, "toee.item_wear_boots")

        return result

    def get_boots_proto_const(cls): return None

########## ARMORS / LEATHER ARMORS
class ItemLeatherArmors(ItemArmors):
    @classmethod
    def get_category(cls): return "LeatherArmor"

    def get_boots_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE"

class ItemLeatherArmorDefault(ItemLeatherArmors):
    @classmethod
    def get_item_codes(cls): return ('00CIARMB', '00LEAT01')

    @classmethod
    def is_default(cls): return True

    @classmethod
    def get_proto_const(cls): return "const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN"

########## ARMORS / STUDDED LEATHER ARMORS
class ItemLeatherStuddedArmors(ItemArmors):
    @classmethod
    def get_category(cls): return "StuddedLeatherArmor"

    def get_boots_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE"

class ItemLeatherStuddedArmorPlus2(ItemLeatherStuddedArmors):
    @classmethod
    def get_item_codes(cls): return ('00LEAT07', )

    @classmethod
    def get_proto_const(cls): return "const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_PLUS_2"

########## ARMORS / HELMS HATS
class ItemHelmets(ItemArmors):
    @classmethod
    def get_category(cls): return "HelmsHats"

class ItemHelmHorned(ItemHelmets):
    @classmethod
    def get_item_codes(cls): return ('00HELM01', )

    @classmethod
    def get_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_HELM_DRUIDIC"

class ItemHelmBarbarian(ItemHelmets):
    @classmethod
    def get_item_codes(cls): return ('00HELM02', )

    @classmethod
    def get_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN"

class ItemHelmPlumed1(ItemHelmets):
    @classmethod
    def get_item_codes(cls): return ('00HELM03', )

    @classmethod
    def get_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_HELM_PLUMED_GOLD"

class ItemHelmPlumedRed(ItemHelmets):
    @classmethod
    def get_item_codes(cls): return ('00HELM04', )

    @classmethod
    def get_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_HELM_PLUMED_SILVER"

class ItemHelmPlumedMetal(ItemHelmets):
    @classmethod
    def get_item_codes(cls): return ('00HELM05', )

    @classmethod
    def get_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_HELM_GREAT"

class ItemHelmPlumedBronze(ItemHelmets):
    @classmethod
    def get_item_codes(cls): return ('00HELM06', )

    @classmethod
    def get_proto_const(cls): return "const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN"

########## SHORTSWORDS
class ItemShortswords(ItemBase):
    @classmethod
    def get_category(cls): return "ShortSwords"

class ItemShortsword(ItemShortswords):
    @classmethod
    def get_item_codes(cls): return ('00Swds01'.upper(), )

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_WEAPON_SHORTSWORD"

########## LONGSWORDS
class ItemLongswords(ItemBase):
    @classmethod
    def get_category(cls): return "LongsSwords"

class ItemScimitar(ItemLongswords):
    @classmethod
    def get_item_codes(cls): return ('00SWDC01', )

    @classmethod
    def get_proto_const(cls): return "const_proto_weapon.PROTO_SCIMITAR"

########## GOLD
class ItemGold(ItemBase):
    @classmethod
    def get_category(cls): return "Gold"

    @classmethod
    def get_item_codes(cls): return ('MISC07', )

    def process_item(self):
        Charges1, Charges2, Charges3 = int(self.item_entry["Item"]["Charges1"]), int(self.item_entry["Item"]["Charges2"]), int(self.item_entry["Item"]["Charges3"])
        #platinum, gold, silver, copper = 0, Charges1, Charges2, Charges3
        #self._add_line(f'utils_item.item_money_create_in_inventory(npc, {platinum}, {gold}, {silver}, {copper}) # Charges1: {Charges1}, Charges2: {Charges2}, Charges3: {Charges3}')
        self._add_line(f'utils_item.item_money_create_in_inventory(npc, 0, toee.game.random_range({Charges1}, {Charges2})) # Charges1: {Charges1}, Charges2: {Charges2}, Charges3: {Charges3}')
        return True

    @classmethod
    def give_item_create_line(cls, item_file_name: str, charges1: int = None):
        #return f'utils_item.item_money_create_in_inventory(npc, gold={charges1})'
        return f'utils_pc.pc_party_receive_money_and_print({charges1} * const_toee.gp)'

    @classmethod
    def is_default(cls): return True

########## GEMS
class ItemGems(ItemBase):
    @classmethod
    def get_category(cls): return "Gems"

class ItemGemLynx(ItemGems):
    @classmethod
    def get_item_codes(cls): return ('00GEM02', )

    @classmethod
    def get_proto_const(cls): return "const_proto_items_iwd2.PROTO_GENERIC_LYNX_EYE_GEM"

########## POTIONS
class ItemPotions(ItemBase):
    @classmethod
    def get_category(cls): return "Potions"

class ItemPotionOfHealing(ItemPotions):
    """ It is not exact, as heals 9 hp not 1d8+1. And costs 75, not 50!
    TODO ITEM
    """
    @classmethod
    def get_item_codes(cls): return ('00Potn04', )

    @classmethod
    def get_proto_const(cls): return "const_proto_potions.PROTO_POTION_OF_CURE_LIGHT_WOUNDS"

########## NOTES
class ItemNotes(ItemBase):
    @classmethod
    def get_category(cls): return "Notes"

class ItemNotesExpendedTS(ItemNotes):
    @classmethod
    def get_item_codes(cls): return ('10Vellum'.upper(), )

    @classmethod
    def get_proto_const(cls): return "const_proto_items_iwd2.PROTO_GENERIC_EXPENDED_TELEPORTATION_SCROLL"

########## KEYS
class ItemKeys(ItemBase):
    @classmethod
    def get_category(cls): return "Keys"

class ItemWoodenCraneWheel(ItemKeys):
    @classmethod
    def get_item_codes(cls): return ('10GenCrW'.upper(), )

    @classmethod
    def get_proto_const(cls): return "const_proto_items_iwd2.PROTO_SCROLL_WOODEN_CRANE_WHEEL"

########## MISC | BOOKS
class ItemMisc(ItemBase):
    @classmethod
    def get_category(cls): return "Books"

class ItemMiscJunk(ItemBase):
    # No actual usability, verified
    @classmethod
    def get_category(cls): return "Books"

    @classmethod
    def get_item_codes(cls): return ('00RTGOB1', '00RTFIRE', '00RG05', 'RT01_M', 'RT02_M', 'RT02_R', 'RT02_L')
    
    def process_item(self):
        self._add_line("# junk, skip and forget")
        return True

class ItemMiscMeleeSlashing1d4(ItemMisc):
    # used by Goblins as axes

    def process_item(self):
        if not self.parent.anim.disallow_weapon():
            wear = self.get_wear()
            self._add_line(f'weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc, no_loot = {self.no_loot}, wear_on = {wear}) # {self.item_name} ({self.item_file_name}) at {self.slot_name} # TODO CHECK if condition to lower 1d6=>1d4 is needed!!')
            self._add_line('weapon.obj_set_int(toee.obj_f_weapon_damage_dice, toee.dice_new("1d4").packed)')
        return True

    @classmethod
    def get_item_codes(cls): return ('001D4S', )

class ItemMiscMeleeSlashing1d6(ItemMisc):
    # used by Goblins as axes

    def process_item(self):
        if not self.parent.anim.disallow_weapon():
            wear = self.get_wear()
            self._add_line(f'weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc, no_loot = {self.no_loot}, wear_on = {wear}) # {self.item_name} ({self.item_file_name}) at {self.slot_name}')
            # skip as already 1d6 # self._add_line('weapon.obj_set_int(toee.obj_f_weapon_damage_dice, toee.dice_new("1d4").packed)')
        return True

    @classmethod
    def get_item_codes(cls): return ('001D6S', )

class ItemMiscMeleeSlashing1d8(ItemMisc):
    # used by Goblins as axes

    def process_item(self):
        if not self.parent.anim.disallow_weapon():
            wear = self.get_wear()
            self._add_line(f'weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_BATTLEAXE, npc, no_loot = {self.no_loot}, wear_on = {wear}) # {self.item_name} ({self.item_file_name}) at {self.slot_name}')
        return True

    @classmethod
    def get_item_codes(cls): return ('001D8S', )

class ItemMiscMeleeNatural1d3(ItemMisc):
    # used by Goblin archers as melee

    def process_item(self):
        self._add_line("# see natural")
        return True

    def process_char(self):
        self._add_line('')
        self._add_line(f'# from {self.item_name}({self.item_file_name}) at {self.slot_name} by {self.__class__.__name__}')
        self._add_line('utils_npc.npc_natural_attack(npc, index = 0, attack_type = const_toee.nwt_bite, attack_bonus = 0, number = 1, damage_str = "1d3") # TODO check BAB here')
        return

    @classmethod
    def get_item_codes(cls): return ('001D3P', )

class ItemMiscStaff(ItemMisc):
    # used by Orc Shaman as staffs

    def process_item(self):
        if not self.parent.anim.disallow_weapon():
            wear = self.get_wear()
            self._add_line(f'weapon = utils_item.item_create_in_inventory2(const_proto_weapon.PROTO_WEAPON_QUARTERSTAFF, npc, no_loot = {self.no_loot}, wear_on = {wear}) # {self.item_name} ({self.item_file_name}) at {self.slot_name}')
        return True

    @classmethod
    def get_item_codes(cls): return ('001D6C', )
