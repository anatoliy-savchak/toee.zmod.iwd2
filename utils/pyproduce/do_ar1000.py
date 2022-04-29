import os
from produce_journal import JournalFile
import pyproduce
import produce_npc
import produce_ar
import produce_dialog
import produce_sound

npc_template_file = 'data/py06616_template.py'
out_npcs_file = '../../src/zmod_iwd2_core/scr/py01001_targos_docks_encounters.py'
out_dialog_file = '../../src/zmod_iwd2_core/dlg/01001_targos_docks_encounters.dlg'
out_daemon_file = '../../src/zmod_iwd2_core/scr/py01000_targos_docks_daemon.py'
exp_dir = '../../resources/iwd2_exp'
src_dir = '../../resources/iwd2_src'
core_dir = '../../src/zmod_iwd2_core'
module_dir = '../../src/zmod_iwd2'
wav_dir = r'D:\IE\Resources\IWD2\WAV'
producer_app = pyproduce.ProducerApp(exp_dir=exp_dir, core_dir=core_dir, wav_dir = wav_dir, src_dir = src_dir, module_dir = module_dir)

map_rumors_file = '../../resources/iwd2_exp/journal/journal_map.json'
rumors_file = '../../resources/iwd2_exp/journal/journal.json'
producer_app.load_toee_class_specs('../../../TemplePlus/tpdatasrc/tpgamefiles/rules/char_class')

for i in range(1, 20): print("")

print("################### START")


journalFile = JournalFile()
journalFile.load_map(producer_app.get_path_map_rumors_file())
producer_app.journal = journalFile

producer_app.commands.parse_file_actions(producer_app.get_path_actions())
producer_app.commands.parse_file_triggers(producer_app.get_path_triggers())

#dialog_file = produce_dialog.DialogFile(out_dialog_file)

if False:
    produceSound = produce_sound.ProduceSound(producer_app.get_path_sounds_index()
        , file_path_sound_scheme = producer_app.get_path_sound_scheme()
        , file_path_sound_index = producer_app.get_path_sound_index()
        , dir_wav = producer_app.wav_dir
        , dir_sound = producer_app.get_path_sound()
        , producer_app = producer_app
        )
    produceSound.process_are("AR1000")
    produceSound.save_schemes()
    produceSound.save_map_info_file("AR1000")
    produceSound.save_file_index()
    produceSound.save_music_files()

if True:
    producer_app.produce_are_start("AR1000")
    producer_app.produce_are_npc('10HEDRON')
    producer_app.produce_are_npc('10ELDGUL')
    producer_app.produce_are_npc('10SCREED')
    producer_app.produce_are_npc('10REIG')
    producer_app.produce_are_npc('10JON')
    producer_app.produce_are_npc('10BROGAN')
    producer_app.produce_are_npc('10JORUN')
    producer_app.produce_are_npc('10MALED')
    producer_app.produce_are_npc('10SOLDRD')
    producer_app.produce_are_npc('10GOB')
    producer_app.produce_are_npc('10GOBD')
    producer_app.produce_are_npc('10GOBAR')
    producer_app.produce_are_npc('10GOBARD')
    producer_app.produce_are_npc('10SAILRD')
    producer_app.produce_are_npc('10CRANDA')

    producer_app.produce_are_end()

    producer_app.produce_are("AR1000")

if False:
    dialog_file.copy_sound_files("D:\\IE\\Resources\\IWD2\\WAV", "D:\\Temple\\Temple of Elemental Evil.template\\modules\\zmod_iwd2_core\\sound\\speech\\01001")
    

if False:
    daemon = produce_ar.ProduceDaemon(producer_app, "AR1000")
    daemon.load_template(out_daemon_file)
    daemon.load_npc_classes(out_npcs_file)
    daemon.produce_npcs("place_npcs")
    daemon.save(out_daemon_file)