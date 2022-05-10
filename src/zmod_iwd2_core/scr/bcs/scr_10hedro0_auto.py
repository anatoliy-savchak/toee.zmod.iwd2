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
		while True:
			# !TimerActive(18)
			# Global("SCREED_DEAD","GLOBAL",0)
			# !Allegiance(Myself,ENEMY)
			# !Exists("SCREED")
			if not self.iTimerActive(18) \
				 and self.iGlobal("'SCREED_DEAD'", "'GLOBAL'", 0) \
				 and not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iExists("'SCREED'"):
				# FloatMessage(Myself,8117)  // "Get yer ass back on the boat!"
				# StartRandomTimer(18,3,6)
				# Continue()
				self.iFloatMessage("Myself", 8117)
				self.iStartRandomTimer(18, 3, 6)
				pass # continue() - let it pass below
			
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
				pass # continue() - let it pass below
			
			break # while
		return
		
