import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10ONBOAT_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptRace (Combat Script)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		is_cutscene_execution = self.is_cutscene_mode()
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_02()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_03()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_04()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_05()
			if break_ and not is_cutscene_execution: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Allegiance(Myself,ENEMY)
		if self.iSee("[ENEMY.0.GOBLIN][1887.703.2801.1043]", 0):
			# ChangeCurrentScript("10aGobG0")
			self.iEquipWeapon()
			self.iAttackOneRound("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !IsTeamBitOn(TEAM_1_BIT)
		if self.iSee("[ENEMY.0.GOBLIN][1887.703.2801.1043]", 0):
			# SetTeamBit(TEAM_1_BIT,TRUE)
			# Continue()
			self.iEquipWeapon()
			self.iAttackOneRound("LastMarkedObject")
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("TEAM_1","MYAREA",1)
		# Allegiance(Myself,ENEMY)
		# !CreatureHidden(Myself)
		# See(NearestEnemyOf(Myself),0)
		if self.iSee("[ENEMY.0.GOBLIN][1887.703.2801.1043]", 0):
			# SetGlobal("TEAM_1","MYAREA",1)
			# Continue()
			self.iEquipWeapon()
			self.iAttackOneRound("LastMarkedObject")
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Allegiance(Myself,ENEMY)
		# See([ENEMY][1887.703.2801.1043],0)
		if self.iSee("[ENEMY.0.GOBLIN][1887.703.2801.1043]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iEquipWeapon()
			self.iAttackOneRound("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See([ENEMY.0.GOBLIN][1887.703.2801.1043],0)
		if self.iSee("[ENEMY.0.GOBLIN][1887.703.2801.1043]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iEquipWeapon()
			self.iAttackOneRound("LastMarkedObject")
			return True # break further blocks
		return False
		
