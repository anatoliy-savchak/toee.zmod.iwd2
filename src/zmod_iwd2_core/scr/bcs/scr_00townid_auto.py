import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_00TOWNID_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptSpecial1
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("TEAM_0","MYAREA",0)
			# !TimerActive(2)
			# Allegiance(Myself,ENEMY)
			# See(NearestEnemyOf(Myself),0)
			if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
				 and not self.iTimerActive(2) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# StartTimer(2,6)
				# Continue()
				self.iStartTimer(2, 6)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# Or(2)
			# AttackedBy([GOODCUTOFF],DEFAULT)
			# PickPocketFailed([PC])
			# Or(13)
			# HitBy([GOODCUTOFF],SLASHING)
			# HitBy([GOODCUTOFF],CRUSHING)
			# HitBy([GOODCUTOFF],PIERCING)
			# HitBy([GOODCUTOFF],MISSILE)
			# HitBy([GOODCUTOFF],FIRE)
			# HitBy([GOODCUTOFF],ELECTRICITY)
			# HitBy([GOODCUTOFF],POISON)
			# HitBy([GOODCUTOFF],MAGIC)
			# HitBy([GOODCUTOFF],COLD)
			# HitBy([GOODCUTOFF],ACID)
			# HitBy([GOODCUTOFF],MAGICFIRE)
			# HitBy([GOODCUTOFF],MAGICCOLD)
			# PickPocketFailed([PC])
			if not self.iAllegiance("Myself", "ENEMY") \
				 and ( False \
					or self.iAttackedBy("[GOODCUTOFF]", "DEFAULT") \
					or self.iPickPocketFailed("[PC]") ) \
				 and ( False \
					or self.iHitBy("[GOODCUTOFF]", "SLASHING") \
					or self.iHitBy("[GOODCUTOFF]", "CRUSHING") \
					or self.iHitBy("[GOODCUTOFF]", "PIERCING") \
					or self.iHitBy("[GOODCUTOFF]", "MISSILE") \
					or self.iHitBy("[GOODCUTOFF]", "FIRE") \
					or self.iHitBy("[GOODCUTOFF]", "ELECTRICITY") \
					or self.iHitBy("[GOODCUTOFF]", "POISON") \
					or self.iHitBy("[GOODCUTOFF]", "MAGIC") \
					or self.iHitBy("[GOODCUTOFF]", "COLD") \
					or self.iHitBy("[GOODCUTOFF]", "ACID") \
					or self.iHitBy("[GOODCUTOFF]", "MAGICFIRE") \
					or self.iHitBy("[GOODCUTOFF]", "MAGICCOLD") \
					or self.iPickPocketFailed("[PC]") ):
				# Enemy()
				# SetGlobal("TOWNIE_HOSTILE","MYAREA",1)
				# Help()
				self.iEnemy()
				self.iSetGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 1)
				self.iHelp()
				break
			
			# !Allegiance(Myself,ENEMY)
			# !Global("TEAM_0","MYAREA",0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and not self.iGlobal("'TEAM_0'", "'MYAREA'", 0):
				# Enemy()
				# Continue()
				self.iEnemy()
				pass # continue() - let it pass below
			
			# Dead(Myself)
			if self.iDead("Myself"):
				# ChangeCurrentScript("")
				self.iChangeCurrentScript("''")
				break
			
			# Global("TEAM_0","MYAREA",0)
			# !Global("TOWNIE_HOSTILE","MYAREA",0)
			# !CreatureHidden(Myself)
			# Help([ANYTHING])
			if self.iGlobal("'TEAM_0'", "'MYAREA'", 0) \
				 and not self.iGlobal("'TOWNIE_HOSTILE'", "'MYAREA'", 0) \
				 and not self.iCreatureHidden("Myself") \
				 and self.iHelp("[ANYTHING]"):
				# SetGlobal("TEAM_0","MYAREA",1)
				# Enemy()
				self.iSetGlobal("'TEAM_0'", "'MYAREA'", 1)
				self.iEnemy()
				break
			
			break # while
		return
		
