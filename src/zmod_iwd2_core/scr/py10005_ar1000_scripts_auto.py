import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T01M_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_1","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_1'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00AATGN_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptClass (Special 2)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# See(NearestEnemyOf(Myself),0)
			if self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			break # while
		return
		
class Script_10ONBOAT_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptRace (Combat Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Allegiance(Myself,ENEMY)
			if self.iAllegiance("Myself", "ENEMY"):
				# ChangeCurrentScript("10aGobG0")
				self.iChangeCurrentScript("'10aGobG0'")
				break
			
			# !IsTeamBitOn(TEAM_1_BIT)
			if not self.iIsTeamBitOn("TEAM_1_BIT"):
				# SetTeamBit(TEAM_1_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_1_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_1","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_1'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_1","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_1'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# See([ENEMY][1887.703.2801.1043],0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and self.iSee("[ENEMY][1887.703.2801.1043]", 0):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See([ENEMY.0.GOBLIN][1887.703.2801.1043],0)
			if self.iSee("[ENEMY.0.GOBLIN][1887.703.2801.1043]", 0):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			break # while
		return
		
class Script_00AMVR_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptDefault (Movement Script)
	
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
		
class Script_00T00DET_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_0","MYAREA",1)
			# Or(2)
			# HitBy([GOODCUTOFF],CRUSHING)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_0'", "'MYAREA'", 1) \
				 and ( False \
					or self.iHitBy("[GOODCUTOFF]", "CRUSHING") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_0","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# !Global("TEAM_0","MYAREA",0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iGlobal("'TEAM_0'", "'MYAREA'", 0):
				# Enemy()
				# Continue()
				self.iEnemy()
				pass # continue() - let it pass below
			
			# !Global("TEAM_0","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_0'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_0","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_10HEDRO0_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptSpecial1 (Special1)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !TimerActive(18)
			# Global("SCREED_DEAD","GLOBAL",0)
			# !Allegiance(Myself,ENEMY)
			# !Exists("SCREED")
			if not self.iTimerActive(18) \
				 and self.iGlobal("'SCREED_DEAD'", "'GLOBAL'", 0) \
				 and not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iExists("'SCREED'"):
				# FloatMessage(Myself,8117)  // "Get yer ass back on the boat!"
				# StartRandomTimer(18,3,6)
				# Continue()
				self.iFloatMessage("Myself", 8117)
				self.iStartRandomTimer(18, 3, 6)
				pass # continue() - let it pass below
			
			# !TimerActive(18)
			# Global("ELDGULL_DEAD","GLOBAL",0)
			# !Allegiance(Myself,ENEMY)
			# !Exists("ELDGULL")
			if not self.iTimerActive(18) \
				 and self.iGlobal("'ELDGULL_DEAD'", "'GLOBAL'", 0) \
				 and not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iExists("'ELDGULL'"):
				# FloatMessage(Myself,8117)  // "Get yer ass back on the boat!"
				# StartRandomTimer(18,3,6)
				# Continue()
				self.iFloatMessage("Myself", 8117)
				self.iStartRandomTimer(18, 3, 6)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_10ELDGUM_Auto(inf_scripting.ScriptBase):
	# AR1000 10ELDGUL Eldgull ScriptDefault (Movement Script)
	
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
		
class Script_10SCREEM_Auto(inf_scripting.ScriptBase):
	# AR1000 10SCREED Screed ScriptDefault (Movement Script)
	
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
		
class Script_10REIG0_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("HEALED_REIG","MYAREA",0)
			# HPGT(Myself,3)
			if self.iGlobal("'HEALED_REIG'", "'MYAREA'", 0) \
				 and self.iHPGT("Myself", 3):
				# SetGlobal("HEALED_REIG","MYAREA",1)
				# Continue()
				self.iSetGlobal("'HEALED_REIG'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# NumTimesTalkedTo(0)
			# !Allegiance(Myself,ENEMY)
			# !Dead(Myself)
			# Or(2)
			# See(Protagonist,0)
			# See([PC],0)
			# Range(LastSeenBy(Myself),18,LESS_THAN)
			if self.iNumTimesTalkedTo(0) \
				 and not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iDead("Myself") \
				 and ( False \
					or self.iSee("Protagonist", 0) \
					or self.iSee("[PC]", 0) ) \
				 and self.iRange(self.iLastSeenBy("Myself"), 18, "LESS_THAN"):
				# StartCutSceneMode()
				# ClearAllActions()
				# SetDialogueRange(300)
				# MultiPlayerSync()
				# Dialogue(LastMarkedObject)
				self.iStartCutSceneMode()
				self.iClearAllActions()
				self.iSetDialogueRange(300)
				self.iMultiPlayerSync()
				self.iDialogue("LastMarkedObject")
				break
			
			# NumTimesTalkedTo(0)
			# !Allegiance(Myself,ENEMY)
			# See([PC],0)
			if self.iNumTimesTalkedTo(0) \
				 and not self.iAllegiance("Myself", "ENEMY") \
				 and self.iSee("[PC]", 0):
				# FaceObject(LastMarkedObject)
				self.iFaceObject("LastMarkedObject")
				break
			
			# !Allegiance(Myself,ENEMY)
			# !Dead(Myself)
			# Global("Reig_Heal_Priest","GLOBAL",0)
			# Global("Reig_Quest","GLOBAL",1)
			# !Global("HEALED_REIG","MYAREA",0)
			# See([PC],0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iDead("Myself") \
				 and self.iGlobal("'Reig_Heal_Priest'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Reig_Quest'", "'GLOBAL'", 1) \
				 and not self.iGlobal("'HEALED_REIG'", "'MYAREA'", 0) \
				 and self.iSee("[PC]", 0):
				# SetDialogueRange(300)
				# Dialogue(LastMarkedObject)
				self.iSetDialogueRange(300)
				self.iDialogue("LastMarkedObject")
				break
			
			# !TimerActive(21)
			# GlobalLT("Reig_Quest","GLOBAL",2)
			# !See([ENEMY.0.GOBLIN],0)
			if not self.iTimerActive(21) \
				 and self.iGlobalLT("'Reig_Quest'", "'GLOBAL'", 2) \
				 and not self.iSee("[ENEMY.0.GOBLIN]", 0):
				# FloatMessage(Myself,1659)  // "Damned arm... hurts like the devil."
				# StartRandomTimer(21,10,15)
				self.iFloatMessage("Myself", 1659)
				self.iStartRandomTimer(21, 10, 15)
				break
			
			# !NearSavedLocation(3)
			# !Allegiance(Myself,ENEMY)
			if not self.iNearSavedLocation(3) \
				 and not self.iAllegiance("Myself", "ENEMY"):
				# ReturnToSavedLocation(0)
				self.iReturnToSavedLocation(0)
				break
			
			break # while
		return
		
class Script_10AGOBC0_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptRace (Combat Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# See([ENEMY.0.GOBLIN],0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("[ENEMY.0.GOBLIN]", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_01",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_01'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_02",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_02'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_03",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_03'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_04",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_04'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_05",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_05'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_06",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_06'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_01",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_01'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_07",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_07'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_19",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_19'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_02",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_02'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_08",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_08'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_03",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_03'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_09",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_09'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_10",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_10'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_04",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_04'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_11",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_11'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_12",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_12'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_05",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_05'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_06",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_06'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_07",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_07'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_08",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_08'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_13",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_13'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_14",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_14'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_15",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_15'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_09",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_09'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_16",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_16'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_17",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_17'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_18",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_18'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_10",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_10'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# AttackedBy([ENEMY.0.GOBLIN],DEFAULT)
			if self.iAttackedBy("[ENEMY.0.GOBLIN]", "DEFAULT"):
				# RunAwayFrom(LastMarkedObject,45)
				self.iRunAwayFrom("LastMarkedObject", 45)
				break
			
			# See([ENEMY.0.GOBLIN],0)
			if self.iSee("[ENEMY.0.GOBLIN]", 0):
				# FaceObject(LastMarkedObject)
				self.iFaceObject("LastMarkedObject")
				break
			
			break # while
		return
		
class Script_00T02M_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptDefault (Movement Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_2","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T02ET_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_2","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_2","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# !Global("TEAM_2","MYAREA",0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iGlobal("'TEAM_2'", "'MYAREA'", 0):
				# Enemy()
				# Continue()
				self.iEnemy()
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_2_BIT)
			if not self.iIsTeamBitOn("TEAM_2_BIT"):
				# SetTeamBit(TEAM_2_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_2_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_2","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_2","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_00TOWNID_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptSpecial1 (Special1)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_0","MYAREA",0)
			# !TimerActive(2)
			# Allegiance(Myself,ENEMY)
			# See(NearestEnemyOf(Myself),0)
			if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
				 and not self.iTimerActive(2) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# StartTimer(2,6)
				# Continue()
				self.iStartTimer(2, 6)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			# Or(13)
			# HitBy([GOODCUTOFF],SLASHING)
			# HitBy([GOODCUTOFF],CRUSHING)
			# HitBy([GOODCUTOFF],PIERCING)
			# HitBy([GOODCUTOFF],MISSILE)
			# HitBy([GOODCUTOFF],FIRE)
			# HitBy([GOODCUTOFF],ELECTRICITY)
			# HitBy([GOODCUTOFF],POISON)
			# HitBy([GOODCUTOFF],MAGIC)
			# HitBy([GOODCUTOFF],COLD)
			# HitBy([GOODCUTOFF],ACID)
			# HitBy([GOODCUTOFF],MAGICFIRE)
			# HitBy([GOODCUTOFF],MAGICCOLD)
			# PickPocketFailed([PC])
			if not self.iAllegiance("Myself", "ENEMY") \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ) \
				 and ( False \
					or self.iHitBy("[GOODCUTOFF]", "SLASHING") \
					or self.iHitBy("[GOODCUTOFF]", "CRUSHING") \
					or self.iHitBy("[GOODCUTOFF]", "PIERCING") \
					or self.iHitBy("[GOODCUTOFF]", "MISSILE") \
					or self.iHitBy("[GOODCUTOFF]", "FIRE") \
					or self.iHitBy("[GOODCUTOFF]", "ELECTRICITY") \
					or self.iHitBy("[GOODCUTOFF]", "POISON") \
					or self.iHitBy("[GOODCUTOFF]", "MAGIC") \
					or self.iHitBy("[GOODCUTOFF]", "COLD") \
					or self.iHitBy("[GOODCUTOFF]", "ACID") \
					or self.iHitBy("[GOODCUTOFF]", "MAGICFIRE") \
					or self.iHitBy("[GOODCUTOFF]", "MAGICCOLD") \
					or self.iPickPocketFailed("[PC]") ):
				# Enemy()
				# SetGlobal("TOWNIE_HOSTILE","MYAREA",1)
				# Help()
				self.iEnemy()
				self.iSetGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 1)
				self.iHelp()
				break
			
			# !Allegiance(Myself,ENEMY)
			# !Global("TEAM_0","MYAREA",0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iGlobal("'TEAM_0'", "'MYAREA'", 0):
				# Enemy()
				# Continue()
				self.iEnemy()
				pass # continue() - let it pass below
			
			# Dead(Myself)
			if self.iDead("Myself"):
				# ChangeCurrentScript("")
				self.iChangeCurrentScript("''")
				break
			
			# Global("TEAM_0","MYAREA",0)
			# !Global("TOWNIE_HOSTILE","MYAREA",0)
			# !CreatureHidden(Myself)
			# Help([ANYTHING])
			if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
				 and not self.iGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0) \
				 and not self.iCreatureHidden("Myself") \
				 and self.iHelp("[ANYTHING]"):
				# SetGlobal("TEAM_0","MYAREA",1)
				# Enemy()
				self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
				self.iEnemy()
				break
			
			break # while
		return
		
class Script_10JON0_Auto(inf_scripting.ScriptBase):
	# AR1000 10JON Jon ScriptDefault (Movement Script)
	
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
		
class Script_00T03M_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_3","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_3'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_10GOBF0_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptClass (Special 2)
	
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
		
class Script_10GOBM0_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptRace (Combat Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("I_LIKE_DWARVES","LOCALS",0)
			# See([PC],0)
			if self.iGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 0) \
				 and self.iSee("[PC]", 0):
				# SetGlobal("I_LIKE_DWARVES","LOCALS",2)
				# Continue()
				self.iSetGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 2)
				pass # continue() - let it pass below
			
			# Global("I_LIKE_DWARVES","LOCALS",1)
			# Or(2)
			# See([PC.0.DWARF],0)
			# See([0.0.DWARF],0)
			if self.iGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 1) \
				 and ( False \
					or self.iSee("[PC.0.DWARF]", 0) \
					or self.iSee("[0.0.DWARF]", 0) ):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# Or(9)
			# See(NearestEnemyOf(Myself),0)
			# See("JORUN",0)
			# See("CRANDALL",0)
			# See("BROGAN",0)
			# See("JON",0)
			# See("REIG",0)
			# See("SCREED",0)
			# See("ELDGULL",0)
			# See("HEDRON",0)
			if ( False \
					or self.iSee(self.iNearestEnemyOf("Myself"), 0) \
					or self.iSee("'JORUN'", 0) \
					or self.iSee("'CRANDALL'", 0) \
					or self.iSee("'BROGAN'", 0) \
					or self.iSee("'JON'", 0) \
					or self.iSee("'REIG'", 0) \
					or self.iSee("'SCREED'", 0) \
					or self.iSee("'ELDGULL'", 0) \
					or self.iSee("'HEDRON'", 0) ):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			break # while
		return
		
class Script_00AMVW05_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptDefault (Movement Script)
	
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
		
class Script_00T03T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_3","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_3'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_3","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_3'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_3_BIT)
			if not self.iIsTeamBitOn("TEAM_3_BIT"):
				# SetTeamBit(TEAM_3_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_3_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_3","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_3'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_3","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_3'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_00T04M_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_02 ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_4","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_4'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T04T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_02 ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_4","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_4'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_4","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_4'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_4_BIT)
			if not self.iIsTeamBitOn("TEAM_4_BIT"):
				# SetTeamBit(TEAM_4_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_4_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_4","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_4'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_4","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_4'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_00T05M_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_04 ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_5","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_5'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T05T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_04 ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_5","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_5'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_5","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_5'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_5_BIT)
			if not self.iIsTeamBitOn("TEAM_5_BIT"):
				# SetTeamBit(TEAM_5_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_5_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_5","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_5'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_5","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_5'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_00T06M_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_06 ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_6","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_6'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T06T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_06 ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_6","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_6'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_6","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_6'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_6_BIT)
			if not self.iIsTeamBitOn("TEAM_6_BIT"):
				# SetTeamBit(TEAM_6_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_6_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_6","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_6'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_6","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_6'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_10GOBR0_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOBAR 1000_Goblin_Archer_01 ScriptRace (Combat Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("I_LIKE_DWARVES","LOCALS",0)
			# See([PC],0)
			if self.iGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 0) \
				 and self.iSee("[PC]", 0):
				# SetGlobal("I_LIKE_DWARVES","LOCALS",2)
				# Continue()
				self.iSetGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 2)
				pass # continue() - let it pass below
			
			# Global("I_LIKE_DWARVES","LOCALS",1)
			# Or(2)
			# See([PC.0.DWARF],0)
			# See([0.0.DWARF],0)
			if self.iGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 1) \
				 and ( False \
					or self.iSee("[PC.0.DWARF]", 0) \
					or self.iSee("[0.0.DWARF]", 0) ):
				# SetBestWeapon(LastMarkedObject,3)
				# AttackReevaluate(LastMarkedObject,45)
				self.iSetBestWeapon("LastMarkedObject", 3)
				self.iAttackReevaluate("LastMarkedObject", 45)
				break
			
			# Or(9)
			# See(NearestEnemyOf(Myself),0)
			# See("HEDRON",0)
			# See("JORUN",0)
			# See("CRANDALL",0)
			# See("BROGAN",0)
			# See("JON",0)
			# See("REIG",0)
			# See("SCREED",0)
			# See("ELDGULL",0)
			if ( False \
					or self.iSee(self.iNearestEnemyOf("Myself"), 0) \
					or self.iSee("'HEDRON'", 0) \
					or self.iSee("'JORUN'", 0) \
					or self.iSee("'CRANDALL'", 0) \
					or self.iSee("'BROGAN'", 0) \
					or self.iSee("'JON'", 0) \
					or self.iSee("'REIG'", 0) \
					or self.iSee("'SCREED'", 0) \
					or self.iSee("'ELDGULL'", 0) ):
				# SetBestWeapon(LastMarkedObject,3)
				# AttackReevaluate(LastMarkedObject,45)
				self.iSetBestWeapon("LastMarkedObject", 3)
				self.iAttackReevaluate("LastMarkedObject", 45)
				break
			
			break # while
		return
		
class Script_00T07M_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_14 ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_7","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_7'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T07T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_14 ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_7","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_7'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_7","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_7'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_7_BIT)
			if not self.iIsTeamBitOn("TEAM_7_BIT"):
				# SetTeamBit(TEAM_7_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_7_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_7","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_7'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_7","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_7'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_00T08M_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_16 ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_8","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_8'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T08T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_16 ScriptSpecific (Team Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_8","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_8'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_8","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_8'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_8_BIT)
			if not self.iIsTeamBitOn("TEAM_8_BIT"):
				# SetTeamBit(TEAM_8_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_8_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_8","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_8'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_8","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_8'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_10CRAND0_Auto(inf_scripting.ScriptBase):
	# AR1000 10CRANDA Crandall ScriptDefault (Movement Script)
	
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
		
class Script_AR1000_Auto(inf_scripting.ScriptBase):
	# AR1000
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# OnCreation()
			# Global("HEALED_REIG","MYAREA",0)
			if self.iOnCreation() \
				 and self.iGlobal("'HEALED_REIG'", "'MYAREA'", 0):
				# SetHP("Reig",3)
				# Continue()
				self.iSetHP("'Reig'", 3)
				pass # continue() - let it pass below
			
			# Global("AR1000_CHAPTER_SAVED","MYAREA",0)
			# Global("CHAPTER","GLOBAL",0)
			# !InCutsceneMode()
			# EntirePartyOnMap()
			if self.iGlobal("'AR1000_CHAPTER_SAVED'", "'MYAREA'", 0) \
				 and self.iGlobal("'CHAPTER'", "'GLOBAL'", 0) \
				 and not self.iInCutsceneMode() \
				 and self.iEntirePartyOnMap():
				# SetGlobal("AR1000_CHAPTER_SAVED","MYAREA",1)
				# ResetJoinRequests()
				# MultiPlayerSync()
				# SaveGame(16202)  // Prologue
				self.iSetGlobal("'AR1000_CHAPTER_SAVED'", "'MYAREA'", 1)
				self.iResetJoinRequests()
				self.iMultiPlayerSync()
				self.iSaveGame(16202)
				break
			
			# Global("CHAPTER","GLOBAL",-1)
			# EntirePartyOnMap()
			if self.iGlobal("'CHAPTER'", "'GLOBAL'", -1) \
				 and self.iEntirePartyOnMap():
				# EndCutSceneMode()
				# MultiPlayerSync()
				# IncrementChapter("")
				# MultiPlayerSync()
				# StartCutSceneMode()
				# ClearAllActions()
				# MultiPlayerSync()
				# StartCutScene("10cHedr0")
				self.iEndCutSceneMode()
				self.iMultiPlayerSync()
				self.iIncrementChapter("''")
				self.iMultiPlayerSync()
				self.iStartCutSceneMode()
				self.iClearAllActions()
				self.iMultiPlayerSync()
				self.iStartCutScene("'10cHedr0'")
				break
			
			# Global("CHAPTER","GLOBAL",-1)
			# !InCutsceneMode()
			if self.iGlobal("'CHAPTER'", "'GLOBAL'", -1) \
				 and not self.iInCutsceneMode():
				# StartCutSceneMode()
				self.iStartCutSceneMode()
				break
			
			# Global("CHAPTER","GLOBAL",-1)
			if self.iGlobal("'CHAPTER'", "'GLOBAL'", -1):
				# MultiPlayerSync()
				self.iMultiPlayerSync()
				break
			
			# Global("AR1003_BAR_CLEANUP","GLOBAL",0)
			# GlobalGT("Palisade_Iron_Collar_Quest","GLOBAL",1)
			# EntirePartyOnMap()
			if self.iGlobal("'AR1003_BAR_CLEANUP'", "'GLOBAL'", 0) \
				 and self.iGlobalGT("'Palisade_Iron_Collar_Quest'", "'GLOBAL'", 1) \
				 and self.iEntirePartyOnMap():
				# SetGlobal("AR1003_BAR_CLEANUP","GLOBAL",1)
				# Continue()
				self.iSetGlobal("'AR1003_BAR_CLEANUP'", "'GLOBAL'", 1)
				pass # continue() - let it pass below
			
			# Global("1000_GOBLIN_CLEANUP","GLOBAL",1)
			if self.iGlobal("'1000_GOBLIN_CLEANUP'", "'GLOBAL'", 1):
				# ActionOverride("DEAD_GOBLIN_0",DestroySelf())
				# ActionOverride("DEAD_GOBLIN_1",DestroySelf())
				# ActionOverride("DEAD_GOBLIN_2",DestroySelf())
				# ActionOverride("DEAD_GOBLIN_3",DestroySelf())
				# ActionOverride("Dead_Goblin_J1",DestroySelf())
				# ActionOverride("Dead_Goblin_J2",DestroySelf())
				# ActionOverride("DEAD_GOBLIN_6",DestroySelf())
				# ActionOverride("DEAD_GOBLIN_7",DestroySelf())
				# ActionOverride("DEAD_TOWNSPERSON_0",DestroySelf())
				# ActionOverride("DEAD_TOWNSPERSON_1",DestroySelf())
				# ActionOverride("Dead_Townsperson_2",DestroySelf())
				# ActionOverride("BROHN_DEAD",DestroySelf())
				# ActionOverride("DEAD_SOLDIER_0",DestroySelf())
				# ActionOverride("DEAD_SOLDIER_1",DestroySelf())
				# ActionOverride("DEAD_SAILOR",DestroySelf())
				# SetGlobal("1000_GOBLIN_CLEANUP","GLOBAL",2)
				# Continue()
				self.iActionOverride("'DEAD_GOBLIN_0'", self.iDestroySelf())
				self.iActionOverride("'DEAD_GOBLIN_1'", self.iDestroySelf())
				self.iActionOverride("'DEAD_GOBLIN_2'", self.iDestroySelf())
				self.iActionOverride("'DEAD_GOBLIN_3'", self.iDestroySelf())
				self.iActionOverride("'Dead_Goblin_J1'", self.iDestroySelf())
				self.iActionOverride("'Dead_Goblin_J2'", self.iDestroySelf())
				self.iActionOverride("'DEAD_GOBLIN_6'", self.iDestroySelf())
				self.iActionOverride("'DEAD_GOBLIN_7'", self.iDestroySelf())
				self.iActionOverride("'DEAD_TOWNSPERSON_0'", self.iDestroySelf())
				self.iActionOverride("'DEAD_TOWNSPERSON_1'", self.iDestroySelf())
				self.iActionOverride("'Dead_Townsperson_2'", self.iDestroySelf())
				self.iActionOverride("'BROHN_DEAD'", self.iDestroySelf())
				self.iActionOverride("'DEAD_SOLDIER_0'", self.iDestroySelf())
				self.iActionOverride("'DEAD_SOLDIER_1'", self.iDestroySelf())
				self.iActionOverride("'DEAD_SAILOR'", self.iDestroySelf())
				self.iSetGlobal("'1000_GOBLIN_CLEANUP'", "'GLOBAL'", 2)
				pass # continue() - let it pass below
			
			# Exists("Brogan")
			# !Global("1000_CLEAN_UP","GLOBAL",0)
			if self.iExists("'Brogan'") \
				 and not self.iGlobal("'1000_CLEAN_UP'", "'GLOBAL'", 0):
				# ActionOverride("Brogan",DestroySelf())
				# Continue()
				self.iActionOverride("'Brogan'", self.iDestroySelf())
				pass # continue() - let it pass below
			
			# Exists("Jon")
			# !Global("1000_CLEAN_UP","GLOBAL",0)
			if self.iExists("'Jon'") \
				 and not self.iGlobal("'1000_CLEAN_UP'", "'GLOBAL'", 0):
				# ActionOverride("Jon",DestroySelf())
				# Continue()
				self.iActionOverride("'Jon'", self.iDestroySelf())
				pass # continue() - let it pass below
			
			# Exists("Reig")
			# !Global("1000_CLEAN_UP","GLOBAL",0)
			if self.iExists("'Reig'") \
				 and not self.iGlobal("'1000_CLEAN_UP'", "'GLOBAL'", 0):
				# ActionOverride("Reig",DestroySelf())
				# Continue()
				self.iActionOverride("'Reig'", self.iDestroySelf())
				pass # continue() - let it pass below
			
			# Exists("Brohn_Dead")
			# !Global("1000_CLEAN_UP","GLOBAL",0)
			if self.iExists("'Brohn_Dead'") \
				 and not self.iGlobal("'1000_CLEAN_UP'", "'GLOBAL'", 0):
				# ActionOverride("Brohn_Dead",DestroySelf())
				# Continue()
				self.iActionOverride("'Brohn_Dead'", self.iDestroySelf())
				pass # continue() - let it pass below
			
			# Exists("Crandall")
			# !Global("1000_CLEAN_UP","GLOBAL",0)
			if self.iExists("'Crandall'") \
				 and not self.iGlobal("'1000_CLEAN_UP'", "'GLOBAL'", 0):
				# ActionOverride("Crandall",DestroySelf())
				# Continue()
				self.iActionOverride("'Crandall'", self.iDestroySelf())
				pass # continue() - let it pass below
			
			# Global("BROGAN_LEAVE","GLOBAL",2)
			# Exists("Brogan")
			if self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2) \
				 and self.iExists("'Brogan'"):
				# ActionOverride("Brogan",DestroySelf())
				# Continue()
				self.iActionOverride("'Brogan'", self.iDestroySelf())
				pass # continue() - let it pass below
			
			# Global("BROGAN_LEAVE","GLOBAL",2)
			# !Exists("Brogan")
			if self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2) \
				 and not self.iExists("'Brogan'"):
				# SetGlobal("BROGAN_LEAVE","GLOBAL",3)
				# Continue()
				self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 3)
				pass # continue() - let it pass below
			
			# Global("MAGDAR_LEAVE","GLOBAL",1)
			# EntirePartyOnMap()
			if self.iGlobal("'MAGDAR_LEAVE'", "'GLOBAL'", 1) \
				 and self.iEntirePartyOnMap():
				# SetGlobalTimer("AR1001_Goblin","GLOBAL",15)
				# SetGlobal("MAGDAR_LEAVE","GLOBAL",2)
				# Continue()
				self.iSetGlobalTimer("'AR1001_Goblin'", "'GLOBAL'", 15)
				self.iSetGlobal("'MAGDAR_LEAVE'", "'GLOBAL'", 2)
				pass # continue() - let it pass below
			
			# Global("Crane_Wheel","GLOBAL",1)
			# EntirePartyOnMap()
			if self.iGlobal("'Crane_Wheel'", "'GLOBAL'", 1) \
				 and self.iEntirePartyOnMap():
				# SetGlobal("Crane_Wheel","GLOBAL",2)
				# Continue()
				self.iSetGlobal("'Crane_Wheel'", "'GLOBAL'", 2)
				pass # continue() - let it pass below
			
			# Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
			# Dead([ENEMY.0.GOBLIN][0.0.10000.10000])
			# Dead("1000_Goblin_01")
			# Dead("1000_Goblin_02")
			# Dead("1000_Goblin_03")
			# Dead("1000_Goblin_04")
			# Dead("1000_Goblin_05")
			# Dead("1000_Goblin_06")
			# Dead("1000_Goblin_Archer_01")
			# Dead("1000_Goblin_07")
			# Dead("1000_Goblin_19")
			# Dead("1000_Goblin_Archer_02")
			# Dead("1000_Goblin_08")
			# Dead("1000_Goblin_Archer_03")
			# Dead("1000_Goblin_09")
			# Dead("1000_Goblin_10")
			# Dead("1000_Goblin_Archer_04")
			# Dead("1000_Goblin_11")
			# Dead("1000_Goblin_12")
			# Dead("1000_Goblin_Archer_05")
			# Dead("1000_Goblin_Archer_06")
			# Dead("1000_Goblin_Archer_07")
			# Dead("1000_Goblin_Archer_08")
			# Dead("1000_Goblin_13")
			# Dead("1000_Goblin_14")
			# Dead("1000_Goblin_15")
			# Dead("1000_Goblin_Archer_09")
			# Dead("1000_Goblin_16")
			# Dead("1000_Goblin_17")
			# Dead("1000_Goblin_18")
			# Dead("1000_Goblin_Archer_10")
			if self.iGlobal("'AR1000_GOBLINS_CLEAR'", "'GLOBAL'", 0) \
				 and self.iDead("[ENEMY.0.GOBLIN][0.0.10000.10000]") \
				 and self.iDead("'1000_Goblin_01'") \
				 and self.iDead("'1000_Goblin_02'") \
				 and self.iDead("'1000_Goblin_03'") \
				 and self.iDead("'1000_Goblin_04'") \
				 and self.iDead("'1000_Goblin_05'") \
				 and self.iDead("'1000_Goblin_06'") \
				 and self.iDead("'1000_Goblin_Archer_01'") \
				 and self.iDead("'1000_Goblin_07'") \
				 and self.iDead("'1000_Goblin_19'") \
				 and self.iDead("'1000_Goblin_Archer_02'") \
				 and self.iDead("'1000_Goblin_08'") \
				 and self.iDead("'1000_Goblin_Archer_03'") \
				 and self.iDead("'1000_Goblin_09'") \
				 and self.iDead("'1000_Goblin_10'") \
				 and self.iDead("'1000_Goblin_Archer_04'") \
				 and self.iDead("'1000_Goblin_11'") \
				 and self.iDead("'1000_Goblin_12'") \
				 and self.iDead("'1000_Goblin_Archer_05'") \
				 and self.iDead("'1000_Goblin_Archer_06'") \
				 and self.iDead("'1000_Goblin_Archer_07'") \
				 and self.iDead("'1000_Goblin_Archer_08'") \
				 and self.iDead("'1000_Goblin_13'") \
				 and self.iDead("'1000_Goblin_14'") \
				 and self.iDead("'1000_Goblin_15'") \
				 and self.iDead("'1000_Goblin_Archer_09'") \
				 and self.iDead("'1000_Goblin_16'") \
				 and self.iDead("'1000_Goblin_17'") \
				 and self.iDead("'1000_Goblin_18'") \
				 and self.iDead("'1000_Goblin_Archer_10'"):
				# SetGlobal("AR1000_GOBLINS_CLEAR","GLOBAL",1)
				# Deactivate("Horn_Blow")
				# Continue()
				self.iSetGlobal("'AR1000_GOBLINS_CLEAR'", "'GLOBAL'", 1)
				self.iDeactivate("'Horn_Blow'")
				pass # continue() - let it pass below
			
			# Global("Dock_Goblin_Quest","GLOBAL",0)
			# !Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
			# !Global("AR1002_GOBLINS_CLEAR","GLOBAL",0)
			# !Global("AR1004_GOBLINS_CLEAR","GLOBAL",0)
			# !Global("AR1005_GOBLINS_CLEAR","GLOBAL",0)
			# !Global("AR1007_GOBLINS_CLEAR","GLOBAL",0)
			if self.iGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 0) \
				 and not self.iGlobal("'AR1000_GOBLINS_CLEAR'", "'GLOBAL'", 0) \
				 and not self.iGlobal("'AR1002_GOBLINS_CLEAR'", "'GLOBAL'", 0) \
				 and not self.iGlobal("'AR1004_GOBLINS_CLEAR'", "'GLOBAL'", 0) \
				 and not self.iGlobal("'AR1005_GOBLINS_CLEAR'", "'GLOBAL'", 0) \
				 and not self.iGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				# AddXPVar("Level_2_Very_Hard",26671)  // You have cleared the Targos Docks of goblins.
				# SetGlobal("Dock_Goblin_Quest","GLOBAL",1)
				# AddJournalEntry(27866)  // We managed to drive the last of the goblins off of the Targos Docks.  Reig and Lord Ulbrec should be grateful to hear of our success.
				# Continue()
				self.iAddXPVar("'Level_2_Very_Hard'", 26671)
				self.iSetGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1)
				self.iAddJournalEntry(27866)
				pass # continue() - let it pass below
			
			# Global("TARGOS_HOSTILE","GLOBAL",0)
			# !Global("TEAM_0","MYAREA",0)
			if self.iGlobal("'TARGOS_HOSTILE'", "'GLOBAL'", 0) \
				 and not self.iGlobal("'TEAM_0'", "'MYAREA'", 0):
				# SetGlobal("TARGOS_HOSTILE","GLOBAL",1)
				# Continue()
				self.iSetGlobal("'TARGOS_HOSTILE'", "'GLOBAL'", 1)
				pass # continue() - let it pass below
			
			# Global("TEAM_0","MYAREA",0)
			# !Global("TARGOS_HOSTILE","GLOBAL",0)
			if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
				 and not self.iGlobal("'TARGOS_HOSTILE'", "'GLOBAL'", 0):
				# SetGlobal("TEAM_0","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !Global("TOWNIE_DEAD","GLOBAL",0)
			if not self.iGlobal("'TOWNIE_DEAD'", "'GLOBAL'", 0):
				# SetGlobal("TOWNIE_HOSTILE","MYAREA",0)
				# SetGlobal("TOWNIE_DEAD","GLOBAL",0)
				# Continue()
				self.iSetGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0)
				self.iSetGlobal("'TOWNIE_DEAD'", "'GLOBAL'", 0)
				pass # continue() - let it pass below
			
			# OnCreation()
			if self.iOnCreation():
				# NoAction()
				# Continue()
				self.iNoAction()
				pass # continue() - let it pass below
			
			# !Global("AR1000_RESET_CUTSCENE","GLOBAL",0)
			# Or(2)
			# EntirePartyOnMap()
			# !InCutsceneMode()
			if not self.iGlobal("'AR1000_RESET_CUTSCENE'", "'GLOBAL'", 0) \
				 and ( False \
					or self.iEntirePartyOnMap() \
					or not self.iInCutsceneMode() ):
				# EndCutSceneMode()
				# SetGlobal("AR1000_RESET_CUTSCENE","GLOBAL",0)
				# Continue()
				self.iEndCutSceneMode()
				self.iSetGlobal("'AR1000_RESET_CUTSCENE'", "'GLOBAL'", 0)
				pass # continue() - let it pass below
			
			# !Global("RJ_AR1000","GLOBAL",0)
			# !InCutsceneMode()
			if not self.iGlobal("'RJ_AR1000'", "'GLOBAL'", 0) \
				 and not self.iInCutsceneMode():
				# MultiPlayerSync()
				# ResetJoinRequests()
				# SetGlobal("RJ_AR1000","GLOBAL",0)
				# Continue()
				self.iMultiPlayerSync()
				self.iResetJoinRequests()
				self.iSetGlobal("'RJ_AR1000'", "'GLOBAL'", 0)
				pass # continue() - let it pass below
			
			# Global("1200_BATTLE_CLEANUP","GLOBAL",0)
			# !Global("Goblin_Palisade_Quest","GLOBAL",0)
			if self.iGlobal("'1200_BATTLE_CLEANUP'", "'GLOBAL'", 0) \
				 and not self.iGlobal("'Goblin_Palisade_Quest'", "'GLOBAL'", 0):
				# SetGlobal("1200_BATTLE_CLEANUP","GLOBAL",1)
				# Continue()
				self.iSetGlobal("'1200_BATTLE_CLEANUP'", "'GLOBAL'", 1)
				pass # continue() - let it pass below
			
			# IsActive("cat_singles_exterior")
			# !Global("AR1004_CATS_DEAD","GLOBAL",0)
			if self.iIsActive("'cat_singles_exterior'") \
				 and not self.iGlobal("'AR1004_CATS_DEAD'", "'GLOBAL'", 0):
				# Deactivate("cat_singles_exterior")
				# Continue()
				self.iDeactivate("'cat_singles_exterior'")
				pass # continue() - let it pass below
			
			# IsActive("Horn_Blow")
			# !Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
			if self.iIsActive("'Horn_Blow'") \
				 and not self.iGlobal("'AR1000_GOBLINS_CLEAR'", "'GLOBAL'", 0):
				# Deactivate("Horn_Blow")
				# Continue()
				self.iDeactivate("'Horn_Blow'")
				pass # continue() - let it pass below
			
			# Global("Destroy_Shaengarne_Bridge","GLOBAL",0)
			# Global("Shaengarne_Award_XPVar","GLOBAL",0)
			# Global("AR2102_Visited","GLOBAL",1)
			if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
				 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
				 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
				# Debug("CBN_SetFlag_Destroy_Shaengarne_Bridge")
				# SetGlobal("Destroy_Shaengarne_Bridge","GLOBAL",1)
				# Continue()
				self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
				self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
