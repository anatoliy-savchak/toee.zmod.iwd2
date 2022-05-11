import toee
import inf_scripting
#### IMPORTS ####
from bcs import scr_12cwar1
#### END IMPORTS ####

#### BCS ####
class Script_12cWar0_Auto(inf_scripting.ScriptBase): # 12cWar0
	# None
	
	@classmethod
	def do_execute(cls, self, continuous):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			break_ = cls.do_execute_block_01()
			if break_ and not continuous: break
			
			break_ = cls.do_execute_block_02()
			if break_ and not continuous: break
			
			break_ = cls.do_execute_block_03()
			if break_ and not continuous: break
			
			break_ = cls.do_execute_block_04()
			if break_ and not continuous: break
			
			break_ = cls.do_execute_block_05()
			if break_ and not continuous: break
			
			break_ = cls.do_execute_block_06()
			if break_ and not continuous: break
			
			break_ = cls.do_execute_block_07()
			if break_ and not continuous: break
			
			break_ = cls.do_execute_block_08()
			if break_ and not continuous: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
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
			self.iCutSceneId("'Messenger_Hidden'")
			self.iHideGUI()
			self.iMultiPlayerSync()
			self.iMoveViewObject("Myself", "INSTANT")
			self.iWait(1)
			self.iHideCreature("Myself", False)
			self.iSmallWait(12)
			self.iSetGlobal("'Goblins_Attack_Palisade'", "'GLOBAL'", 1)
			self.iMoveViewObject("'Shawford_Crale'", "VERY_FAST")
			self.iMoveToPoint("[448.295]")
			self.iFaceObject("'Shawford_Crale'")
			self.iFloatMessage("Myself", 16357)
			self.iWait(3)
			self.iStartCutScene(scr_12cwar1.Script_12cWar1)
			self.iWait(2)
			self.iFloatMessage("Myself", 16820)
			self.iSmallWait(4)
			self.iMoveToPoint("[219.417]")
			self.iDestroySelf()
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId("Shawford_Crale")
			# FaceObject("Messenger_Hidden")
			self.iCutSceneId("'Shawford_Crale'")
			self.iFaceObject("'Messenger_Hidden'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player1)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([582.302])
			self.iCutSceneId("Player1")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Messenger_Hidden'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[582.302]")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player2)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([566.351])
			self.iCutSceneId("Player2")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Messenger_Hidden'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[566.351]")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player3)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([519.360])
			self.iCutSceneId("Player3")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Messenger_Hidden'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[519.360]")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player4)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([480.407])
			self.iCutSceneId("Player4")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Messenger_Hidden'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[480.407]")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player5)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([542.419])
			self.iCutSceneId("Player5")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Messenger_Hidden'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[542.419]")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_08(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player6)
			# SmallWaitRandom(1,3)
			# FaceObject("Messenger_Hidden")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([602.388])
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Messenger_Hidden'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			return True # break further blocks
		return False
		
