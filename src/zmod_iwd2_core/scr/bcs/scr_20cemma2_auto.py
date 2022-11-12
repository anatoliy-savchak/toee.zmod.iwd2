import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_20cEmma2_Auto(inf_scripting.ScriptBase): # 20cEmma2
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
		
		# CutSceneId("Emma")
		# FadeToColor([0.0],0)
		# Wait(1)
		# HideCreature(Myself,TRUE)
		# FadeFromColor([0.0],0)
		# Wait(1)
		# EndCutSceneMode()
		# DestroySelf()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_01_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_01_code_03(self, locus)
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
		
		# CutSceneId("Emma")
		# FadeToColor([0.0],0)
		# Wait(1)
		
		self.iCutSceneId("'Emma'")
		self.iFadeToColor("[0.0]", 0)
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# HideCreature(Myself,TRUE)
		# FadeFromColor([0.0],0)
		# Wait(1)
		
		self.iHideCreature("Myself", True)
		self.iFadeFromColor("[0.0]", 0)
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# EndCutSceneMode()
		# DestroySelf()
		
		self.iEndCutSceneMode()
		self.iDestroySelf()
		return 0
		
