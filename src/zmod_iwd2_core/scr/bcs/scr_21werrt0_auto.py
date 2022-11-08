import toee, debug
import inf_scripting
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_21WERRT0_Auto(inf_scripting.ScriptBase): # 21WERRT0
	# AR2100 21WERRAT Wererat_Scripted_Event ScriptSpecial1 (Special1)
	
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
			
			if not block_from or block_from <= 4:
				break_ = cls.do_execute_block_04(self, locus, code_from=code_from if code_from and block_from == 4 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 5:
				break_ = cls.do_execute_block_05(self, locus, code_from=code_from if code_from and block_from == 5 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 6:
				break_ = cls.do_execute_block_06(self, locus, code_from=code_from if code_from and block_from == 6 else None)
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
				# !TimerActive(18)
				# Global("SeePC","LOCALS",1)
				if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
					 and not self.iTimerActive(19) \
					 and self.iGlobal("'SeePC'", "'LOCALS'", 2):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# FloatMessage(Myself,27634)  // "They come!  Seal the pass!"
		# StartTimer(18,5)
		# SetGlobal("SeePC","LOCALS",2)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
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
		
		# FloatMessage(Myself,27634)  // "They come!  Seal the pass!"
		# StartTimer(18,5)
		# SetGlobal("SeePC","LOCALS",2)
		
		self.iFloatMessage("Myself", 27634)
		self.iStartTimer(18, 5)
		self.iSetGlobal("'SeePC'", "'LOCALS'", 2)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# GlobalLT("SeePC","LOCALS",1)
				# See([PC],0)
				if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
					 and not self.iTimerActive(19) \
					 and self.iGlobal("'SeePC'", "'LOCALS'", 2):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("SeePC","LOCALS",1)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_02_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# SetGlobal("SeePC","LOCALS",1)
		
		self.iSetGlobal("'SeePC'", "'LOCALS'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 3
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("ML_0","LOCALS",0)
				# Global("SeePC","LOCALS",2)
				# !TimerActive(19)
				if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
					 and not self.iTimerActive(19) \
					 and self.iGlobal("'SeePC'", "'LOCALS'", 2):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# StartTimer(19,2)
		# CloseDoor("AR2100_Door1")
		# SetGlobal("ML_0","LOCALS",1)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_03_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# StartTimer(19,2)
		# CloseDoor("AR2100_Door1")
		# SetGlobal("ML_0","LOCALS",1)
		
		self.iStartTimer(19, 2)
		self.iCloseDoor("'AR2100_Door1'")
		self.iSetGlobal("'ML_0'", "'LOCALS'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 4
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("ML_0","LOCALS",1)
				# ActionListEmpty()
				# NearLocation(Myself,1375,543,4)
				if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
					 and not self.iTimerActive(19) \
					 and self.iGlobal("'SeePC'", "'LOCALS'", 2):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetStartPos([1375.543])
		# CloseDoor("AR2100_Door1")
		# SetGlobal("ML_0","LOCALS",2)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_04_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetStartPos([1375.543])
		# CloseDoor("AR2100_Door1")
		# SetGlobal("ML_0","LOCALS",2)
		
		self.iSetStartPos("[1375.543]")
		self.iCloseDoor("'AR2100_Door1'")
		self.iSetGlobal("'ML_0'", "'LOCALS'", 2)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 5
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("ML_0","LOCALS",1)
				# Global("SeePC","LOCALS",2)
				if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
					 and not self.iTimerActive(19) \
					 and self.iGlobal("'SeePC'", "'LOCALS'", 2):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MoveToPoint([1375.543])
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_05_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_05_code_02(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# MoveToPoint([1375.543])
		
		self.iMoveToPointPost((?,?), locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 6
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("ML_0","LOCALS",2)
				# !TimerActive(19)
				# Global("SeePC","LOCALS",2)
				if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
					 and not self.iTimerActive(19) \
					 and self.iGlobal("'SeePC'", "'LOCALS'", 2):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CloseDoor("AR2100_Door1")
		# DestroySelf()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_06_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CloseDoor("AR2100_Door1")
		# DestroySelf()
		
		self.iCloseDoor("'AR2100_Door1'")
		self.iDestroySelf()
		return 0
		
