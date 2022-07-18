import toee, debug
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_AR1007_Auto(inf_scripting.ScriptBase): # AR1007
	# AR1007 script_area
	
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
				# Global("AR1007_GOBLINS_CLEAR","GLOBAL",0)
				# Dead([ENEMY.0.GOBLIN][0.0.10000.10000])
				# Dead("Goblin_1")
				# Dead("Goblin_2")
				# Dead("Goblin_3")
				# Dead("Goblin_4")
				# Dead("Goblin_5")
				# Dead("Goblin_Sapper_1")
				# Dead("Goblin_Sapper_2")
				# Dead("Goblin_Sapper_3")
				# Dead("Goblin_6")
				# Dead("Goblin_7")
				# Dead("Goblin_8")
				# Dead("Goblin_9")
				# Dead("Goblin_10")
				# Dead("Goblin_11")
				# Dead("Goblin_Sapper_4")
				# Dead("Goblin_Sapper_5")
				# Dead("Goblin_Sapper_6")
				# Dead("Goblin_12")
				# Dead("Goblin_13")
				# Dead("Goblin_14")
				# Dead("Goblin_15")
				# Dead("Goblin_16")
				# Dead("Goblin_17")
				# Dead("Goblin_18")
				# Dead("Goblin_19")
				# Dead("Goblin_20")
				# Dead("Goblin_21")
				# Dead("Goblin_22")
				# Dead("Goblin_23")
				# Dead("Goblin_24")
				# Dead("Goblin_25")
				# Dead("Goblin_26")
				# Dead("Goblin_27")
				# Dead("Goblin_Sapper_7")
				# Dead("Goblin_Sapper_8")
				# Dead("Goblin_Sapper_9")
				# Dead("Goblin_28")
				# Dead("Goblin_29")
				# Dead("Goblin_30")
				# Dead("Goblin_Sapper_10")
				# Dead("Goblin_Sapper_11")
				# Dead("Goblin_Sapper_12")
				# Dead("Goblin_31")
				# Dead("Goblin_32")
				# Dead("Goblin_33")
				# Dead("Rukwurm")
				# Dead("Ulek")
				if self.iOnCreation():
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("AR1007_GOBLINS_CLEAR","GLOBAL",1)
		# Deactivate("Goblins")
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
		
		# SetGlobal("AR1007_GOBLINS_CLEAR","GLOBAL",1)
		# Deactivate("Goblins")
		
		self.iSetGlobal("'AR1007_GOBLINS_CLEAR'", "'GLOBAL'", 1)
		self.iDeactivate("'Goblins'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("Dock_Goblin_Quest","GLOBAL",0)
				# !Global("AR1000_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1002_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1004_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1005_GOBLINS_CLEAR","GLOBAL",0)
				# !Global("AR1007_GOBLINS_CLEAR","GLOBAL",0)
				if self.iOnCreation():
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# AddXPVar("Level_2_Very_Hard",26671)  // You have cleared the Targos Docks of goblins.
		# SetGlobal("Dock_Goblin_Quest","GLOBAL",1)
		# AddJournalEntry(27866)  // We managed to drive the last of the goblins off of the Targos Docks.  Reig and Lord Ulbrec should be grateful to hear of our success.
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_02_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
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
		
		# AddXPVar("Level_2_Very_Hard",26671)  // You have cleared the Targos Docks of goblins.
		# SetGlobal("Dock_Goblin_Quest","GLOBAL",1)
		# AddJournalEntry(27866)  // We managed to drive the last of the goblins off of the Targos Docks.  Reig and Lord Ulbrec should be grateful to hear of our success.
		
		self.iAddXPVar("'Level_2_Very_Hard'", 26671)
		self.iSetGlobal("'Dock_Goblin_Quest'", "'GLOBAL'", 1)
		self.iAddJournalEntry(27866)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 3
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("TARGOS_HOSTILE","GLOBAL",0)
				# !Global("TEAM_0","MYAREA",0)
				if self.iOnCreation():
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TARGOS_HOSTILE","GLOBAL",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_03_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
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
		
		# SetGlobal("TARGOS_HOSTILE","GLOBAL",1)
		
		self.iSetGlobal("'TARGOS_HOSTILE'", "'GLOBAL'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 4
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Global("TEAM_0","MYAREA",0)
				# !Global("TARGOS_HOSTILE","GLOBAL",0)
				if self.iOnCreation():
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TEAM_0","MYAREA",1)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_04_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
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
		
		# SetGlobal("TEAM_0","MYAREA",1)
		
		self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 5
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !Global("TOWNIE_DEAD","GLOBAL",0)
				if self.iOnCreation():
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetGlobal("TOWNIE_HOSTILE","MYAREA",0)
		# SetGlobal("TOWNIE_DEAD","GLOBAL",0)
		# Continue()
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_05_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 0 # continue() - pass further blocks
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
		
		# SetGlobal("TOWNIE_HOSTILE","MYAREA",0)
		# SetGlobal("TOWNIE_DEAD","GLOBAL",0)
		
		self.iSetGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0)
		self.iSetGlobal("'TOWNIE_DEAD'", "'GLOBAL'", 0)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 6
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# OnCreation()
				if self.iOnCreation():
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# NoAction()
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
		
		# NoAction()
		
		self.iNoAction()
		return 0
		
