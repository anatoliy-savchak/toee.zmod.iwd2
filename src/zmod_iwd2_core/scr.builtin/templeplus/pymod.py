import toee, tpdp

class PythonModifier(tpdp.ModifierSpec):
    def AddHook(self, eventType, eventKey, callbackFcn, argsTuple ):
        """ PythonModifier.AddHook(int[ET_OnGetNumAttacksBase]: eventType, int[EK_NONE]: eventKey, func: callbackFcn, (): argsTuple) -> None"""
        self.add_hook(eventType, eventKey, callbackFcn, argsTuple)
    def ExtendExisting(self, condName):
        self.extend_existing(condName)
    def AddItemForceRemoveHandler(self): # in charge of backing up condition args
        self.add_item_force_remove_callback()
    def MapToFeat(self, feat_enum, feat_list_max = -1, feat_cond_arg2 = 0):
        self.add_to_feat_dict(feat_enum, feat_list_max, feat_cond_arg2)
    # Spell related standard hooks
    def AddSpellCountdownStandardHook(self):
        # adds an ET_OnBeginRound handler that (normally) does:
        # If countdown expired: (<0)
        #   1. Float text "Spell Expired"
        #   2. RemoveSpell() (has case-by-case handlers for Spell_End; Temple+ adds generic handling for wall spells here)
        #   3. RemoveSpellMod()
        # Else:
        #   Decrement count, update spell packet duration
        self.add_spell_countdown_standard()    
    def AddAoESpellEndStandardHook(self): 
        # adds a EK_S_Spell_End handler that:
        # 1. Ends particles for all spell objects
        # 2. RemoveSpellMod()
        self.add_aoe_spell_ender()
    def AddSpellDismissStandardHook(self):
        self.add_spell_dismiss_hook()
