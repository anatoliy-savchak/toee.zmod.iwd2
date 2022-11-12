import utils_npc
import toee
import utils_spell
import utils_npc_spells_tactics

def ctrl_add_spell(ctrl, spell_name_inf, memorized, remaining, stat_class, spell_level):
	spell_name_inf_lower = spell_name_inf.lower()
	spell_rec = next((rec for rec in IWD2_SPELL_MAP if rec["name"].lower() == spell_name_inf_lower), None)
	if not spell_rec:
		print('Spell not found: {}'.format(spell_name_inf))
		return
	spell_id = spell_rec["spell_id"]
	if not spell_id:
		print('Spell id not found: {}'.format(spell_name_inf))
		return
	ctrl.spells.add_spell(spell_id, stat_class, spell_level, memorized)
	return 1

IWD2_SPELL_MAP = [\
	{ "name": "Command", "spell_id": toee.spell_command, "spell_cls": utils_npc_spells_tactics.STCommand }\
	]