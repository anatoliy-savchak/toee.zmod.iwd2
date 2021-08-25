import toee

def OnBeginSpellCast( spell ):
	print("Magic Weapon OnBeginSpellCast")
	print("spell.target_list={}".format(spell.target_list))
	print("spell.caster={}  caster.level= {}".format(spell.caster, spell.caster_level))
	toee.game.particles("sp-transmutation-conjure", spell.caster)
	return

def	OnSpellEffect(spell):
	assert isinstance(spell, toee.PySpell)
	print "Magic Weapon:: OnSpellEffect(spell.caster: {}, caster.level: {}, target_list: {}, )".format(spell.caster, spell.caster_level, spell.target_list)

	spell.duration = 10 * spell.caster_level # minute per caster level
	target_item = spell.target_list[0]

	weapon = None
	target_type = None
	if (target_item.obj):
		target_type = target_item.obj.type

	while (True):
		if target_type == toee.obj_t_weapon:
			weapon = target_item.obj

		if (target_type == toee.obj_t_npc):
			if (not spell.caster.is_friendly(target_item.obj)):
				break

		if (target_type == toee.obj_t_pc or target_type == toee.obj_t_npc):
			weapon = target_item.obj.item_worn_at(toee.item_wear_weapon_primary)
			if (weapon and weapon.d20_query_has_spell_condition(toee.sp_Magic_Weapon)):
				weapon = None
			if (not weapon):
				weapon = target_item.obj.item_worn_at(toee.item_wear_weapon_secondary)

		if (weapon and weapon.d20_query_has_spell_condition(toee.sp_Magic_Weapon)):
			weapon = None

		break

	if weapon:
		print("sp-Magic Weapon: {}".format(weapon))
		if (weapon != target_item.obj):
			target_item.obj = weapon
		weapon.d20_status_init()
		weapon.condition_add_with_args('sp-Magic Weapon', spell.id, spell.duration, 0)
		target_item.partsys_id = toee.game.particles('sp-Detect Magic 2 Med', spell.caster)
	else:
		# not an item!
		target_item.obj.float_mesfile_line('mes\\spell.mes', 30003)
		toee.game.particles( 'Fizzle', spell.caster)
		spell.target_list.remove_target(target_item.obj)
		spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Magic Weapon OnBeginRound"

def OnEndSpellCast( spell ):
	print "Magic Weapon OnEndSpellCast"