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
		while True:
			# !TimerActive(18)
			# GlobalLT("Reig_Quest","GLOBAL",2)
			# !See([ENEMY.0.GOBLIN],0)
			if not self.iTimerActive(18) \
				 and self.iGlobalLT("'Reig_Quest'", "'GLOBAL'", 2) \
				 and not self.iSee("[ENEMY.0.GOBLIN]", 0):
				# FloatMessage(Myself,1662)  // "Brohn didn't even see it coming..."
				# StartRandomTimer(18,10,15)
				self.iFloatMessage("Myself", 1662)
				self.iStartRandomTimer(18, 10, 15)
				break
			
			# !TimerActive(19)
			# !NearSavedLocation(1)
			if not self.iTimerActive(19) \
				 and not self.iNearSavedLocation(1):
				# ReturnToSavedLocation(0)
				# StartRandomTimer(19,1,5)
				self.iReturnToSavedLocation(0)
				self.iStartRandomTimer(19, 1, 5)
				break
			
			# !TimerActive(19)
			# NearSavedLocation(1)
			if not self.iTimerActive(19) \
				 and self.iNearSavedLocation(1):
				# FaceSavedLocation(Myself)
				# StartRandomTimer(19,1,5)
				self.iFaceSavedLocation("Myself")
				self.iStartRandomTimer(19, 1, 5)
				break
			
			break # while
		return
		
