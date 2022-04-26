import os
from produce_journal import JournalFile
import pyproduce
import produce_npc
import produce_ar
import produce_dialog

npc_template_file = 'data/py06616_template.py'
out_npcs_file = '../../src/zmod_iwd2_core/scr/py01001_targos_docks_encounters.py'
out_dialog_file = '../../src/zmod_iwd2_core/dlg/01001_targos_docks_encounters.dlg'
out_daemon_file = '../../src/zmod_iwd2_core/scr/py01000_targos_docks_daemon.py'
out_rumors_file = '../../src/zmod_iwd2_core/mes/game_rd_npc_m2m.mes'
template_rumors_file = '../../src/zmod_iwd2_core/mes/game_rd_npc_f2m.mes'
map_rumors_file = '../../resources/iwd2_exp/journal/journal_map.json'
rumors_file = '../../resources/iwd2_exp/journal/journal.json'
exported_dir = pyproduce.InfinityExportedDir('../../resources/iwd2_exp')
exported_dir.load_toee_class_specs('../../../TemplePlus/tpdatasrc/tpgamefiles/rules/char_class')
#exported_dir.read_cre('10HEDRON')

print(f" cwd: {os.getcwd()}")

journalFile = JournalFile()
#journalFile.load_iwd_journal(rumors_file)
#journalFile.produce_rumors(out_rumors_file, template_rumors_file)
#journalFile.save_map(map_rumors_file)
journalFile.load_map(map_rumors_file)
exported_dir.journal = journalFile

with open(out_npcs_file, 'w') as f:
    with open(npc_template_file, 'r') as fi:
        f.writelines(fi.readlines())

dialog_file = produce_dialog.DialogFile(out_dialog_file)

def produce_cre(name):
    global exported_dir, out_npcs_file, dialog_file
    return produce_npc.ProduceNPC(exported_dir, out_npcs_file, dialog_file).produce_npc(name).save()

if True:
    produce_cre('10HEDRON')
    produce_cre('10ELDGUL')
    produce_cre('10SCREED')
    produce_cre('10REIG')
    produce_cre('10JON')
    produce_cre('10BROGAN')
    produce_cre('10JORUN')
    produce_cre('10MALED')
    produce_cre('10SOLDRD')
    produce_cre('10GOB')
    produce_cre('10GOBD')
    produce_cre('10GOBAR')
    produce_cre('10GOBARD')
    produce_cre('10SAILRD')

if False:
    dialog_file.copy_sound_files("D:\\IE\\Resources\\IWD2\\WAV", "D:\\Temple\\Temple of Elemental Evil.template\\modules\\zmod_iwd2_core\\sound\\speech\\01001")
    

if True:
    daemon = produce_ar.ProduceDaemon(exported_dir, "AR1000")
    daemon.load_template(out_daemon_file)
    daemon.load_npc_classes(out_npcs_file)
    daemon.produce_npcs("place_npcs")
    daemon.save(out_daemon_file)