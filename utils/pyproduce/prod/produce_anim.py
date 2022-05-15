import sys
import inspect

class AnimBase(object):
    def __init__(self, cre: dict, parent):
        self.cre = cre
        self.parent = parent
        self.anim_id = self.cre["Animation"]
        self.anim_name = self.cre["AnimationNameCalc"]
        return

    @classmethod
    def get_codes(cls): return ("", )

    @staticmethod
    def process(cre: dict, parent):
        anim_name = cre["AnimationNameCalc"]
        #print(f"AnimationNameCalc: {anim_name}")

        category_class = next((cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass) if issubclass(cls, AnimBase) and anim_name in cls.get_codes()), None)
        if not category_class:
            return False

        result = category_class(cre, parent)
        return result

    def _add_line(self, line):
        self.parent.writeline(line)
        return

    def produce_hair(self):
        return

    def produce_cloth(self):
        return

    def produce_portrait(self):
        portrait_id = 8680 # none
        portrait_comment_name = "none"
        self._portrait_print(portrait_id, portrait_comment_name)
        return

    def _portrait_print(self, portrait_id, portrait_comment_name):
        self._add_line(f"# npc.obj_set_int(toee.obj_f_critter_portrait, {portrait_id}) # {portrait_comment_name}")
        self._add_line("")
        return

    def get_major_color_name(self):
        name = ""
        return

    def proto_override(self):
        return None

    @classmethod
    def disallow_weapon(cls): return False

class AnimHumanoid(AnimBase):
    def produce_hair(self):
        self._add_line("hairStyle = utils_npc.HairStyle.from_npc(npc)")
        style_const = self.get_hair_style_const()
        self._add_line(f"hairStyle.style = {style_const}")

        if True:
            color_const = "const_toee.hair_color_black"
            hairColourIndex = int(self.cre["HairColourIndex"])
            if hairColourIndex == 0: # Hair Black
                color_const = "const_toee.hair_color_black"
            elif hairColourIndex == 1: # Hair Lt Brown
                color_const = "const_toee.hair_color_light_brown"
            elif hairColourIndex == 2: # Hair Dk Brown
                color_const = "const_toee.hair_color_brown"
            elif hairColourIndex == 3: # Hair Blonde
                color_const = "const_toee.hair_color_blonde"
            elif hairColourIndex == 4: # Hair Red
                color_const = "const_toee.hair_color_red"
            elif hairColourIndex == 5: # Hair Lt Grey
                color_const = "const_toee.hair_color_light_brown"
            elif hairColourIndex == 6: # Hair Dk Grey
                color_const = "const_toee.hair_color_white"
            elif hairColourIndex == 7: # Hair Lt Green
                color_const = "const_toee.hair_color_blue"

            self._add_line(f"hairStyle.color = {color_const} # HairColourIndex: {hairColourIndex}")
        self._add_line("hairStyle.update_npc(npc)")
        return

    def get_hair_style_const(self): return "const_toee.hair_style_shorthair"

    def produce_cloth(self):
        worn_armor = self.parent.wears.get("toee.item_wear_armor")
        if not worn_armor:
            armor_proto_const, wear_on = self.get_armor_proto_const_and_wearon()
            if armor_proto_const:
                aname = armor_proto_const if not isinstance(armor_proto_const, tuple) else armor_proto_const[0]
                acomment = "" if not isinstance(armor_proto_const, tuple) else armor_proto_const[1]
                self._add_line(f'utils_item.item_create_in_inventory2({aname}, npc, no_loot = True, wear_on = {wear_on}) # {acomment}')
        
        worn_boots = self.parent.wears.get("toee.item_wear_boots")
        if not worn_boots:
            boots_proto_const = self.get_boots_proto_const()
            self._add_line(f'utils_item.item_create_in_inventory2({boots_proto_const}, npc, no_loot = True, wear_on = toee.item_wear_boots)')

        return

    def get_boots_proto_const(self): return "const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE"

    def get_armor_proto_const_and_wearon(self): 
        return (self.get_armor_proto_const(), 'toee.item_wear_armor')

    def get_armor_proto_const(self): 
        majorColourName = self.cre["MajorColourName"]
        result = "const_proto_cloth.PROTO_CLOTH_GARB_FARMER_BROWN"

        if "BROWN" in majorColourName:
            # 38	CLOTH LT BROWN 1        
            # 39	CLOTH DK BROWN 1        
            # 40	CLOTH LT BROWN 2        
            # 41	CLOTH DK BROWN 2        
            result = "const_proto_cloth.PROTO_CLOTH_GARB_FARMER_BROWN"
        elif "RED" in majorColourName:
            # 46	CLOTH LT RED            
            # 47	CLOTH DK RED            
            result = "const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_RED"
        elif "OLIVE" in majorColourName:
            # 36	CLOTH LT OLIVE          
            # 37	CLOTH DK OLIVE          
            result = "const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_OCHRE"
        elif "GREEN" in majorColourName:
            # 52	CLOTH LT GREEN          
            # 53	CLOTH MED GREEN         
            # 54	CLOTH DK GREEN          
            result = "const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_GREEN"
        elif "BLUE" in majorColourName:
            # 57	CLOTH LT BLUE           
            # 58	CLOTH DK BLUE           
            result = "const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE"
        elif "WHITE" in majorColourName:
            # 63	CLOTH WHITE             
            result = "const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_WHITE"
        elif "BLACK" in majorColourName:
            # 66	CLOTH BLACK             
            result = "const_proto_cloth.PROTO_CLOTH_GARB_FARMER_BLACK"
        elif "ORANGE" in majorColourName:
            # 48	CLOTH LT ORANGE         
            # 49	CLOTH DK ORANGE         
            result = "const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_ORANGE"
        elif "YELLOW" in majorColourName:
            # 50	CLOTH LT YELLOW         
            # 51	CLOTH DK YELLOW         
            result = "const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_YELLOW"
        elif "GREY" in majorColourName:
            # 64	CLOTH LT GREY           
            # 65	CLOTH DK GREY           
            result = "const_proto_cloth.PROTO_CLOTH_GARB_FARMER_GREY"
        elif "KAIKI" in majorColourName:
            # 42	CLOTH LT KAIKI          
            # 43	CLOTH DK KAIKI          
            result = "const_proto_cloth.PROTO_CLOTH_GARB_FARMER_GREY"
        elif "MAGENTA" in majorColourName:
            # 44	CLOTH LT MAGENTA        
            # 45	CLOTH DK MAGENTA        
            result = "const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_PURPLE"
        elif "AQUA" in majorColourName:
            # 55	CLOTH LT AQUA           
            # 56	CLOTH DK AQUA           
            result = "const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_BLUE"
        elif "INDIGO" in majorColourName:
            # 59	CLOTH LT INDIGO         
            # 60	CLOTH DK INDIGO         
            result = "const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_TEAL"
        elif "VIOLET" in majorColourName:
            # 61	CLOTH LT VIOLET         
            # 62	CLOTH DK VIOLET         
            result = "const_proto_cloth.PROTO_CLOTH_GARB_MYSTIC_TEAL"
        return result, majorColourName

class AnimHuman(AnimHumanoid):
    pass

class AnimPeasantMale(AnimHuman):
    @classmethod
    def get_codes(cls): return ("PEASANT_MAN", )

class AnimPeasantFemale(AnimHuman):
    @classmethod
    def get_codes(cls): return ("PEASANT_WOMAN", )

    def get_hair_style_const(self): return "const_toee.hair_style_longhair"

class AnimPeasantFatWoman(AnimPeasantFemale):
    @classmethod
    def get_codes(cls): return ("FAT_WOMAN", )

class AnimPeasantBoy(AnimHuman):
    @classmethod
    def get_codes(cls): return ("BOY", )

    def proto_override(self):
        return '14704'
    
    def get_armor_proto_const(self): "const_proto_cloth.PROTO_CLOTH_RAGGED_CLOTHES"
    #def get_armor_proto_const_and_wearon(self): return ("const_proto_cloth.PROTO_CLOTH_COAT_LONG_RED", 'toee.item_wear_robes')

class AFighter:
    def get_armor_proto_const(self): return "const_proto_cloth.PROTO_CLOTH_LEATHER_CLOTHING_LONG"

class AnimHumanFighter(AnimHumanoid):
    def get_armor_proto_const(self): return AFighter.get_armor_proto_const(self)

class AnimHumanFighterMale(AnimHumanFighter):
    @classmethod
    def get_codes(cls): 
        return ("FIGHTER_MALE_HUMAN"
            , "CLERIC_MALE_HUMAN_LOW") # IMPROVE CLERIC_MALE_HUMAN_LOW

class AnimHumanFighterFemale(AnimHumanFighter):
    @classmethod
    def get_codes(cls): return ("FIGHTER_FEMALE_HUMAN", )

    def get_hair_style_const(self): return "const_toee.hair_style_ponytail"

class AnimDwarf(AnimHumanoid):
    pass

class AnimDwarfFighter(AnimHumanoid):
    def get_armor_proto_const(self): return AFighter.get_armor_proto_const(self)

class AnimDwarfFighterMale(AnimDwarfFighter):
    @classmethod
    def get_codes(cls): return ("FIGHTER_MALE_DWARF", )

class AnimDwarfFighterFemale(AnimDwarfFighter):
    @classmethod
    def get_codes(cls): return ("FIGHTER_FEMALE_DWARF", )

    def get_hair_style_const(self): return "const_toee.hair_style_ponytail"

class AnimGoblinoids(AnimHumanoid):
    def produce_hair(self): return

    def produce_cloth(self): return

class AnimGoblin(AnimGoblinoids):

    def produce_portrait(self):
        # use default
        return

class AnimGoblinWithAxe(AnimGoblin):
    @classmethod
    def get_codes(cls): return ("Goblin_w_Axe", )

    def produce_cloth(self):
        self._add_line(f'utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: {self.anim_name}')
        #DEBUG self._add_line('npc.obj_set_int(toee.obj_f_hp_damage, 100)')
        return

class AnimGoblinWithBow(AnimGoblin):
    @classmethod
    def get_codes(cls): return ("Goblin_w_Bow", )

    def produce_cloth(self):
        #self._add_line(f'utils_item.item_create_in_inventory2(const_proto_armor_iwd2.PROTO_SHIELD_SMALL_WOODEN_EMPTY, npc, no_loot = True, wear_on = toee.item_wear_shield) # anim: {self.anim_name}')
        #DEBUG self._add_line('npc.obj_set_int(toee.obj_f_hp_damage, 100)')
        return
