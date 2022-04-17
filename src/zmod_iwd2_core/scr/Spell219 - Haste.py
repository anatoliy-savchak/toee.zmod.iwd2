import toee, sys, traceback
import utils_npc

def OnBeginSpellCast( spell ):
	print "Haste OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	toee.game.particles( "sp-transmutation-conjure", spell.caster )
	return

class MyTargetItem(object):
	def __init__(self, obj, partsys_id):
		assert isinstance(obj, toee.PyObjHandle)
		assert isinstance(partsys_id, int)

		self.obj = obj
		self.partsys_id = partsys_id
		return

def OnSpellEffect(spell):
	assert isinstance(spell, toee.PySpell)
	print "Haste:: OnSpellEffect(spell.caster: {}, caster.level: {}, target_list: {}, )".format(spell.caster, spell.caster_level, spell.target_list)
	try:
		target_list = list()

		if spell.caster.type == toee.obj_t_npc and len(spell.target_list) <= 1 and not spell.caster.is_friendly(toee.game.leader):
			# NPC AI
			around_npc = spell.caster
			if len(spell.target_list): around_npc = spell.target_list[0].obj

			candidates = list()
			count = spell.caster_level

			#candidates.append(around_npc)
			for npc in toee.game.obj_list_range(around_npc.location, 30, toee.OLC_NPC):
				if not utils_npc.npc_could_be_attacked(npc) : continue
				if npc == around_npc or not around_npc.is_friendly(npc): continue
				candidates.append(npc)
				

			candidates = sorted(candidates, key = lambda o: o.stat_level_get(toee.stat_level), reverse = True)[:count-1]
			candidates.insert(0, around_npc)

			for npc in candidates:
				if npc == spell.target_list[0].obj:
					target_list.append(spell.target_list[0])
				else:
					target_list.append(MyTargetItem(npc, 0))
		else:
			for target_item in spell.target_list:
				target_list.append(target_item)


		spell.duration = 1 * spell.caster_level
		remove_list = []

		for target_item in target_list:
			if target_item.obj.is_friendly(spell.caster):
				return_val = target_item.obj.condition_add_with_args( 'sp-Haste', spell.id, spell.duration, 1 )
				if return_val == 1:
					target_item.partsys_id = toee.game.particles('sp-Haste', target_item.obj)

			else:
				if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
					# saving throw unsuccessful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
					return_val = target_item.obj.condition_add_with_args( 'sp-Haste', spell.id, spell.duration, 1 )
					if return_val == 1:
						target_item.partsys_id = toee.game.particles( 'sp-Haste', target_item.obj )

				else:
					# saving throw successful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					toee.game.particles( 'Fizzle', target_item.obj )
					remove_list.append( target_item.obj )

		spell.target_list.remove_list(remove_list)
	except Exception, e:
		print "Hold Person OnSpellEffect error:", sys.exc_info()[0]
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	finally:
		spell.spell_end(spell.id)
	return

def OnBeginRound( spell ):
	print "Haste OnBeginRound"

def OnEndSpellCast( spell ):
	print "Haste OnEndSpellCast"