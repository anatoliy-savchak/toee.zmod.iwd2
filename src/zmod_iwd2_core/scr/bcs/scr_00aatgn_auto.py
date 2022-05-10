import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00AATGN_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptClass
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# See(NearestEnemyOf(Myself),0)
			if self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			break # while
		return
		
