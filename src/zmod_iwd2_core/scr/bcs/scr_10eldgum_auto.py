import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10ELDGUM_Auto(inf_scripting.ScriptBase):
	# AR1000 10ELDGUL Eldgull ScriptDefault
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("ML_0","LOCALS",0)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 0) \
				 and not self.iTimerActive(19):
				# StartTimer(19,7)
				# SetGlobal("ML_0","LOCALS",1)
				self.iStartTimer(19, 7)
				self.iSetGlobal("'ML_0'", "'LOCALS'", 1)
				break
			
			# Global("ML_0","LOCALS",1)
			# ActionListEmpty()
			# NearLocation(Myself,2656,861,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 2656, 861, 4):
				# SetStartPos([2656.861])
				# SetGlobal("ML_0","LOCALS",2)
				# Continue()
				self.iSetStartPos("[2656.861]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 2)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1):
				# MoveToPoint([2656.861])
				self.iMoveToPoint("[2656.861]")
				break
			
			# Global("ML_0","LOCALS",2)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
				 and not self.iTimerActive(19):
				# Face(N)
				# SetGlobal("ML_0","LOCALS",3)
				self.iFace("N")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 3)
				break
			
			# Global("ML_0","LOCALS",3)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 3) \
				 and not self.iTimerActive(19):
				# StartTimer(19,10)
				# SetGlobal("ML_0","LOCALS",4)
				self.iStartTimer(19, 10)
				self.iSetGlobal("'ML_0'", "'LOCALS'", 4)
				break
			
			# Global("ML_0","LOCALS",4)
			# ActionListEmpty()
			# NearLocation(Myself,2575,943,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 2575, 943, 4):
				# SetStartPos([2575.943])
				# SetGlobal("ML_0","LOCALS",5)
				# Continue()
				self.iSetStartPos("[2575.943]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 5)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4):
				# MoveToPoint([2575.943])
				self.iMoveToPoint("[2575.943]")
				break
			
			# Global("ML_0","LOCALS",5)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 5) \
				 and not self.iTimerActive(19):
				# Face(S)
				# SetGlobal("ML_0","LOCALS",6)
				self.iFace("S")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 6)
				break
			
			# Global("ML_0","LOCALS",6)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 6) \
				 and not self.iTimerActive(19):
				# StartTimer(19,10)
				# SetGlobal("ML_0","LOCALS",7)
				self.iStartTimer(19, 10)
				self.iSetGlobal("'ML_0'", "'LOCALS'", 7)
				break
			
			# Global("ML_0","LOCALS",7)
			# NearSavedLocation(4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
				 and self.iNearSavedLocation(4):
				# SetGlobal("ML_0","LOCALS",0)
				# SetStartPos([-1.-1])
				# Continue()
				self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
				self.iSetStartPos("[-1.-1]")
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",7)
			# !TimerActive(19)
			# !NearSavedLocation(4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
				 and not self.iTimerActive(19) \
				 and not self.iNearSavedLocation(4):
				# ReturnToSavedLocation(0)
				self.iReturnToSavedLocation(0)
				break
			
			break # while
		return
		
