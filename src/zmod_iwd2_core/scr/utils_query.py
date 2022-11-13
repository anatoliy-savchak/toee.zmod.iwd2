import toee
import ctrl_behaviour

class NPCQuery(object):
	def __init__(self, inf, query):
		self.query = query
		self.query_lo = self.query.lower()
		self.inf = inf

		return

	def gen(self):
		if self.query_lo == 'myself':
			yield self.inf._get_ie_object_myself(self.query)
			return

		return