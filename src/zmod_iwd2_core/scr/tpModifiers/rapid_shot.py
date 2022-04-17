from templeplus.pymod import PythonModifier
from toee import *
import tpdp, debug

print "Registering Rapid Shot extender"

def RapidShotEnabled(attachee, args, evt_obj):
	evt_obj.return_val = args.get_arg(0)
	return 0
	
def RapidShotCheck(attachee, args, evt_obj):
	args.set_arg(0, 1)
	return 0
	
def RapidShotUncheck(attachee, args, evt_obj):
	args.set_arg(0, 0)
	return 0

rapidShotExtender = PythonModifier()
rapidShotExtender.ExtendExisting("Rapid_Shot")
rapidShotExtender.MapToFeat(feat_rapid_shot)
rapidShotExtender.AddHook(ET_OnD20PythonQuery, "Rapid Shot Enabled", RapidShotEnabled, ())
rapidShotExtender.AddHook(ET_OnD20PythonSignal, "Rapid Shot Check", RapidShotCheck, ())
rapidShotExtender.AddHook(ET_OnD20PythonSignal, "Rapid Shot Uncheck", RapidShotUncheck, ())