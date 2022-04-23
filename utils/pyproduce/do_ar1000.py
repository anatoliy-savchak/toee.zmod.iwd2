import os
import pyproduce
import produce_npc
import produce_ar

npc_template_file = 'data/py06616_template.py'
out_npcs_file = '../../src/zmod_iwd2_core/scr/py01001_targos_docks_encounters.py'
out_daemon_file = '../../src/zmod_iwd2_core/scr/py01000_targos_docks_daemon.py'
exported_dir = pyproduce.InfinityExportedDir('../../resources/iwd2_exp')
#exported_dir.read_cre('10HEDRON')

#os_command = f"copy /Y {os.path.abspath(npc_template_file)} {os.path.abspath(out_npcs_file)}"
#print(os_command)
#os.popen(os_command)
with open(out_npcs_file, 'w') as f:
    with open(npc_template_file, 'r') as fi:
        f.writelines(fi.readlines())


if True:
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10HEDRON').save()
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10ELDGUL').save()
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10SCREED').save()
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10REIG').save()
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10JON').save()
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10BROGAN').save()
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10JORUN').save()
    pnpc = produce_npc.ProduceNPC(exported_dir, out_npcs_file).produce_npc('10MALED').save()

if True:
    daemon = produce_ar.ProduceDaemon(exported_dir, "AR1000")
    daemon.load_template(out_daemon_file)
    daemon.load_npc_classes(out_npcs_file)
    daemon.produce_npcs("place_npcs")
    daemon.save(out_daemon_file)