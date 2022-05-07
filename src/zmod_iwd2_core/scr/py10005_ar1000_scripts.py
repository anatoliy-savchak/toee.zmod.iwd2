import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T01M(object):
	
	def script_general(self, npc):
		while True:
			# Global("TEAM_1","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("TEAM_1", "MYAREA", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_10REIG0(object):
	
	def script_general(self, npc):
		while True:
			# Global("HEALED_REIG","MYAREA",0)
			# HPGT(Myself,3)
			if self.iGlobal("HEALED_REIG", "MYAREA", 0) \
				 and self.iHPGT("Myself", 3):
				# SetGlobal("HEALED_REIG","MYAREA",1)
				# Continue()
				self.iSetGlobal("HEALED_REIG", "MYAREA", 1)
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
				 and ( \
					self.iSee("Protagonist", 0) \
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
				 and self.iGlobal("Reig_Heal_Priest", "GLOBAL", 0) \
				 and self.iGlobal("Reig_Quest", "GLOBAL", 1) \
				 and not self.iGlobal("HEALED_REIG", "MYAREA", 0) \
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
				 and self.iGlobalLT("Reig_Quest", "GLOBAL", 2) \
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
		
class Script_00T02ET(object):
	
	def script_general(self, npc):
		while True:
			# !Global("TEAM_2","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("TEAM_2", "MYAREA", 1) \
				 and ( \
					self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_2","MYAREA",1)
				# Continue()
				self.iSetGlobal("TEAM_2", "MYAREA", 1)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# !Global("TEAM_2","MYAREA",0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iGlobal("TEAM_2", "MYAREA", 0):
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
			if not self.iGlobal("TEAM_2", "MYAREA", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_2","MYAREA",1)
				# Continue()
				self.iSetGlobal("TEAM_2", "MYAREA", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_10BROGA0(object):
	
	def script_general(self, npc):
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
				 and self.iGlobal("Brogan_Leave", "GLOBAL", 0):
				# FloatMessage(Myself,1666)  // "Hope there's no other goblins about..."
				# StartRandomTimer(18,10,15)
				# Continue()
				self.iFloatMessage("Myself", 1666)
				self.iStartRandomTimer(18, 10, 15)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",0)
			# ActionListEmpty()
			# NearLocation(Myself,1747,524,4)
			if self.iGlobal("ML_0", "LOCALS", 0) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1747, 524, 4):
				# SetStartPos([1747.524])
				# SetGlobal("ML_0","LOCALS",1)
				# Continue()
				self.iSetStartPos("[1747.524]")
				self.iSetGlobal("ML_0", "LOCALS", 1)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",0)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 0) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([1747.524])
				self.iMoveToPoint("[1747.524]")
				break
			
			# Global("ML_0","LOCALS",1)
			# ActionListEmpty()
			# NearLocation(Myself,1530,781,4)
			if self.iGlobal("ML_0", "LOCALS", 1) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1530, 781, 4):
				# SetStartPos([1530.781])
				# SetGlobal("ML_0","LOCALS",2)
				# Continue()
				self.iSetStartPos("[1530.781]")
				self.iSetGlobal("ML_0", "LOCALS", 2)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",1)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 1) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([1530.781])
				self.iMoveToPoint("[1530.781]")
				break
			
			# Global("ML_0","LOCALS",2)
			# ActionListEmpty()
			# NearLocation(Myself,1241,940,4)
			if self.iGlobal("ML_0", "LOCALS", 2) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 1241, 940, 4):
				# SetStartPos([1241.940])
				# SetGlobal("ML_0","LOCALS",3)
				# Continue()
				self.iSetStartPos("[1241.940]")
				self.iSetGlobal("ML_0", "LOCALS", 3)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",2)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 2) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([1241.940])
				self.iMoveToPoint("[1241.940]")
				break
			
			# Global("ML_0","LOCALS",3)
			# ActionListEmpty()
			# NearLocation(Myself,910,1053,4)
			if self.iGlobal("ML_0", "LOCALS", 3) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 910, 1053, 4):
				# SetStartPos([910.1053])
				# SetGlobal("ML_0","LOCALS",4)
				# Continue()
				self.iSetStartPos("[910.1053]")
				self.iSetGlobal("ML_0", "LOCALS", 4)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",3)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 3) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([910.1053])
				self.iMoveToPoint("[910.1053]")
				break
			
			# Global("ML_0","LOCALS",4)
			# ActionListEmpty()
			# NearLocation(Myself,559,884,4)
			if self.iGlobal("ML_0", "LOCALS", 4) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 559, 884, 4):
				# SetStartPos([559.884])
				# SetGlobal("ML_0","LOCALS",5)
				# Continue()
				self.iSetStartPos("[559.884]")
				self.iSetGlobal("ML_0", "LOCALS", 5)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",4)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 4) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([559.884])
				self.iMoveToPoint("[559.884]")
				break
			
			# Global("ML_0","LOCALS",5)
			# ActionListEmpty()
			# NearLocation(Myself,315,625,4)
			if self.iGlobal("ML_0", "LOCALS", 5) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 315, 625, 4):
				# SetStartPos([315.625])
				# SetGlobal("ML_0","LOCALS",6)
				# Continue()
				self.iSetStartPos("[315.625]")
				self.iSetGlobal("ML_0", "LOCALS", 6)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",5)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 5) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([315.625])
				self.iMoveToPoint("[315.625]")
				break
			
			# Global("ML_0","LOCALS",6)
			# ActionListEmpty()
			# NearLocation(Myself,229,392,4)
			if self.iGlobal("ML_0", "LOCALS", 6) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 229, 392, 4):
				# SetStartPos([229.392])
				# SetGlobal("ML_0","LOCALS",7)
				# Continue()
				self.iSetStartPos("[229.392]")
				self.iSetGlobal("ML_0", "LOCALS", 7)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",6)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 6) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([229.392])
				self.iMoveToPoint("[229.392]")
				break
			
			# Global("ML_0","LOCALS",7)
			# ActionListEmpty()
			# NearLocation(Myself,217,184,4)
			if self.iGlobal("ML_0", "LOCALS", 7) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 217, 184, 4):
				# SetStartPos([217.184])
				# SetGlobal("ML_0","LOCALS",8)
				# Continue()
				self.iSetStartPos("[217.184]")
				self.iSetGlobal("ML_0", "LOCALS", 8)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",7)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 7) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([217.184])
				self.iMoveToPoint("[217.184]")
				break
			
			# Global("ML_0","LOCALS",8)
			# ActionListEmpty()
			# NearLocation(Myself,151,20,4)
			if self.iGlobal("ML_0", "LOCALS", 8) \
				 and self.iActionListEmpty() \
				 and self.iNearLocation("Myself", 151, 20, 4):
				# SetStartPos([151.20])
				# SetGlobal("ML_0","LOCALS",9)
				# Continue()
				self.iSetStartPos("[151.20]")
				self.iSetGlobal("ML_0", "LOCALS", 9)
				pass # continue() - let it pass below
			
			# Global("ML_0","LOCALS",8)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 8) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# MoveToPoint([151.20])
				self.iMoveToPoint("[151.20]")
				break
			
			# Global("ML_0","LOCALS",9)
			# Global("BROGAN_LEAVE","GLOBAL",1)
			if self.iGlobal("ML_0", "LOCALS", 9) \
				 and self.iGlobal("BROGAN_LEAVE", "GLOBAL", 1):
				# SetGlobal("BROGAN_LEAVE","GLOBAL",2)
				# SetGlobal("ML_0","LOCALS",0)
				self.iSetGlobal("BROGAN_LEAVE", "GLOBAL", 2)
				self.iSetGlobal("ML_0", "LOCALS", 0)
				break
			
			break # while
		return
		
class Script_10JORUN0(object):
	
	def script_general(self, npc):
		while True:
			# !TimerActive(18)
			# Global("Dock_Goblin_Quest","GLOBAL",0)
			if not self.iTimerActive(18) \
				 and self.iGlobal("Dock_Goblin_Quest", "GLOBAL", 0):
				# FloatMessage(Myself,1670)  // "Damn fool goblins, thinkin' to torch me boat..."
				# StartTimer(18,5)
				# Continue()
				self.iFloatMessage("Myself", 1670)
				self.iStartTimer(18, 5)
				pass # continue() - let it pass below
			
			# !Global("JORUN_FLOAT","LOCALS",0)
			# NearSavedLocation(1)
			if not self.iGlobal("JORUN_FLOAT", "LOCALS", 0) \
				 and self.iNearSavedLocation(1):
				# SetGlobal("JORUN_FLOAT","LOCALS",0)
				# Face(W)
				self.iSetGlobal("JORUN_FLOAT", "LOCALS", 0)
				self.iFace("W")
				break
			
			# !Global("JORUN_FLOAT","LOCALS",0)
			if not self.iGlobal("JORUN_FLOAT", "LOCALS", 0):
				# SetGlobal("JORUN_FLOAT","LOCALS",0)
				# Continue()
				self.iSetGlobal("JORUN_FLOAT", "LOCALS", 0)
				pass # continue() - let it pass below
			
			break # while
		return
		
class Script_00T03M(object):
	
	def script_general(self, npc):
		while True:
			# Global("TEAM_3","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("TEAM_3", "MYAREA", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T04M(object):
	
	def script_general(self, npc):
		while True:
			# Global("TEAM_4","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("TEAM_4", "MYAREA", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T05M(object):
	
	def script_general(self, npc):
		while True:
			# Global("TEAM_5","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("TEAM_5", "MYAREA", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T06M(object):
	
	def script_general(self, npc):
		while True:
			# Global("TEAM_6","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("TEAM_6", "MYAREA", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T07M(object):
	
	def script_general(self, npc):
		while True:
			# Global("TEAM_7","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("TEAM_7", "MYAREA", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_00T08M(object):
	
	def script_general(self, npc):
		while True:
			# Global("TEAM_8","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("TEAM_8", "MYAREA", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
class Script_10AGOBC0(object):
	
	def script_general(self, npc):
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
			if self.iSee("1000_Goblin_01", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_02",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_02", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_03",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_03", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_04",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_04", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_05",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_05", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_06",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_06", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_01",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_01", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_07",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_07", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_19",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_19", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_02",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_02", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_08",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_08", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_03",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_03", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_09",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_09", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_10",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_10", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_04",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_04", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_11",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_11", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_12",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_12", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_05",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_05", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_06",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_06", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_07",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_07", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_08",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_08", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_13",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_13", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_14",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_14", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_15",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_15", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_09",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_09", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_16",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_16", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_17",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_17", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_18",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_18", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_10",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("1000_Goblin_Archer_10", 0) \
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
		
