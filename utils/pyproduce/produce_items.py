#import produce_npc
import sys
import inspect

def item_to_proto_name(item_file_name: str, item_type: str, slot_name: str, item_name: str, item_entry: dict) -> tuple:
    # returns array of Temple items:
    # (item_const_full_name, wear, comment, line)

    #fn = item_file_name.lower()
    #sname = slot_name.lower()

    result = None

    slot = None
    if slot_name[:11] == 'SLOT_WEAPON':
        slot = "toee.item_wear_weapon_primary"
        if slot_name[:11] == 'SLOT_WEAPON2':
            slot = "toee.item_wear_weapon_secondary"

    if item_type == 'LeatherArmor':
        # Leather Armor 00CIARMA is not used
        do_default = item_file_name in ('00CIARMB', '00LEAT01')
        do_default = True
            
        if do_default:
            if not slot_name == 'SLOT_ARMOR':
                result = (("const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN", None, None), )
            else:
                result = (
                    ("const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN", "toee.item_wear_armor", None),
                    ("const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE", "toee.item_wear_boots", None)
                )
    elif item_type == "Spears":
        do_default = item_file_name in ('00SPER01', )
        do_default = True
        if do_default:
            result = (("const_proto_weapon.PROTO_WEAPON_SHORTSPEAR", slot, None), )
    elif item_type == "Daggers":
        do_default = item_file_name in ('00DAGG01', )
        do_default = True
        if do_default:
            result = (("const_proto_weapon.PROTO_WEAPON_DAGGER", slot, None), )
    elif item_type == "Club":
        do_default = item_file_name in ('00CLUB01', )
        do_default = True
        if do_default:
            result = (("const_proto_weapon.PROTO_WEAPON_CLUB", slot, None), )
    elif item_type == "Gold":
        # TODO verify!!
        platinum, gold, silver, copper = 0, int(item_entry["Item"]["Charges1"]), int(item_entry["Item"]["Charges2"]), int(item_entry["Item"]["Charges3"])
        result = ((None, None, None, f"utils_item.item_money_create_in_inventory(npc, {platinum}, {gold}, {silver}, {copper})"), )


    return result

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
    def process(item_entry: dict, parent):
        item_type = item_entry["ItemTypeEval"]

        category_classes = [cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, ItemBase) and cls.get_category() == item_type]
        if not category_classes:
            return False

        item_file_name = item_entry["Item"]["Filename"]
        # cls = None
        # for c in category_classes:
        #      if item_file_name in c.get_item_codes():
        #          cls = c
        #          break
        cls = next((cls for cls in category_classes if item_file_name in cls.get_item_codes()), None)
        if not cls:
            cls = next((cls for cls in category_classes if cls.is_default()), None)
        if not cls:
            return False

        result = cls(item_entry, parent).process_item()
        return result

    def get_wear(self):
        wear = None
        if self.slot_name == 'SLOT_WEAPON1':
            wear = "toee.item_wear_weapon_primary"
        elif self.slot_name == 'SLOT_WEAPON2':
            wear = "toee.item_wear_weapon_secondary"
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
        self.parent.lines_script.append(self.parent.current_indent
            + f'utils_item.item_create_in_inventory2({item_const_full_name}, npc, no_loot = {self.no_loot}, wear_on = {wear}) # {self.item_name} ({self.item_file_name}) at {self.slot_name} {"OK" if self.item_file_name in self.get_item_codes() else "default TODO ITEM" if self.is_default() else "base! TODO ITEM"}')

        self.log_item(item_const_full_name, wear)
        return True

    def log_item(self, item_const, wear):
        if item_const:
            self.parent.items.append(item_const)
            if wear:
                self.parent.wears[wear] = item_const
        return


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
                    self.parent.lines_script.append(self.parent.current_indent
                        + f'utils_item.item_create_in_inventory2({boots_proto_const}'
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
    def get_proto_const(cls): return "const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_LONG_BROWN"

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

########## GOLD
class ItemGold(ItemBase):
    @classmethod
    def get_category(cls): return "Gold"

    def process_item(self):
        Charges1, Charges2, Charges3 = int(self.item_entry["Item"]["Charges1"]), int(self.item_entry["Item"]["Charges2"]), int(self.item_entry["Item"]["Charges3"])
        platinum, gold, silver, copper = 0, Charges1, Charges2, Charges3
        self.parent.lines_script.append(self.parent.current_indent
            + f'utils_item.item_money_create_in_inventory(npc, {platinum}, {gold}, {silver}, {copper}) # Charges1: {Charges1}, Charges2: {Charges2}, Charges3: {Charges3}')
        return True

    @classmethod
    def is_default(cls): return True
