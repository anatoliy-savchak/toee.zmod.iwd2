import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting, module_difficulty
#### IMPORTS ####
import py20001_ar2000_npc_classes_auto
#### END IMPORTS ####

#### GVARS ####
MODULE_SCRIPT_ID = 20002
#### GVARS END ####

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def cs(): return ctrl_daemon.gdc()
#### NPCS ####
class Ctrl_20ORCACH(py20001_ar2000_npc_classes_auto.Ctrl_20ORCACH_Auto): # 20ORCACH 
	def setup_char(self, npc):
		if module_difficulty.get_difficulty() <= 1:
			super(Ctrl_20ORCSHM, self).setup_char(npc)
			return

		#utils_npc.npc_abilities_set(npc, [10, 15, 11, 9, 8, 8])
		utils_npc_build.NPCAbilitiesSetup(12, 15, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_ranged().npc_setup_random(npc)

		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, const_toee.stat_level_npc_warriror)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL

		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1)

		npc.feat_add(toee.feat_weapon_focus_longbow, 1)

		#utils_npc.ensure_hp(npc, 8) # MaximumHP: 8
		utils_npc.npc_generate_hp_module(npc)
		return
	pass

class Ctrl_20ORCWAR(py20001_ar2000_npc_classes_auto.Ctrl_20ORCWAR_Auto): # 20ORCWAR 
	pass

class Ctrl_20ORCSHM(py20001_ar2000_npc_classes_auto.Ctrl_20ORCSHM_Auto): # 20ORCSHM 
	# Shaman

	def setup_appearance(self, npc):
		super(Ctrl_20ORCSHM, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 5420) # none
		return

	def setup_char(self, npc):
		if module_difficulty.get_difficulty() <= 1:
			super(Ctrl_20ORCSHM, self).setup_char(npc)
			return

		#utils_npc.npc_abilities_set(npc, [10, 15, 11, 9, 8, 8])
		utils_npc_build.NPCAbilitiesSetup(12, 15, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_cleric().npc_setup_random(npc)

		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_cleric)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_cleric)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL

		#npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # target cr: 2

		npc.feat_add(toee.feat_spell_focus_enchantment, 1)

		npc.skill_ranks_set(toee.skill_concentration, 3 + (npc.highest_divine_caster_level-1)*1)

		#utils_npc.ensure_hp(npc, 22) # MaximumHP: 22
		utils_npc.npc_generate_hp_module(npc)
		return

	def enter_combat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)

		stat_class = toee.stat_level_cleric
		caster_level = attachee.highest_divine_caster_level
		self.setup_spells(attachee, stat_class, caster_level)
		return toee.RUN_DEFAULT

	def setup_spells(self, npc, stat_class, caster_level):
		# 1
		self.spells.add_spell(toee.spell_bane, stat_class, caster_level) # domain one
		#self.spells.add_spell(toee.spell_bless, stat_class, caster_level)
		self.spells.add_spell(toee.spell_doom, stat_class, caster_level)
		#self.spells.add_spell(toee.spell_cause_fear, stat_class, caster_level)

		# 0
		self.spells.add_spell(toee.spell_cure_minor_wounds, stat_class, caster_level)
		return

	def create_tactics(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		tac = utils_tactics.TacticsHelper(self.get_name())
		while (1):
			if (not utils_npc_spells_tactics.STBless(npc, self.spells, tac).execute()):
				break

			if (not utils_npc_spells_tactics.STBaneSelf(npc, self.spells, tac).execute()):
				break

			foes_can_los = self._vars_tactics["foes_can_los"]
			if not foes_can_los:
				foes_can_los = self._vars_tactics["foes_can_sense"]

			spell_tactic = utils_npc_spells_tactics.STCauseFear(npc, self.spells, tac)
			if spell_tactic.set_target_first(foes_can_los) and not spell_tactic.execute():
				break

			spell_tactic = utils_npc_spells_tactics.STDoom(npc, self.spells, tac)
			if spell_tactic.set_target_first(foes_can_los) and not spell_tactic.execute():
				break

			# default
			return None
			break

		tac.add_total_defence()
		tac.add_stop()
		print("create_tactics {}".format(npc))
		return tac

	pass

class Ctrl_20ORCA3(py20001_ar2000_npc_classes_auto.Ctrl_20ORCA3_Auto): # 20ORCA3 

	def setup_char(self, npc):
		if module_difficulty.get_difficulty() <= 1:
			super(Ctrl_20ORCA3, self).setup_char(npc)
			return
		#utils_npc.npc_abilities_set(npc, [10, 15, 11, 9, 8, 8])
		utils_npc_build.NPCAbilitiesSetup(12, 15, utils_races.RACE_ABILITY_BONUSES_ORC).generate().focus_melee().npc_setup_random(npc)

		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, const_toee.stat_level_npc_warriror)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, const_toee.stat_level_npc_warriror)

		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_LAWFUL_EVIL) # 0x13 LAWFUL_EVIL

		npc.obj_set_int(toee.obj_f_npc_challenge_rating, -1) # target cr: 1

		npc.feat_add(toee.feat_weapon_focus_battleaxe, 1)

		#utils_npc.ensure_hp(npc, 18) # MaximumHP: 18
		utils_npc.npc_generate_hp_module(npc)
		return
	pass

class Ctrl_20ORCW3(py20001_ar2000_npc_classes_auto.Ctrl_20ORCW3_Auto): # 20ORCW3 
	pass

class Ctrl_20ORCA4(py20001_ar2000_npc_classes_auto.Ctrl_20ORCA4_Auto): # 20ORCA4 
	pass

class Ctrl_20ORCW4(py20001_ar2000_npc_classes_auto.Ctrl_20ORCW4_Auto): # 20ORCW4 
	pass

class Ctrl_20ORCFIR(py20001_ar2000_npc_classes_auto.Ctrl_20ORCFIR_Auto): # 20ORCFIR 
	pass

class Ctrl_20ORCRUN(py20001_ar2000_npc_classes_auto.Ctrl_20ORCRUN_Auto): # 20ORCRUN 
	pass

class Ctrl_20ORCCHF(py20001_ar2000_npc_classes_auto.Ctrl_20ORCCHF_Auto): # 20ORCCHF 
	pass

class Ctrl_20DERETH(py20001_ar2000_npc_classes_auto.Ctrl_20DERETH_Auto): # 20DERETH 
	pass

class Ctrl_20SABRIN(py20001_ar2000_npc_classes_auto.Ctrl_20SABRIN_Auto): # 20SABRIN 
	pass

