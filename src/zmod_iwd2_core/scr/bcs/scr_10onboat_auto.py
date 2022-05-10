import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10ONBOAT_Auto(inf_scripting.ScriptBase):
	# AR1000 10HEDRON Hedron ScriptRace
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Allegiance(Myself,ENEMY)
			if self.iAllegiance("Myself", "ENEMY"):
				# ChangeCurrentScript("10aGobG0")
				self.iChangeCurrentScript("'10aGobG0'")
				break
			
			# !IsTeamBitOn(TEAM_1_BIT)
			if not self.iIsTeamBitOn("TEAM_1_BIT"):
				# SetTeamBit(TEAM_1_BIT,TRUE)
				# Continue()
				self.iSetTeamBit("TEAM_1_BIT", True)
				pass # continue() - let it pass below
			
			# !Global("TEAM_1","MYAREA",1)
			# Allegiance(Myself,ENEMY)
			# !CreatureHidden(Myself)
			# See(NearestEnemyOf(Myself),0)
			if not self.iGlobal("'TEAM_1'", "'MYAREA'", 1) \
				 and self.iAllegiance("Myself", "ENEMY") \
				 and not self.iCreatureHidden("Myself") \
				 and self.iSee(self.iNearestEnemyOf("Myself"), 0):
				# SetGlobal("TEAM_1","MYAREA",1)
				# Continue()
				self.iSetGlobal("'TEAM_1'", "'MYAREA'", 1)
				pass # continue() - let it pass below
			
			# !Allegiance(Myself,ENEMY)
			# See([ENEMY][1887.703.2801.1043],0)
			if not self.iAllegiance("Myself", "ENEMY") \
				 and self.iSee("[ENEMY][1887.703.2801.1043]", 0):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See([ENEMY.0.GOBLIN][1887.703.2801.1043],0)
			if self.iSee("[ENEMY.0.GOBLIN][1887.703.2801.1043]", 0):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			break # while
		return
		
