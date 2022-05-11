import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_12cWar2_Auto(inf_scripting.ScriptBase):
	# None
	
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
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId("SWIFT_THOMAS_HIDDEN")
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
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId("Shawford_Crale")
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player1)
			# SmallWaitRandom(1,3)
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([582.302])
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player2)
			# SmallWaitRandom(1,3)
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([566.351])
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player3)
			# SmallWaitRandom(1,3)
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([519.360])
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player4)
			# SmallWaitRandom(1,3)
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([480.407])
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player5)
			# SmallWaitRandom(1,3)
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([542.419])
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_08(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player6)
			# SmallWaitRandom(1,3)
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			# Wait(1)
			# SmallWait(5)
			# MoveToPoint([602.388])
			# FaceObject("SWIFT_THOMAS_HIDDEN")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			self.iWait(1)
			self.iSmallWait(5)
			self.iMoveToPoint("[602.388]")
			self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
			return True # break further blocks
		return False
		
