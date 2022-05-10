import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10BROGA0_Auto(inf_scripting.ScriptBase):
	# AR1000 10BROGAN Brogan ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# NumTimesTalkedTo(0)
			# !Allegiance(Myself,ENEMY)
			# !Dead(Myself)
			# See([PC],0)
			# Range(LastSeenBy(Myself),15,LESS_THAN)
			if self.iNumTimesTalkedTo(0) \
				 and not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iDead("Myself") \
				 and self.iSee("[PC]", 0) \
				 and self.iRange(self.iLastSeenBy("Myself"), 15, "LESS_THAN"):
				# Dialogue(LastMarkedObject)
				self.iDialogue("LastMarkedObject")
				break
			
			# !TimerActive(18)
			# !See([ENEMY.0.GOBLIN],0)
			# Global("Brogan_Leave","GLOBAL",0)
			if not self.iTimerActive(18) \
				 and not self.iSee("[ENEMY.0.GOBLIN]", 0) \
				 and self.iGlobal("'Brogan_Leave'", "'GLOBAL'", 0):
				# FloatMessage(Myself,1666)  // "Hope there's no other goblins about..."
				# StartRandomTimer(18,10,15)
				# Continue()
				self.iFloatMessage("Myself", 1666)
				self.iStartRandomTimer(18, 10, 15)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",0)
			# ActionListEmpty()
			# NearLocation(Myself,1747,524,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 0) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1747, 524, 4):
				# SetStartPos([1747.524])
				# SetGlobal("ML_0","LOCALS",1)
				# Continue()
				self.iSetStartPos("[1747.524]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 1)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",0)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 0) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([1747.524])
				self.iMoveToPoint("[1747.524]")
				break
			
			# Global("ML_0","LOCALS",1)
			# ActionListEmpty()
			# NearLocation(Myself,1530,781,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1530, 781, 4):
				# SetStartPos([1530.781])
				# SetGlobal("ML_0","LOCALS",2)
				# Continue()
				self.iSetStartPos("[1530.781]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 2)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",1)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 1) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([1530.781])
				self.iMoveToPoint("[1530.781]")
				break
			
			# Global("ML_0","LOCALS",2)
			# ActionListEmpty()
			# NearLocation(Myself,1241,940,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1241, 940, 4):
				# SetStartPos([1241.940])
				# SetGlobal("ML_0","LOCALS",3)
				# Continue()
				self.iSetStartPos("[1241.940]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 3)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",2)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 2) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([1241.940])
				self.iMoveToPoint("[1241.940]")
				break
			
			# Global("ML_0","LOCALS",3)
			# ActionListEmpty()
			# NearLocation(Myself,910,1053,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 3) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 910, 1053, 4):
				# SetStartPos([910.1053])
				# SetGlobal("ML_0","LOCALS",4)
				# Continue()
				self.iSetStartPos("[910.1053]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 4)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",3)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 3) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([910.1053])
				self.iMoveToPoint("[910.1053]")
				break
			
			# Global("ML_0","LOCALS",4)
			# ActionListEmpty()
			# NearLocation(Myself,559,884,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 559, 884, 4):
				# SetStartPos([559.884])
				# SetGlobal("ML_0","LOCALS",5)
				# Continue()
				self.iSetStartPos("[559.884]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 5)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",4)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 4) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([559.884])
				self.iMoveToPoint("[559.884]")
				break
			
			# Global("ML_0","LOCALS",5)
			# ActionListEmpty()
			# NearLocation(Myself,315,625,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 5) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 315, 625, 4):
				# SetStartPos([315.625])
				# SetGlobal("ML_0","LOCALS",6)
				# Continue()
				self.iSetStartPos("[315.625]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 6)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",5)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 5) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([315.625])
				self.iMoveToPoint("[315.625]")
				break
			
			# Global("ML_0","LOCALS",6)
			# ActionListEmpty()
			# NearLocation(Myself,229,392,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 6) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 229, 392, 4):
				# SetStartPos([229.392])
				# SetGlobal("ML_0","LOCALS",7)
				# Continue()
				self.iSetStartPos("[229.392]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 7)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",6)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 6) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([229.392])
				self.iMoveToPoint("[229.392]")
				break
			
			# Global("ML_0","LOCALS",7)
			# ActionListEmpty()
			# NearLocation(Myself,217,184,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 217, 184, 4):
				# SetStartPos([217.184])
				# SetGlobal("ML_0","LOCALS",8)
				# Continue()
				self.iSetStartPos("[217.184]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 8)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",7)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([217.184])
				self.iMoveToPoint("[217.184]")
				break
			
			# Global("ML_0","LOCALS",8)
			# ActionListEmpty()
			# NearLocation(Myself,151,20,4)
			if self.iGlobal("'ML_0'", "'LOCALS'", 8) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 151, 20, 4):
				# SetStartPos([151.20])
				# SetGlobal("ML_0","LOCALS",9)
				# Continue()
				self.iSetStartPos("[151.20]")
				self.iSetGlobal("'ML_0'", "'LOCALS'", 9)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",8)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 8) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# MoveToPoint([151.20])
				self.iMoveToPoint("[151.20]")
				break
			
			# Global("ML_0","LOCALS",9)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
				 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
				# SetGlobal("BROGAN_LEAVE","GLOBAL",2)
				# SetGlobal("ML_0","LOCALS",0)
				self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
				self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
				break
			
			break # while
		return
		
