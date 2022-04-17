import toee, tpdp, const_toee, factions_zmod
import combat_strategy_hooks
import sys, logging


def zmod_conditions_apply_pc():
	for pc in toee.game.party:
		pc.condition_add("Break_Object")
		pc.condition_add("Smash_Object")
		#pc.condition_add("Skill_Appraise_Bonus")
		pc.condition_add("Inspect")
		pc.condition_add('Rest_Full')
		#pc.condition_add("Debug_Location")
		#pc.condition_add("Debug_Rotation")

		#pc.faction_add(factions_zmod.FACTION_ALLY_NPC)
		#pc.faction_add(factions_zmod.FACTION_FIRENDY_NPC)
	return

def zmod_templeplus_config_apply():
	# import startup_zmod
	# startup_zmod.zmod_templeplus_config_apply()
	print("zmod_templeplus_config_apply")
	if ("config_set_string" in dir(tpdp)):
		tpdp.config_set_string("hpfornpchd", "average")
		tpdp.config_set_string("hponlevelup", "average")

	if ("config_set_bool" in dir(tpdp)):
		tpdp.config_set_bool("preferuse5footstep", 1)
		tpdp.config_set_bool("disabletargetsurrounded", 1)
		tpdp.config_set_bool("disablechooserandomspell_regardinvulnerablestatus", 1)
		tpdp.config_set_bool("iszmod", 1)
	

	combat_strategy_hooks.hook_module()

	# could be run from startup.txt
	party = toee.game.party
	if (party):
		firstpc = party[0]
		if (firstpc):
			firstpc.scripts[const_toee.sn_new_map] = 6101
			firstpc.condition_add("InitiativeInfo")
			# DEBUG!!
			#firstpc.feat_add("Forge Weapon and Armor") # CHEAT

	#zmod_setup_logging()
	return

def zmod_change_pcs_radius():
	# import startup_zmod
	# startup_zmod.zmod_change_pcs_radius()
	for pc in toee.game.party:
		print("pc proto: {}".format(pc.proto))
		protoobj = toee.game.getproto(pc.proto)
		protoobj.radius = 30
	return

ghandler = None

def zmod_setup_logging():
	global ghandler
	if (ghandler is None):
		logger = logging.getLogger()
		logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(funcName)s %(message)s')
		stdout_handler = logging.StreamHandler(sys.stdout)
		#stdout_handler.setLevel(logging.DEBUG)
		stdout_handler.setLevel(5)
		stdout_handler.setFormatter(formatter)
		ghandler = stdout_handler
		logger.addHandler(stdout_handler)
	return