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
	rec = get_spell_rec(spell_name_inf)
	if rec:
		spell_id = spell_rec["spell_id"]
		return spell_id
	return

IWD2_SPELL_MAP = [\
	  { "name": "Command", "spell_id": toee.spell_command, "spell_cls": utils_npc_spells_tactics.STCommand }\
	, { "name": "Cure Minor Wounds", "spell_id": toee.spell_cure_minor_wounds, "spell_cls": utils_npc_spells_tactics.STCureMinorWounds }\
	, { "name": "Cure Light Wounds", "spell_id": toee.spell_cure_light_wounds, "spell_cls": utils_npc_spells_tactics.STCureLightWounds }\
	, { "name": "Cure Moderate Wounds", "spell_id": toee.spell_cure_moderate_wounds, "spell_cls": utils_npc_spells_tactics.STCureModerateWounds }\
	, { "name": "Cure Serious Wounds", "spell_id": toee.spell_cure_serious_wounds, "spell_cls": utils_npc_spells_tactics.STCureSeriousWounds }\
	, { "name": "Cure Critical Wounds", "spell_id": toee.spell_cure_critical_wounds, "spell_cls": utils_npc_spells_tactics.STCureCriticalWounds }\
	]