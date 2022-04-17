import toee, debug, tpdp, utils_obj, const_toee, utils_item

def npc_feats_print(npc):
	assert isinstance(npc, toee.PyObjHandle)
	feats = npc.feats
	for f in feats:
		print("Feat Code: {}".format(f))
		print("Feat Name{}".format(toee.game.get_feat_name(f)))
	return

def npc_generate_hp(npc):
	assert isinstance(npc, toee.PyObjHandle)
	npc.obj_set_int(toee.obj_f_hp_pts, -65535)
	hp = npc.stat_level_get(toee.stat_hp_current)
	#print("Current HP: {}".format(hp))
	return hp

def npc_generate_hp_random(npc):
	assert isinstance(npc, toee.PyObjHandle)

	tpdp.config_set_string("hpfornpchd", "Normal")
	npc.obj_set_int(toee.obj_f_hp_pts, -65535)
	hp = npc.stat_level_get(toee.stat_hp_current)
	tpdp.config_set_string("hpfornpchd", "average")
	#print("Current HP: {}".format(hp))
	return hp

def char_class_get_hit_dice(char_class):
	assert isinstance(char_class, int)
	# todo in T+

	d12 = [toee.stat_level_barbarian \
		, toee.stat_level_dragon_disciple, toee.stat_level_dwarven_defender]

	d10 = [toee.stat_level_fighter, toee.stat_level_paladin, toee.stat_level_blackguard, toee.stat_level_duelist, toee.stat_level_abjurant_champion, toee.stat_level_swashbuckler]

	d8 = [toee.stat_level_cleric, toee.stat_level_druid, toee.stat_level_ranger, toee.stat_level_monk \
		, toee.stat_level_arcane_archer, toee.stat_level_hierophant, toee.stat_level_horizon_walker, toee.stat_level_horizon_walker \
		, toee.stat_level_shadowdancer, toee.stat_level_favored_soul, toee.stat_level_stormlord, toee.stat_level_scout \
		, const_toee.stat_level_npc_aristocrat, const_toee.stat_level_npc_warriror]

	d6 = [toee.stat_level_rogue, toee.stat_level_bard \
		, toee.stat_level_assassin, toee.stat_level_eldritch_knight, toee.stat_level_warlock, toee.stat_level_warmage, toee.stat_level_beguiler, toee.stat_level_fochlucan_lyrist \
		, const_toee.stat_level_npc_adept, const_toee.stat_level_npc_expert]

	d4 = [toee.stat_level_sorcerer, toee.stat_level_wizard \
		, toee.stat_level_arcane_trickster, toee.stat_level_archmage, toee.stat_level_loremaster, toee.stat_level_mystic_theurge, toee.stat_level_thaumaturgist \
		, const_toee.stat_level_npc_commoner]

	if (char_class in d12): return 12
	elif (char_class in d10): return 10
	elif (char_class in d8): return 8
	elif (char_class in d6): return 6
	elif (char_class in d4): return 4
	return 8

def npc_generate_hp_random_first(npc, hd_first_is_full = 1):
	return npc_generate_hp_ext(npc, hd_first_is_full, NPC_GENERATE_HP_EXT_RANDOM)

def npc_generate_hp_avg_first(npc, hd_first_is_full = 1):
	return npc_generate_hp_ext(npc, hd_first_is_full, NPC_GENERATE_HP_EXT_AVG)

NPC_GENERATE_HP_EXT_AVG = 0
NPC_GENERATE_HP_EXT_RANDOM = 1
def npc_generate_hp_ext(npc, hd_first_is_full, method):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(hd_first_is_full, int)
	assert isinstance(method, int)# 0: avg, 1: random

	hd = npc.hit_dice
	# con bonus applied in GlobalMaxHPCalc

	pts = 0
	was_hd_natural = 0
	lines = []
	if (hd.size or hd.bonus):
		dstr = "{}d{}".format(hd.number, hd.size)
		print(dstr)
		d = hd.size
		for i in range(1, hd.number+1):
			full = hd_first_is_full == 1 and i == 1
			dstr = "r d{}".format(d)
			if not full:
				if method== NPC_GENERATE_HP_EXT_AVG:
					dstr = "r d{}/2".format(d)
			hp = d
			if not full:
				if method == NPC_GENERATE_HP_EXT_AVG:
					hp = d // 2
				elif method == NPC_GENERATE_HP_EXT_RANDOM: 
					hp = toee.game.random_range(1, d)

			if (i % 2 == 0 and i > 1): 
				hp += 1
				dstr += " + 1"
			pts += hp + hd.bonus
			s = "{}: {}={}".format(i, dstr, hp)
			lines.append(s)
			was_hd_natural = 1

	i = 0
	for c in npc.char_classes:
		i += 1
		d = char_class_get_hit_dice(c)
		full = (hd_first_is_full == 2 or (not was_hd_natural and hd_first_is_full)) and i == 1
		dstr = "r d{}".format(d)
		if not full:
			if method== NPC_GENERATE_HP_EXT_AVG:
				dstr = "r d{}/2".format(d)
		hp = d
		if not full:
			if method == NPC_GENERATE_HP_EXT_AVG:
				hp = d // 2
			elif method == NPC_GENERATE_HP_EXT_RANDOM: 
				hp = toee.game.random_range(1, d)

		if (i % 2 == 0 and i > 1): 
			hp += 1
			dstr += " + 1"
		pts += hp
		s = "{}: {}: {}={}".format(i, toee.game.get_mesline('mes\\stat.mes', c), dstr, hp)
		lines.append(s)
	
	npc.obj_set_int(toee.obj_f_hp_pts, pts)
	hp = npc.stat_level_get(toee.stat_hp_current)

	kindstr = "AVG" if method == NPC_GENERATE_HP_EXT_AVG else "RND"
	kindstr_first = " F" if hd_first_is_full else ""
	print("GEN {}{} HP {} (w/o con: {})={} for {}".format(kindstr, kindstr_first, hp, pts, lines, npc))

	return (hp, lines)

def npc_money_set(npc, copper):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(copper, int)
	diff = npc.money_get()
	diff = copper - diff
	npc.money_adj(diff)
	return diff

def npc_spell_ensure(npc, spell_id, stat_class, spell_level, memorize = 0):
	assert isinstance(npc, toee.PyObjHandle)
	print("{}.npc_spell_ensure(spell_num: {} ({}), stat_class: {}, caster_level: {})".format(npc, spell_id, toee.game.get_spell_mesline(spell_id), stat_class, spell_level))
	if (stat_class == toee.domain_special):
		npc.spell_known_add(spell_id, stat_class, spell_level, 1)
		npc.spell_memorized_add(spell_id, stat_class, spell_level, 1)
	else:
		result = npc.spell_known_add(spell_id, stat_class, spell_level)
		if (not result is None):
			if (not result):
				has = next((ss for ss in npc.spells_known if ss.spell_enum == spell_id), None)
				if has:
					print("Spell {}({}) already known!".format(toee.game.get_spell_mesline(spell_id), spell_id))
				else:
					print("Spell {}({}) was not added!".format(toee.game.get_spell_mesline(spell_id), spell_id))
					debug.breakp("npc_spell_ensure")
					return 0
		npc.spell_memorized_add(spell_id, stat_class, spell_level)
	if (memorize):
		npc.spells_pending_to_memorized()
	return 1

def npc_skill_ensure(npc, skill_id, target_skill_value):
	assert isinstance(npc, toee.PyObjHandle)
	value_total = npc.skill_level_get(skill_id)
	ranks = npc.skill_ranks_get(skill_id)
	delta = target_skill_value - value_total
	ranks += delta
	npc.skill_ranks_set(skill_id, ranks)
	return delta

def npc_is_alive(npc, dead_when_negative_hp = 0):
	assert isinstance(npc, toee.PyObjHandle)
	object_flags = npc.object_flags_get()
	if ((object_flags & toee.OF_DESTROYED) or (object_flags & toee.OF_OFF) or (object_flags & toee.OF_DONTDRAW) or (object_flags & toee.OF_INVULNERABLE)):
		#print("destroyed: {}".format(npc))
		return 0
	result = npc.d20_query(toee.Q_Dead)
	if (result): return 0
	result = npc.d20_query(toee.Q_Dying)
	if (result): return 0
	hp = npc.stat_level_get(toee.stat_hp_current)
	if (dead_when_negative_hp and hp < 0):
		return 0
	if (hp <= -10): return 0
	return 1

def npc_is_dead_or_unconscious(npc, dead_when_negative_hp = False):
	assert isinstance(npc, toee.PyObjHandle)
	if npc_is_dead_or_destroyed(npc, dead_when_negative_hp): return 1
	result = npc.d20_query(toee.Q_Unconscious)
	if (result): return 1
	return 0

def npc_is_dead_or_destroyed(npc, dead_when_negative_hp = False):
	assert isinstance(npc, toee.PyObjHandle)
	if (not npc): return 1
	object_flags = npc.object_flags_get()
	if ((object_flags & toee.OF_DESTROYED) or (object_flags & toee.OF_OFF)): return 1
	hp = npc.stat_level_get(toee.stat_hp_current)
	if (dead_when_negative_hp and hp < 0):
		return 1
	if (hp <= -10): return 1
	result = npc.d20_query(toee.Q_Dead)
	if (result): return 1
	result = npc.d20_query(toee.Q_Dying)
	if (result): return 1
	return 0

def npc_hp_current(npc):
	assert isinstance(npc, toee.PyObjHandle)
	hp = npc.stat_level_get(toee.stat_hp_current)
	return hp

def npc_hp_current_percent(npc):
	assert isinstance(npc, toee.PyObjHandle)
	maxhp = npc.stat_level_get(toee.stat_hp_max)
	hp = npc.stat_level_get(toee.stat_hp_current)
	if (maxhp):
		return 100 * hp / maxhp
	return 100

def npc_find_nearest_pc(npc, distance_ft, should_see):
	assert isinstance(npc, toee.PyObjHandle)
	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(npc.location, distance_ft, toee.OLC_NPC | toee.OLC_PC): # todo check why NPC is here
		assert isinstance(obj, toee.PyObjHandle)
		if (should_see):
			if (not npc.can_see(obj)): continue
		obj_dist = npc.distance_to(obj)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist
	return nearest

def npc_find_nearest_pc_prefer_leader(npc, distance_ft = 25, should_see = 1):
	assert isinstance(npc, toee.PyObjHandle)

	if (toee.game.leader and (not should_see or npc.can_see(toee.game.leader)) and npc.distance_to(toee.game.leader) <= distance_ft):
		return toee.game.leader

	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(npc.location, distance_ft, toee.OLC_PC): 
		assert isinstance(obj, toee.PyObjHandle)
		if (should_see):
			if (not npc.can_see(obj)): continue
		obj_dist = npc.distance_to(obj)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist

	return nearest

def npc_find_nearest_npc_by_proto(npc, distance_ft, proto):
	assert isinstance(npc, toee.PyObjHandle)
	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(npc.location, distance_ft, toee.OLC_NPC):
		assert isinstance(obj, toee.PyObjHandle)
		if (not obj.proto == proto): continue
		obj_dist = npc.distance_to(obj)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist
	return nearest

def npc_find_nearest_pc_loc(loc, distance_ft):
	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(loc, distance_ft, toee.OLC_NPC | toee.OLC_PC):
		assert isinstance(obj, toee.PyObjHandle)
		obj_dist = obj.distance_to(loc)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist
	return nearest

def print_npc_vicinity(leader = None):
	if (not leader):
		leader = toee.game.leader
	for npc in toee.game.obj_list_vicinity(leader.location, toee.OLC_NPC):
		print("{}: {}, distance: {} or {}".format(npc, npc.id, npc.distance_to(leader), leader.distance_to(npc)))
	return

def print_distances_at_origin(locx, locy):
	print("Distances locx, locy: {}, {}".format(locx, locy))
	loc = utils_obj.sec2loc(locx, locy)
	for npc in game.obj_list_vicinity(loc, OLC_NPC | OLC_PC):
		dist = npc.distance_to(loc)
		print("{}: distance: {:06.2f} | id: {}".format(npc, dist, npc.id))
	return

def find_npc_by_proto(loc, proto):
	for obj in toee.game.obj_list_vicinity(loc, OLC_NPC):
		assert isinstance(obj, toee.PyObjHandle)
		if (obj.proto == proto): return obj
	return OBJ_HANDLE_NULL

def npc_get_cr(npc):
	assert isinstance(npc, toee.PyObjHandle)
	cr = 0
	if (npc.type == toee.obj_t_npc):
		cr = npc.obj_get_int(toee.obj_f_npc_challenge_rating)
	level_cr = npc.stat_level_get(toee.stat_level)
	if level_cr:
		if (cr < 0): cr = 0
		result = cr + level_cr
	else:
		if cr == -1:
			result = 0.5
		elif cr == -2:
			result = 0.3
		else:
			result = cr

	return result

def npc_get_cr_exp(pc, cr):
	pc_cr = pc.stat_level_get(toee.stat_level)
	if (pc_cr <= 3):
		if (cr == 1): return 300
		if (cr == 2): return 600
		if (cr == 3): return 900
		if (cr == 4): return 1350
		if (cr == 5): return 1800
		if (cr == 6): return 2700
		if (cr == 7): return 3600
		if (cr == 8): return 5400
		if (cr == 9): return 7200
	return 0

def find_pc_closest_to_origin(loc):
	f = None
	fdist = 0.0
	for obj in toee.game.party:
		assert isinstance(obj, toee.PyObjHandle)
		if (f is None): 
			f = obj
			fdist = obj.distance_to(loc)
			continue
		dist = obj.distance_to(loc)
		if (dist < fdist):
			f = obj
			fdist = dist
	return f, fdist

def pc_travel_time_calc_hours(miles):
	assert isinstance(miles, int)
	# see PH 162, Table: Movement and Distance

	min_speed = None
	for pc in toee.game.party:
		if (not npc_is_alive(pc)): continue
		speed = pc.stat_level_get(toee.stat_movement_speed)
		if (min_speed is None): min_speed = speed
		elif(min_speed > speed): min_speed = speed
	
	if (min_speed is None): 
		print("pc_travel_time_calc_hours => None")
		return

	print("min_speed raw: {}".format(min_speed))
	if (min_speed < 15): min_speed = 15
	elif (min_speed > 40): min_speed = 40
	print("min_speed: {}".format(min_speed))

	minute_speed = min_speed * 10
	hour_speed = minute_speed * 60
	if (min_speed <= 15): hour_speed = 1.5
	elif (min_speed < 20): hour_speed = 2
	elif (min_speed <= 30): hour_speed = 3
	else: hour_speed = 4

	#len_feet = miles * 5280.00
	#result = len_feet / hour_speed
	result = miles / hour_speed
	print("minute_speed: {}, hour_speed: {}, result(hours): {}".format(minute_speed, hour_speed, result))
	return result

def travel_hours_to_day_hours(travel_hours):
	assert isinstance(travel_hours, float)
	max_traveling_time_per_day_in_hours = 8
	days = (int)(travel_hours / max_traveling_time_per_day_in_hours)
	leftover = travel_hours - days * max_traveling_time_per_day_in_hours
	result = days * 24 + leftover
	print("travel_hours: {}, days: {}, leftover: {}, result: {}".format(travel_hours, days, leftover, result))
	return result

def pc_turn_all(rotation):
	for pc in toee.game.party:
		pc.rotation = rotation
	return

def pc_award_experience_all(xp_awarded_each):
	for pc in toee.game.party:
		pc.award_experience(xp_awarded_each)
	return

def pc_award_experience_party(xp_awarded_party):
	count = len(toee.game.party)
	for pc in toee.game.party:
		pc.award_experience(xp_awarded_party // count)
	return

def pc_award_experience_ensure(target_xp):
	for pc in toee.game.party:
		curr_xp = pc.obj_get_int(toee.obj_f_critter_experience)
		delta_xp = target_xp - curr_xp
		if delta_xp > 0:
			pc.award_experience(delta_xp)
	return

def npc_kill_foes():
	# import utils_npc
	# utils_npc.npc_kill_foes()
	# placeholder
	killer = toee.game.leader
	for npc in toee.game.obj_list_vicinity(killer.location, toee.OLC_NPC):
		print("Check {}".format(npc))
		if (npc.type == toee.obj_t_pc): continue
		if (not npc.is_active_combatant(killer)): 
			print("skip, is not is_active_combatant")
			continue
		if (npc.allegiance_shared(toee.game.leader)): 
			print("skip, allegiance_shared")
			continue
		npcleader = npc.leader_get()
		if (npcleader and (npcleader.type == toee.obj_t_pc)): 
			print("skip, leader is pc")
			continue
		#if (npc.reaction_get(killer) > 0): 
		#	print("skip, reaction is >0")
		#	continue
		if (npc.is_friendly(killer)): 
			print("skip, is friendly")
			continue
		if (npc.object_flags_get() & toee.OF_DONTDRAW): 
			print("skip, OF_DONTDRAW")
			continue

		print("killing: {}".format(npc))
		npc.critter_kill_by_effect(killer)
	return

def npc_get_wears(npc):
	assert isinstance(npc, toee.PyObjHandle)
	result = dict()
	result["item_wear_helmet"] = npc.item_worn_at(toee.item_wear_helmet)
	result["item_wear_necklace"] = npc.item_worn_at(toee.item_wear_necklace)
	result["item_wear_gloves"] = npc.item_worn_at(toee.item_wear_gloves)
	result["item_wear_weapon_primary"] = npc.item_worn_at(toee.item_wear_weapon_primary)
	result["item_wear_weapon_secondary"] = npc.item_worn_at(toee.item_wear_weapon_secondary)
	result["item_wear_armor"] = npc.item_worn_at(toee.item_wear_armor)
	result["item_wear_ring_primary"] = npc.item_worn_at(toee.item_wear_ring_primary)
	result["item_wear_ring_secondary"] = npc.item_worn_at(toee.item_wear_ring_secondary)
	result["item_wear_boots"] = npc.item_worn_at(toee.item_wear_boots)
	result["item_wear_ammo"] = npc.item_worn_at(toee.item_wear_ammo)
	result["item_wear_cloak"] = npc.item_worn_at(toee.item_wear_cloak)
	result["item_wear_shield"] = npc.item_worn_at(toee.item_wear_shield)
	result["item_wear_robes"] = npc.item_worn_at(toee.item_wear_robes)
	result["item_wear_bracers"] = npc.item_worn_at(toee.item_wear_bracers)
	result["item_wear_bardic_item"] = npc.item_worn_at(toee.item_wear_bardic_item)
	result["item_wear_lockpicks"] = npc.item_worn_at(toee.item_wear_lockpicks)
	return result

def npc_print_wears(dic):
	assert isinstance(dic, dict)
	for key, value in dic.iteritems():
		if (value):
			assert isinstance(value, toee.PyObjHandle)
			print("{} = {}, proto: {}".format(key, value, value.proto))
	return

def npc_unexploit(npc):
	assert isinstance(npc, toee.PyObjHandle)
	npc.critter_flag_set(toee.OCF_EXPERIENCE_AWARDED)
	items = utils_item.items_get(npc, 0)
	for item in items:
		assert isinstance(item, toee.PyObjHandle)
		item.item_flag_set(toee.OIF_NO_LOOT)
	return npc

def skill_roll2(attachee, triggerer, dc, skill_num, text):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	assert isinstance(dc, int)
	assert isinstance(skill_num, int)
	assert isinstance(text, str)

	bon_list = tpdp.BonusList()
	skill_value = tpdp.dispatch_skill(triggerer, skill_num, bon_list, toee.OBJ_HANDLE_NULL, 1)
	dice = toee.dice_new("1d20")
	roll_result = dice.roll()
	success = skill_value + roll_result >= dc
	hist_id = tpdp.create_history_dc_roll(triggerer, dc, dice, roll_result, text, bon_list)
	toee.game.create_history_from_id(hist_id)

	return success

def skill_roll(attachee, triggerer, dc, ayup, nope, skill_num, text):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	assert isinstance(dc, int)
	assert isinstance(ayup, int)
	assert isinstance(nope, int)
	assert isinstance(skill_num, int)
	assert isinstance(text, str)

	success = skill_roll2(attachee, triggerer, dc, skill_num, text)

	if success:
		triggerer.begin_dialog( attachee, ayup )
	else:
		triggerer.begin_dialog( attachee, nope )
	return success

def intim_roll(attachee, triggerer, dc, ayup, nope, text = None):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	assert isinstance(dc, int)
	assert isinstance(ayup, int)
	assert isinstance(nope, int)
	print("intim_roll")
	if (text is None): text = "Intimidate"
	return skill_roll(attachee, triggerer, dc, ayup, nope, toee.skill_intimidate, text)

def bluff_roll(attachee, triggerer, dc, ayup, nope, text = None):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	assert isinstance(dc, int)
	assert isinstance(ayup, int)
	assert isinstance(nope, int)
	print("bluff_roll")
	if (text is None): text = "Bluff"
	return skill_roll(attachee, triggerer, dc, ayup, nope, toee.skill_bluff, text)

def spot_check(attachee, triggerer, dc, text = None):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	assert isinstance(dc, int)
	assert isinstance(ayup, int)
	assert isinstance(nope, int)
	print("bluff_roll")
	if (text is None): text = "Spot"
	return skill_roll2(attachee, triggerer, dc, toee.skill_spot, text)

def party_add_skill_bonus(skill_num, bonus):
	# import utils_npc
	# utils_npc.party_add_skill_bonus(skill_intimidate, 20)
	# utils_npc.party_add_skill_bonus(skill_diplomacy, 20)
	# utils_npc.party_add_skill_bonus(skill_bluff, 9)
	for pc in toee.game.party:
		if (skill_num == toee.skill_intimidate):
			pc.condition_add("Skill_Intimidate_Bonus", bonus, 0)
		elif (skill_num == toee.skill_diplomacy):
			pc.condition_add("Skill_Diplomacy_Bonus", bonus, 0)
		elif (skill_num == toee.skill_bluff):
			pc.condition_add("Skill_Bluff_Bonus", bonus, 0)
	return

class HairStyle:
	def __init__(self, packed = 0):
		self.packed = packed
		self.race = (packed & 7) # HairStyleRace
		self.gender = (packed >> 3) & 1 # Gender
		self.size = (packed >> 10) & 3 # HairStyleSize;
		self.style = (packed >> 4) & 7
		self.color = (packed >> 7) & 7 # const_toee.hair_color_black, const_toee.hair_color_white
		return

	def pack(self):
		self.packed = (self.race & 7) | ((self.gender) & 1) << 3 | ((self.size) & 3) << 10 | (self.style & 7) << 4| (self.color & 7) << 7
		return self.packed

	def update_npc(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		self.pack()
		npc.obj_set_int(toee.obj_f_critter_hair_style, self.packed)
		return self.packed

	@classmethod
	def from_npc(cls, npc):
		assert isinstance(npc, toee.PyObjHandle)
		return cls(npc.obj_get_int(toee.obj_f_critter_hair_style))

class Waypoint:
	def __init__(self, x = 0, y = 0, rotation = 0, delay = 0, flags = 0, anim1 = 0, anim2 = 0, anim3 = 0, anim4 = 0, anim5 = 0, anim6 = 0, anim7 = 0, anim8 = 0, off_x = 0, off_y = 0):
		self.flags = flags
		self.x = x
		self.y = y
		self.off_x = off_x
		self.off_y = off_y
		self.rotation = rotation
		self.delay = delay
		self.anim1 = anim1
		self.anim2 = anim2
		self.anim3 = anim3
		self.anim4 = anim4
		self.anim5 = anim5
		self.anim6 = anim6
		self.anim7 = anim7
		self.anim8 = anim8
		self.name = None
		return

	def loc(self):
		return utils_obj.sec2loc(self.x, self.y)
	
	@classmethod
	def produce_code_from_list(cls, lst):
		assert isinstance(lst, list)

		lines = list()
		for o in lst:
			if (o is None): continue
			d = None
			if (isinstance(o, dict)): d = o
			else: d = o.__dict__
			print(d)

			#wp = Waypoint(sf(d, "x"), sf(d, "y"), sf(d, "rotation"), sf(d, "delay"), sf(d, "flags"), sf(d, "anim1"), sf(d, "anim2"), sf(d, "anim3"), sf(d, "anim4"), sf(d, "anim5"), sf(d, "anim6"), sf(d, "anim7"), sf(d, "anim8"), sf(d, "off_x"), sf(d, "off_y"))
			wp = Waypoint()
			wp.__dict__ = d

			line = wp.produce_code_create()
			line = "waypoints.append({})".format(line)
			lines.append(line)
			print(line)
		return lines

	def produce_code_create(self):
		line = "utils_npc.Waypoint({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(self.x, self.y, self.rotation, self.delay, self.flags, self.anim1, self.anim2, self.anim3, self.anim4, self.anim5, self.anim6, self.anim7, self.anim8, self.off_x, self.off_y)
		return line

class WaypointFlag:
	FixedRotation = 1
	Delay = 2
	Animate = 4
	#NoLoop = 8

def sf(d, name):
	assert isinstance(d, dict)
	if (name in d): return d[name]
	return 0

def stat_roll(val_min, val_max):
	assert isinstance(val_min, int)
	assert isinstance(val_max, int)
	dice = toee.dice_new("3d6")
	while (1):
		result = dice.roll()
		if (result < val_min or result > val_max): continue
		return result
	return

def stats_roll(val_min, val_max):
	assert isinstance(val_min, int)
	assert isinstance(val_max, int)
	result = list()
	for i in range(0, 6):
		result.append(stat_roll(val_min, val_max))
	return sorted(result, None, None, True)

def stats_random(val_min, val_max):
	assert isinstance(val_min, int)
	assert isinstance(val_max, int)
	result = list()
	for i in range(0, 6):
		result.append(toee.game.random_range(val_min, val_max))
	return result

def stats_sum(stats, sum_stats):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(stats, list)
	assert isinstance(stats, list)
	for i in range(0, len(stats)-1):
		if (i >= len(sum_stats)): break
		stats[i] += sum_stats[i]
		if (stats[i] < 1):
			stats[i] = 1
	return stats

def stats_elite_array():
	result = list()
	result.append(15)
	result.append(14)
	result.append(13)
	result.append(12)
	result.append(10)
	result.append(8)
	return result

def stats_common_array():
	result = list()
	result.append(11)
	result.append(11)
	result.append(11)
	result.append(10)
	result.append(10)
	result.append(10)
	return result

def npc_abilities_set(npc, stats):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(stats, list)
	npc.stat_base_set(toee.stat_strength, stats[0])
	npc.stat_base_set(toee.stat_dexterity, stats[1])
	npc.stat_base_set(toee.stat_constitution, stats[2])
	npc.stat_base_set(toee.stat_intelligence, stats[3])
	npc.stat_base_set(toee.stat_wisdom, stats[4])
	npc.stat_base_set(toee.stat_charisma, stats[5])
	return

def npc_hp_set(npc, hp):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(hp, int)
	adjust = npc.stat_level_get(toee.stat_con_mod) * npc.stat_level_get(toee.stat_level)
	npc.obj_set_int(toee.obj_f_hp_pts, hp - adjust)
	hpc = npc.stat_level_get(toee.stat_hp_current)
	return hpc

def npc_description_set_new(npc, new_name = None, new_name_id = None):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(new_name, str)
	assert isinstance(new_name_id, int)
	if (not npc): return

	if (not new_name_id and not new_name is None):
		new_name_id = toee.game.make_custom_name(new_name)
	if (not new_name_id): return

	npc.obj_set_int(toee.obj_f_critter_description_unknown, new_name_id)
	npc.obj_set_int(const_toee.obj_f_description_correct, new_name_id)
	return new_name_id

def npc_goto(npc, x, y):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(x, int)
	assert isinstance(y, int)
	loc = utils_obj.sec2loc(x, y)
	return npc_goto_loc(npc, loc)

def npc_goto_loc_full(npc, loc, off_x, off_y):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(loc, int)
	x, y = utils_obj.loc2sec(loc)
	print("goto {}, {} ({}, {}) of {}".format(x, y, off_x, off_y, npc))
	if False:
		toee.game.obj_create(2071, loc, off_x, off_y)
	npc.standpoint_set(toee.STANDPOINT_DAY, -1, loc, 0, off_x, off_y)
	npc.standpoint_set(toee.STANDPOINT_NIGHT, -1, loc, 0, off_x, off_y)
	return loc

def npc_goto_loc_fullo(npc, loc):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(loc, tpdp.LocAndOffsets)
	x, y = utils_obj.loc2sec(loc.get_location())
	return npc_goto_loc_full(npc, loc.get_location(), loc.off_x, loc.off_y)

def npc_goto_loc(npc, loc):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(loc, int)
	return npc_goto_loc_full(npc, loc, 0, 0)

def npc_loc_near_random(npc):
	assert isinstance(npc, toee.PyObjHandle)
	x, y = utils_obj.loc2sec(npc.location)
	sign = 1 if toee.game.random_range(0, 1) else -1
	x += toee.game.random_range(1, 2) * sign
	sign = 1 if toee.game.random_range(0, 1) else -1
	y += toee.game.random_range(1, 2) * sign
	return utils_obj.sec2loc(x, y)

def npc_find_path_to_target(npc, target, reach_ft = None):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)
	if (not target or not npc): return

	if ("find_path_to_obj" in dir(npc)):
		loc = npc.find_path_to_obj(target)
		if (not loc is None):
			return loc.get_location(), loc.off_x, loc.off_y
		else: return None
	elif ("find_path_to" in dir(npc)):
		d = dict()
		if (not reach_ft is None):
			d["reach_ft"] = reach_ft
		result_dict = npc.find_path_to(target, d)
		if (result_dict and "location" in result_dict and "off_x" in result_dict and "off_y" in result_dict):
			return long(result_dict["location"]), float(result_dict["off_x"]), float(result_dict["off_y"])

	loc = npc_loc_near_random(target)
	return loc, 0, 0

def npc_hitdice_set(npc, number, size, bonus):
	assert isinstance(npc, toee.PyObjHandle)
	npc.obj_set_idx_int(toee.obj_f_npc_hitdice_idx, 0, number)
	npc.obj_set_idx_int(toee.obj_f_npc_hitdice_idx, 1, size)
	npc.obj_set_idx_int(toee.obj_f_npc_hitdice_idx, 2, bonus)
	return

def get_npcs_range(loc, range = 200, lst = None):
	npcs = list()
	if (lst != None): npcs = lst
	for obj in toee.game.obj_list_range(loc, range, toee.OLC_NPC):
		if (not obj in npcs):
			npcs.append(obj)
	return npcs

def print_npcs(npcs):
	for obj in npcs:
		x, y = utils_obj.loc2sec(obj.location)
		print("{} ({}, {}) {}".format(obj.proto, x, y, obj))
	debug.breakp("print_npcs")
	return

def build_npcs(npcs, options):
	lines = list()
	for npc in npcs:
		assert isinstance(npc, toee.PyObjHandle)
		standpoint = npc.standpoint_get()
		locx, locy= utils_obj.loc2sec(npc.location)
		off_x, off_y = npc.off_x, npc.off_y
		if (standpoint):
			locx, locy, off_x, off_y = standpoint["loc_x"], standpoint["loc_y"], standpoint["off_x"], standpoint["off_y"]
		line = "obj = toee.game.obj_create({}, utils_obj.sec2loc({}, {}), {}, {}) # {}".format(npc.proto, locx, locy, off_x, off_y, npc.description)
		lines.append(line)
		lines.append("if (obj):")
		lines.append("\tobj.rotation = {}".format(npc.rotation))

		object_flags = npc.npc_flags_get()
		if (object_flags):
			i = -1
			for f in const_toee.OBJECT_FLAGS:
				i += 1
				if (object_flags & f):
					lines.append("\tobj.npc_flag_set({})".format(const_toee.OBJECT_FLAGS_NAMES[i]))
			
		waypoints = npc.npc_waypoints_get()
		if (waypoints):
			wplines = Waypoint.produce_code_from_list(waypoints)
			if (wplines):
				lines.append("\twaypoints = list()")
				for l in wplines:
					lines.append("\t" + l)
				if (npc.npc_flags_get() & toee.ONF_WAYPOINTS_DAY):
					lines.append("\tobj.npc_flag_set(toee.ONF_WAYPOINTS_DAY)")
				if (npc.npc_flags_get() & toee.ONF_WAYPOINTS_NIGHT):
					lines.append("\tobj.npc_flag_set(toee.ONF_WAYPOINTS_NIGHT)")
				lines.append("\tobj.npc_waypoints_set(waypoints, 1)")
					
		npc_scripts = npc.scripts
		proto_scripts = None
		proto_obj = toee.game.getproto(npc.proto)
		if (proto_obj): proto_scripts = proto_obj.scripts
		i = -1
		for san in const_toee.san_all:
			i += 1
			npc_script = npc_scripts[san]
			proto_script = proto_scripts[san] if (proto_scripts) else None
			if (npc_script == proto_script): continue
			elif( not npc_script): continue

			lines.append("\tobj.scripts[const_toee.{}] = {}".format(const_toee.san_all_names[i], npc_script))

		utils_item.npc_build_items(npc, lines, "\t".format(1))
		lines.append("")

	file_path = None
	if (options and "save_to" in options):
		file_path = options["save_to"]
	if (file_path):
		txt = "\n".join(lines)
		f = open(file_path, "w")
		f.write(txt)
		f.close()

	debug.breakp("build_npcs")
	return

def npc_get_reach(npc):
	assert isinstance(npc, toee.PyObjHandle)

	if ("get_reaches" in dir(npc)):
		reaches = npc.get_reaches()
		if reaches:
			return reaches[0]

	reach = 5.0
	weapon = npc.item_worn_at(toee.item_wear_weapon_primary)
	if (weapon):
		weapon_type = weapon.get_weapon_type()
		if (weapon_type in [toee.wt_glaive, toee.wt_guisarme, toee.wt_longspear, toee.wt_ranseur, toee.wt_spike_chain]):
			reach += 5

	return reach - 2.0

def npc_get_radius_ft(npc):
	assert isinstance(npc, toee.PyObjHandle)
	if (not npc): return 0.0
	radius_inches = npc.radius
	#print("\t\tnpc_get_radius_ft {} in = {}".format(radius_inches, npc))
	return radius_inches / 12.0

def npc_is_within_reach_ext(npc, target_or_loc, npc_radius, npc_reach):
	assert isinstance(npc, toee.PyObjHandle)
	#print("\t\tnpc_is_within_reach_ext start ({}, {}, {}, {})".format(npc, target_or_loc, npc_radius, npc_reach))

	target_radius = 0.0
	if (not isinstance(target_or_loc, toee.PyObjHandle)):
		target_radius = npc_get_radius_ft(target_or_loc)

	distance_to_target = npc.distance_to(target_or_loc) # obj to targ will be clean (without both radiuses); obj to loc will have obj radius removed from result;
	if (target_radius + npc_reach < distance_to_target): 
		#print("\t\tFalse: target_radius {} + npc_reach {} < distance_to_target {}".format(target_radius, npc_reach, distance_to_target))
		return 0
	#print("\t\tTrue: target_radius {} + npc_reach {} >= distance_to_target {}".format(target_radius, npc_reach, distance_to_target))
	return 1

def npc_is_within_reach(npc, target_or_loc):
	assert isinstance(npc, toee.PyObjHandle)

	npc_radius = npc_get_radius_ft(npc)
	npc_reach = npc_get_reach(npc)

	return npc_is_within_reach_ext(npc, target_or_loc, npc_radius, npc_reach)

def npc_can_melee(npc, target):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)

	if (npc_is_dead_or_unconscious(npc)): return 0

	weapon = npc.item_worn_at(toee.item_wear_weapon_primary)
	if (weapon):
		weapon_type = weapon.get_weapon_type()
		if (weapon_type != toee.obj_t_weapon): return 0
		if (toee.game.is_ranged_weapon(weapon_type)): return 0
	else:
		critter_flags = npc.critter_flags_get()
		if ( not (critter_flags & toee.OCF_MONSTER) and not (toee.feat_improved_unarmed_strike in npc.feats)): return 0

	if (not target): return 1

	if (npc_is_dead_or_unconscious(target)): return 0 # not sure

	npc_radius = npc_get_radius_ft(npc)
	target_radius = npc_get_radius_ft(target)
	npc_reach = npc_get_reach(npc)
	distance_to_target = max(0.0, npc.distance_to(target.location))

	if (target_radius + npc_reach < distance_to_target): return 0

	return 1

def npc_has_miss_chance_ac(npc):
	assert isinstance(npc, toee.PyObjHandle)
	if (npc.d20_query_has_spell_condition(toee.spell_invisibility)):
		return 50
	if (npc.d20_query_has_spell_condition(toee.spell_improved_invisibility)):
		return 50
	if (npc.d20_query_has_spell_condition(toee.spell_blur)):
		return 20
	if (npc.d20_query(toee.Q_Critter_Is_Invisible)):
		return 50
	return 0

def npc_has_miss_chance_hit(npc):
	assert isinstance(npc, toee.PyObjHandle)
	if (npc.d20_query(toee.Q_Critter_Is_Blinded)):
		return 50
	return 0

def npc_to_hit_get(npc, target):
	""" Returns how much NPC should roll to hit the target and reason text. -1 if never."""
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)
	atk = npc.stat_level_get(toee.stat_attack_bonus)
	ac = target.stat_level_get(toee.stat_ac)

	miss_chance = npc_has_miss_chance_ac(target)
	if miss_chance: ac += miss_chance // 10 # to be improved

	if (not miss_chance):
		miss_chance = npc_has_miss_chance_hit(target)
		if miss_chance: ac += miss_chance // 10 # to be improved

	tohit = ac - atk
	return tohit, ""

def npc_get_weapon(npc, primary = 1, should_be_ranged = 0, should_have_ammo = 0):
	assert isinstance(npc, toee.PyObjHandle)
	weapon = npc.item_worn_at(toee.item_wear_weapon_primary) if (primary) else npc.item_worn_at(toee.item_wear_weapon_secondary)
	if not weapon:
		return toee.OBJ_HANDLE_NULL

	if should_be_ranged:
		if toee.game.is_ranged_weapon(weapon.get_weapon_type()):
			if should_have_ammo:
				loaded = False
				if weapon.get_weapon_type() in (toee.wt_heavy_crossbow, toee.wt_light_crossbow):
					loaded = weapon.obj_get_int(toee.obj_f_weapon_flags) & toee.OWF_WEAPON_LOADED
				ammou_q = utils_item.weapon_has_ammo(npc, weapon)
				if ammou_q <= 0 and not loaded:
					weapon = toee.OBJ_HANDLE_NULL
		else:
			weapon = toee.OBJ_HANDLE_NULL

	return weapon


def npc_could_be_attacked(npc, debug_print = 0):
	assert isinstance(npc, toee.PyObjHandle)
	object_flags = npc.object_flags_get()
	if (object_flags & toee.OF_DESTROYED or object_flags & toee.OF_OFF or object_flags & toee.OF_DONTDRAW or object_flags & toee.OF_INVULNERABLE):
		if (debug_print): print("\t\tnpc_could_be_attacked=0 due to flags {}".format(npc))
		return 0
	hp = npc.stat_level_get(toee.stat_hp_current)
	if (hp <= -10):
		if (debug_print): print("\t\tnpc_could_be_attacked=0 due to hp <= -10 {}".format(npc))
		return 0
	if (hp < 0): #if (hp < 0 and npc.type == toee.obj_t_pc):
		if (debug_print): print("\t\tnpc_could_be_attacked=0 due to PC hp < 0 {}".format(npc))
		return 0
	if (debug_print): print("\t\tnpc_could_be_attacked=1 {}".format(npc))
	return 1

def critters_vicinity(npc, include_self = 0):
	assert isinstance(npc, toee.PyObjHandle)
	result = list()
	for obj in toee.game.obj_list_vicinity(npc.location, toee.OLC_CRITTERS):
		assert isinstance(obj, toee.PyObjHandle)
		if (not include_self and obj == npc): continue
		if (npc_is_alive(obj, 1)):
			result.append(obj)
	return result

def npc_anim_goal_push_walk_to_tile(npc, loc):
	return npc.anim_goal_push_walk_to_tile(loc.loc_xy.x, loc.loc_xy.y, loc.off_x, loc.off_y)

def npc_get_alignment_short(npc):
	return get_alignment_short(npc.obj_get_int(toee.obj_f_critter_alignment))

def get_alignment_short(a):
	if (a == toee.ALIGNMENT_NEUTRAL): return "N"
	if (a == toee.ALIGNMENT_LAWFUL): return "L"
	if (a == toee.ALIGNMENT_LAWFUL_NEUTRAL): return "LN"
	if (a == toee.ALIGNMENT_CHAOTIC): return "C"
	if (a == toee.ALIGNMENT_CHAOTIC_NEUTRAL): return "CN"
	if (a == toee.ALIGNMENT_GOOD): return "G"
	if (a == toee.ALIGNMENT_NEUTRAL_GOOD): return "NG"
	if (a == toee.ALIGNMENT_LAWFUL_GOOD): return "LG"
	if (a == toee.ALIGNMENT_CHAOTIC_GOOD): return "CG"
	if (a == toee.ALIGNMENT_EVIL): return "E"
	if (a == toee.ALIGNMENT_NEUTRAL_EVIL): return "NE"
	if (a == toee.ALIGNMENT_LAWFUL_EVIL): return "LE"
	if (a == toee.ALIGNMENT_CHAOTIC_EVIL ): return "CE"
	return None

def npc_can_sense_in_combat(npc, target):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)

	if (target.d20_query(toee.Q_Critter_Is_Invisible) and not target.d20_query(toee.Q_Critter_Can_See_Invisible)):
		return 0
	return 1

def npc_find_nearest_enemy_loc(npc, loc, distance_ft, need_attackable = 1, need_sense = 1, need_los = 0):
	assert isinstance(npc, toee.PyObjHandle)
	nearest = None
	nearest_dist = 10000
	for obj in toee.game.obj_list_range(loc, distance_ft, toee.OLC_NPC | toee.OLC_PC):
		assert isinstance(obj, toee.PyObjHandle)
		if npc == obj: continue
		if need_attackable and not npc_could_be_attacked(obj): continue
		if need_sense and not npc_can_sense_in_combat(npc, obj): continue
		if need_los and not npc.has_los(obj): continue
		if npc.allegiance_shared(obj): continue
		obj_dist = obj.distance_to(loc)
		if (obj_dist < nearest_dist):
			nearest = obj
			nearest_dist = obj_dist
	return nearest

def npc_approach(npc, target):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)
	print("npc_approach {}, {}".format(npc, target))
	loc_tup = npc_find_path_to_target(npc, target)
	if loc_tup:
		npc_goto_loc_full(npc, loc_tup[0], loc_tup[1], loc_tup[2])
		if "anim_goal_push_walk_to_tile" in dir(npc):
			x, y = utils_obj.loc2sec(loc_tup[0])
			npc.anim_goal_push_walk_to_tile(x, y, loc_tup[1], loc_tup[2])
	return loc_tup

def npc_natural_attack(npc, index, attack_type, attack_bonus, number, damage_str):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(index, int)
	assert isinstance(attack_type, int) # const_toee.nwt_claw
	assert isinstance(attack_bonus, int) # monster bab, or minus second attack -5, or when multiattack then -3
	assert isinstance(damage_str, str) # "1d4"

	npc.obj_set_idx_int(toee.obj_f_attack_types_idx, index, attack_type)
	npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, index, attack_bonus) # natural bab: +4
	npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, index, 2) # x
	npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, index, toee.dice_new(damage_str).packed)
	return