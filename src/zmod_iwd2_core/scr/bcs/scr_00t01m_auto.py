import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T01M_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptGeneral
	
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
		# Global("TEAM_1","MYAREA",1)
		# Exists(NearestPC)
		# !See(NearestPC,0)
		if self.iGlobal("'TEAM_1'", "'MYAREA'", 1) \
			 and self.iExists("NearestPC") \
			 and not self.iSee("NearestPC", 0):
			# MoveToObject(NearestPC)
			self.iMoveToObject("NearestPC")
			return True # break further blocks
		return False
		
