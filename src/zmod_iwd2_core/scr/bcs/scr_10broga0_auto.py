import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10BROGA0_Auto(inf_scripting.ScriptBase):
	# AR1000 10BROGAN Brogan ScriptGeneral
	
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
			
			break_ = cls.do_execute_block_16()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_17()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_18()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_19()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_20()
			if break_ and not is_cutscene_execution: break
			
			break_ = cls.do_execute_block_21()
			if break_ and not is_cutscene_execution: break
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# NumTimesTalkedTo(0)
		# !Allegiance(Myself,ENEMY)
		# !Dead(Myself)
		# See([PC],0)
		# Range(LastSeenBy(Myself),15,LESS_THAN)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# Dialogue(LastMarkedObject)
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(18)
		# !See([ENEMY.0.GOBLIN],0)
		# Global("Brogan_Leave","GLOBAL",0)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# FloatMessage(Myself,1666)  // "Hope there's no other goblins about..."
			# StartRandomTimer(18,10,15)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",0)
		# ActionListEmpty()
		# NearLocation(Myself,1747,524,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([1747.524])
			# SetGlobal("ML_0","LOCALS",1)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",0)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([1747.524])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",1)
		# ActionListEmpty()
		# NearLocation(Myself,1530,781,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([1530.781])
			# SetGlobal("ML_0","LOCALS",2)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",1)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([1530.781])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_07(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",2)
		# ActionListEmpty()
		# NearLocation(Myself,1241,940,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([1241.940])
			# SetGlobal("ML_0","LOCALS",3)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_08(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",2)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([1241.940])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_09(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",3)
		# ActionListEmpty()
		# NearLocation(Myself,910,1053,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([910.1053])
			# SetGlobal("ML_0","LOCALS",4)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_10(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",3)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([910.1053])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_11(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",4)
		# ActionListEmpty()
		# NearLocation(Myself,559,884,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([559.884])
			# SetGlobal("ML_0","LOCALS",5)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_12(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",4)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([559.884])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_13(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",5)
		# ActionListEmpty()
		# NearLocation(Myself,315,625,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([315.625])
			# SetGlobal("ML_0","LOCALS",6)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_14(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",5)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([315.625])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_15(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",6)
		# ActionListEmpty()
		# NearLocation(Myself,229,392,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([229.392])
			# SetGlobal("ML_0","LOCALS",7)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_16(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",6)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([229.392])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_17(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",7)
		# ActionListEmpty()
		# NearLocation(Myself,217,184,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([217.184])
			# SetGlobal("ML_0","LOCALS",8)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_18(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",7)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([217.184])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_19(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",8)
		# ActionListEmpty()
		# NearLocation(Myself,151,20,4)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetStartPos([151.20])
			# SetGlobal("ML_0","LOCALS",9)
			# Continue()
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_20(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",8)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# MoveToPoint([151.20])
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_21(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("ML_0","LOCALS",9)
		# Global("BROGAN_LEAVE","GLOBAL",1)
		if self.iGlobal("'ML_0'", "'LOCALS'", 9) \
			 and self.iGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 1):
			# SetGlobal("BROGAN_LEAVE","GLOBAL",2)
			# SetGlobal("ML_0","LOCALS",0)
			self.iSetGlobal("'BROGAN_LEAVE'", "'GLOBAL'", 2)
			self.iSetGlobal("'ML_0'", "'LOCALS'", 0)
			return True # break further blocks
		return False
		
