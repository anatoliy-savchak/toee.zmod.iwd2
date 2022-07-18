import toee, debug
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_00T02T_Auto(inf_scripting.ScriptBase): # 00T02T
	# AR1007 10GOBC Goblin_4 ScriptSpecific (Team Script)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute(cls, self, locus, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from <= 1:
				break_ = cls.do_execute_block_01(self, locus, code_from=code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 2:
				break_ = cls.do_execute_block_02(self, locus, code_from=code_from if code_from and block_from == 2 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 3:
				break_ = cls.do_execute_block_03(self, locus, code_from=code_from if code_from and block_from == 3 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 1
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !Global("TEAM_2","MYAREA",1)
				# Or(2)
				# AttackedBy([GOODCUTOFF],DEFAULT)
				# PickPocketFailed([PC])
				if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
					 and self.iAllegiance("Myself", "ENEMY") \
					 and not self.iCreatureHidden("Myself") \
					 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TEAM_2","MYAREA",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("TEAM_2","MYAREA",1)
		
		self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !IsTeamBitOn(TEAM_2_BIT)
				if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
					 and self.iAllegiance("Myself", "ENEMY") \
					 and not self.iCreatureHidden("Myself") \
					 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetTeamBit(TEAM_2_BIT,TRUE)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_02_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetTeamBit(TEAM_2_BIT,TRUE)
		
		self.iSetTeamBit("TEAM_2_BIT", True)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 3
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !Global("TEAM_2","MYAREA",1)
				# Allegiance(Myself,ENEMY)
				# !CreatureHidden(Myself)
				# See(NearestEnemyOf(Myself),0)
				if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
					 and self.iAllegiance("Myself", "ENEMY") \
					 and not self.iCreatureHidden("Myself") \
					 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TEAM_2","MYAREA",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_03_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("TEAM_2","MYAREA",1)
		
		self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
		return 0
		
