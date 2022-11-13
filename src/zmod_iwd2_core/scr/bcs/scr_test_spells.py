import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_TestSpells(inf_scripting.ScriptBase): # 20ORCSH1 SIMPLE
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
			 and self.iHPLostGT("Myself", 5):
			
			self.iMarkSpellAndObject("Cure Moderate Wounds", "Myself", const_inf.SPELLCAST_IGNORE_SEE)
		
		return