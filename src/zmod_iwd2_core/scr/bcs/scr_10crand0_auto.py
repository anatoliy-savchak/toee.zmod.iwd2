import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10CRAND0_Auto(inf_scripting.ScriptBase):
	# AR1000 10CRANDA Crandall ScriptDefault
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !TimerActive(18)
			# Global("Crandall_Leave","GLOBAL",0)
			# !See([ENEMY.0.GOBLIN],0)
			if not self.iTimerActive(18) \
				 and self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0) \
				 and not self.iSee("[ENEMY.0.GOBLIN]", 0):
				# FloatMessage(Myself,1771)  // "Where are the rest of the Targos Guard?"
				# StartRandomTimer(18,10,15)
				# Continue()
				self.iFloatMessage("Myself", 1771)
				self.iStartRandomTimer(18, 10, 15)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",0)
			# ActionListEmpty()
			# NearLocation(Myself,1317,1489,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 0) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1317, 1489, 4):
				# SetStartPos([1317.1489])
				# SetGlobal("ML_0","LOCALS",1)
				# Continue()
				self.iSetStartPos("[1317.1489]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 1)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",0)
			# !Global("Crandall_Leave","GLOBAL",0)
			if self.iGlobal("'ML_0'", "'LOCALS'", 0) \
				 and not self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0):
				# MoveToPoint([1317.1489])
				self.iMoveToPoint("[1317.1489]")
				break
			
			# Global("ML_0","LOCALS",1)
			# ActionListEmpty()
			# NearLocation(Myself,733,1450,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 733, 1450, 4):
				# SetStartPos([733.1450])
				# SetGlobal("ML_0","LOCALS",2)
				# Continue()
				self.iSetStartPos("[733.1450]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 2)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",1)
			# !Global("Crandall_Leave","GLOBAL",0)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1) \
				 and not self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0):
				# MoveToPoint([733.1450])
				self.iMoveToPoint("[733.1450]")
				break
			
			# Global("ML_0","LOCALS",2)
			# ActionListEmpty()
			# NearLocation(Myself,221,1356,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 221, 1356, 4):
				# SetStartPos([221.1356])
				# SetGlobal("ML_0","LOCALS",3)
				# Continue()
				self.iSetStartPos("[221.1356]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 3)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",2)
			# !Global("Crandall_Leave","GLOBAL",0)
			if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
				 and not self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0):
				# MoveToPoint([221.1356])
				self.iMoveToPoint("[221.1356]")
				break
			
			# Global("ML_0","LOCALS",3)
			# ActionListEmpty()
			# NearLocation(Myself,335,819,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 3) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 335, 819, 4):
				# SetStartPos([335.819])
				# SetGlobal("ML_0","LOCALS",4)
				# Continue()
				self.iSetStartPos("[335.819]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 4)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",3)
			# !Global("Crandall_Leave","GLOBAL",0)
			if self.iGlobal("'ML_0'", "'LOCALS'", 3) \
				 and not self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0):
				# MoveToPoint([335.819])
				self.iMoveToPoint("[335.819]")
				break
			
			# Global("ML_0","LOCALS",4)
			# ActionListEmpty()
			# NearLocation(Myself,225,383,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 225, 383, 4):
				# SetStartPos([225.383])
				# SetGlobal("ML_0","LOCALS",5)
				# Continue()
				self.iSetStartPos("[225.383]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 5)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",4)
			# !Global("Crandall_Leave","GLOBAL",0)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4) \
				 and not self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0):
				# MoveToPoint([225.383])
				self.iMoveToPoint("[225.383]")
				break
			
			# Global("ML_0","LOCALS",5)
			# ActionListEmpty()
			# NearLocation(Myself,159,31,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 5) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 159, 31, 4):
				# SetStartPos([159.31])
				# SetGlobal("ML_0","LOCALS",6)
				# Continue()
				self.iSetStartPos("[159.31]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 6)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",5)
			# !Global("Crandall_Leave","GLOBAL",0)
			if self.iGlobal("'ML_0'", "'LOCALS'", 5) \
				 and not self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0):
				# MoveToPoint([159.31])
				self.iMoveToPoint("[159.31]")
				break
			
			# Global("ML_0","LOCALS",6)
			# !Global("Crandall_Leave","GLOBAL",0)
			if self.iGlobal("'ML_0'", "'LOCALS'", 6) \
				 and not self.iGlobal("'Crandall_Leave'", "'GLOBAL'", 0):
				# DestroySelf()
				self.iDestroySelf()
				break
			
			# !TimerActive(20)
			# !NearSavedLocation(3)
			# !Allegiance(Myself,ENEMY)
			if not self.iTimerActive(20) \
				 and not self.iNearSavedLocation(3) \
				 and not self.iAllegiance("Myself", "ENEMY"):
				# ReturnToSavedLocation(0)
				# StartTimer(20,5)
				self.iReturnToSavedLocation(0)
				self.iStartTimer(20, 5)
				break
			
			break # while
		return
		
