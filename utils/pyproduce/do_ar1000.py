import os
from produce_journal import JournalFile
import pyproduce
import produce_npc
import produce_ar
import produce_dialog
import produce_sound
import produce_icon
import produce_proto
import common
import script_items
import produce_bcs_manager

npc_template_file = 'data/py06616_template.py'
out_npcs_file = '../../src/zmod_iwd2_core/scr/py01001_targos_docks_encounters.py'
out_dialog_file = '../../src/zmod_iwd2_core/dlg/01001_targos_docks_encounters.dlg'
out_daemon_file = '../../src/zmod_iwd2_core/scr/py01000_targos_docks_daemon.py'
exp_dir = '../../resources/iwd2_exp'
src_dir = '../../resources/iwd2_src'
core_dir = '../../src/zmod_iwd2_core'
module_dir = '../../src/zmod_iwd2'
wav_dir = r'D:\IE\Resources\IWD2\WAV'
baf_dir = r'D:\IE\Resources\IWD2\SCR'
bam_dir = r'D:\IE\Resources\IWD2\BAM'
protos_paths = fr'D:\Temple\Temple of Elemental Evil.template\data\rules\protos.tab;D:\Dev.Home\GitHub\anatoliy-savchak\TemplePlus\tpdatasrc\tpgamefiles\rules\protos;{core_dir}/rules/protos'
producer_app = pyproduce.ProducerApp(exp_dir=exp_dir, core_dir=core_dir
    , wav_dir = wav_dir, src_dir = src_dir, module_dir = module_dir
    , baf_dir = baf_dir, bam_dir = bam_dir, protos_paths = protos_paths)

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

script_items.process(producer_app)

if True:
    #producer_app.produceSound.build_index()
    producer_app.produceSound.load_file_index()
    #producer_app.produceSound.build_and_save_sounds_file()
    #producer_app.produceSound.save_music_files()
    #producer_app.produceSound.build_and_save_schemes()
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
