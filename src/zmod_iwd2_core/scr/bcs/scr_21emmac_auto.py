import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_21EMMAC_Auto(inf_scripting.ScriptBase): # 21EMMAC SIMPLE
	# AR2100 20EMMA Emma ScriptRace (Combat Script)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_simple(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# IF
		# 	!NumTimesTalkedTo(0)
		# 	!Allegiance(Myself,ENEMY)
		# THEN
		#   RESPONSE #100
		# 		Enemy()
		
		if not self.iNumTimesTalkedTo(0) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			
			self.iEnemy()
			return
		
		# IF
		# 	HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 	HPPercentLT(Myself,20)
		# 	IsSpellTargetValid(Myself,CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
		# THEN
		#   RESPONSE #100
		# 		Spell(Myself,CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Heal") \
			 and self.iHPPercentLT("Myself", 20) \
			 and self.iIsSpellTargetValid("Myself", const_inf.CLERIC_HEAL, 0):
			
			self.iSpell("Myself", const_inf.CLERIC_HEAL)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 	HPLostGT(Myself,29)
		# 	IsSpellTargetValid(Myself,CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(Myself,CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Critical Wounds") \
			 and self.iHPLostGT("Myself", 29) \
			 and self.iIsSpellTargetValid("Myself", const_inf.CLERIC_CURE_CRITICAL_WOUNDS, 0):
			
			self.iSpell("Myself", const_inf.CLERIC_CURE_CRITICAL_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 	HPLostGT(Myself,23)
		# 	IsSpellTargetValid(Myself,CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(Myself,CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Serious Wounds") \
			 and self.iHPLostGT("Myself", 23) \
			 and self.iIsSpellTargetValid("Myself", const_inf.CLERIC_CURE_SERIOUS_WOUNDS, 0):
			
			self.iSpell("Myself", const_inf.CLERIC_CURE_SERIOUS_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 	HPLostGT(Myself,11)
		# 	IsSpellTargetValid(Myself,CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(Myself,CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Moderate Wounds") \
			 and self.iHPLostGT("Myself", 11) \
			 and self.iIsSpellTargetValid("Myself", const_inf.CLERIC_CURE_MODERATE_WOUNDS, 0):
			
			self.iSpell("Myself", const_inf.CLERIC_CURE_MODERATE_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 	See("Kristian",0)
		# 	HPPercentLT(LastSeenBy(Myself),20)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Heal") \
			 and self.iSee("'Kristian'", 0) \
			 and self.iHPPercentLT(self.iLastSeenBy("Myself"), 20) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 	See("Kristian",0)
		# 	HPLostGT(LastSeenBy(Myself),29)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Critical Wounds") \
			 and self.iSee("'Kristian'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 29) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 	See("Kristian",0)
		# 	HPLostGT(LastSeenBy(Myself),23)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Serious Wounds") \
			 and self.iSee("'Kristian'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 23) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 	See("Kristian",0)
		# 	HPLostGT(LastSeenBy(Myself),11)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Moderate Wounds") \
			 and self.iSee("'Kristian'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 11) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 	See("WarriorofVirtue1",0)
		# 	HPPercentLT(LastSeenBy(Myself),20)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Heal") \
			 and self.iSee("'WarriorofVirtue1'", 0) \
			 and self.iHPPercentLT(self.iLastSeenBy("Myself"), 20) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 	See("WarriorofVirtue1",0)
		# 	HPLostGT(LastSeenBy(Myself),29)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Critical Wounds") \
			 and self.iSee("'WarriorofVirtue1'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 29) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 	See("WarriorofVirtue1",0)
		# 	HPLostGT(LastSeenBy(Myself),23)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Serious Wounds") \
			 and self.iSee("'WarriorofVirtue1'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 23) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 	See("WarriorofVirtue1",0)
		# 	HPLostGT(LastSeenBy(Myself),11)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Moderate Wounds") \
			 and self.iSee("'WarriorofVirtue1'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 11) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 	See("WarriorofVirtue2",0)
		# 	HPPercentLT(LastSeenBy(Myself),20)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Heal") \
			 and self.iSee("'WarriorofVirtue2'", 0) \
			 and self.iHPPercentLT(self.iLastSeenBy("Myself"), 20) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 	See("WarriorofVirtue2",0)
		# 	HPLostGT(LastSeenBy(Myself),29)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Critical Wounds") \
			 and self.iSee("'WarriorofVirtue2'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 29) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 	See("WarriorofVirtue2",0)
		# 	HPLostGT(LastSeenBy(Myself),23)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Serious Wounds") \
			 and self.iSee("'WarriorofVirtue2'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 23) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 	See("WarriorofVirtue2",0)
		# 	HPLostGT(LastSeenBy(Myself),11)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Moderate Wounds") \
			 and self.iSee("'WarriorofVirtue2'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 11) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 	See("WarriorofVirtue3",0)
		# 	HPPercentLT(LastSeenBy(Myself),20)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_HEAL,0)  // SPPR607.SPL (Heal)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_HEAL)  // SPPR607.SPL (Heal)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Heal") \
			 and self.iSee("'WarriorofVirtue3'", 0) \
			 and self.iHPPercentLT(self.iLastSeenBy("Myself"), 20) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_HEAL)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 	See("WarriorofVirtue3",0)
		# 	HPLostGT(LastSeenBy(Myself),29)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS,0)  // SPPR502.SPL (Cure Critical Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_CRITICAL_WOUNDS)  // SPPR502.SPL (Cure Critical Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Critical Wounds") \
			 and self.iSee("'WarriorofVirtue3'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 29) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_CRITICAL_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 	See("WarriorofVirtue3",0)
		# 	HPLostGT(LastSeenBy(Myself),23)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS,0)  // SPPR401.SPL (Cure Serious Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_SERIOUS_WOUNDS)  // SPPR401.SPL (Cure Serious Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Serious Wounds") \
			 and self.iSee("'WarriorofVirtue3'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 23) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_SERIOUS_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	HaveSpell(CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 	See("WarriorofVirtue3",0)
		# 	HPLostGT(LastSeenBy(Myself),11)
		# 	IsSpellTargetValid(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS,0)  // SPPR214.SPL (Cure Moderate Wounds)
		# THEN
		#   RESPONSE #100
		# 		Spell(LastSeenBy(Myself),CLERIC_CURE_MODERATE_WOUNDS)  // SPPR214.SPL (Cure Moderate Wounds)
		# 		WaitAnimation(Myself,WALK)
		# 		WaitAnimation(Myself,CONJURE)
		# 		WaitAnimation(Myself,CAST)
		
		if self.iHaveSpell("Cure Moderate Wounds") \
			 and self.iSee("'WarriorofVirtue3'", 0) \
			 and self.iHPLostGT(self.iLastSeenBy("Myself"), 11) \
			 and self.iIsSpellTargetValid(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS, 0):
			
			self.iSpell(self.iLastSeenBy("Myself"), const_inf.CLERIC_CURE_MODERATE_WOUNDS)
			self.iWaitAnimation("Myself", "WALK")
			self.iWaitAnimation("Myself", "CONJURE")
			self.iWaitAnimation("Myself", "CAST")
			return
		
		# IF
		# 	NumTimesTalkedTo(0)
		# 	See([PC],0)
		# THEN
		#   RESPONSE #100
		# 		SetDialogueRange(300)
		# 		Dialogue(LastMarkedObject)
		
		if self.iNumTimesTalkedTo(0) \
			 and self.iSee("[PC]", 0):
			
			self.iSetDialogueRange(300)
			self.iDialogue("LastMarkedObject")
			return
		
		# IF
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("1414","Kristian",0)  // [CLERIC_RECITATION]
		# 		MarkSpellAndObject("14231721",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_WALL_OF_MOONLIGHT, CLERIC_HOLY_WORD]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			self.iMarkSpellAndObject("Recitation", "'Kristian'", 0)
			self.iMarkSpellAndObject(["Wall of Moonlight", "Holy Word"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET)
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
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	NumCreatureGT([ENEMY],1)
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("12261518130313101324250725072507",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_MOON_MOTES, CLERIC_GREATER_COMMAND, CLERIC_DISPEL_MAGIC, CLERIC_MISCAST_MAGIC, CLERIC_HOLY_SMITE, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON]
		# 		MarkSpellAndObject("23062306230612112425",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, CLERIC_SILENCE_15_RADIUS, CLERIC_CONTAGION]
		# 		Continue()
		#   RESPONSE #100
		# 		MarkSpellAndObject("23062306230612112425",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, WIZARD_HOLD_PERSON, CLERIC_SILENCE_15_RADIUS, CLERIC_CONTAGION]
		# 		MarkSpellAndObject("12261518130313101324250725072507",LastMarkedObject,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET | SPELLCAST_RANDOM)  // [CLERIC_MOON_MOTES, CLERIC_GREATER_COMMAND, CLERIC_DISPEL_MAGIC, CLERIC_MISCAST_MAGIC, CLERIC_HOLY_SMITE, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON, WIZARD_DOMINATE_PERSON]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and self.iNumCreatureGT("[ENEMY]", 1) \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			response = toee.game.random_range(1, 200)
			#   RESPONSE #100
			if 0 < response <= 100:
				self.iMarkSpellAndObject(["Moon Motes", "Greater Command", "Dispel Magic", "Miscast Magic", "Holy Smite", "Dominate Person", "Dominate Person", "Dominate Person"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject(["Hold Person", "Hold Person", "Hold Person", "CLERIC_SILENCE_15_RADIUS", "Contagion"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				# continue
				
			#   RESPONSE #100
			if 100 < response <= 200:
				self.iMarkSpellAndObject(["Hold Person", "Hold Person", "Hold Person", "CLERIC_SILENCE_15_RADIUS", "Contagion"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
				self.iMarkSpellAndObject(["Moon Motes", "Greater Command", "Dispel Magic", "Miscast Magic", "Holy Smite", "Dominate Person", "Dominate Person", "Dominate Person"], "LastMarkedObject", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET | const_inf.SPELLCAST_RANDOM)
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
		# 	Or(2)
		# 		HasItem("CMDamag",Myself)  // Inflict Moderate Wounds
		# 		HasItem("MStone",Myself)  // Magic Stone
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		AttackOneRound(LastMarkedObject)
		
		if ( False \
				or self.iHasItem("'CMDamag'", "Myself") \
				or self.iHasItem("'MStone'", "Myself") ) \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			self.iAttackOneRound("LastMarkedObject")
			return
		
		# IF
		# 	ForceMarkedSpell(MARKED_SPELL)
		# 	SetSpellTarget(Nothing)
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		MarkSpellAndObject("131912181106",Myself,SPELLCAST_IGNORE_SEE | SPELLCAST_IGNORE_VALID_SPELL_TARGET)  // [CLERIC_CIRCLE_OF_BONES, CLERIC_CAUSE_MODERATE_WOUNDS, CLERIC_MAGICAL_STONE]
		# 		Continue()
		
		if self.iForceMarkedSpell("MARKED_SPELL") \
			 and self.iSetSpellTarget("Nothing") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			self.iMarkSpellAndObject(["Circle of Bones", "Inflict Moderate Wounds", "CLERIC_MAGICAL_STONE"], "Myself", const_inf.SPELLCAST_IGNORE_SEE | const_inf.SPELLCAST_IGNORE_VALID_SPELL_TARGET)
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
		
		if self.iSee(self.iNearestEnemyOf("Myself"), 0):
			
			self.iEquipWeapon()
			self.iAttackOneRound("LastMarkedObject")
			return
		return
