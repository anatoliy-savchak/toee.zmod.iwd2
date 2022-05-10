import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_AR1000_Auto(inf_scripting.ScriptBase):
	# AR1000 script_area
	
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
				self.iStartCutScene(scr_10chedr0.Script_10cHedr0)
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
		
