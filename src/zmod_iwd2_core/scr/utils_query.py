import toee
import ctrl_behaviour
import utils_inf

class NPCQuery(object):
	def __init__(self, inf, query):
		self.query = query
		self.query_lo = self.query.lower()
		self.inf = inf
		self.should_see = 0

		return

	def gen(self):
		if self.query_lo == 'myself':
			yield self.inf._get_ie_object_myself(self.query)
			return
		elif self.query_lo == 'lastmarkedobject':
			iLastMarkedObject = self.inf.script_vars.get('iLastMarkedObject')
			if iLastMarkedObject:
				yield iLastMarkedObject
			return
		elif self.query_lo == "nearestenemyof":
			tups = self.nearest_enemy_of_myself()
			if tups:
				for tup in tups:
					yield tup
		elif self.query_lo == "farthestenemyof":
			tups = self.nearest_enemy_of_myself(reverse = True)
			#print('check for farthestenemyof: {}'.format(tups))
			if tups:
				for tup in tups:
					yield tup
		elif self.query_lo == "nearest":
			tups = self.nearest_of_myself()
			if tups:
				for tup in tups:
					yield tup
		elif self.query_lo == "[enemy.0.orc]":
			tups = self.friends_by_race(race_code='orc')
			if tups:
				for tup in tups:
					yield tup
		else:
			raise Exception("Not implemented NPCQuery: {}!".format(self.query))
		return

	def nearest_enemy_of_myself(self, reverse = False):
		foes_can_sense = self.inf._vars_tactics.get("foes_can_sense")
		foes_can_los = self.inf._vars_tactics.get("foes_can_los")

		foes = foes_can_los if self.should_see else foes_can_los

		#print('foes: {}'.format(foes))
		if not foes:
			return
		result = [(n, None) for n in foes]
		if reverse:
			result.reverse()
		return result

	def nearest_of_myself(self, reverse = False):
		critters_all = self.inf._vars_tactics.get("critters_all")

		npc = self.inf.npc_get()
		if not critters_all:
			return
		result = [(n, None) for n in critters_all if not self.should_see or (npc.can_see(n) or npc.has_loa(n))]
		if reverse:
			result.reverse()
		return result

	def friends_by_race(self, race_code):
		friends = self.inf._vars_tactics.get("friends")
		if not friends:
			return
		race_ = None
		if race_code.lower() == 'orc':
			race_ = toee.race_half_orc
		else:
			race_ = utils_inf.iwd2_race_convert(race_code)
		if not race_:
			return
		result = []
		for npc in friends:
			if npc.obj_get_int(toee.obj_f_critter_race) == race_:
				result.append((npc, None))
		return result
