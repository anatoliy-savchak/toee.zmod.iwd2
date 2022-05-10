import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00AMVW05_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_01 ScriptDefault
	
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
		# Global("RW_00AMVW050","LOCALS",0)
		# !NearSavedLocation(5)
		if not self.iTimerActive(19) \
			 and self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
			 and self.iRange("[PC]", 40, "LESS_THAN"):
			# SetGlobal("RW_00AMVW050","LOCALS",1)
			# Continue()
			self.iRandomWalk()
			self.iStartRandomTimer(19, 10, 15)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("RW_00AMVW050","LOCALS",0)
		# NearSavedLocation(5)
		if not self.iTimerActive(19) \
			 and self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
			 and self.iRange("[PC]", 40, "LESS_THAN"):
			# SetGlobal("RW_00AMVW050","LOCALS",0)
			# NoAction()
			self.iRandomWalk()
			self.iStartRandomTimer(19, 10, 15)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("RW_00AMVW050","LOCALS",0)
		# Range([PC],40,LESS_THAN)
		if not self.iTimerActive(19) \
			 and self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
			 and self.iRange("[PC]", 40, "LESS_THAN"):
			# MoveToPoint([-2.-2])
			self.iRandomWalk()
			self.iStartRandomTimer(19, 10, 15)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(19)
		# Global("RW_00AMVW050","LOCALS",0)
		# Range([PC],40,LESS_THAN)
		if not self.iTimerActive(19) \
			 and self.iGlobal("'RW_00AMVW050'", "'LOCALS'", 0) \
			 and self.iRange("[PC]", 40, "LESS_THAN"):
			# RandomWalk()
			# StartRandomTimer(19,10,15)
			self.iRandomWalk()
			self.iStartRandomTimer(19, 10, 15)
			return True # break further blocks
		return False
		
