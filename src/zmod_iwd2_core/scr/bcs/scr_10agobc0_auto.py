import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10AGOBC0_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptRace
	
	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			# See([ENEMY.0.GOBLIN],0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("[ENEMY.0.GOBLIN]", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_01",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_01'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_02",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_02'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_03",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_03'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_04",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_04'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_05",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_05'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_06",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_06'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_01",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_01'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_07",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_07'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_19",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_19'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_02",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_02'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_08",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_08'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_03",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_03'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_09",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_09'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_10",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_10'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_04",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_04'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_11",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_11'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_12",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_12'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_05",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_05'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_06",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_06'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_07",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_07'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_08",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_08'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_13",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_13'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_14",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_14'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_15",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_15'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_09",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_09'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_16",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_16'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_17",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_17'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_18",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_18'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# See("1000_Goblin_Archer_10",0)
			# NearLocation(LastSeenBy(Myself),-2,-2,9)
			if self.iSee("'1000_Goblin_Archer_10'", 0) \
				 and self.iNearLocation(self.iLastSeenBy("Myself"), -2, -2, 9):
				# EquipWeapon()
				# AttackOneRound(LastMarkedObject)
				self.iEquipWeapon()
				self.iAttackOneRound("LastMarkedObject")
				break
			
			# AttackedBy([ENEMY.0.GOBLIN],DEFAULT)
			if self.iAttackedBy("[ENEMY.0.GOBLIN]", "DEFAULT"):
				# RunAwayFrom(LastMarkedObject,45)
				self.iRunAwayFrom("LastMarkedObject", 45)
				break
			
			# See([ENEMY.0.GOBLIN],0)
			if self.iSee("[ENEMY.0.GOBLIN]", 0):
				# FaceObject(LastMarkedObject)
				self.iFaceObject("LastMarkedObject")
				break
			
			break # while
		return
		
