import toee
import inf_scripting
#### IMPORT ####
#### IMPORT END ####

#### BCS ####
class Script_10REIG0_Auto(inf_scripting.ScriptBase):
	# AR1000 10REIG Reig ScriptGeneral
	
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
			
			break # while
		return
		
	@classmethod
	def do_execute_block_01(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# Global("HEALED_REIG","MYAREA",0)
		# HPGT(Myself,3)
		if not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetGlobal("HEALED_REIG","MYAREA",1)
			# Continue()
			self.iReturnToSavedLocation(0)
			return False # continue() - pass further blocks
		return False
		
	@classmethod
	def do_execute_block_02(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# NumTimesTalkedTo(0)
		# !Allegiance(Myself,ENEMY)
		# !Dead(Myself)
		# Or(2)
		# See(Protagonist,0)
		# See([PC],0)
		# Range(LastSeenBy(Myself),18,LESS_THAN)
		if not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# StartCutSceneMode()
			# ClearAllActions()
			# SetDialogueRange(300)
			# MultiPlayerSync()
			# Dialogue(LastMarkedObject)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_03(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# NumTimesTalkedTo(0)
		# !Allegiance(Myself,ENEMY)
		# See([PC],0)
		if not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# FaceObject(LastMarkedObject)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_04(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !Allegiance(Myself,ENEMY)
		# !Dead(Myself)
		# Global("Reig_Heal_Priest","GLOBAL",0)
		# Global("Reig_Quest","GLOBAL",1)
		# !Global("HEALED_REIG","MYAREA",0)
		# See([PC],0)
		if not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# SetDialogueRange(300)
			# Dialogue(LastMarkedObject)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_05(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !TimerActive(21)
		# GlobalLT("Reig_Quest","GLOBAL",2)
		# !See([ENEMY.0.GOBLIN],0)
		if not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# FloatMessage(Myself,1659)  // "Damned arm... hurts like the devil."
			# StartRandomTimer(21,10,15)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
	@classmethod
	def do_execute_block_06(cls, self):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		# !NearSavedLocation(3)
		# !Allegiance(Myself,ENEMY)
		if not self.iNearSavedLocation(3) \
			 and not self.iAllegiance("Myself", "ENEMY"):
			# ReturnToSavedLocation(0)
			self.iReturnToSavedLocation(0)
			return True # break further blocks
		return False
		
