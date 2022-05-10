import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10cHedr0_Auto(inf_scripting.ScriptBase):
	# AR1000 script_area
	
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
			# CutSceneId(Player1)
			# FaceObject("Hedron")
			self.iCutSceneId("'Hedron'")
			self.iSetDialogueRange(300)
			self.iMultiPlayerSync()
			self.iFaceObject("Protagonist")
			self.iSmallWait(3)
			self.iDialogue("Protagonist")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player2)
			# FaceObject("Hedron")
			self.iCutSceneId("'Hedron'")
			self.iSetDialogueRange(300)
			self.iMultiPlayerSync()
			self.iFaceObject("Protagonist")
			self.iSmallWait(3)
			self.iDialogue("Protagonist")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player3)
			# FaceObject("Hedron")
			self.iCutSceneId("'Hedron'")
			self.iSetDialogueRange(300)
			self.iMultiPlayerSync()
			self.iFaceObject("Protagonist")
			self.iSmallWait(3)
			self.iDialogue("Protagonist")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player4)
			# FaceObject("Hedron")
			self.iCutSceneId("'Hedron'")
			self.iSetDialogueRange(300)
			self.iMultiPlayerSync()
			self.iFaceObject("Protagonist")
			self.iSmallWait(3)
			self.iDialogue("Protagonist")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player5)
			# FaceObject("Hedron")
			self.iCutSceneId("'Hedron'")
			self.iSetDialogueRange(300)
			self.iMultiPlayerSync()
			self.iFaceObject("Protagonist")
			self.iSmallWait(3)
			self.iDialogue("Protagonist")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId(Player6)
			# FaceObject("Hedron")
			self.iCutSceneId("'Hedron'")
			self.iSetDialogueRange(300)
			self.iMultiPlayerSync()
			self.iFaceObject("Protagonist")
			self.iSmallWait(3)
			self.iDialogue("Protagonist")
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# True()
		if True:
			# CutSceneId("Hedron")
			# SetDialogueRange(300)
			# MultiPlayerSync()
			# FaceObject(Protagonist)
			# SmallWait(3)
			# Dialogue(Protagonist)
			self.iCutSceneId("'Hedron'")
			self.iSetDialogueRange(300)
			self.iMultiPlayerSync()
			self.iFaceObject("Protagonist")
			self.iSmallWait(3)
			self.iDialogue("Protagonist")
			return True # break further blocks
		return False
		
