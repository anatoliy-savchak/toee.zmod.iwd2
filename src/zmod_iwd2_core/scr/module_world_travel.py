import toee
import const_toee
import const_proto_npc
import module_consts
import module_globals
import utils_obj
import ctrl_behaviour
import py14764_npc_portal

class CtrlWorldPortal(py14764_npc_portal.CtrlPortalOut):
	@classmethod
	def can_travel_keep_to_corinth(cls, npc):
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CORINTH]
		print("can_travel_keep_to_corinth")
		return True

	@classmethod
	def travel_keep_to_corinth(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_KEEP_TO_CORINTH, 0, 0, 
			module_consts.MAP_ID_ZMOD_CORINTH, 
			module_consts.ZMOD_CORINTH_ENTRY_COORDS[0], 
			module_consts.ZMOD_CORINTH_ENTRY_COORDS[1]
			)
		return

	@classmethod
	def can_travel_corinth_to_keep(cls, npc):
		return True

	@classmethod
	def travel_corinth_to_keep(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_KEEP_TO_CORINTH, 0, 0, 
			module_consts.MAP_ID_ZMOD_KEEP_LV1, 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_OUTSKIRT[0], 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_OUTSKIRT[1]
			)
		return

	@classmethod
	def can_travel_keep_to_caves(cls, npc):
		return True
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CAVES]

	@classmethod
	def travel_keep_to_caves(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_KEEP_TO_CAVES, 0, 0, 
			module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE,
			module_consts.ZMOD_CAVE_ENTRY_ENTRY_OUTSKIRTS[0], 
			module_consts.ZMOD_CAVE_ENTRY_ENTRY_OUTSKIRTS[1]
			)
		return

	@classmethod
	def can_travel_keep_to_orc_fort(cls, npc):
		return True
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CAVES]

	@classmethod
	def travel_keep_to_orc_fort(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_KEEP_TO_ORC_FORT, 0, 0, 
			module_consts.MAP_ID_ZMOD_ORC_FORT,
			module_consts.ZMOD_ORC_FORT_ENTRY1[0], 
			module_consts.ZMOD_ORC_FORT_ENTRY1[1]
			)
		return

	@classmethod
	def can_travel_corinth_to_orc_fort(cls, npc):
		return True
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CAVES]

	@classmethod
	def travel_corinth_to_orc_fort(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_CORINTH_ORC_FORT, 0, 0, 
			module_consts.MAP_ID_ZMOD_ORC_FORT,
			module_consts.ZMOD_ORC_FORT_ENTRY1[0], 
			module_consts.ZMOD_ORC_FORT_ENTRY1[1]
			)
		return

	@classmethod
	def can_travel_orc_fort_to_corinth(cls, npc):
		return True
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CAVES]

	@classmethod
	def travel_orc_fort_to_corinth(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_CORINTH_ORC_FORT, 0, 0, 
			module_consts.MAP_ID_ZMOD_CORINTH,
			module_consts.ZMOD_CORINTH_ENTRY_COORDS[0], 
			module_consts.ZMOD_CORINTH_ENTRY_COORDS[1]
			)
		return

	@classmethod
	def can_travel_orc_fort_to_keep(cls, npc):
		return True
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CAVES]

	@classmethod
	def travel_orc_fort_to_keep(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_KEEP_TO_ORC_FORT, 0, 0, 
			module_consts.MAP_ID_ZMOD_KEEP_LV1, 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_OUTSKIRT[0], 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_OUTSKIRT[1]
			)
		return

	@classmethod
	def can_travel_corinth_to_cave_entrance(cls, npc):
		return True
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CAVES]

	@classmethod
	def travel_corinth_to_cave_entrance(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_CORINTH_TO_CAVES, 0, 0, 
			module_consts.MAP_ID_ZMOD_CAVE_ENTRANCE, 
			module_consts.ZMOD_CAVE_ENTRY_ENTRY_OUTSKIRTS[0], 
			module_consts.ZMOD_CAVE_ENTRY_ENTRY_OUTSKIRTS[1]
			)
		return

	@classmethod
	def can_travel_cave_entrance_to_keep(cls, npc):
		return True
		#return toee.game.global_flags[module_globals.GFLAG_KNOWN_CAVES]

	@classmethod
	def travel_cave_entrance_to_keep(cls, npc):
		toee.game.fade_and_teleport(
			module_consts.ZMOD_TRAVEL_TIME_KEEP_TO_CAVES, 0, 0, 
			module_consts.MAP_ID_ZMOD_KEEP_LV1, 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_OUTSKIRT[0], 
			module_consts.ZMOD_KEEP_LV1_ENTRY_COORDS_OUTSKIRT[1]
			)
		return

class CtrlWorldPortalKeep(CtrlWorldPortal):
	@classmethod
	def get_dialog_line_cls(cls, npc): return 1

class CtrlWorldPortalCorinth(CtrlWorldPortal):
	@classmethod
	def get_dialog_line_cls(cls, npc): return 21

class CtrlWorldPortalOrcFort(CtrlWorldPortal):
	@classmethod
	def get_dialog_line_cls(cls, npc): return 31

class CtrlWorldPortalCaveEntrance(CtrlWorldPortal):
	@classmethod
	def get_dialog_line_cls(cls, npc): return 41
