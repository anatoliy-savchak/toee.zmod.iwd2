import toee
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_000TEST_Shawford_Crale1_Auto(inf_scripting.ScriptBase): # 000TEST_Shawford_Crale1
	# AR1201 script_area
	
	@classmethod
	def do_execute(cls, self, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from >= 1:
				break_ = cls.do_execute_block_01(self, code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# StartCutSceneMode()
			# CutSceneId("Shawford_Crale")
			# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
			# Wait(5)
			# FloatMessage(Myself,16822)  // "Everyone!  To arms!  To arms!"
			# EndCutSceneMode()
			cls.do_execute_block_01_code_01(self)
			cls.do_execute_block_01_code_02(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_01_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# StartCutSceneMode()
		# CutSceneId("Shawford_Crale")
		# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
		# Wait(5)
		
		self.iStartCutSceneMode()
		self.iCutSceneId("'Shawford_Crale'")
		self.iFloatMessage("Myself", 16360)
		self.iWait(5)
		return
		
	@classmethod
	def do_execute_block_01_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# FloatMessage(Myself,16822)  // "Everyone!  To arms!  To arms!"
		# EndCutSceneMode()
		
		self.iFloatMessage("Myself", 16822)
		self.iEndCutSceneMode()
		return
		
