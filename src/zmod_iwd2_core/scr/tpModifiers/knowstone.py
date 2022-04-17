import toee, templeplus.pymod, sys, tpdp, math, traceback, debug
import item_knowstone

###################################################

def GetConditionName():
	return "Knowstone"

print("Registering " + GetConditionName())
###################################################

D20_ACTION_CODE_KNOWSTONE_LEARN = 3022

def OnBuildRadialMenuEntry(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	#print("Knowstone OnBuildRadialMenuEntry item: {}".format(item))

	item, inv_idx = get_item_and_inv_idx(attachee, args)
	if not item:
		print ("Inventory Knowstone at {} not found!".format(inv_idx))
		return 0

	radial_parent = tpdp.RadialMenuEntryParent("Knowstone")
	radial_parent_id = radial_parent.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)

	radial_action = tpdp.RadialMenuEntryPythonAction(item.description, toee.D20A_PYTHON_ACTION, D20_ACTION_CODE_KNOWSTONE_LEARN, inv_idx, "TAG_INTERFACE_HELP")
	radial_action.add_as_child(attachee, radial_parent_id)
	return 0

def OnD20PythonActionPerformLearn(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("OnD20PythonActionPerformLearn start")
	try:
		item, inv_idx = get_item_and_inv_idx(attachee, args)
		if (item):
			item_knowstone.knowstone_learn(attachee, item, inv_idx)
	except Exception, e:
		print "OnD20PythonActionPerformLearn ERROR"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3, 0) # none, none, item_inv
modObj.AddHook(toee.ET_OnBuildRadialMenuEntry, toee.EK_NONE, OnBuildRadialMenuEntry, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, D20_ACTION_CODE_KNOWSTONE_LEARN, OnD20PythonActionPerformLearn, ())

def get_item_and_inv_idx(attachee, args):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	inv_idx = args.get_arg(2)
	item = attachee.inventory_item(inv_idx)
	if (not item):
		print("not item for attachee: {}, inv_idx: {}".format(attachee, inv_idx))
		debug.breakp("not item")
	return item, inv_idx
