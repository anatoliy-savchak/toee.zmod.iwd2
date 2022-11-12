import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_00AATKN_Auto(inf_scripting.ScriptBase): # 00AATKN SIMPLE
	# AR2100 20ORCACH GTH01_05 ScriptRace (Combat Script)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_simple(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# IF
		# 	IsWeaponRanged(Myself)
		# 	Range(NearestEnemyOf(Myself),5,LESS_THAN)
		# THEN
		#   RESPONSE #100
		# 		RunAwayFrom(LastMarkedObject,45)
		
		if self.iIsWeaponRanged("Myself") \
			 and self.iRange(self.iNearestEnemyOf("Myself"), 5, "LESS_THAN"):
			
			self.iRunAwayFrom("LastMarkedObject", 45)
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
