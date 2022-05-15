import os
import producer_base
import produce_anim
import common
import produce_items
import produce_dialog

class ProducerOfCtrlAuto(producer_base.ProducerOfFile):
    def __init__(self, doc
        , cre_name: str
        , are_name: str
        , script_id: int
        , make_new: bool
        , dialog_file
    ):
        template_path = doc.get_path_template_npcs_class_auto_file()
        out_path = doc.get_path_out_npcs_class_auto_file(are_name, script_id)
        src_path = doc.get_path_cre(cre_name)
        super().__init__(doc, out_path=out_path, template_path=template_path, make_new=make_new, src_path=src_path)

        self.cre_name = cre_name
        self.are_name = are_name
        self.script_id = script_id
        self.dialog_file = dialog_file

        self.ctrl_name = None
        self.base_class = 'ctrl_behaviour_ie.CtrlBehaviourIE'
        self.cre = self.src
        self.wears = dict()
        self.items = list()
        self.classes_toee = dict()
        return

    @classmethod
    def overwrite_by_template(cls, doc, are_name, script_id):
        template_path = doc.get_path_template_npcs_class_auto_file()
        out_path = doc.get_path_out_npcs_class_auto_file(are_name, script_id)
        with open(template_path, 'r') as fs:
            with open(out_path, 'w') as fo:
                fo.writelines(fs.readlines())
        return

    def produce(self):
        self.anim = produce_anim.AnimBase.process(self.cre, self)
        if not self.anim:
            raise Exception(f'No anim object for {self.cre["AnimationNameCalc"]}!!')
            
        self.current_line_id = common.lines_after_before_cutoff(self.lines, '#### GVARS ####', '#### GVARS END ####')
        if self.current_line_id and self.current_line_id > 0:
            self.writeline(f'MODULE_SCRIPT_ID = {self.script_id}')
            self.current_line_id = -1

        self.ctrl_name = f'Ctrl_{self.cre_name}_Auto'
        self.writeline(f"class {self.ctrl_name}({self.base_class}): # {self.cre_name} ") # leave trailing whitespace here
        self.indent(True)
        
        self.produce_npc_baseproto()
        self.produce_npc_script_hooks()
        self.produce_npc_appearance()
        self.produce_npc_char()
        self.setup_gear()
        self.produce_dialog()
        self.produce_imports()
        return

    def get_ctrl_tuple(self): return (self.ctrl_name, os.path.basename(self.out_path).replace('.py', ''))

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
        elif race_name == "dwarf":
            if gander:
                proto = "const_proto_npc.PROTO_NPC_DWARF_MAN"
            else:
                proto = "const_proto_npc.PROTO_NPC_DWARF_WOMAN"
        elif race_name == "goblin":
            if gander:
                proto = "const_proto_npc.PROTO_NPC_GOBLIN"
            else:
                proto = "const_proto_npc.PROTO_NPC_GOBLIN"
        else:
            raise Exception(f"Unknown race: {race_name}({race})")

        if proto_override := self.anim.proto_override():
            proto = proto_override

        self.writeline("@classmethod")
        self.writeline(f"def get_proto_id(cls): return {proto}")
        self.writeline("")
        return

    def produce_npc_script_hooks(self):
        self.writeline("def setup_scripts(self, npc):")
        self.indent(True)
        self.writeline(f'super({self.ctrl_name}, self).setup_scripts(npc)')
        if (dialog_name := self.cre["DialogFile"]) and (dialog_name != "None"):
            self.writeline("npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID")
        #self.writeline("npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID")
        self.writeline("return")
        self.indent(False)
        self.writeline("")
        return

    def produce_npc_appearance(self):
        self.writeline("def setup_appearance(self, npc):")
        self.indent()

        full_name = self.cre_get_full_name()
        if full_name:
            self.writeline(f'utils_npc.npc_description_set_new(npc, "{full_name}")');
            self.writeline()

        self.anim.produce_portrait()
        self.anim.produce_hair()

        self.writeline("return")
        self.indent(False)
        self.writeline()
        return

    def cre_get_full_name(self):
        return common.text_of_strrefs(self.cre, "LongName", "ShortName")

    def produce_npc_char(self):
        self.writeline("def setup_char(self, npc):")
        self.indent()

        if True:
            Strength = int(self.cre["Strength"])
            # StrengthBonus is never used in IWD2, checked
            Dexterity = int(self.cre["Dexterity"])
            Constitution = int(self.cre["Constitution"])
            Intelligence = int(self.cre["Intelligence"])
            Wisdom = int(self.cre["Wisdom"])
            Charisma = int(self.cre["Charisma"])
            self.writeline(f"utils_npc.npc_abilities_set(npc, [{Strength}, {Dexterity}, {Constitution}, {Intelligence}, {Wisdom}, {Charisma}])");

        LevelTotal = int(self.cre["LevelTotal"])
        ClassLevels = (int(self.cre["LevelBarbarian"]), int(self.cre["LevelBard"]), int(self.cre["LevelCleric"]), int(self.cre["LevelDruid"])
            , int(self.cre["LevelFighter"]), int(self.cre["LevelMonk"]), int(self.cre["LevelPaladin"])
            , int(self.cre["LevelRanger"]), int(self.cre["LevelRogue"]), int(self.cre["LevelSorcerer"])
            , int(self.cre["LevelWizard"]))
        levelsFromClasses = sum(ClassLevels)
        classes = ("stat_level_barbarian", "stat_level_bard", "stat_level_cleric", "stat_level_druid", "stat_level_fighter"
            , "stat_level_monk", "stat_level_paladin", "stat_level_ranger", "stat_level_rogue", "stat_level_sorcerer"
            , "stat_level_wizard")

        if levelsFromClasses:
            classLevel = 0
            self.writeline()
            self.writeline(f"# class levels: {levelsFromClasses}")
            for i, levels in enumerate(ClassLevels):
                if not levels: continue
                statLevel = classes[i]
                self.writeline(f"# {statLevel}: {levels}")
                for l in range(0, levels):
                    self.classes_toee[statLevel] = int(self.classes_toee.get(statLevel, 0)) + 1
                    self.writeline(f"npc.obj_set_idx_int(toee.obj_f_critter_level_idx, {classLevel}, toee.{statLevel})");
                    classLevel += 1
        else:
            raise Exception("No Classes!")

        items = self.cre["Items"]
        for item in items:
            if item_process := produce_items.ItemBase.pick(item, self):
                item_process.process_char()

        self.writeline()

        self.produce_alignment()
        #self.writeline(f'npc.obj_set_int(toee.obj_f_critter_experience, {int(self.cre["XPReward"])})
        crnum_iwd2 = int(self.cre["ChallangeRating"])
        cr = crnum_iwd2 - 2
        if crnum_iwd2 == 1:
            cr = crnum_iwd2 - 3 # IWD2 does no have entry for 1/3 cr
        cr_str = f'{cr+2}'
        if cr == -2:
            cr_str = '1/4'
        elif cr == -1:
            cr_str = '1/3'
        elif cr == 0:
            cr_str = '1/2'
        self.writeline(f'cr = {cr} # crnum_iwd2: {crnum_iwd2}, D&D CR: {cr_str}')
        self.writeline('cr_bonus = cr - npc.stat_level_get(toee.stat_level)')
        self.writeline('npc.obj_set_int(toee.obj_f_npc_challenge_rating, cr_bonus)')
        
        self.produce_feats()
        self.produce_saves()
        self.produce_hp()
        self.produce_skills()

        hidden = bool(self.cre["Hidden"])
        if hidden:
            self.writeline('self.hide_creature(npc, True)')

        self.writeline("return")
        self.indent(False)
        self.writeline()
        return

    def produce_alignment(self):
        al = int(self.cre["Alignment"])
        alignment = "ALIGNMENT_NEUTRAL"
        ids_line = str(al)
        if al == 0x11: 
            ids_line = "0x11 LAWFUL_GOOD"
            alignment = "ALIGNMENT_LAWFUL_GOOD"
        elif al == 0x12: 
            ids_line = "0x12 LAWFUL_NEUTRAL"
            alignment = "ALIGNMENT_LAWFUL_NEUTRAL"
        elif al == 0x13: 
            ids_line = "0x13 LAWFUL_EVIL"
            alignment = "ALIGNMENT_LAWFUL_EVIL"
        elif al == 0x21: 
            ids_line = "0x21 NEUTRAL_GOOD"
            alignment = "ALIGNMENT_NEUTRAL_GOOD"
        elif al == 0x22: 
            ids_line = "0x22 NEUTRAL"
            alignment = "ALIGNMENT_TRUE_NEUTRAL"
        elif al == 0x23: 
            ids_line = "0x23 NEUTRAL_EVIL"
            alignment = "ALIGNMENT_NEUTRAL_EVIL"
        elif al == 0x31: 
            ids_line = "0x31 CHAOTIC_GOOD"
            alignment = "ALIGNMENT_CHAOTIC_GOOD"
        elif al == 0x32: 
            ids_line = "0x32 CHAOTIC_NEUTRAL"
            alignment = "ALIGNMENT_CHAOTIC_NEUTRAL"
        elif al == 0x33: 
            ids_line = "0x33 CHAOTIC_EVIL"
            alignment = "ALIGNMENT_CHAOTIC_EVIL"

        self.writeline(f"npc.obj_set_int(toee.obj_f_critter_alignment, toee.{alignment}) # {ids_line}")
        return

    def produce_saves(self):
        def produce_safe(prop: str, save: str):
            value = int(self.cre[prop])
            self.writeline(f"{save} = npc.stat_level_get(toee.stat_{save})")
            self.writeline(f"if {save} < {value}: npc.obj_set_int(toee.obj_f_npc_{save}_bonus, {value}-{save}) # {prop}: {value}")
            return
        
        # should go after d20_refresh
        self.writeline()
        self.writeline("# saves")
        #produce_safe("SaveVsDeath", "save_fortitude")
        #produce_safe("SaveVsWands", "save_reflexes")
        #produce_safe("SaveVsPolymorph", "save_willpower")
        self.writeline(f'utils_npc.ensure_saves_natural(npc, {int(self.cre["SaveVsDeath"])}, {int(self.cre["SaveVsWands"])}, {int(self.cre["SaveVsPolymorph"])}) # SaveVsDeath: {int(self.cre["SaveVsDeath"])}, SaveVsWands: {int(self.cre["SaveVsWands"])}, SaveVsPolymorph: {int(self.cre["SaveVsPolymorph"])}')
        return

    def produce_hp(self):
        self.writeline()
        self.writeline("# HP")
        maximumHP = int(self.cre["MaximumHP"])
        currentHP = int(self.cre["CurrentHP"])
        damage = maximumHP - currentHP
        self.writeline(f'utils_npc.ensure_hp(npc, {maximumHP}) # MaximumHP: {maximumHP}')
        statusFlags = self.cre["StatusFlags"]
        STATE_DEAD = ""
        if "STATE_DEAD" in str(statusFlags):
            damage = 10 + maximumHP
            STATE_DEAD = ", STATE_DEAD"
        self.writeline(f'npc.obj_set_int(toee.obj_f_hp_damage, {damage}) # CurrentHP: {currentHP}{STATE_DEAD}')
        return

    def produce_faction(self):
        allegiance = int(self.cre["EnemyAlly"])
        faction = "factions_zmod.FACTION_NEUTRAL_NPC"
        if allegiance == 128:
            faction = "factions_zmod.FACTION_NEUTRAL_NPC"
        elif allegiance == 255:
            faction = "factions_zmod.FACTION_ENEMY"
        self.writeline("@classmethod")
        self.writeline(f"def get_class_faction(cls): return {faction} # allegiance: {allegiance}")
        self.writeline()
        return
    
    def setup_gear(self):
        self.writeline("def setup_gear(self, npc):")
        self.indent()
        items = self.cre["Items"]
        for item in items:
            item_file_name = None
            if (item_item := item["Item"]):
                item_file_name = item_item["Filename"]
            item_type = item["ItemTypeEval"]
            slot_name = item["SlotCode"]
            item_name = item["ItemNameEval"]
            droppable = bool(item["ItemDroppableEval"])
            no_loot = not droppable

            self.writeline(f'# {slot_name}: {item_name}({item_type}) from {item_file_name}')
            res = False
            if item_process := produce_items.ItemBase.pick(item, self):
                res = item_process.process_item()

            if not res:
                self.writeline("# Not found! TODO ITEM")
            self.writeline()

        self.anim.produce_cloth()
        self.writeline("return")
        self.indent(False)
        self.writeline()
        return

    def check_feat(self, feat_to_add, value_name, value):
        if "proficiency" in feat_to_add:
            classes_toee = self.classes_toee
            if classes_toee:
                for class_toee, level_count in classes_toee.items():
                    if not level_count: continue
                    if cname := self.doc.templeClassSpecs.toee_class_spec_has_prof(class_toee, feat_to_add):
                        self.writeline(f"# {value_name}: {value} => {feat_to_add} skip for {cname}")
                        return True
        return False

    def produce_feats(self):

        def feat_pro_add(value_name: str, levels: list):
            value = self.cre[value_name]
            splitter_added = False
            for level in range(1, value+1):
                feat_to_addv = levels[level-1]
                if not feat_to_addv: continue

                if isinstance(feat_to_addv, str):
                    if not self.check_feat(feat_to_addv, value_name, value):
                        if not splitter_added:
                            splitter_added = True
                            self.writeline()
                            self.writeline(f"# {value_name}: {value}")
                        self.writeline(f"npc.feat_add(toee.{feat_to_addv})")
                else:
                    for feat_to_add in feat_to_addv:
                        if not feat_to_add: continue
                        if self.check_feat(feat_to_add, value_name, value):
                            continue
                        if not splitter_added:
                            splitter_added = True
                            self.writeline()
                            self.writeline(f"# {value_name}: {value}")
                        self.writeline(f"npc.feat_add(toee.{feat_to_add})")
            return

        def feat_pro_add_weapon(value_name: str, levels: list, weapons: list):
            if not levels:
                return
            value = self.cre[value_name]
            splitter_added = False
            for weapon in weapons:
                for level in range(1, value+1):
                    feat_template = levels[level-1]
                    if not feat_template: continue
                    feat_to_add = feat_template + weapon
                    if self.check_feat(feat_to_add, value_name, value):
                        return
                    if not splitter_added:
                        splitter_added = True
                        self.writeline()
                        self.writeline(f"# {value_name}: {value}")
                    self.writeline(f"npc.feat_add(toee.{feat_to_add})")
            return

        self.writeline()
        self.writeline("# feats")
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
        feat_pro_add_weapon("FeatToughness", None
            , ["feat_toughness"]
        )

        self.writeline()
        self.writeline(f"npc.feat_add(toee.feat_athletic, 1) # workaround for do_refresh_d20_status")
        return

    def produce_feat(self, feat: str):
        # https://sorcerers.net/Games/IWD2/feats.php

        ft = feat.lower()
        feat_to_add = None
        feat_to_add0 = None
        if True:
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
            if self.check_feat(feat_to_add, ft, ""):
                return
            if feat_to_add.startswith("feat_"):
                self.writeline(f"npc.feat_add(toee.{feat_to_add}) # {feat}")
            else:
                self.writeline(f'npc.feat_add("{feat_to_add}") # {feat}')
        return

    def produce_skills(self):
        def produce_skill(prop: str, skill: str):
            value = self.cre[prop]
            self.writeline(f"# {prop}: {value}")
            if value:
                self.writeline(f"utils_npc.npc_skill_ensure(npc, toee.{skill}, {value})")
            return

        self.writeline()
        self.writeline("# skills")
        produce_skill("SkillAlchemy", "skill_alchemy")
        produce_skill("SkillAnimalEmpathy", "skill_handle_animal")
        produce_skill("SkillBluff", "skill_bluff")
        produce_skill("SkillConcentration", "skill_concentration")
        produce_skill("SkillDiplomacy", "skill_diplomacy")
        produce_skill("SkillDisableDevice", "skill_disable_device")
        produce_skill("SkillHide", "skill_hide")
        produce_skill("SkillIntimidate", "skill_intimidate")
        produce_skill("SkillKnowledgeArcana", "skill_knowledge_arcana")
        produce_skill("SkillMoveSilently", "skill_move_silently")
        produce_skill("SkillOpenLock", "skill_open_lock")
        produce_skill("SkillPickPocket", "skill_pick_pocket")
        produce_skill("SkillSearch", "skill_search")
        produce_skill("SkillSpellcraft", "skill_spellcraft")
        produce_skill("SkillUseMagicDevice", "skill_use_magic_device")
        produce_skill("SkillWildernessLaw", "skill_wilderness_lore")
        return

    def produce_dialog(self):
        dialog_name = self.cre["DialogFile"]
        if not dialog_name or dialog_name == "None":
            return
        fn = os.path.join(self.doc.exp_dir, 'Dialogs', dialog_name + '.json')
        dialog_dict = common.read_file_json(fn)
        self.dialog = produce_dialog.ProduceNPCDialog(dialog_name, self, dialog_dict, self.dialog_file)
        self.dialog.produce(self.are_name, self.cre_name)
        return

    @classmethod
    def scan_dialog(cls, doc, dialog_name: str, are_name: str, cre_name: str):
        if not dialog_name or dialog_name == "None":
            return
        fn = os.path.join(doc.exp_dir, 'Dialogs', dialog_name + '.json')
        if os.path.exists(fn):
            dialog_dict = common.read_file_json(fn)
            produce_dialog.ProduceNPCDialog.scan(doc, dialog_dict, are_name, cre_name)
        return

    def save(self):
        super().save()

        self.dialog_file.save()
        return