import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc, factions_zmod
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_toee, tpai, tpactions, utils_strategy
import py04000_monster_manual1_p1, utils_npc_spells_tactics, module_quests, module_consts, rumor_control, utils_pc
import const_proto_armor_iwd2, ctrl_behaviour_ie, const_proto_items_iwd2, ctrl_daemon
import utils_journal as uj, inf_scripting
#### IMPORT ####
import py10003_ar1000_npc_inst_classes_auto
#### IMPORT END ####


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
class Ctrl_10HEDRON_AR1000_Hedron(py10003_ar1000_npc_inst_classes_auto.Ctrl_10HEDRON_AR1000_Hedron_Auto): # 10HEDRON 

	def setup_appearance(self, npc):
		super(Ctrl_10HEDRON_AR1000_Hedron, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7140) # NPC_7142_s_Moneir
		# phaen: NPC_7162_s_Falrinth
		# some brute: NPC_7212_s_GisterNoshim
		# serious dark: NPC_7322_s_Jinnerth
		# funny fighter: NPC_7332_s_Deggum
		# bald merchant: NPC_7392_s_MerchantPrisoner
		# poor peasant: NPC_7412_s_Nybble
		# beard: NPC_7442_s_HoltenKindlehopper
		# one eyed: NPC_7452_s_Rentsch
		# fat: NPC_7462_s_Ploceus
		# zelenskyy: NPC_7782_s_EarthTempleLt
		# cleric lite?: NPC_8482_s_Hextor_Acolyte
		return 

	@classmethod
	def test_Hedron_Quest_4_max_diplomacy_manual(cls, self):
		hedron_npc, hedron = self._get_ie_object("'Hedron'")
		assert isinstance(hedron, inf_scripting.InfScriptSupportNPC)

		hedron.iSetNumTimesTalkedTo(1) # to get to 33: You're back - any word of me Ma?
		hedron.iSetGlobal("Reig_Quest", "GLOBAL", 1) # to get to 33: You're back - any word of me Ma?
		hedron.iSetGlobal("Hedron_Know_Attack","GLOBAL", 2) # to get to 33: You're back - any word of me Ma?
		hedron.iSetGlobal("Hedron_Quest", "GLOBAL", 2) # to get to 33: You're back - any word of me Ma?
		hedron.iSetGlobal("Dock_Goblin_Quest","GLOBAL", 1) # to get to 33: You're back - any word of me Ma?

		toee.game.leader.stat_base_set(toee.stat_charisma, 16) # to get to resp 62: You're back - any word of me Ma?
		print('toee.game.leader.stat_base_set(toee.stat_charisma, 16) => {}'.format(toee.game.leader.stat_base_get(toee.stat_charisma)))
		return

	@classmethod
	@inf_scripting.dump_args
	def test_Hedron_identifiers_test_auto(cls, self):
		hedron_npc, hedron = self._get_ie_object("'Hedron'")
		if not hedron_npc or not hedron:
			raise Exception('Test Failed: Object Hedron not found!')
		else:
			print('Test: Hedron acquiring passed: {}'.format(hedron_npc))

		assert isinstance(hedron, inf_scripting.InfScriptSupportNPC)

		try:
			hedron._prepare_scripting()

			if True:
				obj, ctrl = hedron._get_ie_object("Myself")
				if not obj or not ctrl:
					raise Exception('Test Failed: Object Myself not found!')
				else:
					print('Test: Hedron Object Myself passed: {}'.format(obj))

			if True:
				obj, ctrl = hedron._get_ie_object("Protagonist")
				if not obj:
					raise Exception('Test Failed: Object Protagonist not found!')

				if obj.type != toee.obj_t_pc:
					raise Exception('Test Failed: Object Protagonist not correct PC!')
				else:
					print('Test: Hedron Object Protagonist passed: {}'.format(obj))

			if True:
				obj, ctrl = hedron._get_ie_object("NearestPC")
				if not obj:
					raise Exception('Test Failed: Object NearestPC not found!')

				if obj.type != toee.obj_t_pc:
					raise Exception('Test Failed: Object NearestPC not correct PC!')
				else:
					print('Test: Hedron Object NearestPC passed: {}'.format(obj))

			if True:
				obj, ctrl = hedron._get_ie_object("Nearest")
				if not obj:
					raise Exception('Test Failed: Object Nearest not found!')
				else:
					print('Test: Hedron Object Nearest passed: {}'.format(obj))
		finally:
			hedron._unprepare_scripting()
		return

class Ctrl_10ELDGUL_AR1000_Eldgull(py10003_ar1000_npc_inst_classes_auto.Ctrl_10ELDGUL_AR1000_Eldgull_Auto): # 10ELDGUL 

	def setup_appearance(self, npc):
		super(Ctrl_10ELDGUL_AR1000_Eldgull, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 6680) # NPC_6682_s_Morgan
		return 

class Ctrl_10SCREED_AR1000_Screed(py10003_ar1000_npc_inst_classes_auto.Ctrl_10SCREED_AR1000_Screed_Auto): # 10SCREED 

	def setup_appearance(self, npc):
		super(Ctrl_10SCREED_AR1000_Screed, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 6680) # NPC_6682_s_Morgan
		return 

	@classmethod
	@inf_scripting.dump_args
	def test_identifiers_auto(cls, self):
		name = 'Screed'
		this_npc, this_ctrl = self._get_ie_object("'{}'".format(name))
		if not this_npc or not this_ctrl:
			raise Exception('Test Failed: Object {} not found!'.format(name))
		else:
			print('Test: {} acquiring passed: {}'.format(name, this_npc))

		assert isinstance(this_ctrl, inf_scripting.InfScriptSupportNPC)

		try:
			this_ctrl._prepare_scripting(this_npc)

			if True:
				obj, ctrl = this_ctrl._get_ie_object("NearestPC")
				if not obj:
					raise Exception('Test Failed: Object NearestPC not found!')

				if obj.type != toee.obj_t_pc:
					raise Exception('Test Failed: Object NearestPC not correct PC!')
				else:
					print('Test: {} Object NearestPC passed: {}'.format(name, obj))

			if True:
				obj, ctrl = this_ctrl._get_ie_object("Nearest")
				if not obj:
					raise Exception('Test Failed: Object Nearest not found!')
				else:
					print('Test: {} Object Nearest passed: {}'.format(name, obj))
		finally:
			this_ctrl._unprepare_scripting()
		return

class Ctrl_10REIG_AR1000_Reig(py10003_ar1000_npc_inst_classes_auto.Ctrl_10REIG_AR1000_Reig_Auto): # 10REIG 

	def setup_appearance(self, npc):
		super(Ctrl_10REIG_AR1000_Reig, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 6670) # NPC_6672_s_Bertram
		return 

class Ctrl_10JON_AR1000_Jon(py10003_ar1000_npc_inst_classes_auto.Ctrl_10JON_AR1000_Jon_Auto): # 10JON 

	def setup_appearance(self, npc):
		super(Ctrl_10JON_AR1000_Jon, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7040) # NPC_7042_s_Valden
		return 

class Ctrl_10BROGAN_AR1000_Brogan(py10003_ar1000_npc_inst_classes_auto.Ctrl_10BROGAN_AR1000_Brogan_Auto): # 10BROGAN 

	def setup_appearance(self, npc):
		super(Ctrl_10BROGAN_AR1000_Brogan, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7050) # NPC_7052_s_Mytch
		return 

class Ctrl_10JORUN_AR1000_Jorun(py10003_ar1000_npc_inst_classes_auto.Ctrl_10JORUN_AR1000_Jorun_Auto): # 10JORUN 

	def setup_appearance(self, npc):
		super(Ctrl_10JORUN_AR1000_Jorun, self).setup_appearance(npc)
		npc.obj_set_int(toee.obj_f_critter_portrait, 7170) # NPC_7172_s_Grank
		return 

	@inf_scripting.dump_args
	def test_race_auto(self):
		try:
			self._prepare_scripting()

			if True:
				result = self.iRace("'Jorun'", 'human')
				if result:
					raise Exception('Test Failed: result should be False!')
				else:
					print('Test Succ: result should be False')

			if True:
				result = self.iRace("'Jorun'", 'dwarf')
				if not result:
					raise Exception('Test Failed: result should be True!')
				else:
					print('Test Succ: result should be True')
		finally:
			self._unprepare_scripting()
		return

class Ctrl_10GOB_AR1000_1000_Goblin_01(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_01_Auto): # 10GOB 
	pass

class Ctrl_10GOBD_AR1000_Dead_Goblin_0(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBD_AR1000_Dead_Goblin_0_Auto): # 10GOBD 
	pass

class Ctrl_10MALED_AR1000_Dead_Townsperson_0(py10003_ar1000_npc_inst_classes_auto.Ctrl_10MALED_AR1000_Dead_Townsperson_0_Auto): # 10MALED 
	pass

class Ctrl_10SOLDRD_AR1000_Brohn_Dead(py10003_ar1000_npc_inst_classes_auto.Ctrl_10SOLDRD_AR1000_Brohn_Dead_Auto): # 10SOLDRD 
	pass

class Ctrl_10GOBD_AR1000_Dead_Goblin_1(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBD_AR1000_Dead_Goblin_1_Auto): # 10GOBD 
	pass

class Ctrl_10GOBD_AR1000_Dead_Goblin_2(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBD_AR1000_Dead_Goblin_2_Auto): # 10GOBD 
	pass

class Ctrl_10GOBD_AR1000_Dead_Goblin_3(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBD_AR1000_Dead_Goblin_3_Auto): # 10GOBD 
	pass

class Ctrl_10SOLDRD_AR1000_Dead_Soldier_0(py10003_ar1000_npc_inst_classes_auto.Ctrl_10SOLDRD_AR1000_Dead_Soldier_0_Auto): # 10SOLDRD 
	pass

class Ctrl_10GOBD_AR1000_Dead_Goblin_J1(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBD_AR1000_Dead_Goblin_J1_Auto): # 10GOBD 
	pass

class Ctrl_10GOBD_AR1000_Dead_Goblin_J2(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBD_AR1000_Dead_Goblin_J2_Auto): # 10GOBD 
	pass

class Ctrl_10GOBD_AR1000_Dead_Goblin_6(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBD_AR1000_Dead_Goblin_6_Auto): # 10GOBD 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_02(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_02_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_03(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_03_Auto): # 10GOB 
	pass

class Ctrl_10MALED_AR1000_Dead_Townsperson_1(py10003_ar1000_npc_inst_classes_auto.Ctrl_10MALED_AR1000_Dead_Townsperson_1_Auto): # 10MALED 
	pass

class Ctrl_10GOBARD_AR1000_Dead_Goblin_7(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBARD_AR1000_Dead_Goblin_7_Auto): # 10GOBARD 
	pass

class Ctrl_10SOLDRD_AR1000_Dead_Soldier_1(py10003_ar1000_npc_inst_classes_auto.Ctrl_10SOLDRD_AR1000_Dead_Soldier_1_Auto): # 10SOLDRD 
	pass

class Ctrl_10SAILRD_AR1000_Dead_Sailor(py10003_ar1000_npc_inst_classes_auto.Ctrl_10SAILRD_AR1000_Dead_Sailor_Auto): # 10SAILRD 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_04(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_04_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_05(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_05_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_06(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_06_Auto): # 10GOB 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_01(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_01_Auto): # 10GOBAR 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_07(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_07_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_19(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_19_Auto): # 10GOB 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_02(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_02_Auto): # 10GOBAR 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_08(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_08_Auto): # 10GOB 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_03(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_03_Auto): # 10GOBAR 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_09(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_09_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_10(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_10_Auto): # 10GOB 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_04(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_04_Auto): # 10GOBAR 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_11(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_11_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_12(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_12_Auto): # 10GOB 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_05(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_05_Auto): # 10GOBAR 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_06(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_06_Auto): # 10GOBAR 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_07(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_07_Auto): # 10GOBAR 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_08(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_08_Auto): # 10GOBAR 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_13(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_13_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_14(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_14_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_15(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_15_Auto): # 10GOB 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_09(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_09_Auto): # 10GOBAR 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_16(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_16_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_17(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_17_Auto): # 10GOB 
	pass

class Ctrl_10GOB_AR1000_1000_Goblin_18(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOB_AR1000_1000_Goblin_18_Auto): # 10GOB 
	pass

class Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_10(py10003_ar1000_npc_inst_classes_auto.Ctrl_10GOBAR_AR1000_1000_Goblin_Archer_10_Auto): # 10GOBAR 
	pass

class Ctrl_10CRANDA_AR1000_Crandall(py10003_ar1000_npc_inst_classes_auto.Ctrl_10CRANDA_AR1000_Crandall_Auto): # 10CRANDA 
	pass

class Ctrl_10MALED_AR1000_Dead_Townsperson_2(py10003_ar1000_npc_inst_classes_auto.Ctrl_10MALED_AR1000_Dead_Townsperson_2_Auto): # 10MALED 
	pass

class Ctrl_10HINT_AR1000_Door_Hint_Text_00(py10003_ar1000_npc_inst_classes_auto.Ctrl_10HINT_AR1000_Door_Hint_Text_00_Auto): # 10HINT 
	pass

class Ctrl_10HINT_AR1000_Door_Hint_Text_01(py10003_ar1000_npc_inst_classes_auto.Ctrl_10HINT_AR1000_Door_Hint_Text_01_Auto): # 10HINT 
	pass

class Ctrl_12SWIFTH_AR1000_Swift_Thomas_Hidden(py10003_ar1000_npc_inst_classes_auto.Ctrl_12SWIFTH_AR1000_Swift_Thomas_Hidden_Auto): # 12SWIFTH 
	pass

class Ctrl_10FIRTHH_AR1000_Firtha_Kerdos(py10003_ar1000_npc_inst_classes_auto.Ctrl_10FIRTHH_AR1000_Firtha_Kerdos_Auto): # 10FIRTHH 
	pass

