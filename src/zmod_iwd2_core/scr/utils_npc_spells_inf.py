import utils_npc
import toee
import utils_spell
import utils_npc_spells_tactics

def ctrl_add_spell(ctrl, spell_name_inf, memorized, remaining, stat_class, spell_level):
	spell_rec = get_spell_rec(spell_name_inf)
	if not spell_rec: return
	ctrl.spells.add_spell(spell_rec["spell_id"], stat_class, spell_level, memorized)
	return 1

def get_spell_rec(spell_name_inf):
	spell_name_inf_lower = spell_name_inf.lower()
	spell_rec = next((rec for rec in IWD2_SPELL_MAP if rec["name"].lower() == spell_name_inf_lower), None)
	if not spell_rec:
		print('Spell not found: {}'.format(spell_name_inf))
		return
	spell_id = spell_rec["spell_id"]
	if not spell_id:
		print('Spell id not found: {}'.format(spell_name_inf))
		return
	return spell_rec

def get_spell_id(spell_name_inf):
	spell_rec = get_spell_rec(spell_name_inf)
	if spell_rec:
		spell_id = spell_rec["spell_id"]
		return spell_id
	return

IWD2_SPELL_MAP = [\
	  { "name": "Aid", "spell_id": toee.spell_aid, "spell_cls": utils_npc_spells_tactics.STAid }\
	, { "name": "Bull's Strength", "spell_id": toee.spell_bulls_strength, "spell_cls": utils_npc_spells_tactics.STBullsStrength }\
	, { "name": "Chant", "spell_id": toee.spell_prayer, "spell_cls": utils_npc_spells_tactics.STPrayer }\
	, { "name": "Command", "spell_id": toee.spell_command, "spell_cls": utils_npc_spells_tactics.STCommand }\
	, { "name": "Cure Minor Wounds", "spell_id": toee.spell_cure_minor_wounds, "spell_cls": utils_npc_spells_tactics.STCureMinorWounds }\
	, { "name": "Cure Light Wounds", "spell_id": toee.spell_cure_light_wounds, "spell_cls": utils_npc_spells_tactics.STCureLightWounds }\
	, { "name": "Cure Moderate Wounds", "spell_id": toee.spell_cure_moderate_wounds, "spell_cls": utils_npc_spells_tactics.STCureModerateWounds }\
	, { "name": "Cure Serious Wounds", "spell_id": toee.spell_cure_serious_wounds, "spell_cls": utils_npc_spells_tactics.STCureSeriousWounds }\
	, { "name": "Cure Critical Wounds", "spell_id": toee.spell_cure_critical_wounds, "spell_cls": utils_npc_spells_tactics.STCureCriticalWounds }\
	, { "name": "Death Armor", "spell_id": 0, "spell_cls": None, "comment": "Could be created", "url": r"https://www.gamebanshee.com/showshot.php?/icewinddaleii/spells/images/frostfingers.jpg" }\
	, { "name": "Dispel Magic", "spell_id": toee.spell_dispel_magic, "spell_cls": utils_npc_spells_tactics.STDispellMagic }\
	, { "name": "Frost Fingers", "spell_id": toee.spell_burning_hands, "spell_cls": utils_npc_spells_tactics.STBurningHands, "comment": "Should be created", "url": r"https://www.gamebanshee.com/showshot.php?/icewinddaleii/spells/images/deatharmor.jpg" }\
	, { "name": "Greater Command", "spell_id": toee.spell_greater_command, "spell_cls": utils_npc_spells_tactics.STGreaterCommand }\
	, { "name": "Heal", "spell_id": toee.spell_heal, "spell_cls": utils_npc_spells_tactics.STHeal }\
	, { "name": "Hold Person", "spell_id": toee.spell_hold_person, "spell_cls": utils_npc_spells_tactics.STHoldPerson }\
	, { "name": "Holy Word", "spell_id": toee.spell_holy_word, "spell_cls": utils_npc_spells_tactics.STHolyWord }\
	, { "name": "Recitation", "spell_id": 0, "spell_cls": None, "comment": "Spell Compendium", "url": r"https://www.gamebanshee.com/showshot.php?/icewinddaleii/spells/images/recitation.jpg" }\
	, { "name": "Moon Motes", "spell_id": 0, "spell_cls": None, "comment": "Could be created", "url": r"https://www.gamebanshee.com/showshot.php?/icewinddaleii/spells/images/moonmotes.jpg" }\
	, { "name": "Summon Monster I", "spell_id": toee.spell_summon_monster_i, "spell_cls": utils_npc_spells_tactics.STSummonMonster }\
	, { "name": "Summon Monster II", "spell_id": toee.spell_summon_monster_ii, "spell_cls": utils_npc_spells_tactics.STSummonMonster2 }\
	, { "name": "Summon Monster III", "spell_id": toee.spell_summon_monster_iii, "spell_cls": utils_npc_spells_tactics.STSummonMonster3 }\
	, { "name": "Summon Monster IV", "spell_id": toee.spell_summon_monster_iv, "spell_cls": utils_npc_spells_tactics.STSummonMonster4 }\
	, { "name": "Summon Monster V", "spell_id": toee.spell_summon_monster_v, "spell_cls": utils_npc_spells_tactics.STSummonMonster5 }\
	, { "name": "Summon Monster VI", "spell_id": toee.spell_summon_monster_vi, "spell_cls": utils_npc_spells_tactics.STSummonMonster6 }\
	, { "name": "Summon Monster VII", "spell_id": toee.spell_summon_monster_vii, "spell_cls": utils_npc_spells_tactics.STSummonMonster7 }\
	, { "name": "Summon Monster VIII", "spell_id": toee.spell_summon_monster_viii, "spell_cls": utils_npc_spells_tactics.STSummonMonster8 }\
	, { "name": "Summon Monster IX", "spell_id": toee.spell_summon_monster_ix, "spell_cls": utils_npc_spells_tactics.STSummonMonster9 }\
	, { "name": "Wall of Moonlight", "spell_id": 0, "spell_cls": None, "comment": "Farhun", "url": r"https://www.gamebanshee.com/showshot.php?/icewinddaleii/spells/images/wallofmoonlight.jpg" }\
	]