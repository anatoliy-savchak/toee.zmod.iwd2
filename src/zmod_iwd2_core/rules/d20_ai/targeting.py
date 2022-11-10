import toee
import d20_ai_utils
import tpai

debug_enabled = 1

MAX_VISIBLE_DISTANCE_FT = 50 #ft
MAX_HEARD_DISTANCE_FT = 25 #ft

# EXPORT find_suitable_target
def find_suitable_target(attacker, aiSearchingTgt):
	assert isinstance(attacker, toee.PyObjHandle)
	assert isinstance(aiSearchingTgt, int)

	if attacker.type == toee.obj_t_npc and not attacker.npc_flags_get() & toee.ONF_KOS:
		return toee.OBJ_HANDLE_NULL

	if debug_enabled >=2: print('find_suitable_target for {}'.format(attacker))
	if aiSearchingTgt: 
		return toee.OBJ_HANDLE_NULL

	#candidates = toee.game.obj_list_range(attacker.location, MAX_VISIBLE_DISTANCE_FT, toee.OLC_CRITTERS)
	candidates = toee.game.obj_list_range(attacker.location, MAX_VISIBLE_DISTANCE_FT, toee.OLC_PC)
	if not candidates or len(candidates) == 0:
		return toee.OBJ_HANDLE_NULL

	pairs = []
	if True:
		for dude in candidates:
			if dude == attacker: continue
			dist = attacker.location_full.distance_to(dude.location_full)
			if dude.is_unconscious():
				dist += 1000.0
			if not (dude in game.party): # added so that party members are prioritized over non-party NPCs (e.g. bystanders or whatever)
				dist += 100.0
			pairs.append((dude, dist))

		pairs.sort(key = lambda p: p[1])

	if debug_enabled >=2: print('find_suit1able_target {} candidates for {}'.format(len(pairs), attacker))

	kos_candidate = toee.OBJ_HANDLE_NULL
	turn_towards = None
	leader = attacker.leader_get()
	for target, dist in pairs:
		assert isinstance(target, toee.PyObjHandle)

		detected = detect(attacker, target)
		if debug_enabled >=2: print('find_suitable_target detected: {} of {} for {}'.format(detected, target, attacker))
		if detected:
			if target.type == toee.obj_t_pc:
				turn_towards = target

			kos = will_kos(attacker, target, aiSearchingTgt)
			if debug_enabled >=2: print('find_suitable_target kos: {} of {} for {}'.format(kos, target, attacker))
			if kos:
				kos_candidate = target
				break

			friendFocus = getFriendsCombatFocus(attacker, target, leader, 1)
			if friendFocus:
				kos_candidate = friendFocus
				break

		deadFriend = getTargetFromDeadFriend(attacker, target)
		if detect(attacker, deadFriend):
			kos_candidate = deadFriend
			break

	if not kos_candidate and turn_towards:
		attacker.turn_towards(turn_towards)

	if debug_enabled >=1 and (debug_enabled >=2 or kos_candidate): print('find_suitable_target kos_candidate: {} for {}'.format(kos_candidate, attacker))
	return kos_candidate

# Common check during find_suitable_target
def detect(attacker, target):
	assert isinstance(attacker, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)

	if not target: 
		return False

	distance = attacker.distance_to(target)
	target_unconcealed = 0 if target.critter_flags_get() & (toee.OCF_IS_CONCEALED | toee.OCF_MOVING_SILENTLY) else 1
	
	able_to_visible_detect = not ((attacker.critter_flags_get() & toee.OCF_SLEEPING) or attacker.d20_query(toee.Q_Critter_Is_Blinded))
	if able_to_visible_detect and distance <= MAX_VISIBLE_DISTANCE_FT:
		loa = attacker.has_loa(target)
		if debug_enabled >=1 and (debug_enabled >=2 or loa): print('detect has_loa: {} of {} for {}'.format(loa, target, attacker))

		if loa:
			blindsight_range = None
			if attacker.d20_query(toee.Q_Critter_Is_Invisible):
				blindsight_range = attacker.d20_query("Blindsight Range") if blindsight_range is None else blindsight_range
				if not target.d20_query(toee.Q_Critter_Can_See_Invisible) and distance > blindsight_range:
					return 0
			if target.is_category_type(toee.mc_type_undead):
				if attacker.d20_query_with_data(toee.Q_Critter_Has_Spell_Active, toee.spell_invisibility_to_undead):
					return 0
			if target.is_category_type(toee.mc_type_animal):
				if attacker.d20_query_with_data(toee.Q_Critter_Has_Spell_Active, toee.spell_invisibility_to_animals):
					return 0
			
			if not target_unconcealed:
				# Hiding
				blindsight_range = attacker.d20_query("Blindsight Range") if blindsight_range is None else blindsight_range
				if distance <= blindsight_range:
					# Blindsight can see Hidden
					return 1
				
				# otherwise it should be handled via spot check in can_see
				return attacker.can_see(target)
			else:
				return 1

	able_to_heard_detect = not (attacker.d20_query(toee.Q_Critter_Is_Deafened))
	if able_to_heard_detect and distance <= MAX_HEARD_DISTANCE_FT:
		heard = attacker.can_hear(target, target_unconcealed)
		if heard:
			return 1
	return 0

def will_kos(attacker, target, aiSearchingTgt):
	assert isinstance(attacker, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)

	if not consider_target(attacker, target, aiSearchingTgt):
		return 0

	if not attacker.object_script_execute(target, toee.san_will_kos):
		if debug_enabled >= 2: print('will_kos no san_will_kos: {} for {}'.format(target, attacker))
		return 0

	aaifs = d20_ai_utils.AiFightStatus(attacker)
	if aaifs.status == toee.AIFS_SURRENDERED and aaifs.target == target:
		return 0

	if target.type == toee.obj_t_npc and not target in toee.game.party:
		# TODO!
		# NPC vs NPC not supported. Revise when it should.
		return 0
		taifs = d20_ai_utils.AiFightStatus(target)
		if taifs.status != toee.AIFS_FIGHTING or taifs.target:
			return 0

		if attacker.allegiance_strength(taifs.target) == 0:
			return 0

		leader = attacker.leader_get()
		if cannot_hate(attacker, target, leader):
			return 0

	return 1

def missing_stub(msg):
	print msg
	return 0

def cannot_hate(obj, tgt, leader):
	if not obj:
		return 0
	spell_flags = obj.obj_get_int(toee.obj_f_spell_flags)
	if (spell_flags & 0x8000000) and leader:
		return 0
	if not tgt or not tgt.is_critter():
		return 0
	if leader and tgt.leader_get() == leader:
		return 4
	if (obj.allegiance_shared(tgt)):
		return 3
	if obj.d20_query_has_condition("sp-Sanctuary Save Failed") == 0 or tgt.d20_query_has_condition("sp-Sanctuary") == 0:
		return 0
	tgt_sanctuary_handle = tgt.d20_query_get_obj(toee.Q_Critter_Has_Condition, tpdp.hash("sp-Sanctuary"))
	sanctuary_handle = obj.d20_query_get_obj(toee.Q_Critter_Has_Condition, tpdp.hash("sp-Sanctuary Save Failed"))
	if sanctuary_handle == tgt_sanctuary_handle:
		return 5
	return 0

# aiSearchingTgt is used to avoid infinite looping since
# consider_target calls will_kos which calls consider_target.
# In the C(++), this is a global variable. Trying to avoid that.

# EXPORT consider_target
def consider_target(attacker, target, aiSearchingTgt=False):
	assert isinstance(attacker, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)

	if not target or attacker == target : return 0
	# if aiSearchingTgt == False:
	# 	debug_print("consider_target: " + str(attacker) + " considering " + str(target))

	ignore_flags = toee.OF_INVULNERABLE | toee.OF_DONTDRAW | toee.OF_OFF | toee.OF_DESTROYED
	target_flags = target.object_flags_get()

	if target_flags & ignore_flags: 
		if debug_enabled >= 2: print("consider_target: ignore_flags of {} by {}".format(attacker, target))
		return 0

	if not target.is_critter():
		if d20_ai_utils.isBusted(target): 
			if debug_enabled >= 2: print("consider_target: busted of {} by {}".format(attacker, target))
			return 0
		return 1

	if target.is_dead_or_destroyed():
		return 0

	a_leader = attacker.leader_get()
	if target == a_leader: 
		return 0

	if d20_ai_utils.aiListFind(attacker, target, toee.AI_LIST_ALLY):
		if debug_enabled >= 2: print("consider_target: ai list ally of {} by {}".format(attacker, target))
		return 0

	if target.is_unconscious():
		if target.critter_flags_get() & toee.OCF_NON_LETHAL_COMBAT: 
			return 0
	
	#if target != find_best_target(attacker, aiSearchingTgt): return 0

	if a_leader:
		t_leader = target.leader_get()
		if t_leader and t_leader == a_leader:
			if debug_enabled >= 2: print("consider_target: same leader of {} by {}".format(attacker, target))
			return 0

	distance = target.distance_to(attacker)
	too_far = 125.0
	if distance > too_far:
		if debug_enabled >= 2: print("consider_target: distance distance {} too far ({}) of {} by {}".format(distance, too_far, attacker, target))
		return 0

	if target.is_friendly(attacker): 
		if debug_enabled >= 2: print("consider_target: is friendly of {} by {}".format(attacker, target))
		return 0

	if d20_ai_utils.isCharmedBy(target, attacker):
		return d20_ai_utils.targetIsPcPartyNotDead(target)

	#if a_leader:
	#	if a_leader.distance_to(target) > 20:
	#		if attacker.distance_to(target) > 15.0:
	#			debug_print("consider tgt: too far from leader")
	#			return 0
	if debug_enabled >= 2: print("consider_target: yes of {} by {}".format(attacker, target))
	return 1

def getFriendsCombatFocus(obj, friend, leader, aiSearchingTgt = False):
	if friend.type != toee.obj_t_npc:
		return toee.OBJ_HANDLE_NULL

	# moved this check here since it's gating anyway; used to be after consider_target
	if obj.allegiance_strength(friend) == 0:
		return toee.OBJ_HANDLE_NULL

	aifs = d20_ai_utils.AiFightStatus(friend)
	tgt = aifs.target
	if not tgt:
		return tgt

	if not aifs.status in [toee.AIFS_FIGHTING, toee.AIFS_FLEEING, toee.AIFS_SURRENDERED]:
		return toee.OBJ_HANDLE_NULL

	if not detect(obj, tgt):
		return toee.OBJ_HANDLE_NULL

	if cannot_hate(obj, tgt, leader):
		return toee.OBJ_HANDLE_NULL

	if not consider_target(obj, tgt, aiSearchingTgt):
		return toee.OBJ_HANDLE_NULL

	# new in Temple+ : check pathfinding short distances (to simulate sensing nearby critters)
	pf_flags = toee.PQF_HAS_CRITTER | toee.PQF_IGNORE_CRITTERS | toee.PQF_800 \
		| toee.PQF_TARGET_OBJ | toee.PQF_ADJUST_RADIUS | toee.PQF_ADJ_RADIUS_REQUIRE_LOS \
		| toee.PQF_DONT_USE_PATHNODES | toee.PQF_A_STAR_TIME_CAPPED | toee.PQF_DOORS_ARE_BLOCKING
	
	# TODO
	missing_stub("tpconfig.alertAiThroughDoors")
	# if tpconfig.alertAiThroughDoors:
	# 	pf_flags |= PQF_DOORS_ARE_BLOCKING

	path_len = obj.can_find_path_to_obj(tgt, pf_flags)
	PATH_LEN_MAX = 40
	if path_len < PATH_LEN_MAX:
		return tgt
	
	return toee.OBJ_HANDLE_NULL

def getTargetFromDeadFriend(obj, friend):
	if not friend:
		return toee.OBJ_HANDLE_NULL

	if not friend.is_dead_or_destroyed(): 
		return toee.OBJ_HANDLE_NULL

	if friend.type != toee.obj_t_npc: 
		return toee.OBJ_HANDLE_NULL

	tgt = friend.obj_get_obj(toee.obj_f_npc_combat_focus)
	if not tgt:
		return toee.OBJ_HANDLE_NULL

	if obj.allegiance_strength(friend) == 0:
		return toee.OBJ_HANDLE_NULL

	if not consider_target(obj, tgt, True):
		return toee.OBJ_HANDLE_NULL
	return tgt

def is_comrade(npc, target):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(target, toee.PyObjHandle)
	npc_leader = npc.leader_get()
	target_leader = target.leader_get()
	return (npc_leader and (npc_leader == target_leader or npc_leader == target)) or (target_leader and (target_leader == npc_leader or target_leader == npc)) or npc.allegiance_shared(target)

def alert_allies(npc, attacker):
	assert isinstance(npc, toee.PyObjHandle)
	assert isinstance(attacker, toee.PyObjHandle)
	if debug_enabled >=2: print('alert_allies {} due to {}'.format(npc, attacker))

	candidates = toee.game.obj_list_range(npc.location, MAX_VISIBLE_DISTANCE_FT, toee.OLC_CRITTERS)
	for obj in candidates:
		if obj.is_dead_or_destroyed(): 
			continue
		is_combatant = obj.is_active_combatant()
		if debug_enabled >=2: print('alert_allies is_combatant: {} of {} by {} due to agitator: {}'.format(is_combatant, obj, npc, attacker))
		if is_combatant:
			continue
		comrade = is_comrade(npc, obj)
		if debug_enabled >=2: print('alert_allies comrade: {} of {} by {} due to agitator: {}'.format(comrade, obj, npc, attacker))
		if not comrade: 
			continue
		kos = will_kos(obj, attacker, 0)
		if debug_enabled >=2: print('alert_allies will_kos: {} of {} by {} due to agitator: {}'.format(kos, obj, npc, attacker))
		if not kos: 
			continue
		if debug_enabled >=1: print('alert_allies of {} by {} due to agitator: {}'.format(obj, npc, attacker))
		attacker.attack(obj)
		
	return toee.SKIP_DEFAULT

def alert_allies2(npc, attacker):
	return alert_allies(npc, attacker)