import toee

sn_examine = 0x0
sn_use = 0x1
sn_destroy = 0x2
sn_unlock = 0x3
sn_get = 0x4
sn_drop = 0x5
sn_throw = 0x6
sn_hit = 0x7
sn_miss = 0x8
sn_dialog = 0x9
sn_first_heartbeat = 0xA
sn_catching_thief_pc = 0xB
sn_dying = 0xC
sn_enter_combat = 0xD
sn_exit_combat = 0xE
sn_start_combat = 0xF
sn_end_combat = 0x10
sn_buy_object = 0x11
sn_resurrect = 0x12
sn_heartbeat = 0x13
sn_leader_killing = 0x14
sn_insert_item = 0x15
sn_will_kos = 0x16
sn_taking_damage = 0x17
sn_wield_on = 0x18
sn_wield_off = 0x19
sn_critter_hits = 0x1A
sn_new_sector = 0x1B
sn_remove_item = 0x1C
sn_leader_sleeping = 0x1D
sn_bust = 0x1E
sn_dialog_override = 0x1F
sn_transfer = 0x20
sn_caught_thief = 0x21
sn_critical_hit = 0x22
sn_critical_miss = 0x23
sn_join = 0x24
sn_disband = 0x25
sn_new_map = 0x26
sn_trap = 0x27
sn_true_seeing = 0x28
sn_spell_cast = 0x29
sn_unlock_attempt = 0x2A

san_all = (sn_examine, sn_use, sn_destroy, sn_unlock, sn_get, sn_drop, sn_throw, sn_hit, sn_miss, sn_dialog, sn_first_heartbeat, sn_catching_thief_pc, sn_dying, sn_enter_combat, sn_exit_combat, sn_start_combat, sn_end_combat, sn_buy_object, sn_resurrect, sn_heartbeat, sn_leader_killing, sn_insert_item, sn_will_kos, sn_taking_damage, sn_wield_on, sn_wield_off, sn_critter_hits, sn_new_sector, sn_remove_item, sn_leader_sleeping, sn_bust, sn_dialog_override, sn_transfer, sn_caught_thief, sn_critical_hit, sn_critical_miss, sn_join, sn_disband, sn_new_map, sn_trap, sn_true_seeing, sn_spell_cast, sn_unlock_attempt)
san_all_names = ("sn_examine", "sn_use", "sn_destroy", "sn_unlock", "sn_get", "sn_drop", "sn_throw", "sn_hit", "sn_miss", "sn_dialog", "sn_first_heartbeat", "sn_catching_thief_pc", "sn_dying", "sn_enter_combat", "sn_exit_combat", "sn_start_combat", "sn_end_combat", "sn_buy_object", "sn_resurrect", "sn_heartbeat", "sn_leader_killing", "sn_insert_item", "sn_will_kos", "sn_taking_damage", "sn_wield_on", "sn_wield_off", "sn_critter_hits", "sn_new_sector", "sn_remove_item", "sn_leader_sleeping", "sn_bust", "sn_dialog_override", "sn_transfer", "sn_caught_thief", "sn_critical_hit", "sn_critical_miss", "sn_join", "sn_disband", "sn_new_map", "sn_trap", "sn_true_seeing", "sn_spell_cast", "sn_unlock_attempt")

obj_f_description_correct = 25
gp = 100

White = 0
Red = 1
Green = 2
Blue = 3
Yellow = 4
LightBlue = 5

rotation_grad_south_east = 135
rotation_grad_south = 180
rotation_grad_south_west = 225

rotation_0000_oclock = 0.00000
rotation_0100_oclock = 0.52360
rotation_0200_oclock = 1.04720
rotation_0300_oclock = 1.57080
rotation_0400_oclock = 2.09440
rotation_0500_oclock = 2.61799
rotation_0600_oclock = 3.14159
rotation_0700_oclock = 3.66519
rotation_0800_oclock = 4.18879
rotation_0900_oclock = 4.71239
rotation_1000_oclock = 5.23599
rotation_1100_oclock = 5.75959

ROTATAION_01_DOOR = 0.785398185253

D20STD_REROLL = 0x1
D20STD_CHARM = 0x2
D20STD_TRAP = 0x4
D20STD_POISON = 0x8
D20STD_SPELL_SCHOOL_ABJURATION = 0x20
D20STD_SPELL_SCHOOL_CONJURATION = 0x40
D20STD_SPELL_SCHOOL_DIVINATION = 0x80
D20STD_SPELL_SCHOOL_ENCHANTMENT = 0x100
D20STD_SPELL_SCHOOL_EVOCATION = 0x200
D20STD_SPELL_SCHOOL_ILLUSION = 0x400
D20STD_SPELL_SCHOOL_NECROMANCY = 0x800
D20STD_SPELL_SCHOOL_TRANSMUTATION = 0x1000
D20STD_SPELL_DESCRIPTOR_ACID = 0x2000
D20STD_SPELL_DESCRIPTOR_CHAOTIC = 0x4000
D20STD_SPELL_DESCRIPTOR_COLD = 0x8000
D20STD_SPELL_DESCRIPTOR_DARKNESS = 0x10000
D20STD_SPELL_DESCRIPTOR_DEATH = 0x20000
D20STD_SPELL_DESCRIPTOR_ELECTRICITY = 0x40000
D20STD_SPELL_DESCRIPTOR_EVIL = 0x80000
D20STD_SPELL_DESCRIPTOR_FEAR = 0x100000
D20STD_SPELL_DESCRIPTOR_FIRE = 0x200000
D20STD_SPELL_DESCRIPTOR_FORCE = 0x400000
D20STD_SPELL_DESCRIPTOR_GOOD = 0x800000
D20STD_SPELL_DESCRIPTOR_LANGUAGE_DEPENDENT = 0x1000000
D20STD_SPELL_DESCRIPTOR_LAWFUL = 0x2000000
D20STD_SPELL_DESCRIPTOR_LIGHT = 0x4000000
D20STD_SPELL_DESCRIPTOR_MIND_AFFECTING = 0x8000000
D20STD_SPELL_DESCRIPTOR_SONIC = 0x10000000
D20STD_SPELL_DESCRIPTOR_TELEPORTATION = 0x20000000
D20STD_SPELL_DESCRIPTOR_AIR = 0x40000000
D20STD_SPELL_DESCRIPTOR_EARTH = 0x80000000

spell_summon_vrock = 729
spell_scorching_ray = 733
spell_hezrou_stench = 735

hair_color_black = 0
hair_color_blonde = 1
hair_color_blue = 2
hair_color_brown = 3
hair_color_light_brown = 4
hair_color_pink = 5
hair_color_red = 6
hair_color_white = 7

hair_colors_human = (hair_color_black, hair_color_blonde, hair_color_brown, hair_color_light_brown, hair_color_red)

hair_style_longhair = 0 # Longhair (m/f)
hair_style_ponytail = 1 # Ponytail (m/f)
hair_style_shorthair = 2 # Shorthair (m/f)
hair_style_topknot = 3 # Topknot (m/f)
hair_style_mullet = 4 # Mullet (m)
hair_style_pigtails = 5 # Pigtails (f)
hair_style_bald = 6 # Bald (m)
hair_style_braids = 7 # Braids (f)
hair_style_mohawk = 8 # Mohawk (m/f)
hair_style_medium = 9 # Medium (m)
hair_style_ponytail2 = 10 # Ponytail2 (f)

hair_styles_all = (hair_style_longhair, hair_style_ponytail, hair_style_shorthair, hair_style_topknot, hair_style_mullet, \
	hair_style_pigtails, hair_style_bald, hair_style_braids, hair_style_mohawk, hair_style_medium, hair_style_ponytail2)

hair_styles_human_man = (hair_style_shorthair, hair_style_bald, hair_style_medium, hair_style_mullet)
hair_styles_human_gentleman = (hair_style_shorthair, hair_style_medium)

hair_styles_human_woman = (hair_style_longhair, hair_style_topknot, hair_style_mullet, \
	hair_style_pigtails, hair_style_braids, hair_style_ponytail2)

OSDF_DC_0 = 0x1
OSDF_DC_1 = 0x2
OSDF_DC_2 = 0x4
OSDF_DC_3 = 0x8
OSDF_DC_4 = 0x10
OSDF_DC_5 = 0x20
OSDF_DC_6 = 0x40
OSDF_RANK_0 = 0x80
OSDF_RANK_1 = 0x100
OSDF_RANK_2 = 0x200
OSDF_RANK_3 = 0x400
OSDF_RANK_4 = 0x800
OSDF_RANK_5 = 0x1000
OSDF_RANK_6 = 0x2000
OSDF_UNUSED = 0x4000
OSDF_UNUSED2 = 0x8000
OSDF_SECRET_DOOR = 0x10000
OSDF_SECRET_DOOR_FOUND = 0x20000

OWF_LOUD = 1
OWF_SILENT= 2
OWF_UNUSED_1 = 4
OWF_UNUSED_2 = 8
OWF_THROWABLE = 0x10
OWF_TRANS_PROJECTILE = 0x20
OWF_BOOMERANGS = 0x40
OWF_IGNORE_RESISTANCE = 0x80
OWF_DAMAGE_ARMOR = 0x100
OWF_DEFAULT_THROWS = 0x200
OWF_RANGED_WEAPON = 0x400
OWF_WEAPON_LOADED = 0x800
OWF_MAGIC_STAFF = 0x1000

OBJECT_FLAGS = (toee.OF_DESTROYED, toee.OF_OFF, toee.OF_FLAT, toee.OF_TEXT, toee.OF_SEE_THROUGH, toee.OF_SHOOT_THROUGH \
	, toee.OF_TRANSLUCENT, toee.OF_SHRUNK, toee.OF_DONTDRAW, toee.OF_INVISIBLE, toee.OF_NO_BLOCK, toee.OF_CLICK_THROUGH \
	, toee.OF_INVENTORY, toee.OF_DYNAMIC, toee.OF_PROVIDES_COVER, toee.OF_RANDOM_SIZE, toee.OF_NOHEIGHT, toee.OF_WADING \
	, toee.OF_UNUSED_40000, toee.OF_STONED, toee.OF_DONTLIGHT, toee.OF_TEXT_FLOATER, toee.OF_INVULNERABLE, toee.OF_EXTINCT \
	, toee.OF_TRAP_PC, toee.OF_TRAP_SPOTTED, toee.OF_DISALLOW_WADING, toee.OF_UNUSED_08000000, toee.OF_HEIGHT_SET \
	, toee.OF_ANIMATED_DEAD, toee.OF_TELEPORTED, toee.OF_RADIUS_SET \
	)

OBJECT_FLAGS_NAMES = ("toee.OF_DESTROYED", "toee.OF_OFF", "toee.OF_FLAT", "toee.OF_TEXT", "toee.OF_SEE_THROUGH", "toee.OF_SHOOT_THROUGH" \
	, "toee.OF_TRANSLUCENT", "toee.OF_SHRUNK", "toee.OF_DONTDRAW", "toee.OF_INVISIBLE", "toee.OF_NO_BLOCK", "toee.OF_CLICK_THROUGH" \
	, "toee.OF_INVENTORY", "toee.OF_DYNAMIC", "toee.OF_PROVIDES_COVER", "toee.OF_RANDOM_SIZE", "toee.OF_NOHEIGHT", "toee.OF_WADING" \
	, "toee.OF_UNUSED_40000", "toee.OF_STONED", "toee.OF_DONTLIGHT", "toee.OF_TEXT_FLOATER", "toee.OF_INVULNERABLE", "toee.OF_EXTINCT" \
	, "toee.OF_TRAP_PC", "toee.OF_TRAP_SPOTTED", "toee.OF_DISALLOW_WADING", "toee.OF_UNUSED_08000000", "toee.OF_HEIGHT_SET" \
	, "toee.OF_ANIMATED_DEAD", "toee.OF_TELEPORTED", "toee.OF_RADIUS_SET" \
	)
