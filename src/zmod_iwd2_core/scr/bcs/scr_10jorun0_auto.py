import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10JORUN0_Auto(inf_scripting.ScriptBase):
	# AR1000 10JORUN Jorun ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !TimerActive(18)
			# Global("Dock_Goblin_Quest","GLOBAL",0)
			if not self.iTimerActive(18) \
				 and self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0):
				# FloatMessage(Myself,1670)  // "Damn fool goblins, thinkin' to torch me boat..."
				# StartTimer(18,5)
				# Continue()
				self.iFloatMessage("Myself", 1670)
				self.iStartTimer(18, 5)
				pass # continue() - let it pass below
			
			# !Global("JORUN_FLOAT","LOCALS",0)
			# NearSavedLocation(1)
			if not self.iGlobal("'JORUN_FLOAT'", "'LOCALS'", 0) \
				 and self.iNearSavedLocation(1):
				# SetGlobal("JORUN_FLOAT","LOCALS",0)
				# Face(W)
				self.iSetGlobal("'JORUN_FLOAT'", "'LOCALS'", 0)
				self.iFace("W")
				break
			
			# !Global("JORUN_FLOAT","LOCALS",0)
			if not self.iGlobal("'JORUN_FLOAT'", "'LOCALS'", 0):
				# SetGlobal("JORUN_FLOAT","LOCALS",0)
				# Continue()
				self.iSetGlobal("'JORUN_FLOAT'", "'LOCALS'", 0)
				pass # continue() - let it pass below
			
			break # while
		return
		
