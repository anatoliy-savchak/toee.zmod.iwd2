import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00TOWNID_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptSpecial1
	
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
		# Global("TEAM_0","MYAREA",0)
		# !TimerActive(2)
		# Allegiance(Myself,ENEMY)
		# See(NearestEnemyOf(Myself),0)
		if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
			 and not self.iGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0) \
			 and not self.iCreatureHidden("Myself") \
			 and self.iHelp("[ANYTHING]"):
			# StartTimer(2,6)
			# Continue()
			self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
			self.iEnemy()
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Allegiance(Myself,ENEMY)
		# Or(2)
		# AttackedBy([GOODCUTOFF],DEFAULT)
		# PickPocketFailed([PC])
		# Or(13)
		# HitBy([GOODCUTOFF],SLASHING)
		# HitBy([GOODCUTOFF],CRUSHING)
		# HitBy([GOODCUTOFF],PIERCING)
		# HitBy([GOODCUTOFF],MISSILE)
		# HitBy([GOODCUTOFF],FIRE)
		# HitBy([GOODCUTOFF],ELECTRICITY)
		# HitBy([GOODCUTOFF],POISON)
		# HitBy([GOODCUTOFF],MAGIC)
		# HitBy([GOODCUTOFF],COLD)
		# HitBy([GOODCUTOFF],ACID)
		# HitBy([GOODCUTOFF],MAGICFIRE)
		# HitBy([GOODCUTOFF],MAGICCOLD)
		# PickPocketFailed([PC])
		if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
			 and not self.iGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0) \
			 and not self.iCreatureHidden("Myself") \
			 and self.iHelp("[ANYTHING]"):
			# Enemy()
			# SetGlobal("TOWNIE_HOSTILE","MYAREA",1)
			# Help()
			self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
			self.iEnemy()
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Allegiance(Myself,ENEMY)
		# !Global("TEAM_0","MYAREA",0)
		if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
			 and not self.iGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0) \
			 and not self.iCreatureHidden("Myself") \
			 and self.iHelp("[ANYTHING]"):
			# Enemy()
			# Continue()
			self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
			self.iEnemy()
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Dead(Myself)
		if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
			 and not self.iGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0) \
			 and not self.iCreatureHidden("Myself") \
			 and self.iHelp("[ANYTHING]"):
			# ChangeCurrentScript("")
			self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
			self.iEnemy()
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("TEAM_0","MYAREA",0)
		# !Global("TOWNIE_HOSTILE","MYAREA",0)
		# !CreatureHidden(Myself)
		# Help([ANYTHING])
		if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
			 and not self.iGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0) \
			 and not self.iCreatureHidden("Myself") \
			 and self.iHelp("[ANYTHING]"):
			# SetGlobal("TEAM_0","MYAREA",1)
			# Enemy()
			self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
			self.iEnemy()
			return True # break further blocks
		return False
		
