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
		is_cutscene_execution = self.is_cutscene_mode()
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_02()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_03()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_04()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_05()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_06()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_07()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_08()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_09()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_10()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_11()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_12()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_13()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_14()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_15()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_16()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_17()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_18()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_19()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_20()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_21()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_22()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_23()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_24()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_25()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_26()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_27()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_28()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_29()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_30()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_31()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_32()
			if break_ and not is_cutscene_execution: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See([ENEMY.0.GOBLIN],0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_01",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_02",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_03",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_04",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_05",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_06",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_08(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_01",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_09(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_07",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_10(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_19",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_11(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_02",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_12(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_08",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_13(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_03",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_14(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_09",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_15(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_10",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_16(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_04",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_17(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_11",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_18(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_12",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_19(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_05",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_20(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_06",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_21(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_07",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_22(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_08",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_23(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_13",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_24(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_14",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_25(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_15",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_26(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_09",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_27(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_16",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_28(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_17",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_29(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_18",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_30(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See("1000_Goblin_Archer_10",0)
		# NearLocation(LastSeenBy(Myself),-2,-2,9)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# EquipWeapon()
			# AttackOneRound(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_31(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# AttackedBy([ENEMY.0.GOBLIN],DEFAULT)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# RunAwayFrom(LastMarkedObject,45)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_32(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# See([ENEMY.0.GOBLIN],0)
		if self.iSee("[ENEMY.0.GOBLIN]", 0):
			# FaceObject(LastMarkedObject)
			self.iFaceObject("LastMarkedObject")
			return True # break further blocks
		return False
		
