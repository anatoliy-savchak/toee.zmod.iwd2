from toee import *

def OnBeginSpellCast( spell ):
	print "Command OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Command OnSpellEffect"

	spell.duration = 1
	target_item = spell.target_list[0]

	if not target_item.obj.is_friendly( spell.caster ):
		if (target_item.obj.type == obj_t_pc) or (target_item.obj.type == obj_t_npc):
			if not target_item.obj.is_category_type( mc_type_animal ):
				if target_item.obj.get_size < STAT_SIZE_LARGE:
					saved = target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id, spell.id )
					if (not saved):
						# saving throw unsuccessful
						target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

						# sub_100C6C00
						# 2: Fall
						# 3: Flee
						# 1, 4: Approach and Halt, v6->tbStatus->tbsFlags |= TBSF_Moved; tbStatus->hourglassState= 0

						preference = spell.caster.d20_query("sp-Command Preference")
						if (not preference): preference = spell.spell_get_menu_arg(RADIAL_MENU_PARAM_MIN_SETTING)
						else: preference += -1 # it is incremented in the condition specifically

						target_item.obj.condition_add_with_args( 'sp-Command', spell.id, spell.duration, preference)
						target_item.partsys_id = game.particles( 'sp-Command', target_item.obj )
						#target_item.obj.condition_add("Prone")
						#target_item.obj.fall_down()

						# add target to initiative, just in case
						#target_item.obj.add_to_initiative()
						#game.update_combat_ui()

					else:

						# saving throw successful
						target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

						game.particles( 'Fizzle', target_item.obj )
						spell.target_list.remove_target( target_item.obj )

				else:
					# not medium sized or smaller
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31005 )

					game.particles( 'Fizzle', target_item.obj )
					spell.target_list.remove_target( target_item.obj )

			else:
				# a monster
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31004 )

				game.particles( 'Fizzle', target_item.obj )
				spell.target_list.remove_target( target_item.obj )

		else:
			# not a person
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31001 )

			game.particles( 'Fizzle', target_item.obj )
			spell.target_list.remove_target( target_item.obj )

	else:

		# can't target friendlies
		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Command OnBeginRound"

def OnEndSpellCast( spell ):
	print "Command OnEndSpellCast"