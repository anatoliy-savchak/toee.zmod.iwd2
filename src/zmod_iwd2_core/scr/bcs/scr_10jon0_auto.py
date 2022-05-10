import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10JON0_Auto(inf_scripting.ScriptBase):
	# AR1000 10JON Jon ScriptDefault
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		is_cutscene_execution = self.is_cutscene_mode()
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_02()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_03()
			if break_ and not is_cutscene_execution: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(18)
		# GlobalLT("Reig_Quest","GLOBAL",2)
		# !See([ENEMY.0.GOBLIN],0)
		if not self.iTimerActive(19) \
			 and self.iNearSavedLocation(1):
			# FloatMessage(Myself,1662)  // "Brohn didn't even see it coming..."
			# StartRandomTimer(18,10,15)
			self.iFaceSavedLocation("Myself")
			self.iStartRandomTimer(19, 1, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(19)
		# !NearSavedLocation(1)
		if not self.iTimerActive(19) \
			 and self.iNearSavedLocation(1):
			# ReturnToSavedLocation(0)
			# StartRandomTimer(19,1,5)
			self.iFaceSavedLocation("Myself")
			self.iStartRandomTimer(19, 1, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(19)
		# NearSavedLocation(1)
		if not self.iTimerActive(19) \
			 and self.iNearSavedLocation(1):
			# FaceSavedLocation(Myself)
			# StartRandomTimer(19,1,5)
			self.iFaceSavedLocation("Myself")
			self.iStartRandomTimer(19, 1, 5)
			return True # break further blocks
		return False
		
