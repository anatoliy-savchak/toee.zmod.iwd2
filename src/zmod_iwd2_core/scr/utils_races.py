import toee, race_defs

RACE_ABILITY_BONUSES_DWARF = race_defs.GetStatModifiers(toee.race_dwarf)
RACE_ABILITY_BONUSES_ELF = race_defs.GetStatModifiers(toee.race_elf)

RACE_ABILITY_BONUSES_GNOLL = [4, 0, 2, -2, 0, -2]
RACE_ABILITY_BONUSES_ORC = [4, 0, 0, -2, -2, -2]

RACE_ABILITY_HUMAN_ARRAY = [13, 11, 12, 10, 9, 8]
RACE_ABILITY_MUL_ARRAY = [15, 9, 12, 10, 9, 8]
RACE_ABILITY_MUL2DWARF_ARRAY = [15, 9+2, 12-2, 10, 9, 8]
RACE_ABILITY_ELF_ARRAY = [13, 13-2, 10+2, 10, 9, 8]
RACE_ABILITY_GNOLL_ARRAY = [15, 10, 13, 8, 11, 8]
RACE_ABILITY_ORC_ARRAY = [17, 11, 12, 8, 7, 6]
RACE_ABILITY_HILL_GIANT_ARRAY = [25, 8, 19, 6, 10, 7]
