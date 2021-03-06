import toee, debug
import inf_scripting
#### IMPORTS ####
from bcs import scr_12cwar1
#### END IMPORTS ####

#### BCS ####
class Script_12cWar2_Auto(inf_scripting.ScriptBase): # 12cWar2
	# None
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute(cls, self, locus, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from <= 1:
				break_ = cls.do_execute_block_01(self, locus, code_from=code_from if code_from and block_from == 1 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 2:
				break_ = cls.do_execute_block_02(self, locus, code_from=code_from if code_from and block_from == 2 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 3:
				break_ = cls.do_execute_block_03(self, locus, code_from=code_from if code_from and block_from == 3 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 4:
				break_ = cls.do_execute_block_04(self, locus, code_from=code_from if code_from and block_from == 4 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 5:
				break_ = cls.do_execute_block_05(self, locus, code_from=code_from if code_from and block_from == 5 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 6:
				break_ = cls.do_execute_block_06(self, locus, code_from=code_from if code_from and block_from == 6 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 7:
				break_ = cls.do_execute_block_07(self, locus, code_from=code_from if code_from and block_from == 7 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			if not block_from or block_from <= 8:
				break_ = cls.do_execute_block_08(self, locus, code_from=code_from if code_from and block_from == 8 else None)
				if (break_ > 1) or (not continuous and break_): break
			
			break # while
		return
		
	@classmethod
	@inf_scripting.dump_args
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
		
		if (code_from is None and do_check()) or (code_from <= 6):
			break_ = cls.do_execute_block_01_code_06(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 7):
			break_ = cls.do_execute_block_01_code_07(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 8):
			break_ = cls.do_execute_block_01_code_08(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 9):
			break_ = cls.do_execute_block_01_code_09(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId("SWIFT_THOMAS_HIDDEN")
		# HideGUI()
		# MultiPlayerSync()
		# MoveViewObject(Myself,INSTANT)
		# Wait(1)
		
		self.iCutSceneId("'SWIFT_THOMAS_HIDDEN'")
		self.iHideGUI()
		self.iMultiPlayerSync()
		self.iMoveViewObject("Myself", "INSTANT")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# HideCreature(Myself,FALSE)
		# SmallWait(12)
		
		self.iHideCreature("Myself", False)
		self.iSmallWait(time=12, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# SetGlobal("Goblins_Attack_Palisade","GLOBAL",1)
		# MoveViewObject("Shawford_Crale",VERY_FAST)
		# MoveToPoint([448.295])
		
		self.iSetGlobal("'Goblins_Attack_Palisade'", "'GLOBAL'", 1)
		self.iMoveViewObject("'Shawford_Crale'", "VERY_FAST")
		self.iMoveToPointPost((479, 478), locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# FaceObject("Shawford_Crale")
		# FloatMessage(Myself,16357)  // "Sir!  The goblins are at the Palisade!"
		# Wait(3)
		
		self.iFaceObject("'Shawford_Crale'")
		self.iFloatMessageDialog("Myself", 16357)
		self.iWait(time=3, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_05(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 5
		
		# StartCutScene("12cWar1")
		
		self.iStartCutScene(scr_12cwar1.Script_12cWar1, locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_06(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 6
		
		# Wait(2)
		
		self.iWait(time=2, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_07(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 7
		
		# FloatMessage(Myself,16820)  // "Yes, sir!"
		# SmallWait(4)
		
		self.iFloatMessageDialog("Myself", 16820)
		self.iSmallWait(time=4, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_08(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 8
		
		# MoveToPoint([219.417])
		
		self.iMoveToPointPost((489, 477), locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_01_code_09(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 9
		
		# DestroySelf()
		
		self.iDestroySelf()
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 2
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId("Shawford_Crale")
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_02_code_01(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_02_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId("Shawford_Crale")
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		self.iCutSceneId("'Shawford_Crale'")
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 3
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId(Player1)
		# SmallWaitRandom(1,3)
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		# SmallWait(5)
		# MoveToPoint([582.302])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_03_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_03_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_03_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_03_code_04(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId(Player1)
		# SmallWaitRandom(1,3)
		
		self.iCutSceneId("Player1")
		self.iSmallWaitRandom(1, 3, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# SmallWait(5)
		
		self.iSmallWait(time=5, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_03_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# MoveToPoint([582.302])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		self.iMoveToPoint((476, 482))
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 4
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId(Player2)
		# SmallWaitRandom(1,3)
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		# SmallWait(5)
		# MoveToPoint([566.351])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_04_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_04_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_04_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_04_code_04(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId(Player2)
		# SmallWaitRandom(1,3)
		
		self.iCutSceneId("Player2")
		self.iSmallWaitRandom(1, 3, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# SmallWait(5)
		
		self.iSmallWait(time=5, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_04_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# MoveToPoint([566.351])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		self.iMoveToPoint((478, 483))
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 5
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId(Player3)
		# SmallWaitRandom(1,3)
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		# SmallWait(5)
		# MoveToPoint([519.360])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_05_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_05_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_05_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_05_code_04(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId(Player3)
		# SmallWaitRandom(1,3)
		
		self.iCutSceneId("Player3")
		self.iSmallWaitRandom(1, 3, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# SmallWait(5)
		
		self.iSmallWait(time=5, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_05_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# MoveToPoint([519.360])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		self.iMoveToPoint((480, 482))
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 6
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId(Player4)
		# SmallWaitRandom(1,3)
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		# SmallWait(5)
		# MoveToPoint([480.407])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_06_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_06_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_06_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_06_code_04(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId(Player4)
		# SmallWaitRandom(1,3)
		
		self.iCutSceneId("Player4")
		self.iSmallWaitRandom(1, 3, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# SmallWait(5)
		
		self.iSmallWait(time=5, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_06_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# MoveToPoint([480.407])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		self.iMoveToPoint((482, 483))
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 7
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId(Player5)
		# SmallWaitRandom(1,3)
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		# SmallWait(5)
		# MoveToPoint([542.419])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_07_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_07_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_07_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_07_code_04(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId(Player5)
		# SmallWaitRandom(1,3)
		
		self.iCutSceneId("Player5")
		self.iSmallWaitRandom(1, 3, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# SmallWait(5)
		
		self.iSmallWait(time=5, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_07_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# MoveToPoint([542.419])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		self.iMoveToPoint((481, 485))
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		return 0
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08(cls, self, locus, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["block"] = 8
		d = {"check": None}
		def do_check():
			if d["check"] is None:
				# True()
				if True:
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# CutSceneId(Player6)
		# SmallWaitRandom(1,3)
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		# SmallWait(5)
		# MoveToPoint([602.388])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_08_code_01(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 2):
			break_ = cls.do_execute_block_08_code_02(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 3):
			break_ = cls.do_execute_block_08_code_03(self, locus)
			if break_ == 2: return break_
		
		if (code_from is None and do_check()) or (code_from <= 4):
			break_ = cls.do_execute_block_08_code_04(self, locus)
			if break_ == 2: return break_
		
		result = 1 # break further blocks
		if not code_from is None:
			result = 1
		elif d["check"]:
			result = 1
		return result
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08_code_01(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 1
		
		# CutSceneId(Player6)
		# SmallWaitRandom(1,3)
		
		self.iCutSceneId("Player6")
		self.iSmallWaitRandom(1, 3, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08_code_02(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 2
		
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		# Wait(1)
		
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		self.iWait(time=1, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08_code_03(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 3
		
		# SmallWait(5)
		
		self.iSmallWait(time=5, locus=locus)
		return 2
		
	@classmethod
	@inf_scripting.dump_args
	def do_execute_block_08_code_04(cls, self, locus):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		locus["code"] = 4
		
		# MoveToPoint([602.388])
		# FaceObject("SWIFT_THOMAS_HIDDEN")
		
		self.iMoveToPoint((479, 485))
		self.iFaceObject("'SWIFT_THOMAS_HIDDEN'")
		return 0
		
