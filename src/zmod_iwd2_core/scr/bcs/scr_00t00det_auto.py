import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00T00DET_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptSpecific
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# !Global("TEAM_0","MYAREA",1)
			# Or(2)
			# HitBy([GOODCUTOFF],CRUSHING)
			# PickPocketFailed([PC])
			if not self.iGlobal("'TEAM_0'", "'MYAREA'", 1) \
				 and ( False \
					or self.iHitBy("[GOODCUTOFF]", "CRUSHING") \
					or self.iPickPocketFailed("[PC]") ):
				# SetGlobal("TEAM_0","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# !Global("TEAM_0","MYAREA",0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iGlobal("'TEAM_0'", "'MYAREA'", 0):
				# Enemy()
				# Continue()
				self.iEnemy()
				pass # continue() - let it pass below
			
			# !Global("TEAM_0","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_0'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_0","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			break # while
		return
		
