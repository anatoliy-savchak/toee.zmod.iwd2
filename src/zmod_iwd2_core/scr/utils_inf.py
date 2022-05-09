import toee
import debug

DEITY_NONE = 0
DEITY_WAUKEEN = 1
DEITY_CORELLON_LARETHIAN = 2
DEITY_CHAUNTEA = 3
DEITY_TALOS = 4
DEITY_SILVANUS = 5
DEITY_GARL_GLITTERGOLD = 6
DEITY_GRUUMSH = 7
DEITY_TYR = 8
DEITY_BANE = 9
DEITY_SELUNE = 10
DEITY_MORADIN = 11
DEITY_MASK = 12
DEITY_OGHMA = 13
DEITY_TEMPUS = 14
DEITY_LATHANDER = 15
DEITY_HELM = 16
DEITY_MYRKUL = 17
DEITY_MYSTRA = 18
DEITY_YONDALLA = 19
DEITY_URDLEN = 20
DEITY_AVOREEN = 21
DEITY_BHAAL = 22
DEITY_LOLTH = 23
DEITY_ILMATAR = 24
DEITY_DUMATHOIN = 25
DEITY_AURIL = 26
DEITY_YURTRUS = 27


def iwd2_classname_to_class_const(classname):
	c = classname.upper()
	if c == "BARBARIAN":
		return "toee.stat_level_barbarian"
	if c == "BARD":
		return "toee.stat_level_bard"
	if c == "CLERIC":
		return "toee.stat_level_cleric"
	if c == "DRUID":
		return "toee.stat_level_druid"
	if c == "FIGHTER":
		return "toee.stat_level_fighter"
	if c == "MONK":
		return "toee.stat_level_monk"
	if c == "PALADIN":
		return "toee.stat_level_paladin"
	if c == "RANGER":
		return "toee.stat_level_ranger"
	if c == "ROGUE":
		return "toee.stat_level_rogue"
	if c == "SORCERER":
		return "toee.stat_level_sorcerer"
	if c == "WIZARD":
		return "toee.stat_level_wizard"
	if c == "MAGE":
		return "toee.stat_level_wizard"
	if c == "THIEF":
		return "toee.stat_level_rogue"
	return

def iwd2_classname_to_class(classname):
	c = classname.upper()
	if c == "BARBARIAN":
		return toee.stat_level_barbarian
	if c == "BARD":
		return toee.stat_level_bard
	if c == "CLERIC":
		return toee.stat_level_cleric
	if c == "DRUID":
		return toee.stat_level_druid
	if c == "FIGHTER":
		return toee.stat_level_fighter
	if c == "MONK":
		return toee.stat_level_monk
	if c == "PALADIN":
		return toee.stat_level_paladin
	if c == "RANGER":
		return toee.stat_level_ranger
	if c == "ROGUE":
		return toee.stat_level_rogue
	if c == "SORCERER":
		return toee.stat_level_sorcerer
	if c == "WIZARD":
		return toee.stat_level_wizard
	if c == "MAGE":
		return toee.stat_level_wizard
	if c == "THIEF":
		return toee.stat_level_rogue
	else:
		err = "Unknown iwd2 class: {}".format(classname)
		print(err)
		debug.breakp("iwd2_classname_to_class")
	return

def iwd2_stat_convert(statname):
	stat = None
	if statname == "CHR":
		stat = toee.stat_charisma
	else:
		err = "Unknown iwd2_stat_convert: {}".format(statname)
		print(err)
		debug.breakp("iwd2_stat_convert")
	return (stat, )

def iwd2_race_convert(race_name):
	rn = race_name.upper()
	if rn == "NO_RACE": return None
	elif rn == "DWARF": return toee.race_dwarf
	elif rn == "ELF": return toee.race_elf
	elif rn == "GNOME": return toee.race_gnome
	elif rn == "HUMAN": return toee.race_human
	elif rn == "HALF_ELF": return toee.race_half_elf
	elif rn == "HALFLING": return toee.race_halfling
	elif rn == "HALFORC": return toee.race_half_orc
	elif rn == "ELF_DROW": return toee.race_drow
	else:
		err = "Unknown iwd2_race_convert: {}".format(race_name)
		print(err)
		debug.breakp("iwd2_race_convert")
	return

def iwd2_skill_convert(name):
	n = name.lower()
	if n == 'alchemy': return toee.skill_alchemy
	if n == 'animal_empathy': return toee.skill_handle_animal
	if n == 'bluff': return toee.skill_bluff
	if n == 'concentration': return toee.skill_concentration
	if n == 'diplomacy': return toee.skill_diplomacy
	if n == 'disable_device': return toee.skill_disable_device
	if n == 'hide': return toee.skill_hide
	if n == 'intimidate': return toee.skill_intimidate
	if n == 'knowledge_arcana': return toee.skill_knowledge_arcana
	if n == 'move_silently': return toee.skill_move_silently
	if n == 'open_lock': return toee.skill_open_lock
	if n == 'pick_pocket': return toee.skill_pick_pocket
	if n == 'search': return toee.skill_search
	if n == 'spellcraft': return toee.skill_spellcraft
	if n == 'use_magic_device': return toee.skill_use_magic_device
	if n == 'wilderness_lore': return toee.skill_wilderness_lore
	else:
		err = "Unknown iwd2_skill_convert: {}".format(name)
		print(err)
		debug.breakp("iwd2_skill_convert")
	return

def iwd2_kit_to_deity(name):
	n = name.lower()
	if n == 'paladin_ilmater': return DEITY_ILMATAR
	if n == 'paladin_helm': return DEITY_HELM
	if n == 'paladin_mystra': return DEITY_MYSTRA
	if n == 'cleric_ilmater': return DEITY_ILMATAR
	if n == 'cleric_lathander': return DEITY_LATHANDER
	if n == 'cleric_selune': return DEITY_SELUNE
	if n == 'cleric_helm': return DEITY_HELM
	if n == 'cleric_oghma': return DEITY_OGHMA
	if n == 'cleric_tempus': return DEITY_TEMPUS
	if n == 'cleric_bane': return DEITY_BANE
	if n == 'cleric_mask': return DEITY_MASK
	if n == 'cleric_talos': return DEITY_TALOS
	else:
		err = "Unknown iwd2_kit_to_deity: {}".format(name)
		print(err)
		debug.breakp("iwd2_kit_to_deity")
	return

def iwd2_kit_to_school(name):
	n = name.lower()
	if n == 'mage_abjurer': return toee.Abjuration
	if n == 'mage_conjurer': return toee.Conjuration
	if n == 'mage_diviner': return toee.Divination
	if n == 'mage_enchanter': return toee.Enchantment
	if n == 'mage_evoker': return toee.Evocation
	if n == 'mage_illusionist': return toee.Illusion
	if n == 'mage_necromancer': return toee.Necromancy
	if n == 'mage_transmuter': return toee.Transmutation
	if n == 'mage_generalist': return 0
	else:
		err = "Unknown iwd2_kit_to_school: {}".format(name)
		print(err)
		debug.breakp("iwd2_kit_to_school")
	return

def iwd2_kit_has(name, npc):
	assert isinstance(name, str)
	assert isinstance(npc, toee.PyObjHandle)

	n = name.lower()
	if "mage" in n:
		school = iwd2_kit_to_school(n) 
		value = npc.obj_get_int(toee.obj_f_critter_school_specialization)
		return value == school
	elif "cleric" in n or "paladin" in n:
		deity = iwd2_kit_to_deity(n) 
		value = npc.obj_get_int(toee.obj_f_critter_deity)
		return value == deity
	else:
		err = "Unknown iwd2_kit_get_value: {}".format(name)
		print(err)
		debug.breakp("iwd2_kit_get_value")
	return

def iwd2_alignment_equals(name, a):
	n = name.lower()
	if n == "LAWFUL_GOOD" or n=="1": return a == toee.ALIGNMENT_LAWFUL_GOOD
	if n == "LAWFUL_NEUTRAL" or n=="2": return a == toee.ALIGNMENT_LAWFUL_NEUTRAL
	if n == "LAWFUL_EVIL" or n=="3": return a == toee.ALIGNMENT_LAWFUL_EVIL
	if n == "NEUTRAL_GOOD" or n=="4": return a == toee.ALIGNMENT_NEUTRAL_GOOD
	if n == "NEUTRAL" or n=="5": return a == toee.ALIGNMENT_TRUE_NEUTRAL
	if n == "NEUTRAL_EVIL" or n=="6": return a == toee.ALIGNMENT_NEUTRAL_EVIL
	if n == "CHAOTIC_GOOD" or n=="7": return a == toee.ALIGNMENT_CHAOTIC_GOOD
	if n == "CHAOTIC_NEUTRAL" or n=="8": return a == toee.ALIGNMENT_CHAOTIC_NEUTRAL
	if n == "CHAOTIC_EVIL" or n=="9": return a == toee.ALIGNMENT_CHAOTIC_EVIL

	if n == "MASK_GOOD" or n=="10": return a == toee.ALIGNMENT_LAWFUL_GOOD or a == toee.ALIGNMENT_NEUTRAL_GOOD or a == toee.ALIGNMENT_CHAOTIC_GOOD
	if n == "MASK_GENEUTRAL" or n=="11": return a == toee.ALIGNMENT_NEUTRAL_GOOD or a == toee.ALIGNMENT_NEUTRAL_EVIL or a == toee.ALIGNMENT_TRUE_NEUTRAL
	if n == "MASK_EVIL" or n=="12": return a == toee.ALIGNMENT_LAWFUL_EVIL or a == toee.ALIGNMENT_NEUTRAL_EVIL or a == toee.ALIGNMENT_CHAOTIC_EVIL
	if n == "MASK_LAWFUL" or n=="13": return a == toee.ALIGNMENT_LAWFUL_GOOD or a == toee.ALIGNMENT_LAWFUL_NEUTRAL or a == toee.ALIGNMENT_LAWFUL_EVIL
	if n == "MASK_LCNEUTRAL" or n=="14": returna == toee.ALIGNMENT_LAWFUL_NEUTRAL or a == toee.ALIGNMENT_CHAOTIC_NEUTRAL or a == toee.ALIGNMENT_TRUE_NEUTRAL
	if n == "MASK_CHAOTIC" or n=="15": return a == toee.ALIGNMENT_CHAOTIC_GOOD or a == toee.ALIGNMENT_CHAOTIC_NEUTRAL or a == toee.ALIGNMENT_CHAOTIC_EVIL
	else:
		err = "Unknown iwd2_alignment_equals: {}".format(name)
		print(err)
		debug.breakp("iwd2_alignment_equals")
	return

XP_VAR = {
	"Level_1_Easy": 300,
	"Level_1_Average": 400,
	"Level_1_Hard": 600,
	"Level_1_Very_Hard": 900,
	"Level_2_Easy": 450,
	"Level_2_Average": 600,
	"Level_2_Hard": 900,
	"Level_2_Very_Hard": 1350,
	"Level_3_Easy": 375,
	"Level_3_Average": 500,
	"Level_3_Hard": 750,
	"Level_3_Very_Hard": 1125,
	"Level_4_Easy": 525,
	"Level_4_Average": 700,
	"Level_4_Hard": 1050,
	"Level_4_Very_Hard": 1575,
	"Level_5_Easy": 525,
	"Level_5_Average": 700,
	"Level_5_Hard": 1050,
	"Level_5_Very_Hard": 1575,
	"Level_6_Easy": 1050,
	"Level_6_Average": 1400,
	"Level_6_Hard": 2100,
	"Level_6_Very_Hard": 3150,
	"Level_7_Easy": 1425,
	"Level_7_Average": 1900,
	"Level_7_Hard": 2850,
	"Level_7_Very_Hard": 4275,
	"Level_8_Easy": 1575,
	"Level_8_Average": 2100,
	"Level_8_Hard": 3150,
	"Level_8_Very_Hard": 4725,
	"Level_9_Easy": 1575,
	"Level_9_Average": 2100,
	"Level_9_Hard": 3150,
	"Level_9_Very_Hard": 4725,
	"Level_10_Easy": 1725,
	"Level_10_Average": 2300,
	"Level_10_Hard": 3450,
	"Level_10_Very_Hard": 5175,
	"Level_11_Easy": 2925,
	"Level_11_Average": 3900,
	"Level_11_Hard": 5850,
	"Level_11_Very_Hard": 8775,
	"Level_12_Easy": 1200,
	"Level_12_Average": 1600,
	"Level_12_Hard": 2400,
	"Level_12_Very_Hard": 3600,
	"Level_13_Easy": 1950,
	"Level_13_Average": 2600,
	"Level_13_Hard": 3900,
	"Level_13_Very_Hard": 5850,
	"Level_14_Easy": 750,
	"Level_14_Average": 1000,
	"Level_14_Hard": 1500,
	"Level_14_Very_Hard": 2250,
	"Level_15_Easy": 2475,
	"Level_15_Average": 3300,
	"Level_15_Hard": 4950,
	"Level_15_Very_Hard": 7425
}

def iwd2_xp_var(xp_var):
	global XP_VAR
	xp_var_lo = xp_var.lower()
	result = next((value for name, value in XP_VAR.iteritems() if name.lower() == xp_var_lo), None)
	return result