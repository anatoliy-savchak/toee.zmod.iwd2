import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T04T_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOB 1000_Goblin_02 ScriptSpecific
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_4","MYAREA",1)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_4'", "'MYAREA'", 1) \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_4","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_4'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !IsTeamBitOn(TEAM_4_BIT)
			if not self.iIsTeamBitOn("TEAM_4_BIT"):
				# SetTeamBit(TEAM_4_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_4_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_4","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_4'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_4","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_4'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
