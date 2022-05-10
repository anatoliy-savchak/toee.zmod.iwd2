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
		while True:
			# !TimerActive(19)
			# !NearSavedLocation(2)
			if not self.iTimerActive(19) \
				 and not self.iNearSavedLocation(2):
				# ReturnToSavedLocation(0)
				# StartRandomTimer(19,2,5)
				self.iReturnToSavedLocation(0)
				self.iStartRandomTimer(19, 2, 5)
				break
			
			# !TimerActive(19)
			# NearSavedLocation(2)
			if not self.iTimerActive(19) \
				 and self.iNearSavedLocation(2):
				# FaceSavedLocation(Myself)
				# StartRandomTimer(19,2,5)
				self.iFaceSavedLocation("Myself")
				self.iStartRandomTimer(19, 2, 5)
				break
			
			break # while
		return
		
