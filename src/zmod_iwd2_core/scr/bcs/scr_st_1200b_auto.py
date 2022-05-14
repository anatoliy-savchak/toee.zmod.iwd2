import toee, debug
import inf_scripting
#### IMPORTS ####
from bcs import scr_lua1200b
#### END IMPORTS ####

#### BCS ####
class Script_ST_1200b_Auto(inf_scripting.ScriptBase): # ST_1200b
	# None
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute(cls, self, locus, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from <= 1:
				break_ = cls.do_execute_block_01(self, locus, code_from=code_from if code_from and block_from == 1 else None)
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
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId(Myself)
		# StartCutSceneMode()
		# ClearAllActions()
		# MultiPlayerSync()
		# ClearActions(Player1)
		# ClearActions(Player2)
		# ClearActions(Player3)
		# ClearActions(Player4)
		# ClearActions(Player5)
		# ClearActions(Player6)
		# MultiPlayerSync()
		# SetGlobal("SWIFT_THOMAS_JUMP","GLOBAL",1)
		# Wait(1)
		# FadeToColor([0.0],0)
		# Wait(1)
		# MultiPlayerSync()
		# SetGlobal("AR1200_RESET_CUTSCENE","GLOBAL",1)
		# StopJoinRequests()
		# SetGlobal("RJ_AR1200","GLOBAL",1)
		# MultiPlayerSync()
		# StartCutScene("LUA1200b")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_01_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_01_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_01_code_04(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# CutSceneId(Myself)
		# StartCutSceneMode()
		# ClearAllActions()
		# MultiPlayerSync()
		# ClearActions(Player1)
		# ClearActions(Player2)
		# ClearActions(Player3)
		# ClearActions(Player4)
		# ClearActions(Player5)
		# ClearActions(Player6)
		# MultiPlayerSync()
		# SetGlobal("SWIFT_THOMAS_JUMP","GLOBAL",1)
		# Wait(1)
		
		self.iCutSceneId("Myself")
		self.iStartCutSceneMode()
		self.iClearAllActions()
		self.iMultiPlayerSync()
		self.iClearActions("Player1")
		self.iClearActions("Player2")
		self.iClearActions("Player3")
		self.iClearActions("Player4")
		self.iClearActions("Player5")
		self.iClearActions("Player6")
		self.iMultiPlayerSync()
		self.iSetGlobal("'SWIFT_THOMAS_JUMP'", "'GLOBAL'", 1)
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FadeToColor([0.0],0)
		# Wait(1)
		
		self.iFadeToColor("[0.0]", 0)
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# MultiPlayerSync()
		# SetGlobal("AR1200_RESET_CUTSCENE","GLOBAL",1)
		# StopJoinRequests()
		# SetGlobal("RJ_AR1200","GLOBAL",1)
		# MultiPlayerSync()
		# StartCutScene("LUA1200b")
		
		self.iMultiPlayerSync()
		self.iSetGlobal("'AR1200_RESET_CUTSCENE'", "'GLOBAL'", 1)
		self.iStopJoinRequests()
		self.iSetGlobal("'RJ_AR1200'", "'GLOBAL'", 1)
		self.iMultiPlayerSync()
		self.iStartCutScene(scr_lua1200b.Script_LUA1200b, locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		
		return 0
		
