import toee
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_00AATGN_Auto(inf_scripting.ScriptBase): # 00AATGN
	# AR1201 12SHAWFO Shawford_Crale ScriptRace (Combat Script)
	
	@classmethod
	def do_execute(cls, self, continuous):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not continuous: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See(NearestEnemyOf(Myself),0)
		if self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iEquipWeapon()
			self.iAttackOneRound("LastMarkedObject")
			return True # break further blocks
		return False
		
