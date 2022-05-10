import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10GOBF0_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptClass
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !TimerActive(18)
			# !See(NearestEnemyOf(Myself),0)
			if not self.iTimerActive(18) \
				 and not self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# FloatMessage(Myself,1677)  // "Targos burn!"
				# StartRandomTimer(18,20,30)
				# Continue()
				self.iFloatMessage("Myself", 1677)
				self.iStartRandomTimer(18, 20, 30)
				pass # continue() - let it pass below
			
			break # while
		return
		
