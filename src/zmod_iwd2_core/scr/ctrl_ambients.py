import toee
import ctrl_behaviour
import const_toee

class CtrlAmbient(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_proto_id(cls): return 2068

	def setup_simple(self, npc, sound_value):
		npc.obj_set_int[obj_f_sound_effect] = sound_value
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
		self.variation = 0
		self.x = 0.0
		self.y = 0.0
		self.sound_indexes = [-1, ]
		self.durations = [-1, ]

		self.status = ""
		self.prev_index = -1
		self.timesec_started = 0
		self.duration = 0
		return

	def setup(self, name, flags, frequency, variation, x, y, sound_indexes, durations):
		self.name = name
		self.flags = flags
		self.frequency = frequency
		self.variation = variation
		self.x = x
		self.y = y
		self.sound_indexes = sound_indexes
		self.durations = durations

		self.status = ""
		self.prev_index = -1
		return

	def tick(self):
		return
		cstime = toee.game.time.time_in_game_in_seconds()
		past = cstime - self.timesec_started
		print("AmbientHanlder {} heartbeat, past: {}, status: {}".format(self.name, past, self.status))
		if not self.status:
			self.status = "playing"
			self.do_play()
		elif (self.status == "playing"):
			if past <= self.duration:
				pass
			else:
				self.status = "cooldown"
				self.do_cooldown()
		elif (self.status == "cooldown"):
			if past <= self.duration:
				pass
			else:
				self.status = "playing"
				self.do_play()
		return

	def do_play(self):
		sound_id = self.sound_indexes[0]
		print("AmbientHanlder {} do_play sound_id: {}".format(self.name, sound_id))
		self.timesec_started = toee.game.time.time_in_game_in_seconds()
		self.duration = self.durations[0]
		#ret = toee.game.sound(sound_id)
		ret = toee.game.sound_local_obj(sound_id, toee.game.leader)
		
		print("AmbientHanlder {} toee.game.sound({})=, duration: ".format(self.name, sound_id, ret, self.duration))
		return

	def do_cooldown(self):
		self.timesec_started = toee.game.time.time_in_game_in_seconds()
		vari = 0 if not self.variation else toee.game.random_range(0, self.variation)
		self.duration = self.frequency + vari
		print("AmbientHanlder {} do_cooldown duraiton: {}".format(self.name, self.duration))
		return