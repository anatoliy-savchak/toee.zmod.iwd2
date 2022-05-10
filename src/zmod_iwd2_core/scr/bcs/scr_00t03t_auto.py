import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T03T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptSpecific
	
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
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("TEAM_3","MYAREA",1)
		# Or(2)
		# AttackedBy([GOODCUTOFF],DEFAULT)
		# PickPocketFailed([PC])
		if not self.iGlobal("'TEAM_3'", "'MYAREA'", 1) \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and not self.iCreatureHidden("Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# SetGlobal("TEAM_3","MYAREA",1)
			# Continue()
			self.iSetGlobal("'TEAM_3'", "'MYAREA'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !IsTeamBitOn(TEAM_3_BIT)
		if not self.iGlobal("'TEAM_3'", "'MYAREA'", 1) \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and not self.iCreatureHidden("Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# SetTeamBit(TEAM_3_BIT,TRUE)
			# Continue()
			self.iSetGlobal("'TEAM_3'", "'MYAREA'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("TEAM_3","MYAREA",1)
		# Allegiance(Myself,ENEMY)
		# !CreatureHidden(Myself)
		# See(NearestEnemyOf(Myself),0)
		if not self.iGlobal("'TEAM_3'", "'MYAREA'", 1) \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and not self.iCreatureHidden("Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# SetGlobal("TEAM_3","MYAREA",1)
			# Continue()
			self.iSetGlobal("'TEAM_3'", "'MYAREA'", 1)
			return False # continue() - pass further blocks
		return False
		
