from toee import *
from math import sqrt, atan2
import os
import tpdp
import subprocess

def readMes(mesfile):
	""" Read the mesfile into a dictionary indexed by line number. """
	mesFile = file(mesfile,'r')
	mesDict = {}
	for line in mesFile.readlines():
		# Remove whitespace.
		line = line.strip()
		# Ignore empty lines.
		if not line:
			continue
		# Ignore comment lines.
		if line[0] != '{':
			continue
		# Decode the line.  Just standard python string processing.
		line = line.split('}')[:-1]
		for i in range(len(line)):
			line[i] = line[i].strip()
			line[i] = line[i][1:]
		contents = line[1:]
		# Insert the line into the mesDict.
		mesDict[int(line[0])] = contents
	mesFile.close()
	# print 'File read'
	return mesDict

def supports_custom_name():
	if (hasattr(game, 'make_custom_name') and callable(getattr(game, 'make_custom_name'))):
		return 1
	return 0

def make_custom_name(new_name):
	if supports_custom_name():
		return game.make_custom_name(new_name)
	return -1

def readMesLine(mesfile, lineId):
	result = ""
	mesFile = file(mesfile,'r')
	for line in mesFile.readlines():
		# Remove whitespace.
		line = line.strip()
		# Ignore empty lines.
		if not line:
			continue
		if line[0] != '{':
			continue
		line = line.split('}')[:-1]
		if (len(line) < 2): continue
		s = unicode(line[0][1:])
		if (not s.isnumeric()): continue
		if (int(line[0][1:]) == lineId): 
			result = line[1][1:]
			break
	mesFile.close()
	return result

def find_dialog_file_name(scriptId):
	files = os.listdir("data\\dlg")
	starts = "{:0>5d}".format(scriptId)
	for fileName in files:
		if (starts in fileName): return fileName
	fn = "overrides\\data\\dlg"
	if (os.path.isdir(fn)):
		files = os.listdir("overrides\\data\\dlg")
		starts = "{:0>5d}".format(scriptId)
		for fileName in files:
			if (starts in fileName): return fileName
	return None

def get_obj_by_id(id):
	result = OBJ_HANDLE_NULL
	try:
		result = game.get_obj_by_id(id)
	except:
		result = OBJ_HANDLE_NULL
	return result

# utils_toee.time_hours2_from_elapsed_sec(game.time.time_game_in_seconds(game.time))
def time_hours2_from_elapsed_sec(elapsed_sec):
	h = elapsed_sec // 3600 % 24
	return h

def map_calc_limits(topLeft, bottomRight):
	# measure: https://co8.org/community/threads/toeezwb-pet-project.12138/#post-145329
	# import utils_toee
	# a=utils_toee.map_calc_limits((501, 434), (450, 494))
	# utils_toee.copy2clip(utils_toee.map_calc_limits((501, 434), (450, 494)))
	# utils_toee.copy2clip(utils_toee.map_calc_limits((546, 408), (428, 526)))

	# Corinth. TopLeft: 510, 420; TopRight: 415, 414; BottomRight: 427, 533; BottomLeft: 541, 512;
	# utils_toee.copy2clip(utils_toee.map_calc_limits((510, 420), (427, 533)))

	# Orc Fort. TopLeft: 525, 427; BottomRight: 416, 524; 
	# utils_toee.copy2clip(utils_toee.map_calc_limits((525, 427), (416, 524)))

	# Orc Fort Towers. TopLeft: 501, 458; BottomRight: 461, 492; 
	# utils_toee.copy2clip(utils_toee.map_calc_limits((501, 458), (461, 492)))

	# Caves Level 2
	# utils_toee.copy2clip(utils_toee.map_calc_limits((532, 424), (426, 530)))

	# AR1000
	# utils_toee.copy2clip(utils_toee.map_calc_limits((478, 342), (482, 616)))
	# x: 342, 619, y: 341, 617
	# utils_toee.copy2clip(utils_toee.map_calc_limits((619, 341), (342, 617)))
	middle = tpdp.LocAndOffsets(480, 489, 0, 0).get_overall_offset()
	left = tpdp.LocAndOffsets(topLeft[0]+40, topLeft[0]+40, 0, 0).get_overall_offset()[0]-middle[0]
	right = tpdp.LocAndOffsets(bottomRight[0]-27, bottomRight[0]-27, 0, 0).get_overall_offset()[0]-middle[0]
	top = -tpdp.LocAndOffsets(topLeft[1]-10, topLeft[1]-10, 0, 0).get_overall_offset()[1]
	bottom = -tpdp.LocAndOffsets(bottomRight[1]+10, bottomRight[1]+10, 0, 0).get_overall_offset()[1]
	return "{},{},{},{}".format(int(left), int(top), int(right), int(bottom))

def copy2clip(txt):
	cmd='echo '+txt.strip()+'|clip'
	return subprocess.check_call(cmd, shell=True)