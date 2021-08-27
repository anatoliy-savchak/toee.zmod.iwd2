import toee, debug

class NPCAbilitiesSetup:
	def __init__(self, score_ability_min = 8, score_ability_max = 14, racial_ability_bonuses = None, ability_minimums = None):
		self.score_ability_min = score_ability_min
		self.score_ability_max = score_ability_max
		self.racial_ability_bonuses = racial_ability_bonuses
		self.ability_rolls = None
		self.ability_minimums = ability_minimums
		return

	@staticmethod
	def stats_roll(val_min, val_max):
		assert isinstance(val_min, int)
		assert isinstance(val_max, int)
		result = list()
		for i in range(0, 6):
			result.append(NPCAbilitiesSetup.stat_roll(val_min, val_max))
		#return sorted(result, None, None, True)
		return result

	@staticmethod
	def stat_roll(val_min, val_max):
		assert isinstance(val_min, int)
		assert isinstance(val_max, int)
		dice = toee.dice_new("1d6")
		while (1):
			rolls = list()
			rolls.append(dice.roll())
			rolls.append(dice.roll())
			rolls.append(dice.roll())
			rolls.append(dice.roll())
			rolls = sorted(rolls, None, None, True)
			result = rolls[0] + rolls[1] + rolls[2]
			print("stat_roll({}, {}): {} = {} + {} + {}".format(val_min, val_max, result, rolls[0], rolls[1], rolls[2]))
			if (result < val_min or result > val_max): continue
			return result
		return

	def generate(self, do_sort = True):
		self.ability_rolls = NPCAbilitiesSetup.stats_roll(self.score_ability_min, self.score_ability_max)
		if (do_sort): self.ability_rolls = sorted(self.ability_rolls, None, None, True)
		return self

	def calc_score(self, ability_index):
		racial_bonus = 0
		if (self.racial_ability_bonuses and len(self.racial_ability_bonuses) >= ability_index): i = self.racial_ability_bonuses[0] 

		ability_minimum = 0
		if (self.ability_minimums and len(self.ability_minimums) >= ability_index): 
			mi = self.ability_minimums[0]
			return min(ability_minimum, racial_bonus + self.ability_rolls[ability_index])

		return max(ability_minimum, racial_bonus + self.ability_rolls[ability_index])

	def npc_setup_random(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.stat_base_set(toee.stat_strength, self.calc_score(0))
		npc.stat_base_set(toee.stat_dexterity, self.calc_score(1))
		npc.stat_base_set(toee.stat_constitution, self.calc_score(2))
		npc.stat_base_set(toee.stat_intelligence, self.calc_score(3))
		npc.stat_base_set(toee.stat_wisdom, self.calc_score(4))
		npc.stat_base_set(toee.stat_charisma, self.calc_score(5))
		return self

	def focus_melee(self):
		srs = self.ability_rolls
		self.ability_rolls = [srs[0], srs[2], srs[1], srs[4], srs[3], srs[5]]
		return self

	def focus_melee_tough(self):
		srs = self.ability_rolls
		self.ability_rolls = [srs[1], srs[2], srs[0], srs[4], srs[3], srs[5]]
		return self

	def focus_ranged(self):
		srs = self.ability_rolls
		self.ability_rolls = [srs[2], srs[0], srs[1], srs[4], srs[3], srs[5]]
		return self

	def focus_cleric(self):
		srs = self.ability_rolls
		self.ability_rolls = [srs[4], srs[2], srs[1], srs[0], srs[3], srs[5]]
		return self

	def focus_wizard(self):
		srs = self.ability_rolls
		self.ability_rolls = [srs[2], srs[3], srs[1], srs[5], srs[0], srs[4]]
		return self