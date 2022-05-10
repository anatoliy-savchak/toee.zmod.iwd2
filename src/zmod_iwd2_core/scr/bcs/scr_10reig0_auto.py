import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
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
		
