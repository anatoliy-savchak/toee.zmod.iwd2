import math
import logging

import toee
import tpai
import tpdp
import tpactions

import utils_tactics
import utils_npc
import utils_path

class TacticBase(object):
	"""Class to assess outcome"""
	def __init__(self, npc, manager):
		assert isinstance(manager, TacticManager)
		assert isinstance(npc, toee.PyObjHandle)
		self.logger = logging.getLogger()
		self.npc = npc
		self.manager = manager
		return

	def assess(self):
		"""The func should assess situation and produce output into manager.outcomes """
		result = 0
		possible = self.check_prerequisites()
		if (not possible):
			outcome = self.create_outcome()
			outcome.possible = False
			self.manager.append_outcome(outcome, self)
		else:
			result = self.do_assess()
		return result

	def check_prerequisites(self):
		return

	def get_tactic_name(self):
		return type(self).__name__

	def do_assess(self):
		return 0 # number of successful outcomes

	def create_outcome(self):
		outcome = TacticOutcome()
		outcome.possible = True
		outcome.tactic_name = self.get_tactic_name()
		outcome.npc = self.npc
		return outcome

	def create_outcome_from_spot(self, target, spot):
		outcome = self.create_outcome()
		outcome.target = target
		outcome.move_destination = spot["dest_loc"]
		outcome.move_distance = spot["path_len"]
		return outcome

class TacticOutcome(object):
	"""Class to store outcome"""
	def __init__(self):
		self.possible = 0 # is tactic even possible
		self.tactic_name = "" # tactic name
		self.npc = toee.OBJ_HANDLE_NULL # aggressor
		self.target = toee.OBJ_HANDLE_NULL # in regards to
		self.move_destination = None
		self.move_distance = 0
		self.tac = utils_tactics.TacticsHelper('')
		self.impossible_reason0 = "" # first reason why not possible
		self.affected_enemy_count = 0 # how many enemies would be affected
		self.deal_damage_to_enemies = 0 # how much possible damage could be done
		self.deal_damage_to_allies = 0 # how much possible damage could be done to friends
		self.deal_damage_to_self = 0 # how much possible damage could be done to self
		self.receive_damage_afterwards = 0 # how much possible damage could be done to you, after the tactic
		self.deal_damage_to_enemies_afterwards = 0 # how much possible damage could be done to enemies, after the tactic; e.g. flank
		return

class TacticManager(object):
	"""Class to store cache, calculate possibilities, etc"""
	def __init__(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		self.logger = logging.getLogger()
		self.npc = npc
		self.outcomes = list()
		self.foes = None
		self.foes_approach_single_spots = None
		self.foes_could_be_attacked = None
		self.foes_within_reach = None
		self.tb_status = None
		self.foes_approach_single_spots_no_aoo = None
		self.foes_within_single_move_radius = None
		return

	def assess(self, strategy, appreiser):
		assert isinstance(strategy, StrategyBase)
		assert isinstance(appreiser, AppreiserBase)

		self.logger.debug('start for {}'.format(self.npc))

		tactics_classes = strategy.get_tactic_classes()
		for tactic_class in tactics_classes:
			#self.logger.log(5, 'tactic_class: {}'.format(tactic_class))
			self.logger.debug('tactic_class: {}'.format(tactic_class))
			tactic = tactic_class(self.npc, self)
			assert isinstance(tactic, TacticBase)
			added = tactic.assess()
			if (added and appreiser.break_on_success()):
				break

		self.logger.debug('ended for {}'.format(self.npc))

		return appreiser.pick_tactic(self.outcomes)

	def append_outcome(self, outcome, tactic):
		# check if possible first, todo
		self.outcomes.append(outcome)
		return

	def foe_is_within_reach_lacking(self, target):
		reach_max, reach_min = self.npc.get_reaches()
		distance_ft = self.npc.distance_to(target)
		lacking = distance_ft - reach_max
		return int(lacking)

	def foe_is_within_reach_lacking_npc_loc(self, target, npc_loc):
		reach_max, reach_min = self.npc.get_reaches()
		distance_ft = self.npc.distance_to(target)
		lacking = distance_ft - reach_max
		return int(lacking)

	def get_foes_approach_single_spots(self):
		if (self.foes_approach_single_spots is None):
			self.foes_approach_single_spots = dict()
			self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
			foes = self.get_foes_within_single_move_radius()
			if (foes):
				for obj in foes:
					spots = self.calc_reachable_spots_near_target(obj)
					if (not spots):
						self.logger.debug(':: {} False: not calc_reachable_spots_near_target({}) for {}'.format(type(self).__name__, obj, self.npc))
						continue
					self.foes_approach_single_spots[obj.id] = [obj, spots]
			self.logger.debug(':: {} finished foes_approach_single_spots: {} for {}'.format(type(self).__name__, self.foes_approach_single_spots, self.npc))
		return self.foes_approach_single_spots

	def get_foes_approach_single_spots_no_aoo(self):
		if (self.foes_approach_single_spots_no_aoo is None):
			self.foes_approach_single_spots_no_aoo = dict()
			self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
			foes = self.get_foes()
			if (foes):
				for obj in foes:
					spots = self.calc_reachable_spots_near_target_no_aoo(obj)
					if (not spots):
						self.logger.debug(':: {} False: not calc_reachable_spots_near_target({}) for {}'.format(type(self).__name__, obj, self.npc))
						continue
					self.foes_approach_single_spots_no_aoo[obj.id] = [obj, spots]
			self.logger.debug(':: {} finished foes_approach_single_spots_no_aoo: {} for {}'.format(type(self).__name__, self.foes_approach_single_spots_no_aoo, self.npc))
		return self.foes_approach_single_spots_no_aoo

	def get_foes_within_reach(self):
		if (self.foes_within_reach is None):
			self.foes_within_reach = list()
			self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
			foes = self.get_foes()
			if (foes):
				for obj in foes:
					lacking = self.foe_is_within_reach_lacking(obj)
					if (lacking > 0):
						self.logger.debug(':: {} False: not foe_is_within_reach_lacking({}) lacking: {} for {}'.format(type(self).__name__, obj, lacking, self.npc))
						continue
					self.foes_within_reach.append(obj)
			self.logger.debug(':: {} finished get_foes_within_reach: {} for {}'.format(type(self).__name__, self.foes_within_reach, self.npc))
		return self.foes_within_reach

	def get_foes(self):
		if (self.foes is None):
			self.foes = list()
			foes_could_be_attacked = self.get_foes_could_be_attacked()
			self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
			if (foes_could_be_attacked):
				for obj in foes_could_be_attacked:
					if (not self.npc.can_sense(obj)): 
						self.logger.debug(':: {} False: can_sense({}) for {}'.format(type(self).__name__, obj, self.npc))
						continue
					self.foes.append(obj)
			self.logger.debug(':: {} finished foes: {} for {}'.format(type(self).__name__, self.foes, self.npc))
		
		assert isinstance(self.foes, list)
		return self.foes

	def get_foes_within_single_move_radius(self):
		if (self.foes_within_single_move_radius is None):
			self.foes_within_single_move_radius = list()
			foes = self.get_foes()
			self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
			if (foes):
				range = self.single_move_left()
				for obj in foes:
					if (self.npc.distance_to(obj) > range):
						self.logger.debug(':: {} False: npc.distance_to({}) > range({}) for {}'.format(type(self).__name__, obj, range, self.npc))
						continue
					self.foes_within_single_move_radius.append(obj)
			self.logger.debug(':: {} finished foes_within_single_move_radius: {} for {}'.format(type(self).__name__, self.foes, self.npc))
		
		assert isinstance(self.foes, list)
		return self.foes

	def get_foes_could_be_attacked(self):
		if (self.foes_could_be_attacked is None):
			self.foes_could_be_attacked = list()
			self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
			for obj in toee.game.obj_list_vicinity(self.npc.location, toee.OLC_CRITTERS):
				if obj == self.npc: continue
				if (self.npc.is_friendly(obj)): continue
				if (not utils_npc.npc_could_be_attacked(obj)): 
					self.logger.debug(':: {} False: npc_could_be_attacked({}) for {}'.format(type(self).__name__, obj, self.npc))
					continue
				self.foes_could_be_attacked.append(obj)

			self.logger.debug(':: {} finished foes_could_be_attacked: {} for {}'.format(type(self).__name__, self.foes_could_be_attacked, self.npc))

		return self.foes_could_be_attacked

	def calc_reachable_spots_near_target(self, target):
		assert isinstance(target, toee.PyObjHandle)
		spots = list()
		loc_target = target.location_full
		loc_npc = self.npc.location_full
		self.logger.debug(':: {} start target:{}, loc_target: {} for {}'.format(type(self).__name__, target, loc_target, self.npc))

		radius_npc = self.npc.radius / 12
		radius_target = target.radius / 12
		reach_max, reach_min = self.npc.get_reaches()
		radius_for_spot = radius_npc + radius_target + reach_max - 1 # sometimes it will not work for big radiuses
		start_angle = round(math.degrees(utils_path.rot_from_locs(loc_target, loc_npc)))
		degr = start_angle
		while(degr <= 360 + start_angle):
			degr += 15
			rot = math.radians(degr)
			dest_loc = loc_target.get_offset_loc(rot, radius_for_spot)
			
			self.logger.debug(':: {} path to loc: {}, radius_for_spot: {}'.format(type(self).__name__, dest_loc, radius_for_spot))
			pq = tpai.PathQuery(self.npc)
			pq.to_loc = dest_loc
			pqr = pq.find_path()
			if (not pqr.is_complete()):
				self.logger.debug(':: {} False (degr: {}): not pqr.is_complete for {}'.format(type(self).__name__, degr, self.npc))
				continue
			path_len = pqr.path_len()
			path_len += 2 # until we can pass this PathQuery to actual sequence we cannot be sure that this route will be reused and len will be the same
			single_move_left = self.single_move_left()
			if (path_len > single_move_left):
				self.logger.debug(':: {} False (degr: {}): due to path_len({:.1f}) > single_move_left({:.1f}) for {}'.format(type(self).__name__, degr, path_len, single_move_left, self.npc))
				continue
			spot = {"dest_loc": dest_loc, "path_len": path_len, "degr": degr, "radius_for_spot": radius_for_spot}
			spots.append(spot)
			self.logger.debug(':: {} spot: {} for {}'.format(type(self).__name__, spot, self.npc))

		self.logger.debug(':: {} finished spots for {}'.format(type(self).__name__, self.npc))
		return spots

	def calc_path_len_from_to(self, loc_from, loc_to):
		pq = tpai.PathQuery(self.npc)
		pq.from_loc = loc_from
		pq.to_loc = dest_loc
		pqr = pq.find_path()
		if (not pqr.is_complete()):
			self.logger.debug(':: {} False: not pqr.is_complete for {}'.format(type(self).__name__, self.npc))
			return -1
		path_len = pqr.path_len()
		return path_len

	def calc_reachable_spots_near_target_no_aoo(self, target):
		assert isinstance(target, toee.PyObjHandle)
		spots = list()
		loc_target = target.location_full
		loc_npc = self.npc.location_full
		self.logger.debug(':: {} start target:{}, loc_target: {} for {}'.format(type(self).__name__, target, loc_target, self.npc))

		radius_npc = self.npc.radius / 12
		radius_target = target.radius / 12
		reach_max, reach_min = self.npc.get_reaches()
		radius_for_spot = radius_npc + radius_target + reach_max - 1 # sometimes it will not work for big radiuses
		start_angle = round(math.degrees(utils_path.rot_from_locs(loc_target, loc_npc)))
		degr = start_angle
		degr = degr + 15*5 #temp
		while(degr <= 360 + start_angle):
			degr += 15
			rot = math.radians(degr)
			dest_loc = loc_target.get_offset_loc(rot, radius_for_spot)
			
			self.logger.debug(':: {} path to loc: {}, radius_for_spot: {}'.format(type(self).__name__, dest_loc, radius_for_spot))
			pq = tpai.PathQuery(self.npc)
			pq.flag_set(tpai.PathQueryFlags.PQF_AVOID_AOOS)
			pq.to_loc = dest_loc
			pqr = pq.find_path()
			if (not pqr.is_complete()):
				self.logger.debug(':: {} False (degr: {}): not pqr.is_complete for {}'.format(type(self).__name__, degr, self.npc))
				continue
			path_len = pqr.path_len()
			path_len += 2 # until we can pass this PathQuery to actual sequence we cannot be sure that this route will be reused and len will be the same
			single_move_left = self.single_move_left()
			if (path_len > single_move_left):
				self.logger.debug(':: {} False (degr: {}): due to path_len({:.1f}) > single_move_left({:.1f}) for {}'.format(type(self).__name__, degr, path_len, single_move_left, self.npc))
				continue
			steps = None
			if (pqr.node_count > 1):
				idx = 0
				while (idx < pqr.node_count):
					iloc = pqr.get_node(idx)
					if (idx == pqr.node_count - 1):
						dest_loc = iloc
						break
					if (steps is None): steps = list()
					steps.append(iloc)
					idx += 1

			spot = {"dest_loc": dest_loc, "path_len": path_len, "degr": degr, "radius_for_spot": radius_for_spot, "steps": steps}
			self.logger.debug(':: {} spot: {} for {}'.format(type(self).__name__, spot, self.npc))

		self.logger.debug(':: {} finished spots for {}'.format(type(self).__name__, self.npc))
		return spots

	def get_tb_status(self):
		if (self.tb_status is None):
			self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
			self.tb_status = tpactions.get_cur_seq().tb_status
			self.logger.debug(':: {} tb_status: {} for {}'.format(type(self).__name__, self.tb_status, self.npc))
			if (self.tb_status):
				self.logger.debug(':: {} tb_status(hourglass_state: {}, surplus_move_dist:{}, num_bonus_attacks: {}, flags: {}, attack_mode_code: {}) for {}'.format(type(self).__name__, self.tb_status.hourglass_state, self.tb_status.surplus_move_dist, self.tb_status.num_bonus_attacks, self.tb_status.flags, self.tb_status.attack_mode_code, self.npc))
		return self.tb_status

	def single_move_left(self):
		if (self.get_tb_status()):
			if (self.get_tb_status().hourglass_state == toee.D20ACT_Full_Round_Action or self.get_tb_status().hourglass_state == toee.D20ACT_Move_Action):
				return self.get_tb_status().surplus_move_dist + self.npc.stat_level_get(toee.stat_movement_speed)
		return 0

	def can_move(self):
		# todo: check if not entangled etc
		return True

	def can_move_out(self):
		# todo check if not surrounded
		return True

	def has_move_single(self):
		if (self.get_tb_status()):
			if (self.get_tb_status().hourglass_state == toee.D20ACT_Full_Round_Action or self.get_tb_status().hourglass_state == toee.D20ACT_Move_Action):
				return True
		return False

	def has_full_action(self):
		if (self.get_tb_status()):
			if (self.get_tb_status().hourglass_state == toee.D20ACT_Full_Round_Action):
				return True
		return False

	def has_standard_action(self):
		if (self.get_tb_status()):
			if (self.get_tb_status().hourglass_state == toee.D20ACT_Full_Round_Action or self.get_tb_status().hourglass_state == toee.D20ACT_Standard_Action):
				return True
		return False

class StrategyBase(object):
	"""Class to give tactic list"""
	def __init__(self):
		return

	def get_tactic_classes(self):
		return list()

class AppreiserBase(object):
	"""Class to pick tactic from assesment outcomes"""
	def __init__(self):
		return

	def pick_tactic(self, outcomes):
		for outcome in outcomes:
			assert isinstance(outcome, TacticOutcome)
			if (outcome.possible):
				return outcome
		return None

	def break_on_success(self):
		return True
