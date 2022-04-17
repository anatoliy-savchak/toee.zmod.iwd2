import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_armor

def san_dialog(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = ctrl_behaviour.CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.dialog(attachee, triggerer)
	return toee.RUN_DEFAULT

class CtrlVillageSmithWife(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 14711

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = self.get_proto_id()
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		utils_item.item_clear_all(npc)

		box = toee.game.obj_create(const_proto_containers.PROTO_CONTAINER_CHEST_GENERIC, npc.location)
		box.object_flag_set(toee.OF_DONTDRAW)
		box.obj_set_int(toee.obj_f_container_inventory_source, 0)
		npc.substitute_inventory = box

		# create inventory
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_KILT, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CLOTH_ARMOR, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		
		npc.item_wield_best_all()
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if not attachee.has_met(triggerer):
			triggerer.begin_dialog(attachee, 1)
			return toee.SKIP_DEFAULT
		else:
			triggerer.begin_dialog(attachee, 100)
		return toee.SKIP_DEFAULT
