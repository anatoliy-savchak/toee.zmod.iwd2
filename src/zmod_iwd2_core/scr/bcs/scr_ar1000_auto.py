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
		is_cutscene_execution = self.is_cutscene_mode()
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_02()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_03()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_04()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_05()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_06()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_07()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_08()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_09()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_10()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_11()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_12()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_13()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_14()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_15()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_16()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_17()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_18()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_19()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_20()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_21()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_22()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_23()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_24()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_25()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_26()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_27()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_28()
			if break_ and not is_cutscene_execution: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# OnCreation()
		# Global("HEALED_REIG","MYAREA",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetHP("Reig",3)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("AR1000_CHAPTER_SAVED","MYAREA",0)
		# Global("CHAPTER","GLOBAL",0)
		# !InCutsceneMode()
		# EntirePartyOnMap()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("AR1000_CHAPTER_SAVED","MYAREA",1)
			# ResetJoinRequests()
			# MultiPlayerSync()
			# SaveGame(16202)  // Prologue
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("CHAPTER","GLOBAL",-1)
		# EntirePartyOnMap()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# EndCutSceneMode()
			# MultiPlayerSync()
			# IncrementChapter("")
			# MultiPlayerSync()
			# StartCutSceneMode()
			# ClearAllActions()
			# MultiPlayerSync()
			# StartCutScene("10cHedr0")
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("CHAPTER","GLOBAL",-1)
		# !InCutsceneMode()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# StartCutSceneMode()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("CHAPTER","GLOBAL",-1)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# MultiPlayerSync()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("AR1003_BAR_CLEANUP","GLOBAL",0)
		# GlobalGT("Palisade_Iron_Collar_Quest","GLOBAL",1)
		# EntirePartyOnMap()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("AR1003_BAR_CLEANUP","GLOBAL",1)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("1000_GOBLIN_CLEANUP","GLOBAL",1)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
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
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_08(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Exists("Brogan")
		# !Global("1000_CLEAN_UP","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# ActionOverride("Brogan",DestroySelf())
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_09(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Exists("Jon")
		# !Global("1000_CLEAN_UP","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# ActionOverride("Jon",DestroySelf())
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_10(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Exists("Reig")
		# !Global("1000_CLEAN_UP","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# ActionOverride("Reig",DestroySelf())
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_11(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Exists("Brohn_Dead")
		# !Global("1000_CLEAN_UP","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# ActionOverride("Brohn_Dead",DestroySelf())
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_12(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Exists("Crandall")
		# !Global("1000_CLEAN_UP","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# ActionOverride("Crandall",DestroySelf())
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_13(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("BROGAN_LEAVE","GLOBAL",2)
		# Exists("Brogan")
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# ActionOverride("Brogan",DestroySelf())
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_14(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("BROGAN_LEAVE","GLOBAL",2)
		# !Exists("Brogan")
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("BROGAN_LEAVE","GLOBAL",3)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_15(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("MAGDAR_LEAVE","GLOBAL",1)
		# EntirePartyOnMap()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobalTimer("AR1001_Goblin","GLOBAL",15)
			# SetGlobal("MAGDAR_LEAVE","GLOBAL",2)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_16(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("Crane_Wheel","GLOBAL",1)
		# EntirePartyOnMap()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("Crane_Wheel","GLOBAL",2)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_17(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
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
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("AR1000_GOBLINS_CLEAR","GLOBAL",1)
			# Deactivate("Horn_Blow")
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_18(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("Dock_Goblin_Quest","GLOBAL",0)
		# !Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
		# !Global("AR1002_GOBLINS_CLEAR","GLOBAL",0)
		# !Global("AR1004_GOBLINS_CLEAR","GLOBAL",0)
		# !Global("AR1005_GOBLINS_CLEAR","GLOBAL",0)
		# !Global("AR1007_GOBLINS_CLEAR","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# AddXPVar("Level_2_Very_Hard",26671)  // You have cleared the Targos Docks of goblins.
			# SetGlobal("Dock_Goblin_Quest","GLOBAL",1)
			# AddJournalEntry(27866)  // We managed to drive the last of the goblins off of the Targos Docks.  Reig and Lord Ulbrec should be grateful to hear of our success.
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_19(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("TARGOS_HOSTILE","GLOBAL",0)
		# !Global("TEAM_0","MYAREA",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("TARGOS_HOSTILE","GLOBAL",1)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_20(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("TEAM_0","MYAREA",0)
		# !Global("TARGOS_HOSTILE","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("TEAM_0","MYAREA",1)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_21(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("TOWNIE_DEAD","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("TOWNIE_HOSTILE","MYAREA",0)
			# SetGlobal("TOWNIE_DEAD","GLOBAL",0)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_22(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# OnCreation()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# NoAction()
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_23(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("AR1000_RESET_CUTSCENE","GLOBAL",0)
		# Or(2)
		# EntirePartyOnMap()
		# !InCutsceneMode()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# EndCutSceneMode()
			# SetGlobal("AR1000_RESET_CUTSCENE","GLOBAL",0)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_24(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("RJ_AR1000","GLOBAL",0)
		# !InCutsceneMode()
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# MultiPlayerSync()
			# ResetJoinRequests()
			# SetGlobal("RJ_AR1000","GLOBAL",0)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_25(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("1200_BATTLE_CLEANUP","GLOBAL",0)
		# !Global("Goblin_Palisade_Quest","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# SetGlobal("1200_BATTLE_CLEANUP","GLOBAL",1)
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_26(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# IsActive("cat_singles_exterior")
		# !Global("AR1004_CATS_DEAD","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# Deactivate("cat_singles_exterior")
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_27(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# IsActive("Horn_Blow")
		# !Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
		if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
			 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
			 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
			# Deactivate("Horn_Blow")
			# Continue()
			self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
			self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_28(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
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
			return False # continue() - pass further blocks
		return False
		
