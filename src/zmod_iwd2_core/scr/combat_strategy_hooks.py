import toee, tpai, debug, traceback, sys
import d20_ai.combat_strategy
import ctrl_behaviour

def hook_module():
    d20_ai.combat_strategy.execute_strategy = execute_strategy
    return

def execute_strategy(obj, tgt):
	result = None
	try:
		#print("combat_strategy_hooks.execute_strategy start {}, {}".format(obj, tgt))

		ctrl = ctrl_behaviour.CtrlBehaviour.get_from_obj(obj)
		if (ctrl):
			result = ctrl.on_execute_strategy(obj, tgt)

		#print("combat_strategy_hooks.execute_strategy result: {}, {}, {}".format(result, obj, tgt))
	except Exception, e:
		print "execute_strategy error:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debug.breakp("execute_strategy error")
	return result
