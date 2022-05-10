import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10JORUN0_Auto(inf_scripting.ScriptBase):
	# AR1000 10JORUN Jorun ScriptGeneral
	
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
		# !TimerActive(18)
		# Global("Dock_Goblin_Quest","GLOBAL",0)
		if not self.iGlobal("'JORUN_FLOAT'", "'LOCALS'", 0):
			# FloatMessage(Myself,1670)  // "Damn fool goblins, thinkin' to torch me boat..."
			# StartTimer(18,5)
			# Continue()
			self.iSetGlobal("'JORUN_FLOAT'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("JORUN_FLOAT","LOCALS",0)
		# NearSavedLocation(1)
		if not self.iGlobal("'JORUN_FLOAT'", "'LOCALS'", 0):
			# SetGlobal("JORUN_FLOAT","LOCALS",0)
			# Face(W)
			self.iSetGlobal("'JORUN_FLOAT'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Global("JORUN_FLOAT","LOCALS",0)
		if not self.iGlobal("'JORUN_FLOAT'", "'LOCALS'", 0):
			# SetGlobal("JORUN_FLOAT","LOCALS",0)
			# Continue()
			self.iSetGlobal("'JORUN_FLOAT'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
