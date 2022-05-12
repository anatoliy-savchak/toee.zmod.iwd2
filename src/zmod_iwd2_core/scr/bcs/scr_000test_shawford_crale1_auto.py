import toee, debug
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_000TEST_Shawford_Crale1_Auto(inf_scripting.ScriptBase): # 000TEST_Shawford_Crale1
	# AR1201 script_area
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute(cls, self, continuous = False, block_from = None, code_from = None):
		debug.breakp('')
		locus = self.locus_make()
		locus["script_class"] = cls
		locus["continuous"] = continuous
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from >= 1:
				break_ = cls.do_execute_block_01(self, locus, code_from=code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		locus["script_class"] = None
		locus["block"] = None
		locus["continuous"] = None
		return
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"]=1
		d = {"check": None}
		def do_check():
			#nonlocal d
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]

		break_ = 0
		# StartCutSceneMode()
		# CutSceneId("Shawford_Crale")
		# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
		# Wait(5)
		# FloatMessage(Myself,16822)  // "Everyone!  To arms!  To arms!"
		# EndCutSceneMode()
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
			if break_ == 2: return break_
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_01_code_02(self, locus)
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
		locus["code"]=1
		
		# StartCutSceneMode()
		# CutSceneId("Shawford_Crale")
		# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
		# Wait(5)
		
		self.iStartCutSceneMode()
		self.iCutSceneId("'Shawford_Crale'")
		self.iFloatMessage("Myself", 16360)
		self.iWait(time=5, locus=locus)
		return 2 # iWait
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_02(cls, self, continuous = False):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# FloatMessage(Myself,16822)  // "Everyone!  To arms!  To arms!"
		# EndCutSceneMode()
		
		self.iFloatMessage("Myself", 16822)
		self.iEndCutSceneMode()
		return 0
		
