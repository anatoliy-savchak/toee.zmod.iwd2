import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_21KRISC_Auto(inf_scripting.ScriptBase): # 21KRISC SIMPLE
	# AR2100 20KRIS Kristian ScriptRace (Combat Script)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_simple(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(Myself,ENEMY)
		# 	HPLostGT(Myself,12)
		# 	IsSpellTargetValid(Myself,CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(Myself,CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and self.iHPLostGT("Myself", 12) \
			 and self.iIsSpellTargetValid("Myself", "Cure Light Wounds", 0):
			
			self.iSpell("Myself", const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(Nearest(Myself),ENEMY)
		# 	See(Nearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(SecondNearest(Myself),ENEMY)
		# 	See(SecondNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iSecondNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iSecondNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(ThirdNearest(Myself),ENEMY)
		# 	See(ThirdNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iThirdNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iThirdNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(FourthNearest(Myself),ENEMY)
		# 	See(FourthNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iFourthNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iFourthNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(FifthNearest(Myself),ENEMY)
		# 	See(FifthNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iFifthNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iFifthNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(SixthNearest(Myself),ENEMY)
		# 	See(SixthNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iSixthNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iSixthNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(SeventhNearest(Myself),ENEMY)
		# 	See(SeventhNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iSeventhNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iSeventhNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(EighthNearest(Myself),ENEMY)
		# 	See(EighthNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iEighthNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iEighthNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(NinthNearest(Myself),ENEMY)
		# 	See(NinthNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iNinthNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iNinthNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 	Allegiance(TenthNearest(Myself),ENEMY)
		# 	See(TenthNearest(Myself),0)
		# 	HPLostGT(LastSeenBy(Myself),12)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS,0)  // SPPR103.SPL (Cure Light Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_LIGHT_WOUNDS)  // SPPR103.SPL (Cure Light Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Light Wounds") \
			 and self.iAllegiance(self.iTenthNearest("Myself"), "ENEMY") \
			 and self.iSee(self.iTenthNearest("Myself"), 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 12) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), "Cure Light Wounds", 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_LIGHT_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HasItem("CLDamag",Myself)  // Inflict Light Wounds
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		AttackOneRound(LastMarkedObject)
		
		if self.iHasItem("'CLDamag'", "Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			self.iAttackOneRound("LastMarkedObject")
			return
		
		# IF
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("11071112",Myself,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_PROTECTION_FROM_EVIL, CLERIC_CAUSE_LIGHT_WOUNDS]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			self.iMarkSpellAndObject(["Protection From Evil", "Inflict Light Wounds"], "Myself", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET)
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
		
		if not self.iIsMarkedSpell(const_inf.MARKED_SPELL):
			
			self.iSpell("SpellTarget", const_inf.MARKED_SPELL)
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
