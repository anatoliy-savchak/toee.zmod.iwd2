import toee, tpdp, debug
import const_toee
import utils_spell

def knowstone_create(spell_num, loc, caster_class = toee.stat_level_sorcerer, off_x = 0.0, off_y = 0.0):
	assert isinstance(spell_num, int)
	assert isinstance(loc, int)

	spell_entry = tpdp.SpellEntry(spell_num)
	if not spell_entry or not spell_entry.spell_enum: 
		return None

	spell_class = utils_spell.get_spell_class(caster_class)
	spell_level = spell_entry.level_for_spell_class(spell_class)

	print("spell_class: {}, spell_level: {}".format(spell_class, spell_level))

	result = toee.game.obj_create(12701, loc, off_x, off_y)
	result.spell_known_add(spell_num, spell_class, spell_level)

	# price
	if (1):
		caster_level = spell_level * 2 - 1
		price_gp = spell_level * caster_level * 25
		worth = price_gp * 100
		result.obj_set_int(toee.obj_f_item_worth, worth)

	# description
	if (1):
		name = "{} Knowstone".format(utils_spell.spell_name(spell_num))
		description_id = toee.game.make_custom_name(name)
		print("new name: {} from {}".format(description_id, name))
		result.obj_set_int(const_toee.obj_f_description_correct, description_id)
		result.obj_set_int(toee.obj_f_item_description_unknown, description_id)

	# icon
	if (1):
		#{00414} {Ioun_dusty_rose.tga}
		#{00415} {Ioun_pale_blue.tga}
		#{00416} {Ioun_scarlet_and_blue.tga}
		#{00417} {Ioun_incadescent_blue.tga}
		#{00418} {Ioun_Deep_red.tga}
		#{00419} {Ioun_pink.tga}
		#{00420} {Ioun_Pink_and_green.tga}

		spell_school_enum = spell_entry.spell_school_enum
		icon_num = 414 #Ioun_dusty_rose.tga
		if (spell_school_enum == toee.Evocation):
			icon_num = 418 # {00418} {Ioun_Deep_red.tga} like {154} {scroll_red_icon.tga}
		elif (spell_school_enum == toee.Conjuration):
			icon_num = 417 # {00417} {Ioun_incadescent_blue.tga} like {00379} {scroll_DarkBlue_icon.tga}
		elif (spell_school_enum == toee.Necromancy):
			icon_num = 419 # {00419} {Ioun_pink.tga} like {00380} {scroll_Deeppurple_icon.tga}
		elif (spell_school_enum == toee.Transmutation):
			icon_num = 420 # {00420} {Ioun_Pink_and_green.tga} like {00381} {scroll_green_icon.tga}
		elif (spell_school_enum == toee.Illusion):
			icon_num = 416 # {00416} {Ioun_scarlet_and_blue.tga} like {00382} {scroll_grey_icon.tga}
		elif (spell_school_enum == toee.Enchantment):
			icon_num = 415 # {00415} {Ioun_pale_blue.tga} like {00383} {scroll_LightBlue_icon.tga}
		elif (spell_school_enum == toee.Abjuration):
			icon_num = 420 # {00420} {Ioun_Pink_and_green.tga} like {00384} {scroll_orange_icon.tga}
		elif (spell_school_enum == toee.Divination):
			icon_num = 420 # {00420} {Ioun_Pink_and_green.tga} like {00386} {scroll_yellow_icon.tga}

		result.obj_set_int(toee.obj_f_item_inv_aid, icon_num)

	#result.item_flag_set(toee.OIF_IDENTIFIED)
	#result.item_flag_set(toee.OIF_WONT_SELL)
	#result.item_flag_set(toee.OIF_WONT_SELL)
	return result

def _test_knowstone_create():
	# import item_knowstone
	# ks = item_knowstone._test_knowstone_create()

	#pc = toee.game.leader
	pc = toee.game.party[3]
	item = knowstone_create(toee.spell_blur, pc.location)
	spell_store = item.obj_get_spell(toee.obj_f_item_spell_idx, 0)
	print("Spell: {}({}), spell level: {}".format(spell_store.spell_name, spell_store.spell_enum, spell_store.spell_level))
	pc.item_get(item)
	return item

def knowstone_learn(npc, item, item_inv_idx = -1):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(item, toee.PyObjHandle)
	assert isinstance(item_inv_idx, int)

	def show_user_error(msg):
		npc.float_text_line(msg, toee.tf_red)
		toee.game.create_history_freeform(msg + "\n\n")
		return

	def show_user_warning(msg):
		npc.float_text_line(msg, toee.tf_yellow)
		toee.game.create_history_freeform(msg + "\n\n")
		return

	def show_user_info(msg):
		npc.float_text_line(msg, toee.tf_green)
		toee.game.create_history_freeform(msg + "\n\n")
		return

	result = 0
	spell_store = item.obj_get_spell(toee.obj_f_item_spell_idx, 0)
	if not spell_store.spell_enum:
		print("knowstone_learn error - item does not have valid spell store spell_enum: {}, item: {}".format(spell_store.spell_enum, item))
		show_user_error("Item {} has no spells!".format(item.description))
		return result

	if npc.is_spell_known(spell_store.spell_enum):
		print("knowstone_learn warning - item spell alrady known. spell: {}({}), item: {}, npc: {}".format(spell_store.spell_name, spell_store.spell_enum, item, npc))
		show_user_warning("Spell {} already known!".format(spell_store.spell_name))
		return result

	result = npc.spell_known_add(spell_store.spell_enum, spell_store.spell_class, spell_store.spell_level)
	if not result:
		print("knowstone_learn unknown error spell_enum: {}, item: {}".format(spell_store.spell_enum, item))
		show_user_error("{} learning unknown error!".format(item.description))
		return result

	show_user_info("{} learned successfully!".format(item.description))

	if item.item_flags_get() & toee.OIF_EXPIRES_AFTER_USE:
		item.destroy()
		show_user_warning("{} used up!".format(item.description))
	return result

def knowstone_create_list(spell_nums, loc, caster_class = toee.stat_level_sorcerer):
	result = list()
	for spell_num in spell_nums:
		result.append(knowstone_create(spell_num, loc, caster_class))
	return result
