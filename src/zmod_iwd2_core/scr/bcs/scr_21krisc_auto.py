import toee, debug
import inf_scripting
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_21KRISC_Auto(inf_scripting.ScriptBase): # 21KRISC
	# AR2100 20KRIS Kristian ScriptRace (Combat Script)
	
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
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(Myself,ENEMY)
				# HPLostGT(Myself,12)
				# IsSpellTargetValid(Myself,CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(Myself,CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(Myself,CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell("Myself", "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(Nearest(Myself),ENEMY)
				# See(Nearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 3
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(SecondNearest(Myself),ENEMY)
				# See(SecondNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_03_code_01(self, locus)
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 4
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(ThirdNearest(Myself),ENEMY)
				# See(ThirdNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 5
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(FourthNearest(Myself),ENEMY)
				# See(FourthNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 6
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(FifthNearest(Myself),ENEMY)
				# See(FifthNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_06_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 7
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(SixthNearest(Myself),ENEMY)
				# See(SixthNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_07_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 8
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(SeventhNearest(Myself),ENEMY)
				# See(SeventhNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_08_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_09(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 9
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(EighthNearest(Myself),ENEMY)
				# See(EighthNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_09_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_10(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 10
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(NinthNearest(Myself),ENEMY)
				# See(NinthNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_10_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_11(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 11
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
				# Allegiance(TenthNearest(Myself),ENEMY)
				# See(TenthNearest(Myself),0)
				# HPLostGT(LastSeenBy(Myself),12)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_11_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_LIGHT_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_12(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 12
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HasItem("CLDamag",Myself)  // Inflict Light Wounds
				# See(NearestEnemyOf(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# AttackOneRound(LastMarkedObject)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_12_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# AttackOneRound(LastMarkedObject)
		
		self.iAttackOneRound("LastMarkedObject")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_13(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 13
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# ForceMarkedSpell(MARKED_SPELL)
				# SetSpellTarget(Nothing)
				# See(NearestEnemyOf(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MarkSpellAndObject("11071112",Myself,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_PROTECTION_FROM_EVIL, CLERIC_CAUSE_LIGHT_WOUNDS]
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
		
		# MarkSpellAndObject("11071112",Myself,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_PROTECTION_FROM_EVIL, CLERIC_CAUSE_LIGHT_WOUNDS]
		
		self.iMarkSpellAndObject("'11071112'", "Myself", "SPELLCAST_IGNORE_SEE" | "SPELLCAST_IGNORE_VALID_SPELL_TARGET")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_14(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 14
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# !IsMarkedSpell(MARKED_SPELL)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(SpellTarget,MARKED_SPELL)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		# ForceMarkedSpell(MARKED_SPELL)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_14_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(SpellTarget,MARKED_SPELL)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		# ForceMarkedSpell(MARKED_SPELL)
		
		self.iSpell("SpellTarget", "MARKED_SPELL")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		self.iForceMarkedSpell("MARKED_SPELL")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_15(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 15
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# See(NearestEnemyOf(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# EquipWeapon()
		# AttackOneRound(LastMarkedObject)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_15_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# EquipWeapon()
		# AttackOneRound(LastMarkedObject)
		
		self.iEquipWeapon()
		self.iAttackOneRound("LastMarkedObject")
		return 0
		
