import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00AMVW05_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptDefault
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("RW_00AMVW050","LOCALS",0)
			# !NearSavedLocation(5)
			if self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
				 and not self.iNearSavedLocation(5):
				# SetGlobal("RW_00AMVW050","LOCALS",1)
				# Continue()
				self.iSetGlobal("'RW_00AMVW050'", "'LOCALS'", 1)
				pass # continue() - let it pass below
			
			# !Global("RW_00AMVW050","LOCALS",0)
			# NearSavedLocation(5)
			if not self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
				 and self.iNearSavedLocation(5):
				# SetGlobal("RW_00AMVW050","LOCALS",0)
				# NoAction()
				self.iSetGlobal("'RW_00AMVW050'", "'LOCALS'", 0)
				self.iNoAction()
				break
			
			# !Global("RW_00AMVW050","LOCALS",0)
			# Range([PC],40,LESS_THAN)
			if not self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
				 and self.iRange("[PC]", 40, "LESS_THAN"):
				# MoveToPoint([-2.-2])
				self.iMoveToPoint("[-2.-2]")
				break
			
			# !TimerActive(19)
			# Global("RW_00AMVW050","LOCALS",0)
			# Range([PC],40,LESS_THAN)
			if not self.iTimerActive(19) \
				 and self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
				 and self.iRange("[PC]", 40, "LESS_THAN"):
				# RandomWalk()
				# StartRandomTimer(19,10,15)
				self.iRandomWalk()
				self.iStartRandomTimer(19, 10, 15)
				break
			
			break # while
		return
		
