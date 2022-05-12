import toee
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_00AATGN_Auto(inf_scripting.ScriptBase): # 00AATGN
	# AR1201 12SHAWFO Shawford_Crale ScriptRace (Combat Script)
	
	@classmethod
	def do_execute(cls, self, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from >= 1:
				break_ = cls.do_execute_block_01(self, code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See(NearestEnemyOf(Myself),0)
		if self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			cls.do_execute_block_01_code_01(self)
			return 1 # break further blocks
		return False
		
	def do_execute_block_01_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# EquipWeapon()
		# AttackOneRound(LastMarkedObject)
		
		self.iEquipWeapon()
		self.iAttackOneRound("LastMarkedObject")
		return
		
