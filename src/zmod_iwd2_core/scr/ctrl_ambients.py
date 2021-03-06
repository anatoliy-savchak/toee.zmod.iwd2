import toee
import ctrl_behaviour
import const_toee

class CtrlAmbient(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 2068

	def setup_simple(self, npc, sound_value):
		npc.obj_set_int[toee.obj_f_sound_effect] = sound_value
		return

	def setup(self, name, flags, frequency, frequency_variation, radius, x, y, schedule):
		self.vars["name"] = name
		self.vars["flags"] = flags
		self.vars["frequency"] = frequency
		self.vars["frequency_variation"] = frequency_variation
		self.vars["radius"] = radius
		self.vars["x"] = x
		self.vars["y"] = y
		self.vars["schedule"] = schedule
		self.vars["sound_files"] = list()
		return

	def setup_sound(self, sound_id, durationf, volume, title = None):
		sound_files = self.vars["sound_files"]
		#sound_files.append({"sound_id": sound_id, "durationf": durationf, "volume": volume, "title": title})
		sound_files.append((sound_id, durationf, volume, title))
		self.vars["sound_files"] = sound_files
		return

	def run(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.object_flag_set(toee.OF_DONTDRAW)
		npc.object_flag_set(toee.OF_NO_BLOCK)
		npc.object_flag_set(toee.OF_CLICK_THROUGH)
		npc.object_flag_set(toee.OF_INVULNERABLE)
		# or now we support only loop (buggy: or self.vars["frequency"] <= 10)
		if "Looping" in self.vars["flags"]:
			sound_files = self.vars["sound_files"]
			sound_id = sound_files[0][0]
			npc.obj_set_int(toee.obj_f_sound_effect, sound_id)
			radius_flag = const_toee.OSCF_SOUND_SMALL
			radius = self.vars["radius"]
			if radius >= 800 or "IgnoreRadius" in self.vars["flags"]:
				radius_flag = const_toee.OSCF_SOUND_EXTRA_LARGE
			elif radius > 300:
				radius_flag = const_toee.OSCF_SOUND_MEDIUM
			npc.obj_set_int(toee.obj_f_scenery_flags, radius)
		return

class AmbientHanlder(object):
	def __init__(self):
		self.name = ""
		self.flags = ""
		self.frequency = 0
		self.frequency_variation = 0
		self.radius = 0
		self.loc = 0
		self.schedule = ""
		self.sounds = list()

		self.status = ""
		self.prev_index = -1
		self.timesec_started = 0
		self.duration = 0
		return

	def setup(self, name, flags, frequency, frequency_variation, radius, loc, schedule):
		self.name = name
		self.flags = flags
		self.frequency = frequency
		self.frequency_variation = frequency_variation
		self.radius = radius
		self.loc = loc
		self.schedule = schedule

		self.status = ""
		self.prev_index = -1
		return

	def setup_sound(self, sound_id, durationf, volume, title = None):
		self.sounds.append((sound_id, durationf, volume, title))
		return

	def tick(self):
		cstime = toee.game.time.time_in_game_in_seconds()
		past = cstime - self.timesec_started
		#print("AmbientHanlder {} heartbeat, past: {}, duration: {}, status: {}".format(self.name, past, self.duration, self.status))
		if not self.status:
			self.do_play()
		elif (self.status == "playing"):
			if past <= self.duration:
				pass
			else:
				self.do_cooldown()
		elif (self.status == "cooldown"):
			if past <= self.duration:
				pass
			else:
				self.do_play()
		return

	def do_play(self):
		self.status = "playing"
		sound_index = 0
		if "RandomOrder" in self.flags and len(self.sounds) > 1:
			sound_index = -1
			while sound_index < 0 or sound_index == self.prev_index:
				sound_index = toee.game.random_range(0, len(self.sounds)-1)
		sound_id = self.sounds[sound_index][0]
		#print("AmbientHanlder {} do_play sound_id: {}".format(self.name, sound_id))
		self.timesec_started = toee.game.time.time_in_game_in_seconds()
		self.duration = self.sounds[sound_index][1]
		#ret = toee.game.sound(sound_id)
		ret = toee.game.sound_local_loc(sound_id, self.loc)
		
		#print("AmbientHanlder {} toee.game.sound({})={}, duration: {}, index: {} (old: {})".format(self.name, sound_id, ret, self.duration, sound_index, self.prev_index))
		self.prev_index = sound_index
		return

	def do_cooldown(self):
		self.status = "cooldown"
		self.timesec_started = toee.game.time.time_in_game_in_seconds()
		vari = 0 if not self.frequency_variation else toee.game.random_range(0, self.frequency_variation)
		self.duration = self.frequency + vari
		#print("AmbientHanlder {} do_cooldown duraiton: {}".format(self.name, self.duration))
		return