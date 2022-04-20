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
            # add code to check if actual difference is needed

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

        self.lines_script.append(i_code+"return")
        self.lines_script.append("")
        return