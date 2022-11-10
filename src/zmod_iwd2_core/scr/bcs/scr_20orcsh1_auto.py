import toee, debug
import inf_scripting
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_20ORCSH1_Auto(inf_scripting.ScriptBase): # 20ORCSH1
	# AR2100 20ORCSHM GTH01_07 ScriptRace (Combat Script)
	
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
				# ForceMarkedSpell(MARKED_SPELL)
				# SetSpellTarget(Nothing)
				# HPLostGT(Myself,25)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MarkSpellAndObject("1214",Myself,SPELLCAST_IGNORE_SEE)  // [CLERIC_CURE_MODERATE_WOUNDS]
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
		
		# MarkSpellAndObject("1214",Myself,SPELLCAST_IGNORE_SEE)  // [CLERIC_CURE_MODERATE_WOUNDS]
		
		self.iMarkSpellAndObject("'1214'", "Myself", "SPELLCAST_IGNORE_SEE")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# IsMarkedSpell(MARKED_SPELL)
				# HPLostGT(Nearest(Myself),25)
				# See(Nearest(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MarkSpellAndObject("1214",LastSeenBy(Myself),SPELLCAST_IGNORE_SEE)  // [CLERIC_CURE_MODERATE_WOUNDS]
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
		
		# MarkSpellAndObject("1214",LastSeenBy(Myself),SPELLCAST_IGNORE_SEE)  // [CLERIC_CURE_MODERATE_WOUNDS]
		
		self.iMarkSpellAndObject("'1214'", self.iLastSeenBy("Myself"), "SPELLCAST_IGNORE_SEE")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 3
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
	def do_execute_block_04(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 4
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# HaveSpell(WIZARD_DEATH_ARMOR)  // SPWI228.SPL (Death Armor)
				# HPPercentLT(Myself,100)
				# IsSpellTargetValid(Myself,WIZARD_DEATH_ARMOR,0)  // SPWI228.SPL (Death Armor)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# Spell(Myself,WIZARD_DEATH_ARMOR)  // SPWI228.SPL (Death Armor)
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
		
		# Spell(Myself,WIZARD_DEATH_ARMOR)  // SPWI228.SPL (Death Armor)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		
		self.iSpell("Myself", "WIZARD_DEATH_ARMOR")
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
				# ForceMarkedSpell(MARKED_SPELL)
				# SetSpellTarget(Nothing)
				# !Global("OBJ_SP_20ORCSH1_1","LOCALS",-1)
				# See(NearestEnemyOf(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# MarkSpellAndObject("1201",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [CLERIC_AID]
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
		
		# MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# MarkSpellAndObject("1201",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [CLERIC_AID]
		
		self.iMarkSpellAndObject("'2230'", self.iFarthestEnemyOf("Myself"), "SPELLCAST_RANDOM")
		self.iMarkSpellAndObject("'1201'", "[ENEMY.0.ORC]", "SPELLCAST_RANDOM")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 6
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
		# SetGlobal("OBJ_SP_20ORCSH1_1","LOCALS",-1)
		
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
		
		# Spell(SpellTarget,MARKED_SPELL)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		# ForceMarkedSpell(MARKED_SPELL)
		# SetGlobal("OBJ_SP_20ORCSH1_1","LOCALS",-1)
		
		self.iSpell("SpellTarget", "MARKED_SPELL")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		self.iForceMarkedSpell("MARKED_SPELL")
		self.iSetGlobal("'OBJ_SP_20ORCSH1_1'", "'LOCALS'", -1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 7
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# ForceMarkedSpell(MARKED_SPELL)
				# SetSpellTarget(Nothing)
				# !Global("OBJ_SP_20ORCSH1_2","LOCALS",-1)
				# See(NearestEnemyOf(Myself),0)
				if self.iSee(self.iNearestEnemyOf("Myself"), 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# MarkSpellAndObject("1203",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_CHANT]
		# MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
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
		
		# MarkSpellAndObject("1203",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_CHANT]
		# MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		
		self.iMarkSpellAndObject("'1203'", "LastMarkedObject", "SPELLCAST_IGNORE_SEE" | "SPELLCAST_IGNORE_VALID_SPELL_TARGET" | "SPELLCAST_RANDOM")
		self.iMarkSpellAndObject("'2230'", self.iFarthestEnemyOf("Myself"), "SPELLCAST_RANDOM")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 8
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
		# SetGlobal("OBJ_SP_20ORCSH1_2","LOCALS",-1)
		
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
		
		# Spell(SpellTarget,MARKED_SPELL)
		# WaitAnimation(Myself,WALK)
		# WaitAnimation(Myself,CONJURE)
		# WaitAnimation(Myself,CAST)
		# ForceMarkedSpell(MARKED_SPELL)
		# SetGlobal("OBJ_SP_20ORCSH1_2","LOCALS",-1)
		
		self.iSpell("SpellTarget", "MARKED_SPELL")
		self.iWaitAnimation("Myself", "WALK")
		self.iWaitAnimation("Myself", "CONJURE")
		self.iWaitAnimation("Myself", "CAST")
		self.iForceMarkedSpell("MARKED_SPELL")
		self.iSetGlobal("'OBJ_SP_20ORCSH1_2'", "'LOCALS'", -1)
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_09(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 9
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
		
		# MarkSpellAndObject("110223061117",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_COMMAND, WIZARD_HOLD_PERSON, CLERIC_FROST_FINGERS]
		# MarkSpellAndObject("2214",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [WIZARD_STRENGTH]
		# MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
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
		
		# MarkSpellAndObject("110223061117",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_COMMAND, WIZARD_HOLD_PERSON, CLERIC_FROST_FINGERS]
		# MarkSpellAndObject("2214",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [WIZARD_STRENGTH]
		# MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		
		self.iMarkSpellAndObject("'110223061117'", "LastMarkedObject", "SPELLCAST_IGNORE_SEE" | "SPELLCAST_IGNORE_VALID_SPELL_TARGET" | "SPELLCAST_RANDOM")
		self.iMarkSpellAndObject("'2214'", "[ENEMY.0.ORC]", "SPELLCAST_RANDOM")
		self.iMarkSpellAndObject("'2230'", self.iFarthestEnemyOf("Myself"), "SPELLCAST_RANDOM")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_10(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 10
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
	def do_execute_block_11(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 11
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
		
		# EquipWeapon()
		# AttackOneRound(LastMarkedObject)
		
		self.iEquipWeapon()
		self.iAttackOneRound("LastMarkedObject")
		return 0
		
