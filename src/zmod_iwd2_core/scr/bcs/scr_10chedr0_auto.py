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
		while True:
			# True()
			if True:
				# CutSceneId(Player1)
				# FaceObject("Hedron")
				self.iCutSceneId("Player1")
				self.iFaceObject("'Hedron'")
				break
			
			# True()
			if True:
				# CutSceneId(Player2)
				# FaceObject("Hedron")
				self.iCutSceneId("Player2")
				self.iFaceObject("'Hedron'")
				break
			
			# True()
			if True:
				# CutSceneId(Player3)
				# FaceObject("Hedron")
				self.iCutSceneId("Player3")
				self.iFaceObject("'Hedron'")
				break
			
			# True()
			if True:
				# CutSceneId(Player4)
				# FaceObject("Hedron")
				self.iCutSceneId("Player4")
				self.iFaceObject("'Hedron'")
				break
			
			# True()
			if True:
				# CutSceneId(Player5)
				# FaceObject("Hedron")
				self.iCutSceneId("Player5")
				self.iFaceObject("'Hedron'")
				break
			
			# True()
			if True:
				# CutSceneId(Player6)
				# FaceObject("Hedron")
				self.iCutSceneId("Player6")
				self.iFaceObject("'Hedron'")
				break
			
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
				break
			
			break # while
		return
		
