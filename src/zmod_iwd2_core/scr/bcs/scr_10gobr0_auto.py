import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10GOBR0_Auto(inf_scripting.ScriptBase):
	# AR1000 10GOBAR 1000_Goblin_Archer_01 ScriptRace
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# Global("I_LIKE_DWARVES","LOCALS",0)
			# See([PC],0)
			if self.iGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 0) \
				 and self.iSee("[PC]", 0):
				# SetGlobal("I_LIKE_DWARVES","LOCALS",2)
				# Continue()
				self.iSetGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 2)
				pass # continue() - let it pass below
			
			# Global("I_LIKE_DWARVES","LOCALS",1)
			# Or(2)
			# See([PC.0.DWARF],0)
			# See([0.0.DWARF],0)
			if self.iGlobal("'I_LIKE_DWARVES'", "'LOCALS'", 1) \
				 and ( False \
					or self.iSee("[PC.0.DWARF]", 0) \
					or self.iSee("[0.0.DWARF]", 0) ):
				# SetBestWeapon(LastMarkedObject,3)
				# AttackReevaluate(LastMarkedObject,45)
				self.iSetBestWeapon("LastMarkedObject", 3)
				self.iAttackReevaluate("LastMarkedObject", 45)
				break
			
			# Or(9)
			# See(NearestEnemyOf(Myself),0)
			# See("HEDRON",0)
			# See("JORUN",0)
			# See("CRANDALL",0)
			# See("BROGAN",0)
			# See("JON",0)
			# See("REIG",0)
			# See("SCREED",0)
			# See("ELDGULL",0)
			if ( False \
					or self.iSee(self.iNearestEnemyOf("Myself"), 0) \
					or self.iSee("'HEDRON'", 0) \
					or self.iSee("'JORUN'", 0) \
					or self.iSee("'CRANDALL'", 0) \
					or self.iSee("'BROGAN'", 0) \
					or self.iSee("'JON'", 0) \
					or self.iSee("'REIG'", 0) \
					or self.iSee("'SCREED'", 0) \
					or self.iSee("'ELDGULL'", 0) ):
				# SetBestWeapon(LastMarkedObject,3)
				# AttackReevaluate(LastMarkedObject,45)
				self.iSetBestWeapon("LastMarkedObject", 3)
				self.iAttackReevaluate("LastMarkedObject", 45)
				break
			
			break # while
		return
		
