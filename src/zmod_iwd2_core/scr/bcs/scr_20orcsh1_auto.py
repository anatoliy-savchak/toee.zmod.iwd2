import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_20ORCSH1_Auto(inf_scripting.ScriptBase): # 20ORCSH1 SIMPLE
	# AR2100 20ORCSHM GTH01_07 ScriptRace (Combat Script)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_simple(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# IF
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	HPLostGT(Myself,25)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("1214",Myself,SPELLCAST_IGNORE_SEE)  // [CLERIC_CURE_MODERATE_WOUNDS]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and self.iHPLostGT("Myself", 25):
			
			self.iMarkSpellAndObject("Cure Moderate Wounds", "Myself", const_inf.SPELLCAST_IGNORE_SEE)
			# continue
		
		# IF
		# 	IsMarkedSpell(MARKED_SPELL)
		# 	HPLostGT(Nearest(Myself),25)
		# 	See(Nearest(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("1214",LastSeenBy(Myself),SPELLCAST_IGNORE_SEE)  // [CLERIC_CURE_MODERATE_WOUNDS]
		# 		Continue()
		
		if self.iIsMarkedSpell("MARKED_SPELL") \
			 and self.iHPLostGT(self.iNearest("Myself"), 25) \
			 and self.iSee(self.iNearest("Myself"), 0):
			
			self.iMarkSpellAndObject("Cure Moderate Wounds", self.iLastSeenBy("Myself"), const_inf.SPELLCAST_IGNORE_SEE)
			# continue
		
		# IF
		# 	!IsMarkedSpell(MARKED_SPELL)
		# THEN
		#   RESPONSE #100
		# 		Spell(SpellTarget,MARKED_SPELL)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		# 		ForceMarkedSpell(MARKED_SPELL)
		
		if not self.iIsMarkedSpell("MARKED_SPELL"):
			
			self.iSpell("SpellTarget", "MARKED_SPELL")
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			self.iForceMarkedSpell("MARKED_SPELL")
			return
		
		# IF
		# 	HaveSpell(WIZARD_DEATH_ARMOR)  // SPWI228.SPL (Death Armor)
		# 	HPPercentLT(Myself,100)
		# 	IsSpellTargetValid(Myself,WIZARD_DEATH_ARMOR,0)  // SPWI228.SPL (Death Armor)
		# THEN
		#   RESPONSE #100
		# 		Spell(Myself,WIZARD_DEATH_ARMOR)  // SPWI228.SPL (Death Armor)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Death Armor") \
			 and self.iHPPercentLT("Myself", 100) \
			 and self.iIsSpellTargetValid("Myself", "Death Armor", 0):
			
			self.iSpell("Myself", "WIZARD_DEATH_ARMOR")
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	!Global("OBJ_SP_20ORCSH1_1","LOCALS",-1)
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# 		MarkSpellAndObject("1201",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [CLERIC_AID]
		# 		Continue()
		#   RESPONSE #100
		# 		MarkSpellAndObject("1201",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [CLERIC_AID]
		# 		MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and not self.iGlobal("'OBJ_SP_20ORCSH1_1'", "'LOCALS'", -1) \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			response = toee.game.random_range(1, 200)
			#   RESPONSE #100
			if 0 < response <= 100:
				self.iMarkSpellAndObject("Summon Monster II", self.iFarthestEnemyOf("Myself"), const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Aid", "[ENEMY.0.ORC]", const_inf.SPELLCAST_RANDOM)
				# continue
				
			#   RESPONSE #100
			if 100 < response <= 200:
				self.iMarkSpellAndObject("Aid", "[ENEMY.0.ORC]", const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Summon Monster II", self.iFarthestEnemyOf("Myself"), const_inf.SPELLCAST_RANDOM)
				# continue
		
		# IF
		# 	!IsMarkedSpell(MARKED_SPELL)
		# THEN
		#   RESPONSE #100
		# 		Spell(SpellTarget,MARKED_SPELL)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		# 		ForceMarkedSpell(MARKED_SPELL)
		# 		SetGlobal("OBJ_SP_20ORCSH1_1","LOCALS",-1)
		
		if not self.iIsMarkedSpell("MARKED_SPELL"):
			
			self.iSpell("SpellTarget", "MARKED_SPELL")
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			self.iForceMarkedSpell("MARKED_SPELL")
			self.iSetGlobal("'OBJ_SP_20ORCSH1_1'", "'LOCALS'", -1)
			return
		
		# IF
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	!Global("OBJ_SP_20ORCSH1_2","LOCALS",-1)
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("1203",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_CHANT]
		# 		MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# 		Continue()
		#   RESPONSE #100
		# 		MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# 		MarkSpellAndObject("1203",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_CHANT]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and not self.iGlobal("'OBJ_SP_20ORCSH1_2'", "'LOCALS'", -1) \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			response = toee.game.random_range(1, 200)
			#   RESPONSE #100
			if 0 < response <= 100:
				self.iMarkSpellAndObject("Chant", "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Summon Monster II", self.iFarthestEnemyOf("Myself"), const_inf.SPELLCAST_RANDOM)
				# continue
				
			#   RESPONSE #100
			if 100 < response <= 200:
				self.iMarkSpellAndObject("Summon Monster II", self.iFarthestEnemyOf("Myself"), const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Chant", "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				# continue
		
		# IF
		# 	!IsMarkedSpell(MARKED_SPELL)
		# THEN
		#   RESPONSE #100
		# 		Spell(SpellTarget,MARKED_SPELL)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		# 		ForceMarkedSpell(MARKED_SPELL)
		# 		SetGlobal("OBJ_SP_20ORCSH1_2","LOCALS",-1)
		
		if not self.iIsMarkedSpell("MARKED_SPELL"):
			
			self.iSpell("SpellTarget", "MARKED_SPELL")
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			self.iForceMarkedSpell("MARKED_SPELL")
			self.iSetGlobal("'OBJ_SP_20ORCSH1_2'", "'LOCALS'", -1)
			return
		
		# IF
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("110223061117",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_COMMAND, WIZARD_HOLD_PERSON, CLERIC_FROST_FINGERS]
		# 		MarkSpellAndObject("2214",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [WIZARD_STRENGTH]
		# 		MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# 		Continue()
		#   RESPONSE #100
		# 		MarkSpellAndObject("2214",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [WIZARD_STRENGTH]
		# 		MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# 		MarkSpellAndObject("110223061117",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_COMMAND, WIZARD_HOLD_PERSON, CLERIC_FROST_FINGERS]
		# 		Continue()
		#   RESPONSE #100
		# 		MarkSpellAndObject("2230",FarthestEnemyOf(Myself),SPELLCAST_RANDOM)  // [WIZARD_SUMMON_MONSTER_II]
		# 		MarkSpellAndObject("110223061117",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_COMMAND, WIZARD_HOLD_PERSON, CLERIC_FROST_FINGERS]
		# 		MarkSpellAndObject("2214",[ENEMY.0.ORC],SPELLCAST_RANDOM)  // [WIZARD_STRENGTH]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			response = toee.game.random_range(1, 300)
			#   RESPONSE #100
			if 0 < response <= 100:
				self.iMarkSpellAndObject(["Command", "Hold Person", "Frost Fingers"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Bull's Strength", "[ENEMY.0.ORC]", const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Summon Monster II", self.iFarthestEnemyOf("Myself"), const_inf.SPELLCAST_RANDOM)
				# continue
				
			#   RESPONSE #100
			if 100 < response <= 200:
				self.iMarkSpellAndObject("Bull's Strength", "[ENEMY.0.ORC]", const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Summon Monster II", self.iFarthestEnemyOf("Myself"), const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject(["Command", "Hold Person", "Frost Fingers"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				# continue
				
			#   RESPONSE #100
			if 200 < response <= 300:
				self.iMarkSpellAndObject("Summon Monster II", self.iFarthestEnemyOf("Myself"), const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject(["Command", "Hold Person", "Frost Fingers"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject("Bull's Strength", "[ENEMY.0.ORC]", const_inf.SPELLCAST_RANDOM)
				# continue
		
		# IF
		# 	!IsMarkedSpell(MARKED_SPELL)
		# THEN
		#   RESPONSE #100
		# 		Spell(SpellTarget,MARKED_SPELL)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		# 		ForceMarkedSpell(MARKED_SPELL)
		
		if not self.iIsMarkedSpell("MARKED_SPELL"):
			
			self.iSpell("SpellTarget", "MARKED_SPELL")
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			self.iForceMarkedSpell("MARKED_SPELL")
			return
		
		# IF
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		EquipWeapon()
		# 		AttackOneRound(LastMarkedObject)
		
		# SUPPRESSED
		return
