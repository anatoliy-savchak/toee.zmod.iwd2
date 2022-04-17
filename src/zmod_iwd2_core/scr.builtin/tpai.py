import toee, tpdp

def get_tactic_def(name):
	assert isinstance(name, str)
	return AiTacticDef()

def parse_tactic(name, middle, spell_code):
	assert isinstance(name, str)
	assert isinstance(middle, str)
	assert isinstance(spell_code, str)
	return (AiTacticDef(), AiTactic())

class AiTacticDef:
	def __init__(self):
		return

	def get_name(self):
		return "name"

	def execute(self, aiTactic):
		assert isinstance(aiTactic, AiTactic)
		return 0

class AiTactic:
	def __init__(self):
		self.performer = toee.PyObjHandle()
		self.target = toee.PyObjHandle()
		self.id = 0
		self.spell_pkt = tpdp.SpellPacket()
		self.d20_spell_data = tpdp.D20SpellData()
		self.data1 = 0
		self.data2 = 0
		return

class PathQuery:
	def __init__(self):
		self.flags = 0
		self.from_loc = tpdp.LocAndOffsets()
		self.to_loc = tpdp.LocAndOffsets()
		self.max_short_path_find_length = 0.0
		self.critter = toee.PyObjHandle()
		self.target_obj = toee.PyObjHandle()
		self.tolerance_radius = 0.0
		return

	def __init__(self, critter):
		assert isinstance(critter, toee.PyObjHandle)
		self.__init__()
		self.critter = critter
		return

	def find_path(self):
		return PathQueryResult()

	def dest_is_clear(self):
		return True

class PathQueryFlags:
	PQF_TO_EXACT = 1
	# todo
	PQF_AVOID_AOOS = 0x1000000

class PathQueryResult:
	def __init__(self):
		self.flags = 0
		self.from_loc = tpdp.LocAndOffsets()
		self.to_loc = tpdp.LocAndOffsets()
		self.mover = toee.PyObjHandle()
		self.node_count = 0
		return

	def is_complete(self):
		return True

	def path_len(self): #ft
		return 1.1

	def get_node(self, index):
		return tpdp.LocAndOffsets()