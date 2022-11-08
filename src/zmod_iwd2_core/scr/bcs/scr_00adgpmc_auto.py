import toee, debug
import inf_scripting
import module_difficulty
#### IMPORTS ####
#### END IMPORTS ####

#### BCS ####
class Script_00ADGPMC_Auto(inf_scripting.ScriptBase): # 00ADGPMC
	# AR2100 21GAERNT Gaernat Sharptooth ScriptSpecial1 (Special1)
	
	@classmethod
	@inf_scripting.dump_args
	def do_execute(cls, self, locus, continuous = False, block_from = None, code_from = None):
		assert isinstance(self, inf_scripting.InfScriptSupport)
		while True:
			if not block_from or block_from <= 1:
				break_ = cls.do_execute_block_01(self, locus, code_from=code_from if code_from and block_from == 1 else None)
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
				# NumTimesTalkedTo(0)
				# !Allegiance(Myself,ENEMY)
				# !Dead(Myself)
				# See([PC],0)
				if self.iNumTimesTalkedTo(0) \
					 and not self.iAllegiance("Myself", "ENEMY") \
					 and not self.iDead("Myself") \
					 and self.iSee("[PC]", 0):
					d["check"] = 1
				else: d["check"] = 0
			return d["check"]
		
		# StartCutSceneMode()
		# ClearAllActions()
		# SetDialogueRange(75)
		# MultiPlayerSync()
		# Dialogue(LastMarkedObject)
		
		if (code_from is None and do_check()) or (code_from <= 1):
			break_ = cls.do_execute_block_01_code_01(self, locus)
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
		
		# StartCutSceneMode()
		# ClearAllActions()
		# SetDialogueRange(75)
		# MultiPlayerSync()
		# Dialogue(LastMarkedObject)
		
		self.iStartCutSceneMode()
		self.iClearAllActions()
		self.iSetDialogueRange(75)
		self.iMultiPlayerSync()
		self.iDialogue("LastMarkedObject")
		return 0
		
