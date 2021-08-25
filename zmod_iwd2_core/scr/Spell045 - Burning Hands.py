from toee import *
from utilities import location_from_axis, location_to_axis

def OnBeginSpellCast( spell ):
	print "Burning Hands OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Burning Hands OnSpellEffect"

	remove_list = []

	dam = dice_new( '1d4' )
	dam.number = min( 5, spell.caster_level )

	if spell.caster.name == 14540: # Hell Hound's Breath Weapon
		dam = dice_new( '2d6' )
		spell.dc = 13
	xx,yy = location_to_axis(spell.caster.location)
	if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
	# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
		game.particles( 'swirled gas', spell.caster )
		spell.caster.float_mesfile_line( 'mes\\skill_ui.mes', 2000,1 )
		game.sound(7581,1)
		game.sound(7581,1)
	else: # caster himself is outside Chamber, now check the targets:
		soundfizzle = 0
		game.particles( 'sp-Burning Hands', spell.caster )

		npc = spell.caster

		#### Caster is NOT in game party
		if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL:
			range = 15
			target_list = list(game.obj_list_cone( spell.caster, OLC_CRITTERS, range, -30, 150 ))
			target_list.remove(spell.caster)
			for obj in target_list:
				xx,yy = location_to_axis(obj.location)
				if obj.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
					obj.float_mesfile_line( 'mes\\skill_ui.mes', 2000,1 )
		
					game.particles( 'swirled gas', obj.location )
					soundfizzle = 1

				else:
					if obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_FIRE, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
						# saving throw successful
						obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					else:
						# saving throw unsuccessful
						obj.float_mesfile_line( 'mes\\spell.mes', 30002 )


		#### Caster is in game party
		if npc.type == obj_t_pc or npc.leader_get() != OBJ_HANDLE_NULL:
			
			# get all targets in a 10ft cone (180')
			soundfizzle = 0
			for target_item in spell.target_list:
				remove_list.append( target_item.obj )
				xx,yy = location_to_axis(target_item.obj.location)
				if target_item.obj.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
					# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
					target_item.obj.float_mesfile_line( 'mes\\skill_ui.mes', 2000,1 )
		
					game.particles( 'swirled gas', target_item.obj.location )
					soundfizzle = 1
					spell.target_list.remove_target( target_item.obj )
				else:

					if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_FIRE, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
						# saving throw successful
						target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					else:
						# saving throw unsuccessful
						target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		if soundfizzle == 1:
			game.sound(7581,1)
			game.sound(7581,1)

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Burning Hands OnBeginRound"

def OnEndSpellCast( spell ):
	print "Burning Hands OnEndSpellCast"