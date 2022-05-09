import toee
import debug
import inspect, itertools
import utils_storage
import utils_inf
import utils_pc
import utils_npc
import utils_item
import const_toee
import ctrl_behaviour

__metaclass__ = type

def get_globals():
	data = utils_storage.obj_storage_by_id("globals").data
	#result = data.get("globals")
	#if result is None:
	#	result = dict()
	#	data["globals"] = result
	return data #result

# from inf_scripting import *
# gv("Hedron_Quest")
def gv(name): return get_globals().get(name, 0)
# gvs("Hedron_Quest", 1)
def gvs(name, value): get_globals()[name] = value

def dump_args(func):
	"This decorator dumps out the arguments passed to a function before calling it"
	argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
	fname = func.func_name

	def echo_func(*args,**kwargs):
		r = "error!"
		try:
			r = func(*args, **kwargs)
		finally:
			line = '{}({})={}'.format(fname, ', '.join('%s=%r' % entry for entry in zip(argnames,args) + kwargs.items()), r)
			print(line)
		return r
	return echo_func

def strip_quotes(s, notify = False):
	if s and (s[0] == "'" or s[0] == '"'):
		r = s.strip()
		r = r[1:-1]
		if notify:
			return r, s[0]
		else:
			return r
	else:
		if notify:
			return s, None
		else:
			return s
	return

class InfScriptSupport:
	def _gnpc(self):
		return toee.OBJ_HANDLE_NULL

	def _gtriggerer(self):
		return toee.OBJ_HANDLE_NULL

	def _get_globals(self, area):
		area = strip_quotes(area)
		if area.lower() == "global":
			return get_globals()

		raise Exception("globals of {} nof supported!!".format(area))
		return dict()

	def _ensure_global(self, name, area):
		name = strip_quotes(name)
		g = self._get_globals(area)
		v = g.get(name)
		assert isinstance(v, int)
		if v is None:
			g[name] = 0
			v = 0
		return v

	def _set_global(self, name, area, value):
		name = strip_quotes(name)
		g = self._get_globals(area)
		g[name] = value
		return

	def _get_ie_object(self, name):
		# returns (npc, ctrl) if known
		# see object.ids
		if isinstance(name, toee.PyObjHandle):
			return (name, ctrl_behaviour.get_ctrl(name.id))

		name, q = strip_quotes(name, True)
		_name = name.lower()
		npc = None
		ctrl = None
		while True:
			if _name == "myself":
				npc, ctrl = self._get_ie_object_myself(name)
				break

			if _name == "protagonist": 
				npc, ctrl = self._get_ie_object_protagonist(name)
				break

			if _name == "nearest": 
				npc, ctrl = self._get_ie_object_nearest()
				break

			if _name == "nearestpc": 
				npc, ctrl = self._get_ie_object_nearest_pc()
				break

			if True: #q:
				npc, ctrl = self._get_ie_object_by_name(name)
				break

			err = "Unknown objname: {}".format(name)
			print(err)
			debug.breakp("_get_ie_object")
			break
		return (npc, ctrl)

	def _get_ie_object_myself(self, name):
		npc = self._gnpc()
		ctrl = self
		return (npc, ctrl)

	def _get_ie_object_protagonist(self, name):
		npc = toee.OBJ_HANDLE_NULL
		ctrl = None
		while True:
			npc = self._gnpc()
			ctrl = self
			if npc and npc.type == toee.obj_t_pc:
				break

			# opposite dude
			npc = self._gtriggerer()
			ctrl = None
			if npc and npc.type == toee.obj_t_pc:
				break

			# Protagonist : Synonymous with Player1. https://gibberlings3.github.io/iesdp/files/ids/bgee/object.htm#Player1
			npc = toee.game.leader # toee.game.party[0]
			ctrl = None
			break
		return (npc, ctrl)

	def _get_ie_object_by_name(self, name):
		npc = toee.OBJ_HANDLE_NULL
		ctrl = None
		storage = utils_storage.obj_storage_by_alias(name)
		if storage:
			ctrl = ctrl_behaviour.get_ctrl_from_storage(storage)
			if ctrl:
				npc = toee.game.get_obj_by_id(ctrl.id)
		return (npc, ctrl)

	def _get_ie_object_nearest_pc(self):
		raise Exception("Not implemented here function: _get_ie_object_nearest_pc!")
		return (None, None)

	def _get_ie_object_myself(self, name):
		npc = self._gnpc()
		ctrl = self
		return (npc, ctrl)

	def _hp(self, obj_name):
		obj, ctrl = self._get_ie_object(obj_name)
		result = 0
		if obj:
			result = obj.stat_level_get(toee.stat_hp_current)
		return result

	def _skill(self, obj_name, skill_name):
		obj, ctrl = self._get_ie_object(obj_name)
		result = 0
		if obj:
			stat = utils_inf.iwd2_skill_convert(skill_name)
			if not stat is None:
				result = obj.stat_level_get(stat)
		return result

	def _get_proto(self, item_name):
		if isinstance(item_name, int):
			return int(item_name)
		err = "Unknown item: {}".format(item_name)
		print(err)
		debug.breakp("_get_proto")
		return None

	def _check_race():
		return

	########## TRIGGERS ##########
	@dump_args
	def ActionListEmpty(self):
		"""
		ActionListEmpty()
		"""
		raise Exception("Not implemented function: ActionListEmpty!")
		return
	
	@dump_args
	def Alignment(self, obj, alignment):
		"""
		Alignment(O:Object*, I:Alignment*ALIGNMNT)
		"""
		raise Exception("Not implemented function: Alignment!")
		return
	
	@dump_args
	def Allegiance(self, obj, allegience):
		"""
		Allegiance(O:Object*, I:Allegience*EA)
		"""
		raise Exception("Not implemented function: Allegiance!")
		return
	
	@dump_args
	def AnyPCOnMap(self):
		"""
		AnyPCOnMap()
		"""
		raise Exception("Not implemented function: AnyPCOnMap!")
		return
	
	@dump_args
	def AnyPCSeesEnemy(self):
		"""
		AnyPCSeesEnemy()
		"""
		raise Exception("Not implemented function: AnyPCSeesEnemy!")
		return
	
	@dump_args
	def AreaRestDisabled(self):
		"""
		AreaRestDisabled()
		"""
		raise Exception("Not implemented function: AreaRestDisabled!")
		return
	
	@dump_args
	def AttackedBy(self, obj, style):
		"""
		AttackedBy(O:Object*, I:Style*ATTSTYLE)
		"""
		raise Exception("Not implemented function: AttackedBy!")
		return
	
	@dump_args
	def ChargeCount(self, item, obj, ability, number, operation):
		"""
		ChargeCount(S:Item*, O:Object*, I:Ability*, I:Number*, I:Operation*diffmode)
		"""
		raise Exception("Not implemented function: ChargeCount!")
		return
	
	@dump_args
	def CheckAreaDiffLevel(self, level):
		"""
		CheckAreaDiffLevel(I:Level*)
		"""
		raise Exception("Not implemented function: CheckAreaDiffLevel!")
		return
	
	@dump_args
	def CheckDoorFlags(self, obj, flags):
		"""
		CheckDoorFlags(O:Object*, I:Flags*DoorFlag)
		"""
		raise Exception("Not implemented function: CheckDoorFlags!")
		return
	
	@dump_args
	def CheckSkillGT(self, obj, value, skillnum):
		"""
		CheckSkillGT(O:Object*, I:Value*, I:SkillNum*Skills)
		"""
		raise Exception("Not implemented function: CheckSkillGT!")
		return
	
	@dump_args
	def CheckSpellState(self, obj, state):
		"""
		CheckSpellState(O:Object*, I:State*splstate)
		"""
		raise Exception("Not implemented function: CheckSpellState!")
		return
	
	@dump_args
	def iCheckStat(self, obj, value, statnum):
		"""
		CheckStat(O:Object*, I:Value*, I:StatNum*Stats)
		"""
		raise Exception("Not implemented here function: CheckStat!")
		return
	
	@dump_args
	def iCheckStatGT(self, obj, value, statnum):
		"""
		CheckStatGT(O:Object*, I:Value*, I:StatNum*Stats)
		"""
		raise Exception("Not implemented here function: CheckStatGT!")
		return
	
	@dump_args
	def iCheckStatLT(self, obj, value, statnum):
		"""
		CheckStatLT(O:Object*, I:Value*, I:StatNum*Stats)
		"""
		raise Exception("Not implemented here function: CheckStatLT!")
		return
	
	@dump_args
	def iClass(self, obj, class_):
		"""
		Class(O:Object*, I:Class*Class)
		Returns true only if the Class of the specified object matches that in the second parameter.
		"""
		toee_class = utils_inf.iwd2_classname_to_class(class_)
		npc, ctrl = self._get_ie_object(obj)
		if npc:
			cc = npc.get_character_classes()
			if toee_class in cc:
				return True
		return False
	
	@dump_args
	def iClassEx(self, obj, class_):
		"""
		ClassEx(O:Object*, I:Class*Class)
		"""
		"""
		Actually I see only these values in IWD2:
		FIGHTER
		BARD
		MAGE
		SORCERER
		CLERIC
		DRUID
		"""
		toee_class = utils_inf.iwd2_classname_to_class(class_)
		npc, ctrl = self._get_ie_object(obj)
		if npc:
			cc = npc.get_character_classes()
			if toee_class in cc:
				return True
		return False
	
	@dump_args
	def CreatureHidden(self, obj):
		"""
		CreatureHidden(O:Object*)
		"""
		raise Exception("Not implemented function: CreatureHidden!")
		return
	
	@dump_args
	def CurrentAreaIs(self, obj, areanum):
		"""
		CurrentAreaIs(O:Object*, I:AreaNum*)
		"""
		raise Exception("Not implemented function: CurrentAreaIs!")
		return
	
	@dump_args
	def Dead(self, obj):
		"""
		Dead(O:Object*)
		"""
		raise Exception("Not implemented function: Dead!")
		return
	
	@dump_args
	def Died(self, obj):
		"""
		Died(O:Object*)
		"""
		raise Exception("Not implemented function: Died!")
		return
	
	@dump_args
	def Difficulty(self, level, mode):
		"""
		Difficulty(I:Level*DiffLevl, I:Mode*diffmode)
		"""
		raise Exception("Not implemented function: Difficulty!")
		return
	
	@dump_args
	def iEntirePartyOnMap(self):
		"""
		EntirePartyOnMap()
		"""
		return True
	
	@dump_args
	def Exists(self, obj):
		"""
		Exists(O:Object*)
		"""
		raise Exception("Not implemented function: Exists!")
		return
	
	@dump_args
	def iGlobal(self, name, area, value):
		"""
		Global(S:Name*, S:Area*, I:Value*)
		Returns true only if the variable with name 1st parameter of type 2nd parameter has value 3rd parameter.
		"""
		global_value = self._ensure_global(name, area)
		return global_value == value
	
	@dump_args
	def iGlobalGT(self, name, area, value):
		"""
		GlobalGT(S:Name*, S:Area*, I:Value*)
		As above except for less than.
		"""
		global_value = self._ensure_global(name, area)
		return global_value > value

	@dump_args
	def iGlobalLT(self, name, area, value):
		""" 
		GlobalLT(S:Name*, S:Area*, I:Value*)
		As above except for less than.
		"""
		global_value = self._ensure_global(name, area)
		return global_value < value
	
	@dump_args
	def Gender(self, obj, sex):
		"""
		Gender(O:Object*, I:Sex*Gender)
		"""
		raise Exception("Not implemented function: Gender!")
		return
	
	@dump_args
	def General(self, obj, general):
		"""
		General(O:Object*, I:General*General)
		"""
		raise Exception("Not implemented function: General!")
		return
	
	@dump_args
	def GlobalTimerExpired(self, name, area):
		"""
		GlobalTimerExpired(S:Name*, S:Area*)
		"""
		raise Exception("Not implemented function: GlobalTimerExpired!")
		return
	
	@dump_args
	def GlobalTimerNotExpired(self, name, area):
		"""
		GlobalTimerNotExpired(S:Name*, S:Area*)
		"""
		raise Exception("Not implemented function: GlobalTimerNotExpired!")
		return
	
	@dump_args
	def iHP(self, obj, hit_points):
		"""
		HP(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented here function: HP!")
		return
	
	@dump_args
	def iHPGT(self, obj, hit_points):
		"""
		HPGT(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented here function: HPGT!")
		return
	
	@dump_args
	def iHPLT(self, obj, hit_points):
		"""
		HPLT(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented here function: HPLT!")
		return
	
	@dump_args
	def HPLost(self, obj, hit_points):
		"""
		HPLost(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented function: HPLost!")
		return
	
	@dump_args
	def HPLostGT(self, obj, hit_points):
		"""
		HPLostGT(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented function: HPLostGT!")
		return
	
	@dump_args
	def HPPercent(self, obj, hit_points):
		"""
		HPPercent(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented function: HPPercent!")
		return
	
	@dump_args
	def HPPercentGT(self, obj, hit_points):
		"""
		HPPercentGT(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented function: HPPercentGT!")
		return
	
	@dump_args
	def HPPercentLT(self, obj, hit_points):
		"""
		HPPercentLT(O:Object*, I:Hit Points*)
		"""
		raise Exception("Not implemented function: HPPercentLT!")
		return
	
	@dump_args
	def HasItem(self, resref, obj):
		"""
		HasItem(S:ResRef*, O:Object*)
		"""
		raise Exception("Not implemented function: HasItem!")
		return
	
	@dump_args
	def HasItemInSlot(self, item, obj, slot):
		"""
		HasItemInSlot(S:Item*, O:Object*, I:Slot*SLOTS)
		"""
		raise Exception("Not implemented function: HasItemInSlot!")
		return
	
	@dump_args
	def HaveSpell(self, spell):
		"""
		HaveSpell(I:Spell*Spell)
		"""
		raise Exception("Not implemented function: HaveSpell!")
		return
	
	@dump_args
	def Heard(self, obj, id):
		"""
		Heard(O:Object*, I:ID*)
		"""
		raise Exception("Not implemented function: Heard!")
		return
	
	@dump_args
	def HitBy(self, obj, dametype):
		"""
		HitBy(O:Object*, I:DameType*Damages)
		"""
		raise Exception("Not implemented function: HitBy!")
		return
	
	@dump_args
	def iInCutsceneMode(self):
		"""
		InCutsceneMode()
		"""
		#raise Exception("Not implemented function: InCutsceneMode!")
		# TODO!
		return False
	
	@dump_args
	def InParty(self, obj):
		"""
		InParty(O:Object*)
		"""
		raise Exception("Not implemented function: InParty!")
		return
	
	@dump_args
	def Internal(self, obj, index, value):
		"""
		Internal(O:Object*, I:Index*, I:Value*)
		"""
		raise Exception("Not implemented function: Internal!")
		return
	
	@dump_args
	def InternalGT(self, obj, index, value):
		"""
		InternalGT(O:Object*, I:Index*, I:Value*)
		"""
		raise Exception("Not implemented function: InternalGT!")
		return
	
	@dump_args
	def IsActive(self, obj):
		"""
		IsActive(O:Object*)
		"""
		raise Exception("Not implemented function: IsActive!")
		return
	
	@dump_args
	def IsAnimationID(self, obj, animid):
		"""
		IsAnimationID(O:Object*, I:AnimID*Animate)
		"""
		raise Exception("Not implemented function: IsAnimationID!")
		return
	
	@dump_args
	def IsCreatureAreaFlag(self, obj, flag):
		"""
		IsCreatureAreaFlag(O:Object*, I:Flag*CREAREFL)
		"""
		raise Exception("Not implemented function: IsCreatureAreaFlag!")
		return
	
	@dump_args
	def IsCreatureHiddenInShadows(self, obj):
		"""
		IsCreatureHiddenInShadows(O:Object*)
		"""
		raise Exception("Not implemented function: IsCreatureHiddenInShadows!")
		return
	
	@dump_args
	def IsExtendedNight(self):
		"""
		IsExtendedNight()
		"""
		raise Exception("Not implemented function: IsExtendedNight!")
		return
	
	@dump_args
	def IsFacingSavedRotation(self, obj):
		"""
		IsFacingSavedRotation(O:Object*)
		"""
		raise Exception("Not implemented function: IsFacingSavedRotation!")
		return
	
	@dump_args
	def IsHeartOfFuryModeOn(self):
		"""
		IsHeartOfFuryModeOn()
		"""
		raise Exception("Not implemented function: IsHeartOfFuryModeOn!")
		return
	
	@dump_args
	def IsMarkedSpell(self, spell):
		"""
		IsMarkedSpell(I:Spell*Spell)
		"""
		raise Exception("Not implemented function: IsMarkedSpell!")
		return
	
	@dump_args
	def IsPathCriticalObject(self, obj):
		"""
		IsPathCriticalObject(O:Object*)
		"""
		raise Exception("Not implemented function: IsPathCriticalObject!")
		return
	
	@dump_args
	def IsRotation(self, obj, direction):
		"""
		IsRotation(O:Object*, I:Direction*DIR)
		"""
		raise Exception("Not implemented function: IsRotation!")
		return
	
	@dump_args
	def IsScriptName(self, scriptname, obj):
		"""
		IsScriptName(S:ScriptName*, O:Object*)
		"""
		raise Exception("Not implemented function: IsScriptName!")
		return
	
	@dump_args
	def IsSpellTargetValid(self, obj, spell, flags):
		"""
		IsSpellTargetValid(O:Object*, I:Spell*Spell, I:Flags*SplCast)
		"""
		raise Exception("Not implemented function: IsSpellTargetValid!")
		return
	
	@dump_args
	def IsTeamBitOn(self, teamflag):
		"""
		IsTeamBitOn(I:TeamFlag*TeamBit)
		"""
		raise Exception("Not implemented function: IsTeamBitOn!")
		return
	
	@dump_args
	def IsWeaponRanged(self, obj):
		"""
		IsWeaponRanged(O:Object*)
		"""
		raise Exception("Not implemented function: IsWeaponRanged!")
		return
	
	@dump_args
	def ItemIsIdentified(self, resref, obj):
		"""
		ItemIsIdentified(S:ResRef*, O:Object*)
		"""
		raise Exception("Not implemented function: ItemIsIdentified!")
		return
	
	@dump_args
	def Kit(self, obj, kit):
		"""
		Kit(O:Object*, I:Kit*Kit)
		"""
		raise Exception("Not implemented function: Kit!")
		return
	
	@dump_args
	def LOS(self, obj, range):
		"""
		LOS(O:Object*, I:Range*)
		"""
		raise Exception("Not implemented function: LOS!")
		return
	
	@dump_args
	def Level(self, obj, level):
		"""
		Level(O:Object*, I:Level*)
		"""
		raise Exception("Not implemented function: Level!")
		return
	
	@dump_args
	def LevelGT(self, obj, level):
		"""
		LevelGT(O:Object*, I:Level*)
		"""
		raise Exception("Not implemented function: LevelGT!")
		return
	
	@dump_args
	def LevelInClass(self, obj, level, class_):
		"""
		LevelInClass(O:Object*, I:Level, I:Class*Class)
		"""
		raise Exception("Not implemented function: LevelInClass!")
		return
	
	@dump_args
	def LevelInClassGT(self, obj, level, class_):
		"""
		LevelInClassGT(O:Object*, I:Level, I:Class*Class)
		"""
		raise Exception("Not implemented function: LevelInClassGT!")
		return
	
	@dump_args
	def NearLocation(self, obj, pointx, pointy, range):
		"""
		NearLocation(O:Object*, I:PointX*, I:PointY*, I:Range*)
		"""
		raise Exception("Not implemented function: NearLocation!")
		return
	
	@dump_args
	def NearSavedLocation(self, range):
		"""
		NearSavedLocation(I:Range*)
		"""
		raise Exception("Not implemented function: NearSavedLocation!")
		return
	
	@dump_args
	def NumInParty(self, num):
		"""
		NumInParty(I:Num*)
		"""
		raise Exception("Not implemented function: NumInParty!")
		return
	
	@dump_args
	def NumInPartyGT(self, num):
		"""
		NumInPartyGT(I:Num*)
		"""
		raise Exception("Not implemented function: NumInPartyGT!")
		return
	
	@dump_args
	def NumInPartyLT(self, num):
		"""
		NumInPartyLT(I:Num*)
		"""
		raise Exception("Not implemented function: NumInPartyLT!")
		return
	
	@dump_args
	def iNumTimesTalkedTo(self, num):
		"""
		NumTimesTalkedTo(I:Num*)
		"""
		raise Exception("Not implemented here function: NumTimesTalkedTo!")
		return
	
	@dump_args
	def iNumTimesTalkedToGT(self, num):
		"""
		NumTimesTalkedToGT(I:Num*)
		"""
		raise Exception("Not implemented here function: NumTimesTalkedToGT!")
		return
	
	@dump_args
	def iNumTimesTalkedToLT(self, num):
		"""
		NumTimesTalkedToLT(I:Num*)
		"""
		raise Exception("Not implemented here function: NumTimesTalkedToLT!")
		return
	
	@dump_args
	def iOnCreation(self):
		"""
		OnCreation()
		"""
		raise Exception("Not implemented here function: OnCreation!")
		return
	
	@dump_args
	def OpenState(self, obj, open):
		"""
		OpenState(O:Object*, I:Open*BOOLEAN)
		"""
		raise Exception("Not implemented function: OpenState!")
		return
	
	@dump_args
	def OutOfAmmo(self):
		"""
		OutOfAmmo()
		"""
		raise Exception("Not implemented function: OutOfAmmo!")
		return
	
	@dump_args
	def PartyHasItem(self, item):
		"""
		PartyHasItem(S:Item*)
		"""
		raise Exception("Not implemented function: PartyHasItem!")
		return
	
	@dump_args
	def PickLockFailed(self, obj):
		"""
		PickLockFailed(O:Object*)
		"""
		raise Exception("Not implemented function: PickLockFailed!")
		return
	
	@dump_args
	def PickPocketFailed(self, obj):
		"""
		PickPocketFailed(O:Object*)
		"""
		raise Exception("Not implemented function: PickPocketFailed!")
		return
	
	@dump_args
	def Race(self, obj, race):
		"""
		Race(O:Object*, I:Race*Race)
		Returns true only if the Race of the specified object is the same as that specified by the 2nd parameter.
		"""
		npc, ctrl = self._get_ie_object(obj)
		return self._check_race(npc, race)
	
	@dump_args
	def RandomNum(self, range, value):
		"""
		RandomNum(I:Range*, I:Value*)
		"""
		raise Exception("Not implemented function: RandomNum!")
		return
	
	@dump_args
	def RandomNumLT(self, range, value):
		"""
		RandomNumLT(I:Range*, I:Value*)
		"""
		raise Exception("Not implemented function: RandomNumLT!")
		return
	
	@dump_args
	def Range(self, obj, range, diffmode):
		"""
		Range(O:Object*, I:Range*, I:diffmode*diffmode)
		"""
		raise Exception("Not implemented function: Range!")
		return
	
	@dump_args
	def See(self, obj, seedead):
		"""
		See(O:Object*, I:SeeDead*)
		"""
		raise Exception("Not implemented function: See!")
		return
	
	@dump_args
	def Sequence(self, obj, sequence):
		"""
		Sequence(O:Object*, I:Sequence*Sequence)
		"""
		raise Exception("Not implemented function: Sequence!")
		return
	
	@dump_args
	def SetLastMarkedObject(self, obj):
		"""
		SetLastMarkedObject(O:Object*)
		"""
		raise Exception("Not implemented function: SetLastMarkedObject!")
		return
	
	@dump_args
	def SetSpellTarget(self, obj):
		"""
		SetSpellTarget(O:Object*)
		"""
		raise Exception("Not implemented function: SetSpellTarget!")
		return
	
	@dump_args
	def Specifics(self, obj, specifics):
		"""
		Specifics(O:Object*, I:Specifics*Specific)
		"""
		raise Exception("Not implemented function: Specifics!")
		return
	
	@dump_args
	def StateCheck(self, obj, state):
		"""
		StateCheck(O:Object*, I:State*State)
		"""
		raise Exception("Not implemented function: StateCheck!")
		return
	
	@dump_args
	def SubRace(self, obj, subrace):
		"""
		SubRace(O:Object*, I:SubRace*SubRace)
		"""
		raise Exception("Not implemented function: SubRace!")
		return
	
	@dump_args
	def Subrace(self, obj, subrace):
		"""
		Subrace(O:Object*, I:SubRace*SubRace)
		"""
		raise Exception("Not implemented function: Subrace!")
		return
	
	@dump_args
	def TargetUnreachable(self, obj):
		"""
		TargetUnreachable(O:Object*)
		"""
		raise Exception("Not implemented function: TargetUnreachable!")
		return
	
	@dump_args
	def TimeGT(self, time):
		"""
		TimeGT(I:Time*Time)
		"""
		raise Exception("Not implemented function: TimeGT!")
		return
	
	@dump_args
	def TimeLT(self, time):
		"""
		TimeLT(I:Time*Time)
		"""
		raise Exception("Not implemented function: TimeLT!")
		return
	
	@dump_args
	def TimeOfDay(self, time_of_day):
		"""
		TimeOfDay(I:Time Of Day*TimeODay)
		"""
		raise Exception("Not implemented function: TimeOfDay!")
		return
	
	@dump_args
	def TimerActive(self, timerid):
		"""
		TimerActive(I:TimerID*)
		"""
		raise Exception("Not implemented function: TimerActive!")
		return
	
	@dump_args
	def TimerExpired(self, id):
		"""
		TimerExpired(I:ID*)
		"""
		raise Exception("Not implemented function: TimerExpired!")
		return
	
	########## ACTIONS ##########
	@dump_args
	def ActionOverride(self, actor, action):
		"""
		ActionOverride(O:Actor*, A:Action*)
		"""
		raise Exception("Not implemented function: ActionOverride!")
		return
	
	@dump_args
	def Activate(self, obj):
		"""
		Activate(O:Object*)
		"""
		raise Exception("Not implemented function: Activate!")
		return
	
	@dump_args
	def AddExperiencePartyCR(self, cr):
		"""
		AddExperiencePartyCR(I:CR*)
		"""
		raise Exception("Not implemented function: AddExperiencePartyCR!")
		return
	
	@dump_args
	def AddFeat(self, obj, value):
		"""
		AddFeat(O:Object*, I:Value*Feats)
		"""
		raise Exception("Not implemented function: AddFeat!")
		return
	
	@dump_args
	def AddJournalEntry(self, entry):
		"""
		AddJournalEntry(I:Entry*)
		"""
		raise Exception("Not implemented function: AddJournalEntry!")
		return
	
	@dump_args
	def iAddXPVar(self, vartableentry, strref):
		"""
		AddXPVar(S:VarTableEntry*, I:Strref*)
		"""
		vartableentry = strip_quotes(vartableentry)
		xp = utils_inf.iwd2_xp_var(vartableentry)
		utils_pc.pc_award_experience_party(xp, 1)
		if strref:
			line = toee.game.get_mesline('mes\\floats.mes', strref)
			if line:
				toee.game.create_history_freeform(line)
				toee.game.leader.float_mesfile_line('mes\\floats.mes', strref, toee.tf_green)
		# core->PlaySound(DS_GOTXP, SFX_CHAN_ACTIONS);
		return
	
	#@dump_args
	def iAddXpVar(self, vartableentry, strref):
		"""
		AddXpVar(S:VarTableEntry*, I:Strref*)
		"""
		self.iAddXPVar(vartableentry, strref)
		return
	
	@dump_args
	def AllowAreaResting(self, trueorfalse):
		"""
		AllowAreaResting(I:TrueOrFalse*BOOLEAN)
		"""
		raise Exception("Not implemented function: AllowAreaResting!")
		return
	
	@dump_args
	def ApplySpell(self, target, spell):
		"""
		ApplySpell(O:Target, I:Spell*Spell)
		"""
		raise Exception("Not implemented function: ApplySpell!")
		return
	
	@dump_args
	def Attack(self, target):
		"""
		Attack(O:Target*)
		"""
		raise Exception("Not implemented function: Attack!")
		return
	
	@dump_args
	def AttackOneRound(self, target):
		"""
		AttackOneRound(O:Target*)
		"""
		raise Exception("Not implemented function: AttackOneRound!")
		return
	
	@dump_args
	def AttackReevaluate(self, target, reevaluationperiod):
		"""
		AttackReevaluate(O:Target*, I:ReevaluationPeriod*)
		"""
		raise Exception("Not implemented function: AttackReevaluate!")
		return
	
	@dump_args
	def BackStab(self, target):
		"""
		BackStab(O:Target*)
		"""
		raise Exception("Not implemented function: BackStab!")
		return
	
	@dump_args
	def BitGlobal(self, string1, string2, value, mode):
		"""
		BitGlobal(S:String1*, S:String2*, I:Value, I:Mode*BitMode)
		"""
		raise Exception("Not implemented function: BitGlobal!")
		return
	
	@dump_args
	def ChangeAIScript(self, scriptfile, level):
		"""
		ChangeAIScript(S:ScriptFile*, I:Level*Scrlev)
		"""
		raise Exception("Not implemented function: ChangeAIScript!")
		return
	
	@dump_args
	def ChangeCurrentScript(self, script):
		"""
		ChangeCurrentScript(S:Script*)
		"""
		raise Exception("Not implemented function: ChangeCurrentScript!")
		return
	
	@dump_args
	def ChangeEnemyAlly(self, obj, value):
		"""
		ChangeEnemyAlly(O:Object*, I:Value*EA)
		"""
		raise Exception("Not implemented function: ChangeEnemyAlly!")
		return
	
	@dump_args
	def ChangeSpecifics(self, obj, value):
		"""
		ChangeSpecifics(O:Object*, I:Value*Specific)
		"""
		raise Exception("Not implemented function: ChangeSpecifics!")
		return
	
	@dump_args
	def ChangeStat(self, obj, stat, value, modifier):
		"""
		ChangeStat(O:Object*, I:Stat*Stats, I:Value*, I:Modifier*StatMod)
		"""
		raise Exception("Not implemented function: ChangeStat!")
		return
	
	@dump_args
	def ChunkCreature(self, obj):
		"""
		ChunkCreature(O:Object*)
		"""
		raise Exception("Not implemented function: ChunkCreature!")
		return
	
	@dump_args
	def ClearActions(self, obj):
		"""
		ClearActions(O:Object*)
		"""
		raise Exception("Not implemented function: ClearActions!")
		return
	
	@dump_args
	def ClearAllActions(self):
		"""
		ClearAllActions()
		"""
		raise Exception("Not implemented function: ClearAllActions!")
		return
	
	@dump_args
	def ClearPartyEffects(self):
		"""
		ClearPartyEffects()
		"""
		raise Exception("Not implemented function: ClearPartyEffects!")
		return
	
	@dump_args
	def ClearSpriteEffects(self, obj):
		"""
		ClearSpriteEffects(O:Object*)
		"""
		raise Exception("Not implemented function: ClearSpriteEffects!")
		return
	
	@dump_args
	def CloseDoor(self, obj):
		"""
		CloseDoor(O:Object*)
		"""
		raise Exception("Not implemented function: CloseDoor!")
		return
	
	@dump_args
	def CreateCreature(self, newobject, scriptname, location, face):
		"""
		CreateCreature(S:NewObject*, S:ScriptName*, P:Location*, I:Face*)
		"""
		raise Exception("Not implemented function: CreateCreature!")
		return
	
	@dump_args
	def CreateItem(self, resref, usage1, usage2, usage3):
		"""
		CreateItem(S:ResRef*, I:Usage1*, I:Usage2*, I:Usage3*)
		"""
		raise Exception("Not implemented function: CreateItem!")
		return
	
	@dump_args
	def DayNight(self, timeofday):
		"""
		DayNight(I:TimeOfDay*Time)
		"""
		raise Exception("Not implemented function: DayNight!")
		return
	
	@dump_args
	def Deactivate(self, obj):
		"""
		Deactivate(O:Object*)
		"""
		raise Exception("Not implemented function: Deactivate!")
		return
	
	@dump_args
	def Debug(self, message):
		"""
		Debug(S:Message*)
		"""
		raise Exception("Not implemented function: Debug!")
		return
	
	@dump_args
	def DestroyItem(self, resref):
		"""
		DestroyItem(S:ResRef*)
		"""
		raise Exception("Not implemented here function: DestroyItem!")
		return
	
	@dump_args
	def DestroySelf(self):
		"""
		DestroySelf()
		"""
		raise Exception("Not implemented function: DestroySelf!")
		return
	
	@dump_args
	def DialogInterrupt(self, state):
		"""
		DialogInterrupt(I:State*Boolean)
		"""
		raise Exception("Not implemented function: DialogInterrupt!")
		return
	
	@dump_args
	def Dialogue(self, obj):
		"""
		Dialogue(O:Object*)
		"""
		raise Exception("Not implemented function: Dialogue!")
		return
	
	@dump_args
	def DisplayMessage(self, strref):
		"""
		DisplayMessage(I:StrRef*)
		"""
		raise Exception("Not implemented function: DisplayMessage!")
		return
	
	@dump_args
	def DisplayString(self, obj, strref):
		"""
		DisplayString(O:Object*, I:StrRef*)
		"""
		raise Exception("Not implemented function: DisplayString!")
		return
	
	@dump_args
	def DropInventory(self):
		"""
		DropInventory()
		"""
		raise Exception("Not implemented function: DropInventory!")
		return
	
	@dump_args
	def DropInventoryEX(self, obj):
		"""
		DropInventoryEX(O:Object)
		"""
		raise Exception("Not implemented function: DropInventoryEX!")
		return
	
	@dump_args
	def DropItem(self, obj, location):
		"""
		DropItem(S:Object*, P:Location*)
		"""
		raise Exception("Not implemented function: DropItem!")
		return
	
	@dump_args
	def EndCutSceneMode(self):
		"""
		EndCutSceneMode()
		"""
		raise Exception("Not implemented function: EndCutSceneMode!")
		return
	
	@dump_args
	def EndGame(self, strref):
		"""
		EndGame(I:StrRef*)
		"""
		raise Exception("Not implemented function: EndGame!")
		return
	
	@dump_args
	def Enemy(self):
		"""
		Enemy()
		"""
		raise Exception("Not implemented function: Enemy!")
		return
	
	@dump_args
	def EquipItem(self, obj, equipunequip):
		"""
		EquipItem(S:Object*, I:EquipUnEquip*)
		"""
		raise Exception("Not implemented function: EquipItem!")
		return
	
	@dump_args
	def EquipMostDamagingMelee(self):
		"""
		EquipMostDamagingMelee()
		"""
		raise Exception("Not implemented function: EquipMostDamagingMelee!")
		return
	
	@dump_args
	def EquipRanged(self):
		"""
		EquipRanged()
		"""
		raise Exception("Not implemented function: EquipRanged!")
		return
	
	@dump_args
	def EquipWeapon(self):
		"""
		EquipWeapon()
		"""
		raise Exception("Not implemented function: EquipWeapon!")
		return
	
	@dump_args
	def EscapeArea(self):
		"""
		EscapeArea()
		"""
		raise Exception("Not implemented function: EscapeArea!")
		return
	
	@dump_args
	def EscapeAreaDestroy(self, delay):
		"""
		EscapeAreaDestroy(I:Delay*)
		"""
		raise Exception("Not implemented function: EscapeAreaDestroy!")
		return
	
	@dump_args
	def Explore(self):
		"""
		Explore()
		"""
		raise Exception("Not implemented function: Explore!")
		return
	
	@dump_args
	def Face(self, direction):
		"""
		Face(I:Direction*dir)
		"""
		raise Exception("Not implemented function: Face!")
		return
	
	@dump_args
	def FaceObject(self, obj):
		"""
		FaceObject(O:Object*)
		"""
		raise Exception("Not implemented function: FaceObject!")
		return
	
	@dump_args
	def FaceSavedLocation(self, obj):
		"""
		FaceSavedLocation(O:Object*)
		"""
		raise Exception("Not implemented function: FaceSavedLocation!")
		return
	
	@dump_args
	def iFadeFromColor(self, point, blue):
		"""
		FadeFromColor(P:Point*, I:Blue*)
		"""
		# do nothing
		return
	
	@dump_args
	def iFadeToColor(self, point, blue):
		"""
		FadeToColor(P:Point*, I:Blue*)
		"""
		# do nothing
		return
	
	@dump_args
	def iFloatMessage(self, obj, strref):
		"""
		FloatMessage(O:Object*, I:STRREF*)
		"""
		npc, ctrl = self._get_ie_object(obj)
		if npc:
			line = toee.game.get_mesline('mes\\floats.mes', strref)
			if line:
				toee.game.create_history_freeform(line)
				npc.float_mesfile_line('mes\\floats.mes', strref, toee.tf_white)

		return
	
	@dump_args
	def ForceHide(self, target):
		"""
		ForceHide(O:Target*)
		"""
		raise Exception("Not implemented function: ForceHide!")
		return
	
	@dump_args
	def ForceMarkedSpell(self, spell):
		"""
		ForceMarkedSpell(I:Spell*Spell)
		"""
		raise Exception("Not implemented function: ForceMarkedSpell!")
		return
	
	@dump_args
	def ForceSpell(self, target, spell):
		"""
		ForceSpell(O:Target, I:Spell*Spell)
		"""
		raise Exception("Not implemented function: ForceSpell!")
		return
	
	@dump_args
	def ForceSpellPoint(self, target, spell):
		"""
		ForceSpellPoint(P:Target, I:Spell*Spell)
		"""
		raise Exception("Not implemented function: ForceSpellPoint!")
		return
	
	@dump_args
	def iGiveItem(self, obj, target):
		"""
		GiveItem(S:Object*, O:Target*)
		"""
		raise Exception("Not implemented here function: GiveItem!")
		return
	
	@dump_args
	def iGiveItemCreate(self, resref, obj, usage1, usage2, usage3):
		"""
		GiveItemCreate(S:ResRef*, O:Object*, I:Usage1*, I:Usage2*, I:Usage3*)
		This action creates the item specified by the resref parameter on the creature specified by the object parameter, with quantity/charges controlled by the usage parameters. 
		"""
		npc, ctrl = self._get_ie_object(obj)
		if npc:
			proto = self._get_proto(resref)
			#if isinstance(proto, str):
			#	if proto == "Misc07": # gold
			#		utils_pc.pc_party_receive_money_and_print(usage1 * const_toee.gp)
			if not proto is None:
				item_obj = utils_item.item_create_in_inventory2(proto, npc, 0, None)
			#else:
			#	item = utils_item.item_create_in_inventory2(proto, target, 0, None)

		# TODO
		return
	
	@dump_args
	def Help(self, obj):
		"""
		Help(O:Object*)
		"""
		raise Exception("Not implemented function: Help!")
		return
	
	@dump_args
	def Hide(self):
		"""
		Hide()
		"""
		raise Exception("Not implemented function: Hide!")
		return
	
	@dump_args
	def HideCreature(self, obj, state):
		"""
		HideCreature(O:Object*, I:State*Boolean)
		"""
		raise Exception("Not implemented function: HideCreature!")
		return
	
	@dump_args
	def IncrementChapter(self, resref):
		"""
		IncrementChapter(S:RESREF*)
		"""
		raise Exception("Not implemented function: IncrementChapter!")
		return
	
	@dump_args
	def IncrementGlobal(self, name, area, value):
		"""
		IncrementGlobal(S:Name*, S:Area*, I:Value*)
		"""
		raise Exception("Not implemented function: IncrementGlobal!")
		return
	
	@dump_args
	def IncrementInternal(self, obj, index, value):
		"""
		IncrementInternal(O:Object*, I:Index*, I:Value*)
		"""
		raise Exception("Not implemented function: IncrementInternal!")
		return
	
	@dump_args
	def JumpToObject(self, target):
		"""
		JumpToObject(O:Target*)
		"""
		raise Exception("Not implemented function: JumpToObject!")
		return
	
	@dump_args
	def JumpToPoint(self, target):
		"""
		JumpToPoint(P:Target*)
		"""
		raise Exception("Not implemented function: JumpToPoint!")
		return
	
	@dump_args
	def JumpToSavedLocation(self):
		"""
		JumpToSavedLocation()
		"""
		raise Exception("Not implemented function: JumpToSavedLocation!")
		return
	
	@dump_args
	def Kill(self, obj):
		"""
		Kill(O:Object*)
		"""
		raise Exception("Not implemented function: Kill!")
		return
	
	@dump_args
	def Lock(self, obj):
		"""
		Lock(O:Object*)
		"""
		raise Exception("Not implemented function: Lock!")
		return
	
	@dump_args
	def MakeUnselectable(self, time):
		"""
		MakeUnselectable(I:Time*)
		"""
		raise Exception("Not implemented function: MakeUnselectable!")
		return
	
	@dump_args
	def MarkObject(self, obj):
		"""
		MarkObject(O:Object*)
		"""
		raise Exception("Not implemented function: MarkObject!")
		return
	
	@dump_args
	def MarkSpellAndObject(self, spells, obj, flags):
		"""
		MarkSpellAndObject(S:Spells*, O:Object*, I:Flags*SplCast)
		"""
		raise Exception("Not implemented function: MarkSpellAndObject!")
		return
	
	@dump_args
	def MoraleSet(self, target, morale):
		"""
		MoraleSet(O:Target*, I:Morale*)
		"""
		raise Exception("Not implemented function: MoraleSet!")
		return
	
	@dump_args
	def MoveToObject(self, target):
		"""
		MoveToObject(O:Target*)
		"""
		raise Exception("Not implemented function: MoveToObject!")
		return
	
	@dump_args
	def MoveToObjectFollow(self, obj):
		"""
		MoveToObjectFollow(O:Object*)
		"""
		raise Exception("Not implemented function: MoveToObjectFollow!")
		return
	
	@dump_args
	def MoveToObjectUntilSee(self, target):
		"""
		MoveToObjectUntilSee(O:Target*)
		"""
		raise Exception("Not implemented function: MoveToObjectUntilSee!")
		return
	
	@dump_args
	def MoveToPoint(self, point):
		"""
		MoveToPoint(P:Point*)
		"""
		raise Exception("Not implemented function: MoveToPoint!")
		return
	
	@dump_args
	def MoveViewObject(self, target, scrollspeed):
		"""
		MoveViewObject(O:Target*, I:ScrollSpeed*Scroll)
		"""
		raise Exception("Not implemented function: MoveViewObject!")
		return
	
	@dump_args
	def MoveViewPoint(self, target, scrollspeed):
		"""
		MoveViewPoint(P:Target*, I:ScrollSpeed*Scroll)
		"""
		raise Exception("Not implemented function: MoveViewPoint!")
		return
	
	@dump_args
	def iMultiPlayerSync(self):
		"""
		MultiPlayerSync()
		"""
		# do nothing
		return
	
	@dump_args
	def NoAction(self):
		"""
		NoAction()
		"""
		# do nothing
		return
	
	@dump_args
	def OpenDoor(self, obj):
		"""
		OpenDoor(O:Object*)
		"""
		raise Exception("Not implemented function: OpenDoor!")
		return
	
	@dump_args
	def Panic(self):
		"""
		Panic()
		"""
		raise Exception("Not implemented function: Panic!")
		return
	
	@dump_args
	def PlayDead(self, time):
		"""
		PlayDead(I:Time*)
		"""
		raise Exception("Not implemented function: PlayDead!")
		return
	
	@dump_args
	def PlaySequence(self, target, sequence):
		"""
		PlaySequence(O:Target*, I:Sequence*Sequence)
		"""
		raise Exception("Not implemented function: PlaySequence!")
		return
	
	@dump_args
	def PlaySound(self, sound):
		"""
		PlaySound(S:Sound*)
		"""
		raise Exception("Not implemented function: PlaySound!")
		return
	
	@dump_args
	def Polymorph(self, animationtype):
		"""
		Polymorph(I:AnimationType*Animate)
		"""
		raise Exception("Not implemented function: Polymorph!")
		return
	
	@dump_args
	def RandomTurn(self):
		"""
		RandomTurn()
		"""
		raise Exception("Not implemented function: RandomTurn!")
		return
	
	@dump_args
	def RandomWalk(self):
		"""
		RandomWalk()
		"""
		raise Exception("Not implemented function: RandomWalk!")
		return
	
	@dump_args
	def ReallyForceSpell(self, target, spell):
		"""
		ReallyForceSpell(O:Target, I:Spell*Spell)
		"""
		raise Exception("Not implemented function: ReallyForceSpell!")
		return
	
	@dump_args
	def RemoveSpell(self, spell):
		"""
		RemoveSpell(I:Spell*Spell)
		"""
		raise Exception("Not implemented function: RemoveSpell!")
		return
	
	@dump_args
	def iResetJoinRequests(self):
		"""
		ResetJoinRequests()
		"""
		# do nothing
		return
	
	@dump_args
	def Rest(self):
		"""
		Rest()
		"""
		raise Exception("Not implemented function: Rest!")
		return
	
	@dump_args
	def RestParty(self):
		"""
		RestParty()
		"""
		raise Exception("Not implemented function: RestParty!")
		return
	
	@dump_args
	def iRestUntilHealed(self):
		"""
		RestUntilHealed()
		"""
		# do nothing, perhaps Temple todo
		return
	
	@dump_args
	def ReturnToSavedLocation(self, tollerance):
		"""
		ReturnToSavedLocation(I:Tollerance*)
		"""
		raise Exception("Not implemented function: ReturnToSavedLocation!")
		return
	
	@dump_args
	def RunAwayFrom(self, creature, time):
		"""
		RunAwayFrom(O:Creature*, I:Time*)
		"""
		raise Exception("Not implemented function: RunAwayFrom!")
		return
	
	@dump_args
	def RunAwayFromNoLeaveArea(self, obj, duration):
		"""
		RunAwayFromNoLeaveArea(O:Object*, I:Duration*)
		"""
		raise Exception("Not implemented function: RunAwayFromNoLeaveArea!")
		return
	
	@dump_args
	def iSaveGame(self, strref):
		"""
		SaveGame(I:STRREF*)
		"""
		# do nothing
		# TODO!
		return
	
	@dump_args
	def ScreenShake(self, duration, magx, magy):
		"""
		ScreenShake(I:Duration*, I:MagX*, I:MagY*)
		"""
		raise Exception("Not implemented function: ScreenShake!")
		return
	
	@dump_args
	def SendTrigger(self, target, triggernum):
		"""
		SendTrigger(O:Target*, I:TriggerNum*)
		"""
		raise Exception("Not implemented function: SendTrigger!")
		return
	
	@dump_args
	def SetApparentNameSTRREF(self, obj, strref):
		"""
		SetApparentNameSTRREF(O:Object*, I:StrRef*)
		"""
		raise Exception("Not implemented function: SetApparentNameSTRREF!")
		return
	
	@dump_args
	def SetBestWeapon(self, obj, range):
		"""
		SetBestWeapon(O:Object*, I:Range*)
		"""
		raise Exception("Not implemented function: SetBestWeapon!")
		return
	
	@dump_args
	def SetCreatureAreaFlag(self, obj, flag, value):
		"""
		SetCreatureAreaFlag(O:Object*, I:Flag*CREAREFL, I:Value*BOOLEAN)
		"""
		raise Exception("Not implemented function: SetCreatureAreaFlag!")
		return
	
	@dump_args
	def SetCriticalPathObject(self, obj, critical):
		"""
		SetCriticalPathObject(O:Object*, I:Critical*Boolean)
		"""
		raise Exception("Not implemented function: SetCriticalPathObject!")
		return
	
	@dump_args
	def SetDialog(self, dialogfile):
		"""
		SetDialog(S:DialogFile*)
		"""
		raise Exception("Not implemented function: SetDialog!")
		return
	
	@dump_args
	def SetDialogueRange(self, range):
		"""
		SetDialogueRange(I:Range*)
		"""
		raise Exception("Not implemented function: SetDialogueRange!")
		return
	
	@dump_args
	def SetDoorFlag(self, obj, flags, value):
		"""
		SetDoorFlag(O:Object*, I:Flags*DoorFlag, I:Value*BOOLEAN)
		"""
		raise Exception("Not implemented function: SetDoorFlag!")
		return
	
	@dump_args
	def SetExtendedNight(self, trueorfalse):
		"""
		SetExtendedNight(I:TrueOrFalse*BOOLEAN)
		"""
		raise Exception("Not implemented function: SetExtendedNight!")
		return
	
	@dump_args
	def iSetGlobal(self, name, area, value):
		"""
		SetGlobal(S:Name*, S:Area*, I:Value*)
		This action sets a variable (specified by name) in the scope (specified by area) to the value (specified by value).
		"""
		self._set_global(name, area, value)
		g = self._ensure_global(name, area)
		return g
	
	@dump_args
	def SetGlobalRandom(self, name, area, min, max):
		"""
		SetGlobalRandom(S:Name*, S:Area*, I:Min*, I:Max*)
		"""
		raise Exception("Not implemented function: SetGlobalRandom!")
		return
	
	@dump_args
	def SetGlobalTimer(self, name, area, time):
		"""
		SetGlobalTimer(S:Name*, S:Area*, I:Time*GTimes)
		"""
		raise Exception("Not implemented function: SetGlobalTimer!")
		return
	
	@dump_args
	def SetGlobalTimerOnce(self, name, area, time):
		"""
		SetGlobalTimerOnce(S:Name*, S:Area*, I:Time*GTimes)
		"""
		raise Exception("Not implemented function: SetGlobalTimerOnce!")
		return
	
	@dump_args
	def SetGlobalTimerRandom(self, name, area, min, max):
		"""
		SetGlobalTimerRandom(S:Name*, S:Area*, I:Min*, I:Max*)
		"""
		raise Exception("Not implemented function: SetGlobalTimerRandom!")
		return
	
	@dump_args
	def iSetHP(self, target, hp):
		"""
		SetHP(O:Target, I:HP*)
		"""
		npc, ctrl = self._get_ie_object(target)
		if npc:
			utils_npc.ensure_hp(npc, hp)
		return
	
	@dump_args
	def SetHPPercent(self, obj, percent, flags):
		"""
		SetHPPercent(O:Object*, I:Percent*, I:Flags*HPFlags)
		"""
		raise Exception("Not implemented function: SetHPPercent!")
		return
	
	@dump_args
	def SetInternal(self, obj, index, value):
		"""
		SetInternal(O:Object*, I:Index*, I:Value*)
		"""
		raise Exception("Not implemented function: SetInternal!")
		return
	
	@dump_args
	def SetInterrupt(self, state):
		"""
		SetInterrupt(I:State*Boolean)
		"""
		raise Exception("Not implemented function: SetInterrupt!")
		return
	
	@dump_args
	def SetMusic(self, setslot, with_):
		"""
		SetMusic(I:SetSlot*MUSICS, I:With*MUSIC)
		"""
		raise Exception("Not implemented function: SetMusic!")
		return
	
	@dump_args
	def SetMyTarget(self, obj):
		"""
		SetMyTarget(O:Object*)
		"""
		raise Exception("Not implemented function: SetMyTarget!")
		return
	
	@dump_args
	def iSetNumTimesTalkedTo(self, num):
		"""
		SetNumTimesTalkedTo(I:Num*)
		"""
		raise Exception("Not implemented hre function: SetNumTimesTalkedTo!")
		return
	
	@dump_args
	def SetRegularNameSTRREF(self, obj, strref):
		"""
		SetRegularNameSTRREF(O:Object*, I:StrRef*)
		"""
		raise Exception("Not implemented function: SetRegularNameSTRREF!")
		return
	
	@dump_args
	def SetRestEncounterChance(self, dayprob, nightprob):
		"""
		SetRestEncounterChance(I:DayProb*, I:NightProb*)
		"""
		raise Exception("Not implemented function: SetRestEncounterChance!")
		return
	
	@dump_args
	def SetSavedLocation(self):
		"""
		SetSavedLocation()
		"""
		raise Exception("Not implemented function: SetSavedLocation!")
		return
	
	@dump_args
	def SetSavedLocationPoint(self, x, y, direction):
		"""
		SetSavedLocationPoint(I:X*, I:Y*, I:Direction*Dir)
		"""
		raise Exception("Not implemented function: SetSavedLocationPoint!")
		return
	
	@dump_args
	def SetStartPos(self, point):
		"""
		SetStartPos(P:Point*)
		"""
		raise Exception("Not implemented function: SetStartPos!")
		return
	
	@dump_args
	def SetTeamBit(self, teamflag, value):
		"""
		SetTeamBit(I:TeamFlag*TeamBit, I:Value*BOOLEAN)
		"""
		raise Exception("Not implemented function: SetTeamBit!")
		return
	
	@dump_args
	def Shout(self, id):
		"""
		Shout(I:ID*)
		"""
		raise Exception("Not implemented function: Shout!")
		return
	
	@dump_args
	def SmallWait(self, time):
		"""
		SmallWait(I:Time*)
		"""
		raise Exception("Not implemented function: SmallWait!")
		return
	
	@dump_args
	def Spell(self, target, spell):
		"""
		Spell(O:Target*, I:Spell*Spell)
		"""
		raise Exception("Not implemented function: Spell!")
		return
	
	@dump_args
	def SpellCastEffect(self, source, voice, sound1, sound2, animation, speed, sequence):
		"""
		SpellCastEffect(O:Source*, S:Voice*, S:Sound1*, S:Sound2*, I:Animation*sceffect, I:Speed*, I:Sequence*Sequence)
		"""
		raise Exception("Not implemented function: SpellCastEffect!")
		return
	
	@dump_args
	def SpellHitEffectPoint(self, source, target, effect, height):
		"""
		SpellHitEffectPoint(O:Source*, P:Target*, I:Effect*sheffect, I:Height*)
		"""
		raise Exception("Not implemented function: SpellHitEffectPoint!")
		return
	
	@dump_args
	def SpellHitEffectSprite(self, source, target, effect, height):
		"""
		SpellHitEffectSprite(O:Source*, O:Target*, I:Effect*sheffect, I:Height*)
		"""
		raise Exception("Not implemented function: SpellHitEffectSprite!")
		return
	
	@dump_args
	def SpellPoint(self, target, spell):
		"""
		SpellPoint(P:Target*, I:Spell*Spell)
		"""
		raise Exception("Not implemented function: SpellPoint!")
		return
	
	@dump_args
	def SpellWait(self, spell):
		"""
		SpellWait(I:Spell*Spell)
		"""
		raise Exception("Not implemented function: SpellWait!")
		return
	
	@dump_args
	def StartCutScene(self, cutscene):
		"""
		StartCutScene(S:CutScene*)
		"""
		raise Exception("Not implemented function: StartCutScene!")
		return
	
	@dump_args
	def StartCutSceneMode(self):
		"""
		StartCutSceneMode()
		"""
		raise Exception("Not implemented function: StartCutSceneMode!")
		return
	
	@dump_args
	def StartCutscene(self, cutscene):
		"""
		StartCutscene(S:CutScene*)
		"""
		raise Exception("Not implemented function: StartCutscene!")
		return
	
	@dump_args
	def StartCutsceneMode(self):
		"""
		StartCutsceneMode()
		"""
		raise Exception("Not implemented function: StartCutsceneMode!")
		return
	
	@dump_args
	def StartMovie(self, resref):
		"""
		StartMovie(S:ResRef*)
		"""
		raise Exception("Not implemented function: StartMovie!")
		return
	
	@dump_args
	def StartRandomTimer(self, timerid, mintime, maxtime):
		"""
		StartRandomTimer(I:TimerID*, I:MinTime*, I:MaxTime*)
		"""
		raise Exception("Not implemented function: StartRandomTimer!")
		return
	
	@dump_args
	def StartStore(self, store, target):
		"""
		StartStore(S:Store*, O:Target*)
		"""
		raise Exception("Not implemented function: StartStore!")
		return
	
	@dump_args
	def StartTimer(self, id, time):
		"""
		StartTimer(I:ID*, I:Time*)
		"""
		raise Exception("Not implemented function: StartTimer!")
		return
	
	@dump_args
	def StopJoinRequests(self):
		"""
		StopJoinRequests()
		"""
		raise Exception("Not implemented function: StopJoinRequests!")
		return
	
	@dump_args
	def TakePartyGold(self, amount):
		"""
		TakePartyGold(I:Amount*)
		"""
		raise Exception("Not implemented function: TakePartyGold!")
		return
	
	@dump_args
	def TakePartyItem(self, item):
		"""
		TakePartyItem(S:Item*)
		"""
		raise Exception("Not implemented function: TakePartyItem!")
		return
	
	@dump_args
	def TakePartyItemAll(self, item):
		"""
		TakePartyItemAll(S:Item*)
		"""
		raise Exception("Not implemented function: TakePartyItemAll!")
		return
	
	@dump_args
	def iTakePartyItemNum(self, item, num):
		"""
		TakePartyItemNum(S:Item*, I:Num)

		This action will remove a number of instances (specified by the Num parameter) of the specified item from the party. 
		The items will be removed from players in order, for example; Player1 has 3 instances of “MYITEM” in their inventory, 
		Player2 has 2 instance of “MYITEM,” and Player3 has 1 instance. If the action TakePartyItemNum(“MYITEM”, 4) is run, 
		all 3 instances of “MYITEM” will be taken from Player1, and 1 instance will be taken from Player2. 
		This leaves Player2 and Player3 each with one instance of “MYITEM.” If the last item of an item type stored in a container 
		STO file is removed by this action, the amount becomes zero. Items with zero quantities cannot be seen in-game, 
		cannot be removed by TakePartyItem, and will not count toward a container’s current item load. 
		If the item to be taken is in a stack, and the stack is in a quickslot, the item will be removed, and the remaining stack will be placed in the inventory. 
		If the inventory is full, the stack item will be dropped on the ground.
		"""

		proto = self._get_proto(item)
		if not proto is None:
			for pc in toee.game.party:
				while num:
					item = pc.item_find_by_proto(proto)
					if item:
						item.destroy()
						# TODO - decrease if stack
						num = num - 1
				if not num:
					break
		return
	
	@dump_args
	def TransferInventory(self, source, target):
		"""
		TransferInventory(O:Source*, O:Target*)
		"""
		raise Exception("Not implemented function: TransferInventory!")
		return
	
	@dump_args
	def TriggerActivation(self, obj, state):
		"""
		TriggerActivation(O:Object*, I:State*Boolean)
		"""
		raise Exception("Not implemented function: TriggerActivation!")
		return
	
	@dump_args
	def Turn(self):
		"""
		Turn()
		"""
		raise Exception("Not implemented function: Turn!")
		return
	
	@dump_args
	def UndoExplore(self):
		"""
		UndoExplore()
		"""
		raise Exception("Not implemented function: UndoExplore!")
		return
	
	@dump_args
	def Unlock(self, obj):
		"""
		Unlock(O:Object*)
		"""
		raise Exception("Not implemented function: Unlock!")
		return
	
	@dump_args
	def UseItem(self, obj, target):
		"""
		UseItem(S:Object*, O:Target*)
		"""
		raise Exception("Not implemented function: UseItem!")
		return
	
	@dump_args
	def Wait(self, time):
		"""
		Wait(I:Time*)
		"""
		raise Exception("Not implemented function: Wait!")
		return
	
	@dump_args
	def WaitAnimation(self, target, sequence):
		"""
		WaitAnimation(O:Target*, I:Sequence*Sequence)
		"""
		raise Exception("Not implemented function: WaitAnimation!")
		return
	
	@dump_args
	def WaitRandom(self, mintime, maxtime):
		"""
		WaitRandom(I:MinTime*, I:MaxTime*)
		"""
		raise Exception("Not implemented function: WaitRandom!")
		return
	
	@dump_args
	def Weather(self, weather):
		"""
		Weather(I:Weather*Weather)
		"""
		raise Exception("Not implemented function: Weather!")
		return
	
	@dump_args
	def XEquipItem(self, item, obj, slot, equipunequip):
		"""
		XEquipItem(S:Item*, O:Object*, I:Slot*Slots, I:EquipUnEquip*BOOLEAN)
		"""
		raise Exception("Not implemented function: XEquipItem!")
		return
	
	########## IDENTIFIERS ##########
	@dump_args
	def EighthNearest(self, obj):
		"""
		EighthNearest(O:Object*)
		"""
		raise Exception("Not implemented function: EighthNearest!")
		return
	
	@dump_args
	def EigthNearestEnemyOf(self, obj):
		"""
		EigthNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: EigthNearestEnemyOf!")
		return
	
	@dump_args
	def Farthest(self, obj):
		"""
		Farthest(O:Object*)
		"""
		raise Exception("Not implemented function: Farthest!")
		return
	
	@dump_args
	def FarthestEnemyOf(self, obj):
		"""
		FarthestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: FarthestEnemyOf!")
		return
	
	@dump_args
	def FifthNearest(self, obj):
		"""
		FifthNearest(O:Object*)
		"""
		raise Exception("Not implemented function: FifthNearest!")
		return
	
	@dump_args
	def FifthNearestEnemyOf(self, obj):
		"""
		FifthNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: FifthNearestEnemyOf!")
		return
	
	@dump_args
	def FourthNearest(self, obj):
		"""
		FourthNearest(O:Object*)
		"""
		raise Exception("Not implemented function: FourthNearest!")
		return
	
	@dump_args
	def FourthNearestEnemyOf(self, obj):
		"""
		FourthNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: FourthNearestEnemyOf!")
		return
	
	@dump_args
	def LastAttackerOf(self, obj):
		"""
		LastAttackerOf(O:Object*)
		"""
		raise Exception("Not implemented function: LastAttackerOf!")
		return
	
	@dump_args
	def LastHeardBy(self, obj):
		"""
		LastHeardBy(O:Object*)
		"""
		raise Exception("Not implemented function: LastHeardBy!")
		return
	
	@dump_args
	def LastSeenBy(self, obj):
		"""
		LastSeenBy(O:Object*)
		"""
		raise Exception("Not implemented function: LastSeenBy!")
		return
	
	@dump_args
	def LastTalkedToBy(self, obj):
		"""
		LastTalkedToBy(O:Object*)
		"""
		raise Exception("Not implemented function: LastTalkedToBy!")
		return
	
	@dump_args
	def LastTargetedBy(self, obj):
		"""
		LastTargetedBy(O:Object*)
		"""
		raise Exception("Not implemented function: LastTargetedBy!")
		return
	
	@dump_args
	def MostDamagedOf(self, obj):
		"""
		MostDamagedOf(O:Object*)
		"""
		raise Exception("Not implemented function: MostDamagedOf!")
		return
	
	@dump_args
	def Nearest(self, obj):
		"""
		Nearest(O:Object*)
		"""
		raise Exception("Not implemented function: Nearest!")
		return
	
	@dump_args
	def NearestEnemyOf(self, obj):
		"""
		NearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: NearestEnemyOf!")
		return
	
	@dump_args
	def NearestEnemySummoned(self, obj):
		"""
		NearestEnemySummoned(O:Object*)
		"""
		raise Exception("Not implemented function: NearestEnemySummoned!")
		return
	
	@dump_args
	def NearestPC(self, obj):
		"""
		NearestPC(O:Object*)
		"""
		raise Exception("Not implemented function: NearestPC!")
		return
	
	@dump_args
	def NinthNearest(self, obj):
		"""
		NinthNearest(O:Object*)
		"""
		raise Exception("Not implemented function: NinthNearest!")
		return
	
	@dump_args
	def NinthNearestEnemyOf(self, obj):
		"""
		NinthNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: NinthNearestEnemyOf!")
		return
	
	@dump_args
	def Player1(self, obj):
		"""
		Player1(O:Object*)
		"""
		raise Exception("Not implemented function: Player1!")
		return
	
	@dump_args
	def Player2(self, obj):
		"""
		Player2(O:Object*)
		"""
		raise Exception("Not implemented function: Player2!")
		return
	
	@dump_args
	def Player3(self, obj):
		"""
		Player3(O:Object*)
		"""
		raise Exception("Not implemented function: Player3!")
		return
	
	@dump_args
	def Player4(self, obj):
		"""
		Player4(O:Object*)
		"""
		raise Exception("Not implemented function: Player4!")
		return
	
	@dump_args
	def Player5(self, obj):
		"""
		Player5(O:Object*)
		"""
		raise Exception("Not implemented function: Player5!")
		return
	
	@dump_args
	def Player6(self, obj):
		"""
		Player6(O:Object*)
		"""
		raise Exception("Not implemented function: Player6!")
		return
	
	@dump_args
	def SecondNearest(self, obj):
		"""
		SecondNearest(O:Object*)
		"""
		raise Exception("Not implemented function: SecondNearest!")
		return
	
	@dump_args
	def SecondNearestEnemyOf(self, obj):
		"""
		SecondNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: SecondNearestEnemyOf!")
		return
	
	@dump_args
	def SeventhNearest(self, obj):
		"""
		SeventhNearest(O:Object*)
		"""
		raise Exception("Not implemented function: SeventhNearest!")
		return
	
	@dump_args
	def SeventhNearestEnemyOf(self, obj):
		"""
		SeventhNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: SeventhNearestEnemyOf!")
		return
	
	@dump_args
	def SixthNearest(self, obj):
		"""
		SixthNearest(O:Object*)
		"""
		raise Exception("Not implemented function: SixthNearest!")
		return
	
	@dump_args
	def SixthNearestEnemyOf(self, obj):
		"""
		SixthNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: SixthNearestEnemyOf!")
		return
	
	@dump_args
	def TenthNearest(self, obj):
		"""
		TenthNearest(O:Object*)
		"""
		raise Exception("Not implemented function: TenthNearest!")
		return
	
	@dump_args
	def TenthNearestEnemyOf(self, obj):
		"""
		TenthNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: TenthNearestEnemyOf!")
		return
	
	@dump_args
	def ThirdNearest(self, obj):
		"""
		ThirdNearest(O:Object*)
		"""
		raise Exception("Not implemented function: ThirdNearest!")
		return
	
	@dump_args
	def ThirdNearestEnemyOf(self, obj):
		"""
		ThirdNearestEnemyOf(O:Object*)
		"""
		raise Exception("Not implemented function: ThirdNearestEnemyOf!")
		return
	
class InfScriptSupportNPC(InfScriptSupport):

	def _get_globals(self, area):
		if area.lower() == "locals":
			result = self.vars.get("locals")
			if result is None:
				result = dict()
				self.vars["locals"] = result
			return result

		return super(InfScriptSupportNPC, self)._get_globals(area)

	def _get_nearest_obj(self, this_npc, obj_list_flags = toee.OLC_CRITTERS):
		assert isinstance(this_npc, toee.PyObjHandle)
		nearest = None
		nearest_dist = -1
		for obj in toee.game.obj_list_vicinity(this_npc.location, obj_list_flags):
			assert isinstance(obj, toee.PyObjHandle)
			if obj == this_npc: continue
			if obj.d20_query(toee.Q_Critter_Is_Invisible): continue
			dist = this_npc.distance_to(obj)
			if nearest_dist == -1 or dist < nearest_dist:
				nearest_dist = dist
				nearest = obj
		return nearest

	def _get_ie_object_nearest(self):
		npc = self._get_nearest_obj(self._gnpc(), toee.OLC_CRITTERS)
		return (npc, None)

	def _get_ie_object_nearest_pc(self):
		npc = self._get_nearest_obj(self._gnpc(), toee.OLC_PC)
		return (npc, None)

	def _get_stat_value(self, obj, statnum):
		npc, ctrl = self._get_ie_object(obj)
		if not npc: 
			return

		"""
		ENCUMBERANCE
		CHR
		XP
		RESISTFIRE
		RESISTELECTRICITY
		RESISTMAGIC
		CLASSLEVELSUM
		SEEINVISIBLE
		"""

		statnumu = statnum.upper()
		if statnumu == 'ENCUMBERANCE':
			return npc.d20_query(toee.Q_Critter_Is_Encumbered_Medium)
		elif statnumu == 'CHR':
			return npc.stat_level_get(toee.stat_charisma)
		elif statnumu == 'CLASSLEVELSUM':
			return npc.stat_level_get(toee.stat_level)
		elif statnumu == 'RESISTFIRE':
			# TODO IMPROVE
			return npc.d20_query_has_condition("Monster Energy Resistance")
		elif statnumu == 'RESISTELECTRICITY':
			# TODO IMPROVE
			return npc.d20_query_has_condition("Monster Energy Resistance")
		elif statnumu == 'RESISTMAGIC':
			return npc.d20_query_has_condition("Spell Resistance")
		elif statnumu == 'SEEINVISIBLE':
			return npc.d20_query_has_condition("sp-See Invisibility")
		return

	########## TRIGGERS ##########

	@dump_args
	def iCheckStat(self, obj, value, statnum):
		"""
		CheckStatGT(O:Object*, I:Value*, I:StatNum*Stats)
		"""
		result = self._get_stat_value(obj, statnum)
		return result == value

	@dump_args
	def iCheckStatLT(self, obj, value, statnum):
		""" 
		0x4046 CheckStatLT(O:Object*,I:Value*,I:StatNum*Stats)
		Returns true only if the specified object has the statistic in the 3rd parameter less than the value of the 2nd parameter.
		"""
		result = self._get_stat_value(obj, statnum)
		return result < value
	
	@dump_args
	def iCheckStatGT(self, obj, value, statnum):
		""" 
		0x4045 CheckStatGT(O:Object*,I:Value*,I:StatNum*Stats)
		Returns true only if the specified object has the statistic in the 3rd parameter greater than the value of the 2nd parameter.
		"""
		result = self._get_stat_value(obj, statnum)
		print('stat_value: {}'.format(result))
		return result > value

	
	@dump_args
	def iDestroyItem(self, resref):
		"""
		DestroyItem(S:ResRef*)
		This action removes a single instance of the specified item from the active creature, unless the item exists in a stack, 
		in which case the entire stack is removed. The example script is from ar1000.bcs.
		"""
		npc = self._gnpc()
		proto = self._get_proto(resref)
		item = npc.item_find_by_proto(proto)
		if item:
			# TODO - decrease if stack
			item.destroy()
		return

	@dump_args
	def iGiveItem(self, obj, target):
		"""
		GiveItem(S:Object*, O:Target*)
		This action instructs the active creature to give the specified item (parameter 1) to the specified 
		target (parameter 2). The active creature must possess the item to pass it. 
		"""
		target, ctrl = self._get_ie_object(target)
		if target:
			npc = self._gnpc()
			proto = self._get_proto(obj)
			item = npc.item_find_by_proto(proto)
			if item:
				target.item_get(item)
				if target.type == toee.obj_t_pc:
					utils_pc.pc_receive_item_print(target, item, True)
		return

	@dump_args
	def iHP(self, obj, hit_points):
		""" 
		0x4010 HP(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are equal to the 2nd parameter.
		"""
		return self._hp(obj) == hit_points
	
	@dump_args
	def iHPGT(self, obj, hit_points):
		""" 
		00x4011 HPGT(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are greater than the 2nd parameter.
		"""
		return self._hp(obj) > hit_points
	
	@dump_args
	def iHPLT(self, obj, hit_points):
		""" 
		0x4012 HPLT(O:Object*,I:Hit Points*)
		Returns true only if the current hitpoints of the specified object are less than the 2nd parameter.
		"""
		return self._hp(obj) < hit_points

	@dump_args
	def iNumTimesTalkedTo(self, num):
		""" 
		0x4039 NumTimesTalkedTo(I:Num*)

		Returns true only if the player's party has spoken to the active CRE the exact number of times specified.
		NB. NumTimesTalkedTo seems to increment when a PC initiates conversion with an NPC, or an NPC initiates conversation with a PC.
		NumTimesTalkedTo does not seem to increment for force-talks, interactions, interjections and self-talking.
		"""
		result = self.has_met()
		return result == num

	@dump_args
	def iNumTimesTalkedToGT(self, num):
		""" 
		0x403A NumTimesTalkedToGT(I:Num*)
		Returns true only if the player's party has spoken to the active CRE more than the number of times specified.
		"""
		result = self.has_met()
		return result > num
	
	@dump_args
	def iNumTimesTalkedToLT(self, num):
		"""
		NumTimesTalkedToLT(I:Num*)
		Returns true only if the player's party has spoken to the active CRE less than the number of times specified.
		"""
		result = self.has_met()
		return result < num

	@dump_args
	def iOnCreation(self):
		"""
		OnCreation()
		"""
		is_on_creation = self.vars.get('is_on_creation')
		# TODO
		return is_on_creation == 1

	########## ACTIONS ##########

	@dump_args
	def iSetNumTimesTalkedTo(self, num):
		"""
		SetNumTimesTalkedTo(I:Num*)
		"""
		result = self.has_met_set(num)
		return result

class InfScriptSupportDaemon(InfScriptSupport):
	def _get_globals(self, area):
		if area.lower() == "area":
			result = self.vars.get("area_globals")
			if result is None:
				result = dict()
				self.vars["area_globals"] = result
			return result

		return super(InfScriptSupportDaemon, self)._get_globals(area)

	@dump_args
	def iOnCreation(self):
		"""
		OnCreation()
		"""
		is_on_creation = self.vars.get('is_on_creation')
		# TODO
		return is_on_creation == 1

class ScriptBase(object):
	@classmethod
	def execute(cls, self):
		assert isinstance(self, InfScriptSupport)

		cls.do_execute(self)
		return

	@classmethod
	def do_execute(cls, self):
		assert isinstance(self, InfScriptSupport)
		return
