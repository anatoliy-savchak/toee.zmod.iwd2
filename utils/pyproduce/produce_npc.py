from asyncore import write
import json
import os
import pyproduce

i_def = "\t"
i_code = "\t\t"

class ProduceNPC:
    def __init__(self, exported_dir: pyproduce.InfinityExportedDir) -> None:
        self.exported_dir = exported_dir
        self.elements = dict()

        self.lines_script = list()
        self.lines_dialog = list()
        self.copy_speaches = list()
        self.current_crename = ""
        self.cre = dict()

        self.setup_elements()
        return

    def setup_elements(self):
        self.elements["base_class"] = "NPCBase"
        return

    def read_cre(self, name: str):
        value = self.exported_dir.read_cre(name)
        self.cre = value
        return value

    def cre_get_full_name(self):
        result = self.exported_dir.cre_strref_to_string(self.cre.get("LongName"))
        if not result:
            result = self.exported_dir.cre_strref_to_string(self.cre.get("ShortName"))
        return result

    def load_template(self, file_name):
        with open(file_name, 'r') as f:
            self.lines_script = f.readlines()
        return

    def save(self, file_name):
        with open(file_name, 'w') as f:
            for line in self.lines_script:
                #aline = line
                f.write(line + ("\n" if not "\n" in line else ""))
        return
    
    def produce_npc(self, cre_name):
        self.read_cre(cre_name)
        self.current_crename = cre_name

        self.lines_script.append(f"class Ctrl{self.current_crename}({self.elements['base_class']}):")
        #self.lines_script.append("")

        self.produce_npc_baseproto()
        self.produce_npc_appearance()
        self.produce_npc_char()
        return

    def produce_npc_baseproto(self):
        proto = "const_proto_npc.PROTO_NPC_MAN"

        race_name = self.cre["RaceName"].lower()
        race = self.cre["Race"]
        gander = self.cre["Gender"]
        if not race_name or race_name == "human":
            if gander:
                proto = "const_proto_npc.PROTO_NPC_MAN"
            else:
                proto = "const_proto_npc.PROTO_NPC_WOMAN"
        else:
            raise Exception(f"Unknown race: {race_name}({race})")

        self.lines_script.append(i_def + "@classmethod")
        self.lines_script.append(i_def + f"def get_proto_id(cls): return {proto}")
        self.lines_script.append("")
        return

    def produce_npc_appearance(self):
        self.lines_script.append(i_def + "def setup_appearance(self, npc):")
        portrait_id = 8680 # none
        portrait_comment_name = "none"
        self.lines_script.append(i_code + f"npc.obj_set_int(toee.obj_f_critter_portrait, {portrait_id}) # {portrait_comment_name}");

        full_name = self.cre_get_full_name()
        if full_name:
            self.lines_script.append(i_code + f'utils_npc.npc_description_set_new(npc, "{full_name}")');

        self.lines_script.append(i_code+"return")
        self.lines_script.append("")
        return
    
    def produce_npc_char(self):
        self.lines_script.append(i_def + "def setup_char(self, npc):")

        if True:
            Strength = int(self.cre["Strength"])
            # StrengthBonus is never used in IWD2, checked
            Dexterity = int(self.cre["Dexterity"])
            Constitution = int(self.cre["Constitution"])
            Intelligence = int(self.cre["Intelligence"])
            Wisdom = int(self.cre["Wisdom"])
            Charisma = int(self.cre["Charisma"])
            self.lines_script.append(i_code + f"utils_npc.npc_abilities_set(npc, [{Strength}, {Dexterity}, {Constitution}, {Intelligence}, {Wisdom}, {Charisma}])");

        if True:
            Fortitude = int(self.cre["SaveVsDeath"])
            Reflex = int(self.cre["SaveVsWands"])
            Will = int(self.cre["SaveVsPolymorph"])
            # TODO add code to check if actual difference is needed

        LevelTotal = int(self.cre["LevelTotal"])
        ClassLevels = (int(self.cre["LevelBard"]), int(self.cre["LevelCleric"]), int(self.cre["LevelDruid"])
            , int(self.cre["LevelFighter"]), int(self.cre["LevelMonk"]), int(self.cre["LevelPaladin"])
            , int(self.cre["LevelRanger"]), int(self.cre["LevelRogue"]), int(self.cre["LevelSorcerer"])
            , int(self.cre["LevelWizard"]))
        levelsFromClasses = sum(ClassLevels)
        classes = ("stat_level_bard", "stat_level_cleric", "stat_level_druid", "stat_level_fighter"
            , "stat_level_monk", "stat_level_paladin", "stat_level_ranger", "stat_level_rogue", "stat_level_sorcerer"
            , "stat_level_wizard")
        if levelsFromClasses:
            classLevel = 0
            self.lines_script.append(i_code)
            self.lines_script.append(i_code+f"# class levels: {levelsFromClasses}")
            for i, levels in enumerate(ClassLevels):
                if not levels: continue
                statLevel = classes[i]
                self.lines_script.append(i_code+f"# {statLevel}: {levels}")
                for l in range(0, levels):
                    self.lines_script.append(i_code + f"npc.obj_set_idx_int(toee.obj_f_critter_level_idx, {classLevel}, toee.{statLevel})");
                    classLevel += 1
        else:
            raise Exception("No Classes!")

        self.produce_feats()
        self.lines_script.append(i_code+"return")
        self.lines_script.append("")
        return

    def produce_feats(self):
        def feat_pro_add(value_name: str, levels: list):
            value = self.cre[value_name]
            splitter_added = False
            for level in range(1, value+1):
                feat_to_addv = levels[level-1]
                if not feat_to_addv: continue
                if not splitter_added:
                    splitter_added = True
                    self.lines_script.append(i_code)
                    self.lines_script.append(i_code + f"# {value_name}: {value}")

                if isinstance(feat_to_addv, str):
                    self.lines_script.append(i_code+f"npc.feat_add(toee.{feat_to_addv})")
                else:
                    for feat_to_add in feat_to_addv:
                        if not feat_to_add: continue
                        self.lines_script.append(i_code+f"npc.feat_add(toee.{feat_to_add})")
            return

        def feat_pro_add_weapon(value_name: str, levels: list, weapons: list):
            value = self.cre[value_name]
            splitter_added = False
            for weapon in weapons:
                for level in range(1, value+1):
                    feat_template = levels[level-1]
                    if not feat_template: continue
                    feat_to_add = feat_template + weapon
                    if not splitter_added:
                        splitter_added = True
                        self.lines_script.append(i_code)
                        self.lines_script.append(i_code + f"# {value_name}: {value}")
                    self.lines_script.append(i_code+f"npc.feat_add(toee.{feat_to_add})")
            return

        self.lines_script.append("")
        self.lines_script.append(i_code+"# feats")
        feats = self.cre["Feats"]
        for feat in feats:
            self.produce_feat(feat)

        martial = ("feat_martial_weapon_proficiency_", "feat_weapon_focus_", "feat_weapon_specialization_")
        simple = (None, "feat_weapon_focus_", "feat_weapon_specialization_")
        spells = ("feat_spell_focus_", "feat_greater_spell_focus_")

        feat_pro_add("FeatArmorPreficiency"
            , ["feat_armor_proficiency_light", "feat_armor_proficiency_medium", "feat_armor_proficiency_heavy"])
        
        # TODO FeatArmoredArcana

        feat_pro_add("FeatCleave"
            , ["feat_cleave", "feat_great_cleave"])

        feat_pro_add("FeatWeaponProExoticBastardSword"
            , ["feat_exotic_weapon_proficiency_bastard_sword", "feat_weapon_focus_bastard_sword", "feat_weapon_specialization_bastard_sword"])

        feat_pro_add_weapon("FeatWeaponProAxe", martial
            , ["throwing_axe", "handaxe", "battleaxe", "greataxe"]
        )

        feat_pro_add_weapon("FeatWeaponProBow", martial
            , ["shortbow", "composite_shortbow", "longbow", "composite_longbow"]
        )

        feat_pro_add_weapon("FeatWeaponProFlail", martial
            , ["light_flail", "heavy_flail"]
        )

        feat_pro_add_weapon("FeatWeaponProGreatsword", martial
            , ["greatsword"]
        )

        feat_pro_add_weapon("FeatWeaponProHammer", martial
            , ["light_hammer", "warhammer"]
        )

        feat_pro_add_weapon("FeatWeaponProLargeSword", martial
            , ["longsword", "scimitar"]
        )

        feat_pro_add_weapon("FeatWeaponProPolearm", martial
            , ["halberd"]
        )

        feat_pro_add_weapon("FeatWeaponProCrossbow", simple
            , ["light_crossbow", "heavy_crossbow"]
        )

        feat_pro_add_weapon("FeatWeaponProMace", simple
            , ["heavy_mace"]
        )

        # Slings and Darts
        feat_pro_add_weapon("FeatWeaponProMissle", simple
            , ["sling", "dart"]
        )

        feat_pro_add_weapon("FeatWeaponProQuarterstaff", simple
            , ["quarterstaff"]
        )

        # ShortSwords and Daggers
        feat_pro_add_weapon("FeatWeaponProSmallBlade", simple
            , ["short_sword", "dagger"]
        )

        feat_pro_add_weapon("FeatSpellFocusEnchantment", spells
            , ["enchantment"]
        )

        feat_pro_add_weapon("FeatSpellFocusEvocation", spells
            , ["evocation"]
        )

        feat_pro_add_weapon("FeatSpellFocusNecromancy", spells
            , ["necromancy"]
        )

        feat_pro_add_weapon("FeatSpellFocusTransmutation", spells
            , ["transmutation"]
        )

        # FeatToughness TODO
        feat_pro_add_weapon("FeatToughness", ("")
            , ["feat_toughness"]
        )

        self.lines_script.append("")
        self.lines_script.append(i_code+f"npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status")
        return

    def produce_feat(self, feat: str):
        # https://sorcerers.net/Games/IWD2/feats.php

        ft = feat.lower()
        feat_to_add = None
        feat_to_add0 = None
        if ft == "aegis of rime":
            # 19 entries
            # TODO for NPC
            pass
        elif ft == "ambidexterity":
            # 64 entries
            # 3e one has no penalty... 
            # TODO - add specifically for NPCs
            feat_to_add = "feat_improved_two_weapon_fighting"
        elif ft == "aqua mortis": 
            # 27 entries
            # TODO
            pass
        elif ft == "armor proficiency": 
            # 732 entries
            # handled with FeatArmorPreficiency
            pass
        elif ft == "armored arcana": 
            # 5 entries
            # handled with FeatArmoredArcana
            pass
        elif ft == "arterial strike": 
            # 5 entries
            # TODO - add for NPC
            pass
        elif ft == "blind fight": 
            # 107 entries
            feat_to_add = "feat_blind_fight"
        elif ft == "bullheaded": 
            # 30 entries
            feat_to_add = "feat_iron_will"
        elif ft == "cleave": 
            # 195 entries
            # handled with FeatCleave
            pass
        elif ft == "combat casting": 
            # 198 entries
            feat_to_add = "feat_combat_casting"
        elif ft == "courteous magocracy": 
            # 40 entries
            # TODO
            pass
        elif ft == "crippling strike": 
            # 40 entries
            feat_to_add = "feat_crippling_strike"
        elif ft == "dash": 
            # 40 entries
            # TODO - add it for PC as well
            pass
        elif ft == "deflect arrows": 
            # 107 entries
            feat_to_add = "feat_deflect_arrows"
        elif ft == "dirty fighting": 
            # 142 entries
            # TODO - add it for PC as well
            pass
        elif ft == "discipline": 
            # 56 entries
            # TODO - add it for PC as well
            pass
        elif ft == "dodge":
            # 237 entries
            feat_to_add = "feat_dodge"
        elif ft == "envenom weapon": 
            # 10 entries
            # TODO - add it for PC as well
            pass
        elif ft == "exotic bastard": 
            # 4 entries
            # handled with FeatWeaponProExoticBastardSword
            pass
        elif ft == "expertise":
            # 47 entries
            feat_to_add = "feat_combat_expertise"
        elif ft == "extra rage":
            # 3 entries
            feat_to_add = "Extra Rage"
        elif ft == "extra shapeshifting":
            # 1 entries
            feat_to_add = "Extra Wild Shape"
        elif ft == "extra smiting":
            # 2 entries
            feat_to_add = "Extra Smiting"
        elif ft == "extra turning": 
            # 0 entries
            # MAYBE - add it for PC as well
            pass
        elif ft == "fiendslayer": 
            # 1 entries
            # MAYBE - add it for PC as well
            pass
        elif ft == "forester": 
            # 5 entries
            # MAYBE - add it for PC as well
            pass
        elif ft == "great fortitude":
            # 44 entries
            feat_to_add = "feat_great_fortitude"
        elif ft == "hamstring": 
            # 6 entries
            # MAYBE - add it for PC as well
            pass
        elif ft == "heretic's bane": 
            # 58 entries
            # TODO - for NPC only
            pass
        elif ft == "heroic inspiration": 
            # 18 entries
            # TODO - for NPC only
            pass
        elif ft == "improved critical": 
            # 193 entries
            # TODO - for NPC only
            pass
        elif ft == "improved evasion": 
            # 49 entries
            feat_to_add = "feat_improved_evasion"
        elif ft == "improved initiative": 
            # 325 entries
            feat_to_add = "feat_improved_initiative"
        elif ft == "improved turning": 
            # 193 entries
            # TODO - for NPC only
            pass
        elif ft == "iron will": 
            # 140 entries
            feat_to_add = "feat_iron_will"
        elif ft == "lightning reflexes": 
            # 126 entries
            feat_to_add = "feat_lightning_reflexes"
        elif ft == "lingering song": 
            # 0 entries
            feat_to_add = "Lingering Song"
        elif ft == "luck of heroes": 
            # 34 entries
            # TODO - add it for PC as well
            pass
        elif ft == "martial axe": 
            # 666 entries
            # handled with FeatWeaponProAxe
            pass
        elif ft == "martial bow": 
            # 648 entries
            # handled with FeatWeaponProBow
            pass
        elif ft == "martial flail": 
            # 640 entries
            # handled with FeatWeaponProFlail
            pass
        elif ft == "martial greatsword": 
            # 631 entries
            # handled with FeatWeaponProGreatsword
            pass
        elif ft == "martial hammer": 
            # 629 entries
            # handled with FeatWeaponProHammer
            pass
        elif ft == "martial large sword": 
            # 659 entries
            # handled with FeatWeaponProLargeSword
            pass
        elif ft == "martial polearm": 
            # 666 entries
            # handled with FeatWeaponProPolearm
            pass
        elif ft == "maximized attacks": 
            # 11 entries
            # MAYBE - add it for NPC only
            pass
        elif ft == "mercantile background": 
            # 0 entries
            # I think that one is close enough
            feat_to_add = "feat_diligent"
        elif ft == "power attack": 
            # 105 entries
            feat_to_add = "feat_power_attack"
        elif ft == "precise shot": 
            # 44 entries
            feat_to_add = "feat_precise_shot"
        elif ft == "rapid shot": 
            # 13 entries
            feat_to_add = "feat_rapid_shot"
        elif ft == "resist poison": 
            # 71 entries
            # MAYBE - add it for NPC only
            pass
        elif ft == "scion of storms": 
            # 35 entries
            # TODO - add it for PC as well
            pass
        elif ft == "shield proficiency": 
            # 711 entries
            feat_to_add = "feat_shield_proficiency"
            pass
        elif ft == "simple crossbow": 
            # 772 entries
            # handled with FeatWeaponProCrossbow
            pass
        elif ft == "simple mace": 
            # 792 entries
            # handled with FeatWeaponProMace
            pass
        elif ft == "simple missile": 
            # 794 entries
            # handled with FeatWeaponProMissle
            pass
        elif ft == "simple quarterstaff": 
            # 799 entries
            # handled with FeatWeaponProQuarterstaff
            pass
        elif ft == "simple small blade": 
            # 814 entries
            # handled with FeatWeaponProSmallBlade
            pass
        elif ft == "slippery mind": 
            # 11 entries
            # MAYBE - add it for NPC only
            pass
        elif ft == "snake blood": 
            # 52 entries
            # MAYBE - add it for NPC only
            pass
        elif ft == "spell focus enchantment": 
            # 20 entries
            # handled with FeatSpellFocusEnchantment
            pass
        elif ft == "spell focus evocation": 
            # 26 entries
            # handled with FeatSpellFocusEvocation
            pass
        elif ft == "spell focus necromancy": 
            # 17 entries
            # handled with FeatSpellFocusNecromancy
            pass
        elif ft == "spell focus transmutation": 
            # 33 entries
            # handled with FeatSpellFocusTransmutation
            pass

        elif ft == "spell penetration": 
            # 105 entries
            feat_to_add = "feat_spell_penetration"
        elif ft == "spirit of flame": 
            # 62 entries
            # TODO - for NPC only
            pass
        elif ft == "strong back": 
            # 62 entries
            # MAYBE - for NPC only
            pass
        elif ft == "stunning fist": 
            # 38 entries
            feat_to_add = "feat_stunning_fist"
        elif ft == "subvocal casting": 
            # 58 entries
            feat_to_add = "feat_silent_spell"
        elif ft == "toughness": 
            # 20 entries
            # handled with FeatToughness
            pass
        elif ft == "two-weapon fighting": 
            # 14 entries
            feat_to_add = "feat_two_weapon_fighting"
        elif ft == "weapon finesse": 
            # 52 entries
            # TODO
            feat_to_add = "feat_weapon_finesse_short_sword"
        elif ft == "wild shape boar": 
            # 3 entries
            # MAYBE for NPC
            pass
        elif ft == "wild shape panther": 
            # 12 entries
            # MAYBE for NPC
            pass
        elif ft == "wild shape shambler": 
            # 7 entries
            # MAYBE for NPC
            pass

        else: 
            raise Exception(f"Unknown feat: {feat}")

        if feat_to_add:
            if feat_to_add.startswith("feat_"):
                self.lines_script.append(i_code+f"npc.feat_add(toee.{feat_to_add})")
            else:
                self.lines_script.append(i_code+f'npc.feat_add("{feat_to_add}")')
        return