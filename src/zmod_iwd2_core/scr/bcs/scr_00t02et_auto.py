import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T02ET_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptSpecific
	
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
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("TEAM_2","MYAREA",1)
		# Or(2)
		# AttackedBy([GOODCUTOFF],DEFAULT)
		# PickPocketFailed([PC])
		if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and not self.iCreatureHidden("Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# SetGlobal("TEAM_2","MYAREA",1)
			# Continue()
			self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Allegiance(Myself,ENEMY)
		# !Global("TEAM_2","MYAREA",0)
		if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and not self.iCreatureHidden("Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# Enemy()
			# Continue()
			self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !IsTeamBitOn(TEAM_2_BIT)
		if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and not self.iCreatureHidden("Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# SetTeamBit(TEAM_2_BIT,TRUE)
			# Continue()
			self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("TEAM_2","MYAREA",1)
		# Allegiance(Myself,ENEMY)
		# !CreatureHidden(Myself)
		# See(NearestEnemyOf(Myself),0)
		if not self.iGlobal("'TEAM_2'", "'MYAREA'", 1) \
			 and self.iAllegiance("Myself", "ENEMY") \
			 and not self.iCreatureHidden("Myself") \
			 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
			# SetGlobal("TEAM_2","MYAREA",1)
			# Continue()
			self.iSetGlobal("'TEAM_2'", "'MYAREA'", 1)
			return False # continue() - pass further blocks
		return False
		
