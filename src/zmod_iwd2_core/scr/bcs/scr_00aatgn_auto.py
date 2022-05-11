import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00AATGN_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptClass (Special 2)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		is_cutscene_execution = self.is_cutscene_mode()
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not is_cutscene_execution: break
			
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
		
