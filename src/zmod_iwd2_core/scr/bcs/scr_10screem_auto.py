import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10SCREEM_Auto(inf_scripting.ScriptBase):
	# AR1000 10SCREED Screed ScriptDefault
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("ML_0","LOCALS",0)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 0) \
				 and not self.iTimerActive(19):
				# StartTimer(19,10)
				# SetGlobal("ML_0","LOCALS",1)
				self.iStartTimer(19, 10)
				self.iSetGlobal("'ML_0'", "'LOCALS'", 1)
				break
			
			# Global("ML_0","LOCALS",1)
			# ActionListEmpty()
			# NearLocation(Myself,1957,807,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1957, 807, 4):
				# SetStartPos([1957.807])
				# SetGlobal("ML_0","LOCALS",2)
				# Continue()
				self.iSetStartPos("[1957.807]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 2)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1):
				# MoveToPoint([1957.807])
				self.iMoveToPoint("[1957.807]")
				break
			
			# Global("ML_0","LOCALS",2)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
				 and not self.iTimerActive(19):
				# Face(E)
				# SetGlobal("ML_0","LOCALS",3)
				self.iFace("E")
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
			# NearLocation(Myself,2058,785,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 2058, 785, 4):
				# SetStartPos([2058.785])
				# SetGlobal("ML_0","LOCALS",5)
				# Continue()
				self.iSetStartPos("[2058.785]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 5)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4):
				# MoveToPoint([2058.785])
				self.iMoveToPoint("[2058.785]")
				break
			
			# Global("ML_0","LOCALS",5)
			# !TimerActive(19)
			if self.iGlobal("'ML_0'", "'LOCALS'", 5) \
				 and not self.iTimerActive(19):
				# Face(N)
				# SetGlobal("ML_0","LOCALS",6)
				self.iFace("N")
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
		
