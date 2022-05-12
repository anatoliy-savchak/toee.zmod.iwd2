import toee
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_12cWar1_Auto(inf_scripting.ScriptBase): # 12cWar1
	# None
	
	@classmethod
	def do_execute(cls, self, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from >= 1:
				break_ = cls.do_execute_block_01(self, code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from >= 2:
				break_ = cls.do_execute_block_02(self, code_from if code_from and block_from == 2 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from >= 3:
				break_ = cls.do_execute_block_03(self, code_from if code_from and block_from == 3 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from >= 4:
				break_ = cls.do_execute_block_04(self, code_from if code_from and block_from == 4 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from >= 5:
				break_ = cls.do_execute_block_05(self, code_from if code_from and block_from == 5 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from >= 6:
				break_ = cls.do_execute_block_06(self, code_from if code_from and block_from == 6 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from >= 7:
				break_ = cls.do_execute_block_07(self, code_from if code_from and block_from == 7 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId("Shawford_Crale")
			# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
			# Wait(4)
			# FaceObject(LastTalkedToBy(Myself))
			# Wait(1)
			# FloatMessage(Myself,16821)  // "I must warn Ulbrec and gather the town forces... I need you to report to the Palisade and drive those damned goblins back.  If Tempus grants us victory, then meet me back here after the battle."
			# Wait(11)
			# FloatMessage(Myself,16822)  // "Everyone!  To arms!  To arms!"
			# Wait(2)
			# MoveViewPoint([219.417],VERY_FAST)
			# MoveToPoint([219.417])
			# HideCreature(Myself,TRUE)
			# MultiPlayerSync()
			# UnhideGUI()
			# MoveViewObject(Protagonist,VERY_FAST)
			# JumpToPoint([496.268])
			# Face(S)
			# EndCutSceneMode()
			cls.do_execute_block_01_code_01(self)
			cls.do_execute_block_01_code_02(self)
			cls.do_execute_block_01_code_03(self)
			cls.do_execute_block_01_code_04(self)
			cls.do_execute_block_01_code_05(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_01_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId("Shawford_Crale")
		# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
		# Wait(4)
		
		self.iCutSceneId("'Shawford_Crale'")
		self.iFloatMessage("Myself", 16360)
		self.iWait(4)
		return
		
	@classmethod
	def do_execute_block_01_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# FaceObject(LastTalkedToBy(Myself))
		# Wait(1)
		
		self.iFaceObject(self.iLastTalkedToBy("Myself"))
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_01_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# FloatMessage(Myself,16821)  // "I must warn Ulbrec and gather the town forces... I need you to report to the Palisade and drive those damned goblins back.  If Tempus grants us victory, then meet me back here after the battle."
		# Wait(11)
		
		self.iFloatMessage("Myself", 16821)
		self.iWait(11)
		return
		
	@classmethod
	def do_execute_block_01_code_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# FloatMessage(Myself,16822)  // "Everyone!  To arms!  To arms!"
		# Wait(2)
		
		self.iFloatMessage("Myself", 16822)
		self.iWait(2)
		return
		
	@classmethod
	def do_execute_block_01_code_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveViewPoint([219.417],VERY_FAST)
		# MoveToPoint([219.417])
		# HideCreature(Myself,TRUE)
		# MultiPlayerSync()
		# UnhideGUI()
		# MoveViewObject(Protagonist,VERY_FAST)
		# JumpToPoint([496.268])
		# Face(S)
		# EndCutSceneMode()
		
		self.iMoveViewPoint("[219.417]", "VERY_FAST")
		self.iMoveToPoint("[219.417]")
		self.iHideCreature("Myself", True)
		self.iMultiPlayerSync()
		self.iUnhideGUI()
		self.iMoveViewObject("Protagonist", "VERY_FAST")
		self.iJumpToPoint("[496.268]")
		self.iFace("S")
		self.iEndCutSceneMode()
		return
		
	@classmethod
	def do_execute_block_02(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player1)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			cls.do_execute_block_02_code_01(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player1)
		# SmallWaitRandom(1,3)
		# FaceObject("Shawford_Crale")
		
		self.iCutSceneId("Player1")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Shawford_Crale'")
		return
		
	@classmethod
	def do_execute_block_03(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player2)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			cls.do_execute_block_03_code_01(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player2)
		# SmallWaitRandom(1,3)
		# FaceObject("Shawford_Crale")
		
		self.iCutSceneId("Player2")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Shawford_Crale'")
		return
		
	@classmethod
	def do_execute_block_04(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player3)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			cls.do_execute_block_04_code_01(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player3)
		# SmallWaitRandom(1,3)
		# FaceObject("Shawford_Crale")
		
		self.iCutSceneId("Player3")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Shawford_Crale'")
		return
		
	@classmethod
	def do_execute_block_05(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player4)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			cls.do_execute_block_05_code_01(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player4)
		# SmallWaitRandom(1,3)
		# FaceObject("Shawford_Crale")
		
		self.iCutSceneId("Player4")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Shawford_Crale'")
		return
		
	@classmethod
	def do_execute_block_06(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player5)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			cls.do_execute_block_06_code_01(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player5)
		# SmallWaitRandom(1,3)
		# FaceObject("Shawford_Crale")
		
		self.iCutSceneId("Player5")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Shawford_Crale'")
		return
		
	@classmethod
	def do_execute_block_07(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player6)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			cls.do_execute_block_07_code_01(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player6)
		# SmallWaitRandom(1,3)
		# FaceObject("Shawford_Crale")
		
		self.iCutSceneId("Player6")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Shawford_Crale'")
		return
		
