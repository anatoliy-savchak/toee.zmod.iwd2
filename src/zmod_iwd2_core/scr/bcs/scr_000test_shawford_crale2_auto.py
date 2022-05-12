import toee
import inf_scripting
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_000TEST_Shawford_Crale2_Auto(inf_scripting.ScriptBase): # 000TEST_Shawford_Crale2
	# AR1201 script_area
	
	@classmethod
	def do_execute(cls, self, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus = self.locus_make()
		locus.update({"script_class": cls, "continuous": continuous})
		while True:
			if not block_from or block_from >= 1:
				break_ = cls.do_execute_block_01(self, locus, code_from=code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 1
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# StartCutSceneMode()
		# CutSceneId("Shawford_Crale")
		# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
		# Wait(4)
		# FaceObject(Player1)
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
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_01_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_01_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_01_code_04(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 5):
			break_ = cls.do_execute_block_01_code_05(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	def do_execute_block_01_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# StartCutSceneMode()
		# CutSceneId("Shawford_Crale")
		# FloatMessage(Myself,16360)  // "Order the gate into town sealed!  Sound the alarm!"
		# Wait(4)
		
		self.iStartCutSceneMode()
		self.iCutSceneId("'Shawford_Crale'")
		self.iFloatMessage("Myself", 16360)
		self.iWait(time=4, locus=locus)
		return 2
		
	@classmethod
	def do_execute_block_01_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FaceObject(Player1)
		# Wait(1)
		
		self.iFaceObject("Player1")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	def do_execute_block_01_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# FloatMessage(Myself,16821)  // "I must warn Ulbrec and gather the town forces... I need you to report to the Palisade and drive those damned goblins back.  If Tempus grants us victory, then meet me back here after the battle."
		# Wait(11)
		
		self.iFloatMessage("Myself", 16821)
		self.iWait(time=11, locus=locus)
		return 2
		
	@classmethod
	def do_execute_block_01_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# FloatMessage(Myself,16822)  // "Everyone!  To arms!  To arms!"
		# Wait(2)
		
		self.iFloatMessage("Myself", 16822)
		self.iWait(time=2, locus=locus)
		return 2
		
	@classmethod
	def do_execute_block_01_code_05(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 5
		
		# MoveViewPoint([219.417],VERY_FAST)
		# MoveToPoint([219.417])
		# HideCreature(Myself,TRUE)
		# MultiPlayerSync()
		# UnhideGUI()
		# MoveViewObject(Protagonist,VERY_FAST)
		# JumpToPoint([496.268])
		# Face(S)
		# EndCutSceneMode()
		
		self.iMoveViewPoint((489, 477), "VERY_FAST")
		self.iMoveToPoint((489, 477))
		self.iHideCreature("Myself", True)
		self.iMultiPlayerSync()
		self.iUnhideGUI()
		self.iMoveViewObject("Protagonist", "VERY_FAST")
		self.iJumpToPoint((477, 478))
		self.iFace("S")
		self.iEndCutSceneMode()
		return 0
		
