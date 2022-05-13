# This module is specifically to address missing breakp() function from TemplePlus
import debug, tpdp
import json

def breakp(v):
	""" Debug option for TemplePlus.
	Keyword arguments:
	v --- string or None (default None)
	"""
	if ("breakp" in dir(debug)):
		debug.breakp(v)
	return

def debug_save_conds(file_name):
	f = open(file_name, "w")
	o = debug.dump_conds()
	dm = json.dumps(o, indent = 2)
	f.write(dm)
	f.close()
	return

def debug_save_spells(file_name):
	f = open(file_name, "w")
	o = debug.dump_spells()
	dm = json.dumps(o, indent = 2)
	f.write(dm)
	f.close()
	return

def save_text(file_name, s):
	f = open(file_name, "w")
	f.write(s)
	f.close()
	return

def swap_zmod():
	iszmod = tpdp.config_get_bool("iszmod")
	print("iszmod: {}".format(iszmod))
	iszmod = False
	tpdp.config_set_bool("iszmod", iszmod)
	iszmod = tpdp.config_get_bool("iszmod")
	print("iszmod new: {}".format(iszmod))
	return


DEBUG_STORAGE_PRINT_FOLDER = 1
DEBUG_STORAGE_PRINT_FILE = 1
DEBUG_STORAGE_USE_FOLDER_CURRENT = 0
DEBUG_STORAGE_USE_ALIAS = 1

DEBUG_DUMP_ARGS_START_END = 0
DEBUG_PRINT_GLOBAL_SET_INTO_HISTORY = 1