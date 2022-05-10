import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10CRAND0_Auto(inf_scripting.ScriptBase):
	# AR1000 10CRANDA Crandall ScriptDefault
	
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
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(18)
		# Global("Crandall_Leave","GLOBAL",0)
		# !See([ENEMY.0.GOBLIN],0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# FloatMessage(Myself,1771)  // "Where are the rest of the Targos Guard?"
			# StartRandomTimer(18,10,15)
			# Continue()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",0)
		# ActionListEmpty()
		# NearLocation(Myself,1317,1489,4)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetStartPos([1317.1489])
			# SetGlobal("ML_0","LOCALS",1)
			# Continue()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",0)
		# !Global("Crandall_Leave","GLOBAL",0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# MoveToPoint([1317.1489])
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",1)
		# ActionListEmpty()
		# NearLocation(Myself,733,1450,4)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetStartPos([733.1450])
			# SetGlobal("ML_0","LOCALS",2)
			# Continue()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",1)
		# !Global("Crandall_Leave","GLOBAL",0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# MoveToPoint([733.1450])
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",2)
		# ActionListEmpty()
		# NearLocation(Myself,221,1356,4)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetStartPos([221.1356])
			# SetGlobal("ML_0","LOCALS",3)
			# Continue()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",2)
		# !Global("Crandall_Leave","GLOBAL",0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# MoveToPoint([221.1356])
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_08(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",3)
		# ActionListEmpty()
		# NearLocation(Myself,335,819,4)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetStartPos([335.819])
			# SetGlobal("ML_0","LOCALS",4)
			# Continue()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_09(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",3)
		# !Global("Crandall_Leave","GLOBAL",0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# MoveToPoint([335.819])
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_10(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",4)
		# ActionListEmpty()
		# NearLocation(Myself,225,383,4)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetStartPos([225.383])
			# SetGlobal("ML_0","LOCALS",5)
			# Continue()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_11(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",4)
		# !Global("Crandall_Leave","GLOBAL",0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# MoveToPoint([225.383])
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_12(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",5)
		# ActionListEmpty()
		# NearLocation(Myself,159,31,4)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetStartPos([159.31])
			# SetGlobal("ML_0","LOCALS",6)
			# Continue()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_13(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",5)
		# !Global("Crandall_Leave","GLOBAL",0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# MoveToPoint([159.31])
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_14(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",6)
		# !Global("Crandall_Leave","GLOBAL",0)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# DestroySelf()
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_15(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(20)
		# !NearSavedLocation(3)
		# !Allegiance(Myself,ENEMY)
		if not self.iTimerActive(20) \
			 and not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# ReturnToSavedLocation(0)
			# StartTimer(20,5)
			self.iReturnToSavedLocation(0)
			self.iStartTimer(20, 5)
			return True # break further blocks
		return False
		
