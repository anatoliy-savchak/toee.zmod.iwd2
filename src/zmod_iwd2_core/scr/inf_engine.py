import utils_storage
import toee

def inf_engine():
	sto = utils_storage.obj_storage_by_id('inf_engine')
	inf_engine = sto.data.get('inf_engine')
	if not inf_engine:
		inf_engine = InfEngine()
		sto.data['inf_engine'] = inf_engine
	return inf_engine

class InfEngine(object):
	def __init__(self):
		self.vars = dict()
		self.texts = list()
		return
