import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00AMVR_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptDefault
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		is_cutscene_execution = self.is_cutscene_mode()
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_02()
			if break_ and not is_cutscene_execution: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(19)
		# !NearSavedLocation(2)
		if not self.iTimerActive(19) \
			 and self.iNearSavedLocation(2):
			# ReturnToSavedLocation(0)
			# StartRandomTimer(19,2,5)
			self.iFaceSavedLocation("Myself")
			self.iStartRandomTimer(19, 2, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(19)
		# NearSavedLocation(2)
		if not self.iTimerActive(19) \
			 and self.iNearSavedLocation(2):
			# FaceSavedLocation(Myself)
			# StartRandomTimer(19,2,5)
			self.iFaceSavedLocation("Myself")
			self.iStartRandomTimer(19, 2, 5)
			return True # break further blocks
		return False
		
