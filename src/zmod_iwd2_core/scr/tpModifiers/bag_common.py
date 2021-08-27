import toee, templeplus.pymod, tpdp, debug, sys, traceback, bag_of_holding

###################################################

def GetConditionName():
	return "Bag_Common"

print("Registering " + GetConditionName())
###################################################


modObj = templeplus.pymod.PythonModifier(GetConditionName(), 3) # 0 - reserved, 1 - reserved, 2 - invIdx
modObj.AddHook(toee.ET_OnBuildRadialMenuEntry, toee.EK_NONE, bag_of_holding.Bag_Of_Holding_OnBuildRadialMenuEntry, (1,))
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3006, bag_of_holding.Bag_Of_Holding_OnD20PythonActionPerform_inventory, (1,))
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3007, bag_of_holding.Bag_Of_Holding_OnD20PythonActionPerform_examine_bodies, (1,))
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3008, bag_of_holding.Bag_Of_Holding_OnD20PythonActionPerform_transfer_from_bodies, (1,))
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3009, bag_of_holding.Bag_Of_Holding_OnD20PythonActionPerform_list_bag, (1,))
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3013, bag_of_holding.Bag_Of_Holding_OnD20PythonActionPerform_autosell, (1,))
