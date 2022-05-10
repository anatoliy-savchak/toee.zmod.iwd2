import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T05M_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_04 ScriptGeneral (Special 3)
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_5","MYAREA",1)
			# Exists(NearestPC)
			# !See(NearestPC,0)
			if self.iGlobal("'TEAM_5'", "'MYAREA'", 1) \
				 and self.iExists("NearestPC") \
				 and not self.iSee("NearestPC", 0):
				# MoveToObject(NearestPC)
				self.iMoveToObject("NearestPC")
				break
			
			break # while
		return
		
