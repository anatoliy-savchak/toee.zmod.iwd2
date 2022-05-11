import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_12cWar1_Auto(inf_scripting.ScriptBase):
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
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
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
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Shawford_Crale'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player1)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Shawford_Crale'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player2)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Shawford_Crale'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player3)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Shawford_Crale'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player4)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Shawford_Crale'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player5)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Shawford_Crale'")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player6)
			# SmallWaitRandom(1,3)
			# FaceObject("Shawford_Crale")
			self.iCutSceneId("Player6")
			self.iSmallWaitRandom(1, 3)
			self.iFaceObject("'Shawford_Crale'")
			return True # break further blocks
		return False
		
