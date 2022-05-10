import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10HEDRO0_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptSpecial1
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		is_cutscene_execution = self.is_cutscene_mode()
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_02()
			if break_ and not is_cutscene_execution: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(18)
		# Global("SCREED_DEAD","GLOBAL",0)
		# !Allegiance(Myself,ENEMY)
		# !Exists("SCREED")
		if not self.iTimerActive(18) \
			 and self.iGlobal("'ELDGULL_DEAD'", "'GLOBAL'", 0) \
			 and not self.iAllegiance("Myself", "ENEMY") \
			 and not self.iExists("'ELDGULL'"):
			# FloatMessage(Myself,8117)  // "Get yer ass back on the boat!"
			# StartRandomTimer(18,3,6)
			# Continue()
			self.iFloatMessage("Myself", 8117)
			self.iStartRandomTimer(18, 3, 6)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(18)
		# Global("ELDGULL_DEAD","GLOBAL",0)
		# !Allegiance(Myself,ENEMY)
		# !Exists("ELDGULL")
		if not self.iTimerActive(18) \
			 and self.iGlobal("'ELDGULL_DEAD'", "'GLOBAL'", 0) \
			 and not self.iAllegiance("Myself", "ENEMY") \
			 and not self.iExists("'ELDGULL'"):
			# FloatMessage(Myself,8117)  // "Get yer ass back on the boat!"
			# StartRandomTimer(18,3,6)
			# Continue()
			self.iFloatMessage("Myself", 8117)
			self.iStartRandomTimer(18, 3, 6)
			return False # continue() - pass further blocks
		return False
		
