import toee, debug, utils_storage, utils_item, const_proto_wondrous, const_proto_items

def san_use(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	print("san_use {} {}".format(attachee, triggerer))
	#debug.breakp("san_use")

	if (not triggerer): 
		print("py05001_bag_of_holding::san_use triggerer is none, exit")
		return toee.SKIP_DEFAULT

	bag = find_bag(triggerer, attachee)
	#bag = triggerer.obj_get_obj(toee.obj_f_container_notify_npc)
	if (not bag): 
		print("py05001_bag_of_holding::san_use bag is none, exit")
		return toee.SKIP_DEFAULT

	ctrl = CtrlBagOfHolding.ensure(bag)
	assert isinstance(ctrl, CtrlBagOfHolding)

	#tell somehow, that it was already swpawned
	already_spwawned = attachee.object_flags_get() & toee.OF_STONED
	print("already_spwawned: {}".format(already_spwawned))
	#debug.breakp("already_spwawned")
	if (not already_spwawned):
		utils_item.item_clear_all(attachee)
		ctrl.spawn(attachee)
		attachee.object_flag_set(toee.OF_STONED)

	return toee.RUN_DEFAULT

def san_transfer(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	print("sn_transfer {} {}".format(attachee, triggerer))
	#debug.breakp("sn_transfer")

	if (not triggerer): 
		print("py05001_bag_of_holding::san_transfer triggerer is none, exit")
		return toee.SKIP_DEFAULT

	bag = find_bag(triggerer, attachee)
	print("py05001_bag_of_holding::san_transfer bag: {}".format(bag))
	#if (not bag): 
	#	print("py05001_bag_of_holding::san_transfer bag is none, exit")
	#	return toee.SKIP_DEFAULT

	print("Bag_Of_Holding_timed_elicit go")
	Bag_Of_Holding_timed_elicit(bag, attachee, 1)
	return toee.RUN_DEFAULT

def Bag_Of_Holding_timed_elicit(bag, chest, time):
	assert isinstance(bag, toee.PyObjHandle)
	assert isinstance(chest, toee.PyObjHandle)
	toee.game.timevent_add(_Bag_Of_Holding_elicit_on_timeevent, (bag, chest), time, 1) # 1000 = 1 second
	return

def _Bag_Of_Holding_elicit_on_timeevent(bag, chest):
	assert isinstance(bag, toee.PyObjHandle)
	assert isinstance(chest, toee.PyObjHandle)
	print("_Bag_Of_Holding_elicit_on_timeevent")
	if (not bag or bag.object_flags_get() & toee.OF_DESTROYED or not chest or chest.object_flags_get() & toee.OF_DESTROYED): 
		#print("_Bag_Of_Holding_elicit_on_timeevent::san_transfer bag is none, exit")
		return 1

	CtrlBagOfHolding.eject_incompatible(chest)
	max_weight = 0
	bagproto = bag.proto
	if (bagproto == const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_1):
		max_weight = 250
	elif (bagproto == const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_2):
		max_weight = 500
	elif (bagproto == const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_3):
		max_weight = 1000
	elif (bagproto == const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_4):
		max_weight = 1500
	if (max_weight):
		CtrlBagOfHolding.eject_overweight(chest, max_weight)
	else:
		weight = CtrlBagOfHolding.get_total_weight(chest)
		bag.obj_set_int(toee.obj_f_item_weight, weight)

	ctrl = CtrlBagOfHolding.ensure(bag)
	assert isinstance(ctrl, CtrlBagOfHolding)
	ctrl.extract_from_chest(chest)
	print("BAG OF HOLDING SAVED!")
	#print(ctrl.items)
	return 1

def is_bag_proto(proto):
	return (proto in (const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_1, const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_2, const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_3, const_proto_wondrous.PROTO_WONDROUS_BAG_OF_HOLDING_TYPE_4, const_proto_items.PROTO_GENERIC_BACKPACK))

def find_bag(triggerer, chest):
	assert isinstance(triggerer, toee.PyObjHandle)
	assert isinstance(chest, toee.PyObjHandle)
	print("find_bag({}, {})".format(triggerer, chest))
	if (chest):
		inv_idx = chest.obj_get_int(toee.obj_f_container_pad_i_1)
		print("inv_idx: {}".format(inv_idx))
		item = triggerer.inventory_item(inv_idx)
		assert isinstance(item, toee.PyObjHandle)
		if is_bag_proto(item.proto):
			print("found: {}, {}".format(item, item.description))
			return item
		else:
			print("bag is wrong: {}, bag.type: {}".format(item.id, item.type))

	# workaround
	for i in range(0, 199):
		item = triggerer.inventory_item(i)
		if (not item or item == toee.OBJ_HANDLE_NULL): continue
		if is_bag_proto(item.proto):
			return item
	return None

class CtrlBagOfHolding(object):
	def __init__(self):
		self.items = dict()
		self.id = None
		return

	def created(self, npc):
		self.id = npc.id
		return

	@staticmethod
	def get_name():
		return "CtrlBagOfHolding"

	@classmethod
	def ensure(cls, bag):
		assert isinstance(bag, toee.PyObjHandle)
		print("ensure bag: {}, bag.type: {}".format(bag.id, bag.type))
		data = utils_storage.obj_storage(bag).data
		ctrl = None
		if (cls.get_name() in data):
			ctrl = data[cls.get_name()]
		else:
			ctrl = cls()
			ctrl.created(bag)
			utils_storage.obj_storage(bag).data[cls.get_name()] = ctrl
		return ctrl

	@classmethod
	def get_from_obj(cls, npc):
		data = utils_storage.obj_storage(npc).data
		if (cls.get_name() in data):
			return data[cls.get_name()]
		return None

	@classmethod
	def eject_incompatible(cls, chest):
		assert isinstance(chest, toee.PyObjHandle)
		#print("eject_incompatible on chest: {}".format(chest))
		leader = toee.game.leader 
		for i in range(0, 199):
			obj = chest.inventory_item(i)
			assert isinstance(obj, toee.PyObjHandle)
			if (not obj or obj == toee.OBJ_HANDLE_NULL): continue
			#print("checking incompatible {}".format(obj))
			if (cls.is_obj_incompatible(obj)):
				leader.item_get(obj)
				leader.float_text_line("Incompatible item: {}".format(obj.description), toee.tf_red)
		return

	@classmethod
	def eject_overweight(cls, chest, max_weight):
		assert isinstance(chest, toee.PyObjHandle)
		assert isinstance(max_weight, int)
		if (not max_weight): return
		#print("eject_incompatible on chest: {}".format(chest))
		leader = toee.game.leader 
		curr_weight = 0
		for i in range(0, 199):
			obj = chest.inventory_item(i)
			assert isinstance(obj, toee.PyObjHandle)
			if (not obj or obj == toee.OBJ_HANDLE_NULL): continue
			#print("checking incompatible {}".format(obj))
			weight = obj.obj_get_int(toee.obj_f_item_weight)
			if (curr_weight + weight > max_weight):
				leader.item_get(obj)
				descr = obj.description
				flags = obj.item_flags_get()
				if (flags & OIF_IS_MAGICAL and not flags & OIF_IDENTIFIED):
					descr = 'magic item'
				text = "Overweight! Item: {}, weight: {}.".format(descr, weight)
				leader.float_text_line(text, toee.tf_red)
				text = text + "\n"
				toee.game.create_history_freeform(text)
			else:
				curr_weight += weight
		return

	@classmethod
	def get_total_weight(cls, chest):
		assert isinstance(chest, toee.PyObjHandle)
		#print("get_total_weight on chest: {}".format(chest))
		result = 0
		for i in range(0, 199):
			obj = chest.inventory_item(i)
			assert isinstance(obj, toee.PyObjHandle)
			if (not obj or obj == toee.OBJ_HANDLE_NULL): continue
			weight = obj.obj_get_int(toee.obj_f_item_weight)
			result += weight
		return result

	@classmethod
	def is_obj_incompatible(cls, obj):
		assert isinstance(obj, toee.PyObjHandle)
		if is_bag_proto(obj.proto): return 1
		return 0

	def extract_from_chest(self, chest):
		assert isinstance(chest, toee.PyObjHandle)
		self.items = dict()
		for i in range(0, 199):
			obj = chest.inventory_item(i)
			if (not obj or obj == toee.OBJ_HANDLE_NULL): continue
			item = HoldingItem()
			item.save(obj)
			self.items[item.id] = item
		return
	
	def spawn(self, chest):
		assert isinstance(chest, toee.PyObjHandle)
		items = self.items
		if (not items): return
		for id, item in items.iteritems():
			assert isinstance(item, HoldingItem)
			obj = item.spawn(chest.location)
			if (not obj): continue
			chest.item_get(obj)
		return

class HoldingItem(object):
	def __init__(self):
		self.id = ""
		self.proto = 0
		self.props = dict()
		return

	def save(self, obj):
		assert isinstance(obj, toee.PyObjHandle)
		self.id = obj.id
		self.proto = obj.proto
		print("saved obj: {}, id: {}, proto: {}".format(obj, self.id, self.proto))
		otype = obj.type
		# IsEquipment
		if (otype >= toee.obj_t_weapon and otype <= toee.obj_t_generic or otype <= toee.obj_t_bag):
			self.save_prop(obj, "item_flags", toee.obj_f_item_flags)
			self.save_prop(obj, "item_worth", toee.obj_f_item_worth)
			self.save_prop(obj, "item_spell_charges_idx", toee.obj_f_item_spell_charges_idx)
		if (otype == toee.obj_t_ammo):
			self.save_prop(obj, "ammo_quantity", toee.obj_f_ammo_quantity)
		return

	def load_prop(self, obj, prop_name, prop_code):
		assert isinstance(obj, toee.PyObjHandle)
		val = self.props.get(prop_name)
		if (not val is None and val is int):
			obj.obj_set_int(prop_code, val)
		return

	def save_prop(self, obj, prop_name, prop_code):
		assert isinstance(obj, toee.PyObjHandle)
		val = obj.obj_get_int(prop_code)
		if (val):
			self.props[prop_name] = val
		return

	def spawn(self, loc):
		obj = toee.game.obj_create(self.proto, loc)
		if (not obj): return None
		self.id = obj.id
		otype = obj.type
		# IsEquipment
		if (otype >= toee.obj_t_weapon and otype <= toee.obj_t_generic or otype <= toee.obj_t_bag):
			self.load_prop(obj, "item_flags", toee.obj_f_item_flags)
			self.load_prop(obj, "item_worth", toee.obj_f_item_worth)
			self.load_prop(obj, "item_spell_charges_idx", toee.obj_f_item_spell_charges_idx)
			
		if (otype == toee.obj_t_ammo):
			self.load_prop(obj, "ammo_quantity", toee.obj_f_ammo_quantity)
		return obj