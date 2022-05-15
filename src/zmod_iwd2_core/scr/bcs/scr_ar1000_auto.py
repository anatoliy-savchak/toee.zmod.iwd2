import toee, debug
import inf_scripting
#### IMPORTS ####
from bcs import scr_10chedr0
#### END IMPORTS ####

#### BCS ####
class Script_AR1000_Auto(inf_scripting.ScriptBase): # AR1000
	# AR1000 script_area
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute(cls, self, locus, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from <= 1:
				break_ = cls.do_execute_block_01(self, locus, code_from=code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 2:
				break_ = cls.do_execute_block_02(self, locus, code_from=code_from if code_from and block_from == 2 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 3:
				break_ = cls.do_execute_block_03(self, locus, code_from=code_from if code_from and block_from == 3 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 4:
				break_ = cls.do_execute_block_04(self, locus, code_from=code_from if code_from and block_from == 4 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 5:
				break_ = cls.do_execute_block_05(self, locus, code_from=code_from if code_from and block_from == 5 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 6:
				break_ = cls.do_execute_block_06(self, locus, code_from=code_from if code_from and block_from == 6 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 7:
				break_ = cls.do_execute_block_07(self, locus, code_from=code_from if code_from and block_from == 7 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 8:
				break_ = cls.do_execute_block_08(self, locus, code_from=code_from if code_from and block_from == 8 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 9:
				break_ = cls.do_execute_block_09(self, locus, code_from=code_from if code_from and block_from == 9 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 10:
				break_ = cls.do_execute_block_10(self, locus, code_from=code_from if code_from and block_from == 10 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 11:
				break_ = cls.do_execute_block_11(self, locus, code_from=code_from if code_from and block_from == 11 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 12:
				break_ = cls.do_execute_block_12(self, locus, code_from=code_from if code_from and block_from == 12 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 13:
				break_ = cls.do_execute_block_13(self, locus, code_from=code_from if code_from and block_from == 13 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 14:
				break_ = cls.do_execute_block_14(self, locus, code_from=code_from if code_from and block_from == 14 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 15:
				break_ = cls.do_execute_block_15(self, locus, code_from=code_from if code_from and block_from == 15 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 16:
				break_ = cls.do_execute_block_16(self, locus, code_from=code_from if code_from and block_from == 16 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 17:
				break_ = cls.do_execute_block_17(self, locus, code_from=code_from if code_from and block_from == 17 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 18:
				break_ = cls.do_execute_block_18(self, locus, code_from=code_from if code_from and block_from == 18 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 19:
				break_ = cls.do_execute_block_19(self, locus, code_from=code_from if code_from and block_from == 19 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 20:
				break_ = cls.do_execute_block_20(self, locus, code_from=code_from if code_from and block_from == 20 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 21:
				break_ = cls.do_execute_block_21(self, locus, code_from=code_from if code_from and block_from == 21 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 22:
				break_ = cls.do_execute_block_22(self, locus, code_from=code_from if code_from and block_from == 22 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 23:
				break_ = cls.do_execute_block_23(self, locus, code_from=code_from if code_from and block_from == 23 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 24:
				break_ = cls.do_execute_block_24(self, locus, code_from=code_from if code_from and block_from == 24 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 25:
				break_ = cls.do_execute_block_25(self, locus, code_from=code_from if code_from and block_from == 25 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 26:
				break_ = cls.do_execute_block_26(self, locus, code_from=code_from if code_from and block_from == 26 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 27:
				break_ = cls.do_execute_block_27(self, locus, code_from=code_from if code_from and block_from == 27 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 28:
				break_ = cls.do_execute_block_28(self, locus, code_from=code_from if code_from and block_from == 28 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 1
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# OnCreation()
				# Global("HEALED_REIG","MYAREA",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetHP("Reig",3)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetHP("Reig",3)
		
		self.iSetHP("'Reig'", 3)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("AR1000_CHAPTER_SAVED","MYAREA",0)
				# Global("CHAPTER","GLOBAL",0)
				# !InCutsceneMode()
				# EntirePartyOnMap()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("AR1000_CHAPTER_SAVED","MYAREA",1)
		# ResetJoinRequests()
		# MultiPlayerSync()
		# SaveGame(16202)  // Prologue
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_02_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("AR1000_CHAPTER_SAVED","MYAREA",1)
		# ResetJoinRequests()
		# MultiPlayerSync()
		# SaveGame(16202)  // Prologue
		
		self.iSetGlobal("'AR1000_CHAPTER_SAVED'", "'MYAREA'", 1)
		self.iResetJoinRequests()
		self.iMultiPlayerSync()
		self.iSaveGame(16202)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 3
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("CHAPTER","GLOBAL",-1)
				# EntirePartyOnMap()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# EndCutSceneMode()
		# MultiPlayerSync()
		# IncrementChapter("")
		# MultiPlayerSync()
		# StartCutSceneMode()
		# ClearAllActions()
		# MultiPlayerSync()
		# StartCutScene("10cHedr0")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_03_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_03_code_02(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
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
		self.iStartCutScene(scr_10chedr0.Script_10cHedr0, locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 4
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("CHAPTER","GLOBAL",-1)
				# !InCutsceneMode()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# StartCutSceneMode()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_04_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# StartCutSceneMode()
		
		self.iStartCutSceneMode()
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 5
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("CHAPTER","GLOBAL",-1)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MultiPlayerSync()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_05_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# MultiPlayerSync()
		
		self.iMultiPlayerSync()
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 6
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("AR1003_BAR_CLEANUP","GLOBAL",0)
				# GlobalGT("Palisade_Iron_Collar_Quest","GLOBAL",1)
				# EntirePartyOnMap()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("AR1003_BAR_CLEANUP","GLOBAL",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_06_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("AR1003_BAR_CLEANUP","GLOBAL",1)
		
		self.iSetGlobal("'AR1003_BAR_CLEANUP'", "'GLOBAL'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 7
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("1000_GOBLIN_CLEANUP","GLOBAL",1)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
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
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_07_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
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
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 8
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Exists("Brogan")
				# !Global("1000_CLEAN_UP","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# ActionOverride("Brogan",DestroySelf())
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_08_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# ActionOverride("Brogan",DestroySelf())
		
		self.iActionOverride("'Brogan'", self.iDestroySelf())
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_09(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 9
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Exists("Jon")
				# !Global("1000_CLEAN_UP","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# ActionOverride("Jon",DestroySelf())
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_09_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_09_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# ActionOverride("Jon",DestroySelf())
		
		self.iActionOverride("'Jon'", self.iDestroySelf())
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_10(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 10
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Exists("Reig")
				# !Global("1000_CLEAN_UP","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# ActionOverride("Reig",DestroySelf())
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_10_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_10_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# ActionOverride("Reig",DestroySelf())
		
		self.iActionOverride("'Reig'", self.iDestroySelf())
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_11(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 11
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Exists("Brohn_Dead")
				# !Global("1000_CLEAN_UP","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# ActionOverride("Brohn_Dead",DestroySelf())
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_11_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_11_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# ActionOverride("Brohn_Dead",DestroySelf())
		
		self.iActionOverride("'Brohn_Dead'", self.iDestroySelf())
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_12(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 12
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Exists("Crandall")
				# !Global("1000_CLEAN_UP","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# ActionOverride("Crandall",DestroySelf())
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_12_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_12_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# ActionOverride("Crandall",DestroySelf())
		
		self.iActionOverride("'Crandall'", self.iDestroySelf())
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_13(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 13
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("BROGAN_LEAVE","GLOBAL",2)
				# Exists("Brogan")
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# ActionOverride("Brogan",DestroySelf())
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_13_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_13_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# ActionOverride("Brogan",DestroySelf())
		
		self.iActionOverride("'Brogan'", self.iDestroySelf())
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_14(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 14
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("BROGAN_LEAVE","GLOBAL",2)
				# !Exists("Brogan")
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("BROGAN_LEAVE","GLOBAL",3)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_14_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_14_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("BROGAN_LEAVE","GLOBAL",3)
		
		self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 3)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_15(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 15
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("MAGDAR_LEAVE","GLOBAL",1)
				# EntirePartyOnMap()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobalTimer("AR1001_Goblin","GLOBAL",15)
		# SetGlobal("MAGDAR_LEAVE","GLOBAL",2)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_15_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_15_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobalTimer("AR1001_Goblin","GLOBAL",15)
		# SetGlobal("MAGDAR_LEAVE","GLOBAL",2)
		
		self.iSetGlobalTimer("'AR1001_Goblin'", "'GLOBAL'", 15)
		self.iSetGlobal("'MAGDAR_LEAVE'", "'GLOBAL'", 2)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_16(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 16
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("Crane_Wheel","GLOBAL",1)
				# EntirePartyOnMap()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("Crane_Wheel","GLOBAL",2)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_16_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_16_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("Crane_Wheel","GLOBAL",2)
		
		self.iSetGlobal("'Crane_Wheel'", "'GLOBAL'", 2)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_17(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 17
		d = {"check": None}
		def do_check():
			if d["check"] is None:
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
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("AR1000_GOBLINS_CLEAR","GLOBAL",1)
		# Deactivate("Horn_Blow")
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_17_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_17_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("AR1000_GOBLINS_CLEAR","GLOBAL",1)
		# Deactivate("Horn_Blow")
		
		self.iSetGlobal("'AR1000_GOBLINS_CLEAR'", "'GLOBAL'", 1)
		self.iDeactivate("'Horn_Blow'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_18(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 18
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("Dock_Goblin_Quest","GLOBAL",0)
				# !Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1002_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1004_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1005_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1007_GOBLINS_CLEAR","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# AddXPVar("Level_2_Very_Hard",26671)  // You have cleared the Targos Docks of goblins.
		# SetGlobal("Dock_Goblin_Quest","GLOBAL",1)
		# AddJournalEntry(27866)  // We managed to drive the last of the goblins off of the Targos Docks.  Reig and Lord Ulbrec should be grateful to hear of our success.
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_18_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_18_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# AddXPVar("Level_2_Very_Hard",26671)  // You have cleared the Targos Docks of goblins.
		# SetGlobal("Dock_Goblin_Quest","GLOBAL",1)
		# AddJournalEntry(27866)  // We managed to drive the last of the goblins off of the Targos Docks.  Reig and Lord Ulbrec should be grateful to hear of our success.
		
		self.iAddXPVar("'Level_2_Very_Hard'", 26671)
		self.iSetGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1)
		self.iAddJournalEntry(27866)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_19(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 19
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("TARGOS_HOSTILE","GLOBAL",0)
				# !Global("TEAM_0","MYAREA",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TARGOS_HOSTILE","GLOBAL",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_19_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_19_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("TARGOS_HOSTILE","GLOBAL",1)
		
		self.iSetGlobal("'TARGOS_HOSTILE'", "'GLOBAL'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_20(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 20
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("TEAM_0","MYAREA",0)
				# !Global("TARGOS_HOSTILE","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TEAM_0","MYAREA",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_20_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_20_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("TEAM_0","MYAREA",1)
		
		self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_21(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 21
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !Global("TOWNIE_DEAD","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TOWNIE_HOSTILE","MYAREA",0)
		# SetGlobal("TOWNIE_DEAD","GLOBAL",0)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_21_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_21_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("TOWNIE_HOSTILE","MYAREA",0)
		# SetGlobal("TOWNIE_DEAD","GLOBAL",0)
		
		self.iSetGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0)
		self.iSetGlobal("'TOWNIE_DEAD'", "'GLOBAL'", 0)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_22(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 22
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# OnCreation()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# NoAction()
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_22_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_22_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# NoAction()
		
		self.iNoAction()
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_23(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 23
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !Global("AR1000_RESET_CUTSCENE","GLOBAL",0)
				# Or(2)
				# EntirePartyOnMap()
				# !InCutsceneMode()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# EndCutSceneMode()
		# SetGlobal("AR1000_RESET_CUTSCENE","GLOBAL",0)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_23_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_23_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# EndCutSceneMode()
		# SetGlobal("AR1000_RESET_CUTSCENE","GLOBAL",0)
		
		self.iEndCutSceneMode()
		self.iSetGlobal("'AR1000_RESET_CUTSCENE'", "'GLOBAL'", 0)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_24(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 24
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !Global("RJ_AR1000","GLOBAL",0)
				# !InCutsceneMode()
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MultiPlayerSync()
		# ResetJoinRequests()
		# SetGlobal("RJ_AR1000","GLOBAL",0)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_24_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_24_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# MultiPlayerSync()
		# ResetJoinRequests()
		# SetGlobal("RJ_AR1000","GLOBAL",0)
		
		self.iMultiPlayerSync()
		self.iResetJoinRequests()
		self.iSetGlobal("'RJ_AR1000'", "'GLOBAL'", 0)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_25(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 25
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("1200_BATTLE_CLEANUP","GLOBAL",0)
				# !Global("Goblin_Palisade_Quest","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("1200_BATTLE_CLEANUP","GLOBAL",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_25_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_25_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# SetGlobal("1200_BATTLE_CLEANUP","GLOBAL",1)
		
		self.iSetGlobal("'1200_BATTLE_CLEANUP'", "'GLOBAL'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_26(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 26
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# IsActive("cat_singles_exterior")
				# !Global("AR1004_CATS_DEAD","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Deactivate("cat_singles_exterior")
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_26_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_26_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# Deactivate("cat_singles_exterior")
		
		self.iDeactivate("'cat_singles_exterior'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_27(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 27
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# IsActive("Horn_Blow")
				# !Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Deactivate("Horn_Blow")
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_27_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_27_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# Deactivate("Horn_Blow")
		
		self.iDeactivate("'Horn_Blow'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_28(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 28
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("Destroy_Shaengarne_Bridge","GLOBAL",0)
				# Global("Shaengarne_Award_XPVar","GLOBAL",0)
				# Global("AR2102_Visited","GLOBAL",1)
				if self.iGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 0) \
					 and self.iGlobal("'Shaengarne_Award_XPVar'", "'GLOBAL'", 0) \
					 and self.iGlobal("'AR2102_Visited'", "'GLOBAL'", 1):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Debug("CBN_SetFlag_Destroy_Shaengarne_Bridge")
		# SetGlobal("Destroy_Shaengarne_Bridge","GLOBAL",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_28_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_28_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# Debug("CBN_SetFlag_Destroy_Shaengarne_Bridge")
		# SetGlobal("Destroy_Shaengarne_Bridge","GLOBAL",1)
		
		self.iDebug("'CBN_SetFlag_Destroy_Shaengarne_Bridge'")
		self.iSetGlobal("'Destroy_Shaengarne_Bridge'", "'GLOBAL'", 1)
		return 0
		
