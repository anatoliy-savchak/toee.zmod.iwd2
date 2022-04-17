import toee
import tactition
import math
import utils_path

class StrategyMelee(tactition.StrategyBase):
	def get_tactic_classes(self):
		result = list()
		#result.append(NoMoveAndAttack)
		result.append(ApproachSingleNoAOOAndAttack)
		#result.append(ApproachSingleAndAttack)
		
		return result

class ApproachSingleAndAttack(tactition.TacticBase):
	def check_prerequisites(self):
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		if not (self.manager.has_full_action()): 
			self.logger.debug(':: {} False: not has_full_action for {}'.format(type(self).__name__, self.npc))
			return False
		if not (self.manager.can_move()): 
			self.logger.debug(':: {} False: not can_move for {}'.format(type(self).__name__, self.npc))
			return False
		if not (self.manager.can_move_out()): 
			self.logger.debug(':: {} False: not can_move_out for {}'.format(type(self).__name__, self.npc))
			return False

		foes_approach_single_spots = self.manager.get_foes_approach_single_spots()
		if (not foes_approach_single_spots):
			self.logger.debug(':: {} False: no foes_approach_single_spots for {}'.format(type(self).__name__, self.npc))
			return False
		self.logger.debug(':: {} end: True {}'.format(type(self).__name__, self.npc))
		return True

	def do_assess(self):
		result = 0
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		foes_approach_single_spots = self.manager.get_foes_approach_single_spots()
		self.logger.debug(':: {} processing {} items for {}'.format(type(self).__name__, len(foes_approach_single_spots), self.npc))

		result_outcomes = list()
		for obj_id in foes_approach_single_spots:
			obj, spots = foes_approach_single_spots[obj_id]

			for spot in spots:
				outcome = self.create_outcome_from_spot(obj, spot)
				outcome.tac.set_name(type(self).__name__)
				outcome.tac.add_target_obj(obj_id)
				ox, oy = outcome.move_destination.get_overall_offset()
				outcome.tac.add_move_to(ox, oy)
				outcome.tac.add_halt()
				#outcome.tac.add_attack()
				outcome.tac.add_strike()
				outcome.tac.add_stop()

				result_outcomes.append(outcome)

		#result_outcomes = sorted(result_outcomes, key = lambda o: o.move_distance) # order by move_distance asc
		for outcome in result_outcomes:
			self.manager.append_outcome(outcome, self)
			result += 1

		self.logger.debug(':: {} end, added: {} for {}'.format(type(self).__name__, result, self.npc))
		return result

class ApproachSingleNoAOOAndAttack(tactition.TacticBase):
	""" Does not seem to work """
	def check_prerequisites(self):
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		if not (self.manager.has_full_action()): 
			self.logger.debug(':: {} False: not has_full_action for {}'.format(type(self).__name__, self.npc))
			return False
		if not (self.manager.can_move()): 
			self.logger.debug(':: {} False: not can_move for {}'.format(type(self).__name__, self.npc))
			return False
		if not (self.manager.can_move_out()): 
			self.logger.debug(':: {} False: not can_move_out for {}'.format(type(self).__name__, self.npc))
			return False

		foes_approach_single_spots_no_aoo = self.manager.get_foes_approach_single_spots_no_aoo()
		if (not foes_approach_single_spots_no_aoo):
			self.logger.debug(':: {} False: no foes_approach_single_spots_no_aoo for {}'.format(type(self).__name__, self.npc))
			return False
		self.logger.debug(':: {} end: True {}'.format(type(self).__name__, self.npc))
		return True

	def do_assess(self):
		result = 0
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		foes_approach_single_spots_no_aoo = self.manager.get_foes_approach_single_spots_no_aoo()
		self.logger.debug(':: {} processing {} items for {}'.format(type(self).__name__, len(foes_approach_single_spots_no_aoo), self.npc))

		result_outcomes = list()
		for obj_id in foes_approach_single_spots_no_aoo:
			obj, spots = foes_approach_single_spots_no_aoo[obj_id]

			for spot in spots:
				outcome = self.create_outcome_from_spot(obj, spot)
				outcome.tac.set_name(type(self).__name__)
				outcome.tac.add_target_obj(obj_id)
				steps = spot.get('steps')
				if (steps):
					for step in steps:
						outcome.tac.add_moving_to(step)
				outcome.tac.add_move_to(outcome.move_destination)
				outcome.tac.add_halt()
				#outcome.tac.add_attack()
				outcome.tac.add_strike()
				outcome.tac.add_stop()

				result_outcomes.append(outcome)

		#result_outcomes = sorted(result_outcomes, key = lambda o: o.move_distance) # order by move_distance asc
		for outcome in result_outcomes:
			self.manager.append_outcome(outcome, self)
			result += 1

		self.logger.debug(':: {} end, added: {} for {}'.format(type(self).__name__, result, self.npc))
	
class NoMoveAndAttack(tactition.TacticBase):
	def check_prerequisites(self):
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		if not (self.manager.has_standard_action()): 
			self.logger.debug(':: {} False: not has_standard_action for {}'.format(type(self).__name__, self.npc))
			return False
		foes_within_reach = self.manager.get_foes_within_reach()
		if (not foes_within_reach):
			self.logger.debug(':: {} False: no foes_within_reach for {}'.format(type(self).__name__, self.npc))
			return False

		self.logger.debug(':: {} end: True {}'.format(type(self).__name__, self.npc))
		return True

	def do_assess(self):
		result = 0
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		foes_within_reach = self.manager.get_foes_within_reach()
		self.logger.debug(':: {} processing {} items for {}'.format(type(self).__name__, len(foes_within_reach), self.npc))
		for target in foes_within_reach:
			outcome = self.create_outcome()
			outcome.target = target
			outcome.tac.set_name(type(self).__name__)
			outcome.tac.add_target_obj(target.id)
			outcome.tac.add_attack()
			outcome.tac.add_stop()

			self.manager.append_outcome(outcome, self)
			result += 1
		self.logger.debug(':: {} end, added: {} for {}'.format(type(self).__name__, result, self.npc))
		return result

class MoveToSideAndAttack(tactition.TacticBase):
	def check_prerequisites(self):
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		if not (self.manager.has_full_action()): 
			self.logger.debug(':: {} False: not has_full_action for {}'.format(type(self).__name__, self.npc))
			return False
		if not (self.manager.can_move()): 
			self.logger.debug(':: {} False: not can_move for {}'.format(type(self).__name__, self.npc))
			return False
		if not (self.manager.can_move_out()): 
			self.logger.debug(':: {} False: not can_move_out for {}'.format(type(self).__name__, self.npc))
			return False

		foes_within_single_move_radius = self.manager.get_foes_within_single_move_radius()
		if (not foes_within_single_move_radius):
			self.logger.debug(':: {} False: no foes_within_single_move_radius for {}'.format(type(self).__name__, self.npc))
			return False
		self.logger.debug(':: {} end: True {}'.format(type(self).__name__, self.npc))
		return True

	def do_assess(self):
		result = 0
		self.logger.debug(':: {} start for {}'.format(type(self).__name__, self.npc))
		foes_approach_single_spots = self.manager.get_foes_approach_single_spots()
		self.logger.debug(':: {} processing {} items for {}'.format(type(self).__name__, len(foes_approach_single_spots), self.npc))

		##N###
		####1#
		######
		##T32#
		loc_npc = self.npc.location_full
		radius_npc = self.npc.radius / 12
		reach_max, reach_min = self.npc.get_reaches()

		result_outcomes = list()
		for target in foes_within_single_move_radius:
			len_left = self.manager.single_move_left()
			start_angle = round(math.degrees(utils_path.rot_from_locs(loc_target, loc_npc)))
			radius_target = target.radius / 12
			loc_target = target.location_full

			#go down right diagonal spot
			radius_for_spot = radius_npc + radius_target + reach_max - 1 + 3 # so target cannot reach me
			rot = math.radians(start_angle + 45)
			diagonal_spot = loc_target.get_offset_loc(rot, radius_for_spot) # first spot
			start_to_diagonal_spot_len = self.manager.calc_path_len_from_to(loc_npc, diagonal_spot)
			if (start_to_diagonal_spot_len == -1):
				self.logger.debug(':: {} False: no go to diagonal_spot ({}) for {}'.format(type(self).__name__, diagonal_spot, self.npc))
				continue
			len_left -= start_to_diagonal_spot_len
			if (len_left < 0):
				self.logger.debug(':: {} False: no move left to go to diagonal_spot ({}) for {}'.format(type(self).__name__, diagonal_spot, self.npc))
				continue

			# go down
			radius_for_spot = radius_npc + radius_target + reach_max - 1 + 3 # so target cannot reach me
			rot = math.radians(start_angle + 90)
			side_spot = loc_target.get_offset_loc(rot, radius_for_spot) # second spot
			diagonal_spot_to_side_spot_len = self.manager.calc_path_len_from_to(diagonal_spot, side_spot)
			if (diagonal_spot_to_side_spot_len == -1):
				self.logger.debug(':: {} False: no go to side_spot ({}) for {}'.format(type(self).__name__, side_spot, self.npc))
				continue
			len_left -= diagonal_spot_to_side_spot_len
			if (len_left < 0):
				self.logger.debug(':: {} False: no move left to go to side_spot ({}) for {}'.format(type(self).__name__, side_spot, self.npc))
				continue

			# at this point we are almost near target, just move towards it for a fiew feets


		for outcome in result_outcomes:
			self.manager.append_outcome(outcome, self)
			result += 1

		self.logger.debug(':: {} end, added: {} for {}'.format(type(self).__name__, result, self.npc))
		return result
