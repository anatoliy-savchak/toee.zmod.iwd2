import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_00AATGN_Auto(inf_scripting.ScriptBase): # 00AATGN SIMPLE
	# AR2100 21GAERNT Gaernat Sharptooth ScriptRace (Combat Script)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_simple(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# IF
		# 	See(NearestEnemyOf(Myself),0)
		# THEN
		#   RESPONSE #100
		# 		EquipWeapon()
		# 		AttackOneRound(LastMarkedObject)
		
		# SUPPRESSED
		return
