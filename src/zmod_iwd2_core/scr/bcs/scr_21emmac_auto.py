import toee, debug
import inf_scripting
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_21EMMAC_Auto(inf_scripting.ScriptBase): # 21EMMAC
	# AR2100 20EMMA Emma ScriptRace (Combat Script)
	
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
			
			if not block_from or block_from <= 29:
				break_ = cls.do_execute_block_29(self, locus, code_from=code_from if code_from and block_from == 29 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 30:
				break_ = cls.do_execute_block_30(self, locus, code_from=code_from if code_from and block_from == 30 else None)
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
				# !NumTimesTalkedTo(0)
				# !Allegiance(Myself,ENEMY)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Enemy()
		
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
		
		# Enemy()
		
		self.iEnemy()
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
				# HPPercentLT(Myself,20)
				# IsSpellTargetValid(Myself,CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(Myself,CLERIC_HEAL)  // SPPR607.SPL (Heal)
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
		
		# Spell(Myself,CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell("Myself", "CLERIC_HEAL")
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
				# HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
				# HPLostGT(Myself,29)
				# IsSpellTargetValid(Myself,CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(Myself,CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
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
		
		# Spell(Myself,CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell("Myself", "CLERIC_CURE_CRITICAL_WOUNDS")
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
				# HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
				# HPLostGT(Myself,23)
				# IsSpellTargetValid(Myself,CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(Myself,CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
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
		
		# Spell(Myself,CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell("Myself", "CLERIC_CURE_SERIOUS_WOUNDS")
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
				# HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
				# HPLostGT(Myself,11)
				# IsSpellTargetValid(Myself,CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(Myself,CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
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
		
		# Spell(Myself,CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell("Myself", "CLERIC_CURE_MODERATE_WOUNDS")
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
				# HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
				# See("Kristian",0)
				# HPPercentLT(LastSeenBy(Myself),20)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
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
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_HEAL")
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
				# HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
				# See("Kristian",0)
				# HPLostGT(LastSeenBy(Myself),29)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_CRITICAL_WOUNDS")
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
				# HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
				# See("Kristian",0)
				# HPLostGT(LastSeenBy(Myself),23)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_SERIOUS_WOUNDS")
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
				# HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
				# See("Kristian",0)
				# HPLostGT(LastSeenBy(Myself),11)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_MODERATE_WOUNDS")
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
				# HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
				# See("WarriorofVirtue1",0)
				# HPPercentLT(LastSeenBy(Myself),20)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
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
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_HEAL")
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
				# HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
				# See("WarriorofVirtue1",0)
				# HPLostGT(LastSeenBy(Myself),29)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_CRITICAL_WOUNDS")
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
				# HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
				# See("WarriorofVirtue1",0)
				# HPLostGT(LastSeenBy(Myself),23)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_SERIOUS_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_13(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 13
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
				# See("WarriorofVirtue1",0)
				# HPLostGT(LastSeenBy(Myself),11)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_13_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_MODERATE_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_14(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 14
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
				# See("WarriorofVirtue2",0)
				# HPPercentLT(LastSeenBy(Myself),20)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
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
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_HEAL")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_15(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 15
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
				# See("WarriorofVirtue2",0)
				# HPLostGT(LastSeenBy(Myself),29)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_CRITICAL_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_16(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 16
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
				# See("WarriorofVirtue2",0)
				# HPLostGT(LastSeenBy(Myself),23)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_16_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_SERIOUS_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_17(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 17
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
				# See("WarriorofVirtue2",0)
				# HPLostGT(LastSeenBy(Myself),11)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_17_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_MODERATE_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_18(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 18
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
				# See("WarriorofVirtue3",0)
				# HPPercentLT(LastSeenBy(Myself),20)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_18_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_HEAL")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_19(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 19
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
				# See("WarriorofVirtue3",0)
				# HPLostGT(LastSeenBy(Myself),29)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_19_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_CRITICAL_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_20(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 20
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
				# See("WarriorofVirtue3",0)
				# HPLostGT(LastSeenBy(Myself),23)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_20_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_SERIOUS_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_21(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 21
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
				# See("WarriorofVirtue3",0)
				# HPLostGT(LastSeenBy(Myself),11)
				# IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_21_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell(self.iLastSeenBy("Myself"), "CLERIC_CURE_MODERATE_WOUNDS")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_22(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 22
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# NumTimesTalkedTo(0)
				# See([PC],0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# SetDialogueRange(300)
		# Dialogue(LastMarkedObject)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_22_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# SetDialogueRange(300)
		# Dialogue(LastMarkedObject)
		
		self.iSetDialogueRange(300)
		self.iDialogue("LastMarkedObject")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_23(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 23
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
		
		# MarkSpellAndObject("1414","Kristian",0)  // [CLERIC_RECITATION]
		# MarkSpellAndObject("14231721",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_WALL_OF_MOONLIGHT, CLERIC_HOLY_WORD]
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
		
		# MarkSpellAndObject("1414","Kristian",0)  // [CLERIC_RECITATION]
		# MarkSpellAndObject("14231721",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_WALL_OF_MOONLIGHT, CLERIC_HOLY_WORD]
		
		self.iMarkSpellAndObject("'1414'", "'Kristian'", 0)
		self.iMarkSpellAndObject("'14231721'", "LastMarkedObject", "SPELLCAST_IGNORE_SEE" | "SPELLCAST_IGNORE_VALID_SPELL_TARGET")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_24(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 24
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
			break_ = cls.do_execute_block_24_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
	def do_execute_block_25(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 25
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# ForceMarkedSpell(MARKED_SPELL)
				# SetSpellTarget(Nothing)
				# NumCreatureGT([ENEMY],1)
				# See(NearestEnemyOf(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MarkSpellAndObject("12261518130313101324250725072507",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_MOON_MOTES, CLERIC_GREATER_COMMAND, CLERIC_DISPEL_MAGIC, CLERIC_MISCAST_MAGIC, CLERIC_HOLY_SMITE, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON]
		# MarkSpellAndObject("23062306230612112425",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, CLERIC_SILENCE_15_RADIUS, CLERIC_CONTAGION]
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
		
		# MarkSpellAndObject("12261518130313101324250725072507",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_MOON_MOTES, CLERIC_GREATER_COMMAND, CLERIC_DISPEL_MAGIC, CLERIC_MISCAST_MAGIC, CLERIC_HOLY_SMITE, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON]
		# MarkSpellAndObject("23062306230612112425",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, CLERIC_SILENCE_15_RADIUS, CLERIC_CONTAGION]
		
		self.iMarkSpellAndObject("'12261518130313101324250725072507'", "LastMarkedObject", "SPELLCAST_IGNORE_SEE" | "SPELLCAST_IGNORE_VALID_SPELL_TARGET" | "SPELLCAST_RANDOM")
		self.iMarkSpellAndObject("'23062306230612112425'", "LastMarkedObject", "SPELLCAST_IGNORE_SEE" | "SPELLCAST_IGNORE_VALID_SPELL_TARGET" | "SPELLCAST_RANDOM")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_26(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 26
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
			break_ = cls.do_execute_block_26_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
	def do_execute_block_27(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 27
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# Or(2)
				# HasItem("CMDamag",Myself)  // Inflict Moderate Wounds
				# HasItem("MStone",Myself)  // Magic Stone
				# See(NearestEnemyOf(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# AttackOneRound(LastMarkedObject)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_27_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
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
		
		# AttackOneRound(LastMarkedObject)
		
		self.iAttackOneRound("LastMarkedObject")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_28(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 28
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
		
		# MarkSpellAndObject("131912181106",Myself,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_CIRCLE_OF_BONES, CLERIC_CAUSE_MODERATE_WOUNDS, CLERIC_MAGICAL_STONE]
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
		
		# MarkSpellAndObject("131912181106",Myself,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_CIRCLE_OF_BONES, CLERIC_CAUSE_MODERATE_WOUNDS, CLERIC_MAGICAL_STONE]
		
		self.iMarkSpellAndObject("'131912181106'", "Myself", "SPELLCAST_IGNORE_SEE" | "SPELLCAST_IGNORE_VALID_SPELL_TARGET")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_29(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 29
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
			break_ = cls.do_execute_block_29_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_29_code_01(cls, self, locus):
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
	def do_execute_block_30(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 30
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
			break_ = cls.do_execute_block_30_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_30_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# EquipWeapon()
		# AttackOneRound(LastMarkedObject)
		
		self.iEquipWeapon()
		self.iAttackOneRound("LastMarkedObject")
		return 0
		
