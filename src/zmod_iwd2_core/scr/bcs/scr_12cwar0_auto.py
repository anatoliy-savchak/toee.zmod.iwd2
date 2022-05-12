import toee
import inf_scripting
#### IMPORTS ####
from bcs import scr_12cwar1
#### END IMPORTS ####

#### BCS ####
class Script_12cWar0_Auto(inf_scripting.ScriptBase): # 12cWar0
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
			
			if not block_from or block_from >= 8:
				break_ = cls.do_execute_block_08(self, code_from if code_from and block_from == 8 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId("Messenger_Hidden")
			# HideGUI()
			# MultiPlayerSync()
			# MoveViewObject(Myself,INSTANT)
			# Wait(1)
			# HideCreature(Myself,FALSE)
			# SmallWait(12)
			# SetGlobal("Goblins_Attack_Palisade","GLOBAL",1)
			# MoveViewObject("Shawford_Crale",VERY_FAST)
			# MoveToPoint([448.295])
			# FaceObject("Shawford_Crale")
			# FloatMessage(Myself,16357)  // "Sir!  The goblins are at the Palisade!"
			# Wait(3)
			# StartCutScene("12cWar1")
			# Wait(2)
			# FloatMessage(Myself,16820)  // "Yes, sir!"
			# SmallWait(4)
			# MoveToPoint([219.417])
			# DestroySelf()
			cls.do_execute_block_01_code_01(self)
			cls.do_execute_block_01_code_02(self)
			cls.do_execute_block_01_code_03(self)
			cls.do_execute_block_01_code_04(self)
			cls.do_execute_block_01_code_05(self)
			cls.do_execute_block_01_code_06(self)
			cls.do_execute_block_01_code_07(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_01_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId("Messenger_Hidden")
		# HideGUI()
		# MultiPlayerSync()
		# MoveViewObject(Myself,INSTANT)
		# Wait(1)
		
		self.iCutSceneId("'Messenger_Hidden'")
		self.iHideGUI()
		self.iMultiPlayerSync()
		self.iMoveViewObject("Myself", "INSTANT")
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_01_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# HideCreature(Myself,FALSE)
		# SmallWait(12)
		
		self.iHideCreature("Myself", False)
		self.iSmallWait(12)
		return
		
	@classmethod
	def do_execute_block_01_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# SetGlobal("Goblins_Attack_Palisade","GLOBAL",1)
		# MoveViewObject("Shawford_Crale",VERY_FAST)
		# MoveToPoint([448.295])
		# FaceObject("Shawford_Crale")
		# FloatMessage(Myself,16357)  // "Sir!  The goblins are at the Palisade!"
		# Wait(3)
		
		self.iSetGlobal("'Goblins_Attack_Palisade'", "'GLOBAL'", 1)
		self.iMoveViewObject("'Shawford_Crale'", "VERY_FAST")
		self.iMoveToPoint("[448.295]")
		self.iFaceObject("'Shawford_Crale'")
		self.iFloatMessage("Myself", 16357)
		self.iWait(3)
		return
		
	@classmethod
	def do_execute_block_01_code_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# StartCutScene("12cWar1")
		
		self.iStartCutScene(scr_12cwar1.Script_12cWar1)
		return
		
	@classmethod
	def do_execute_block_01_code_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# Wait(2)
		
		self.iWait(2)
		return
		
	@classmethod
	def do_execute_block_01_code_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# FloatMessage(Myself,16820)  // "Yes, sir!"
		# SmallWait(4)
		
		self.iFloatMessage("Myself", 16820)
		self.iSmallWait(4)
		return
		
	@classmethod
	def do_execute_block_01_code_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveToPoint([219.417])
		# DestroySelf()
		
		self.iMoveToPoint("[219.417]")
		self.iDestroySelf()
		return
		
	@classmethod
	def do_execute_block_02(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId("Shawford_Crale")
			# FaceObject("Messenger_Hidden")
			cls.do_execute_block_02_code_01(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId("Shawford_Crale")
		# FaceObject("Messenger_Hidden")
		
		self.iCutSceneId("'Shawford_Crale'")
		self.iFaceObject("'Messenger_Hidden'")
		return
		
	@classmethod
	def do_execute_block_03(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player1)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([582.302])
			cls.do_execute_block_03_code_01(self)
			cls.do_execute_block_03_code_02(self)
			cls.do_execute_block_03_code_03(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player1)
		# SmallWaitRandom(1,3)
		# FaceObject("Messenger_Hidden")
		# Wait(1)
		
		self.iCutSceneId("Player1")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Messenger_Hidden'")
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_03_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# SmallWait(5)
		
		self.iSmallWait(5)
		return
		
	@classmethod
	def do_execute_block_03_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveToPoint([582.302])
		
		self.iMoveToPoint("[582.302]")
		return
		
	@classmethod
	def do_execute_block_04(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player2)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([566.351])
			cls.do_execute_block_04_code_01(self)
			cls.do_execute_block_04_code_02(self)
			cls.do_execute_block_04_code_03(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player2)
		# SmallWaitRandom(1,3)
		# FaceObject("Messenger_Hidden")
		# Wait(1)
		
		self.iCutSceneId("Player2")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Messenger_Hidden'")
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_04_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# SmallWait(5)
		
		self.iSmallWait(5)
		return
		
	@classmethod
	def do_execute_block_04_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveToPoint([566.351])
		
		self.iMoveToPoint("[566.351]")
		return
		
	@classmethod
	def do_execute_block_05(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player3)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([519.360])
			cls.do_execute_block_05_code_01(self)
			cls.do_execute_block_05_code_02(self)
			cls.do_execute_block_05_code_03(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player3)
		# SmallWaitRandom(1,3)
		# FaceObject("Messenger_Hidden")
		# Wait(1)
		
		self.iCutSceneId("Player3")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Messenger_Hidden'")
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_05_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# SmallWait(5)
		
		self.iSmallWait(5)
		return
		
	@classmethod
	def do_execute_block_05_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveToPoint([519.360])
		
		self.iMoveToPoint("[519.360]")
		return
		
	@classmethod
	def do_execute_block_06(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player4)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([480.407])
			cls.do_execute_block_06_code_01(self)
			cls.do_execute_block_06_code_02(self)
			cls.do_execute_block_06_code_03(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player4)
		# SmallWaitRandom(1,3)
		# FaceObject("Messenger_Hidden")
		# Wait(1)
		
		self.iCutSceneId("Player4")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Messenger_Hidden'")
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_06_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# SmallWait(5)
		
		self.iSmallWait(5)
		return
		
	@classmethod
	def do_execute_block_06_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveToPoint([480.407])
		
		self.iMoveToPoint("[480.407]")
		return
		
	@classmethod
	def do_execute_block_07(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player5)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([542.419])
			cls.do_execute_block_07_code_01(self)
			cls.do_execute_block_07_code_02(self)
			cls.do_execute_block_07_code_03(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player5)
		# SmallWaitRandom(1,3)
		# FaceObject("Messenger_Hidden")
		# Wait(1)
		
		self.iCutSceneId("Player5")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Messenger_Hidden'")
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_07_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# SmallWait(5)
		
		self.iSmallWait(5)
		return
		
	@classmethod
	def do_execute_block_07_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveToPoint([542.419])
		
		self.iMoveToPoint("[542.419]")
		return
		
	@classmethod
	def do_execute_block_08(cls, self, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player6)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([602.388])
			cls.do_execute_block_08_code_01(self)
			cls.do_execute_block_08_code_02(self)
			cls.do_execute_block_08_code_03(self)
			return 1 # break further blocks
		return False
		
	@classmethod
	def do_execute_block_08_code_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# CutSceneId(Player6)
		# SmallWaitRandom(1,3)
		# FaceObject("Messenger_Hidden")
		# Wait(1)
		
		self.iCutSceneId("Player6")
		self.iSmallWaitRandom(1, 3)
		self.iFaceObject("'Messenger_Hidden'")
		self.iWait(1)
		return
		
	@classmethod
	def do_execute_block_08_code_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# SmallWait(5)
		
		self.iSmallWait(5)
		return
		
	@classmethod
	def do_execute_block_08_code_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		
		# MoveToPoint([602.388])
		
		self.iMoveToPoint("[602.388]")
		return
		
