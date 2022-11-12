import toee, debug
import inf_scripting, const_inf
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_21WOVC_Auto(inf_scripting.ScriptBase): # 21WOVC SIMPLE
	# AR2100 20KNTVIR WarriorofVirtue1 ScriptRace (Combat Script)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_simple(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# IF
		# 	True()
		# THEN
		#   RESPONSE #100
		# 		ChangeCurrentScript("00aAtGN")
		
		if True:
			
			self.iChangeCurrentScript("'00aAtGN'")
			return
		return
