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

def npc_money_set(npc, copper):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(copper, int)
	diff = npc.money_get()
	diff = copper - diff
	npc.money_adj(diff)
	return diff

def npc_spell_ensure(npc, spell_id, stat_class, spell_level, memorize = 0):
	assert isinstance(npc, toee.PyObjHandle)
	print("{}.npc_spell_ensure(spell_id: {}, stat_class: {}, spell_level: {})".format(npc, spell_id, stat_class, spell_level))
	if (stat_class == toee.domain_special):
		npc.spell_known_add(spell_id, stat_class, spell_level, 1)
		npc.spell_memorized_add(spell_id, stat_class, spell_level, 1)
	else:
		npc.spell_known_add(spell_id, stat_class, spell_level)
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
	if ((object_flags & toee.OF_DESTROYED) or (object_flags & toee.OF_OFF)): 
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
	result = npc.d20_query(toee.Q_Unconscious)
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
	for obj in toee.game.obj_list_range(npc.location, distance_ft, toee.OLC_NPC | toee.OLC_PC):
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
	cr = 0
	if (npc.type == toee.obj_t_npc):
		cr = npc.obj_get_int(toee.obj_f_npc_challenge_rating)
	level_cr = npc.stat_level_get(toee.stat_level)
	result = cr + level_cr
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

def npc_kill_foes():
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

	if ("critter_get_reach" in dic(npc)):
		return npc.critter_get_reach()

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
	return radius_inches / 12.0

def npc_is_within_reach_ext(npc, target_or_loc, npc_radius, npc_reach):
	assert isinstance(npc, toee.PyObjHandle)

	target_radius = 0.0
	target_loc = 0

	if (target_or_loc is toee.PyObjHandle):
		assert isinstance(target, toee.PyObjHandle)
		target_loc = target.location
		target_radius = npc_get_radius_ft(target)
	else: 
		target_loc = target_or_loc

	distance_to_target = max(0.0, target_or_loc)
	if (target_radius + npc_reach < distance_to_target): return 0
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