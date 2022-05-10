import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10SCREEM_Auto(inf_scripting.ScriptBase):
	# AR1000 10SCREED Screed ScriptDefault
	
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
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",0)
		# !TimerActive(19)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# StartTimer(19,10)
			# SetGlobal("ML_0","LOCALS",1)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",1)
		# ActionListEmpty()
		# NearLocation(Myself,1957,807,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# SetStartPos([1957.807])
			# SetGlobal("ML_0","LOCALS",2)
			# Continue()
			self.iReturnToSavedLocation(0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# MoveToPoint([1957.807])
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",2)
		# !TimerActive(19)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# Face(E)
			# SetGlobal("ML_0","LOCALS",3)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",3)
		# !TimerActive(19)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# StartTimer(19,10)
			# SetGlobal("ML_0","LOCALS",4)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",4)
		# ActionListEmpty()
		# NearLocation(Myself,2058,785,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# SetStartPos([2058.785])
			# SetGlobal("ML_0","LOCALS",5)
			# Continue()
			self.iReturnToSavedLocation(0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# MoveToPoint([2058.785])
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_08(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",5)
		# !TimerActive(19)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# Face(N)
			# SetGlobal("ML_0","LOCALS",6)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_09(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",6)
		# !TimerActive(19)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# StartTimer(19,10)
			# SetGlobal("ML_0","LOCALS",7)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_10(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",7)
		# NearSavedLocation(4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# SetGlobal("ML_0","LOCALS",0)
			# SetStartPos([-1.-1])
			# Continue()
			self.iReturnToSavedLocation(0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_11(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",7)
		# !TimerActive(19)
		# !NearSavedLocation(4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 7) \
			 and not self.iTimerActive(19) \
			 and not self.iNearSavedLocation(4):
			# ReturnToSavedLocation(0)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
