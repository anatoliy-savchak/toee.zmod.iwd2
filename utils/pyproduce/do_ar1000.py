import pyproduce
import produce_npc
import produce_ar

out_npcs_file = '../../src/zmod_iwd2_core/scr/py01001_targos_docks_encounters.py'
out_daemon_file = '../../src/zmod_iwd2_core/scr/py01000_targos_docks_daemon.py'
exported_dir = pyproduce.InfinityExportedDir('../../resources/iwd2_exp')
#exported_dir.read_cre('10HEDRON')

if True:
    current_file = 'data/py06616_template.py'
    pnpc = produce_npc.ProduceNPC(exported_dir)
    #pnpc.elements["base_class"] = 
    pnpc.load_template(current_file)
    pnpc.produce_npc('10HEDRON')
    current_file = out_npcs_file
    pnpc.save(current_file)

    pnpc = produce_npc.ProduceNPC(exported_dir)
    pnpc.load_template(current_file)
    pnpc.produce_npc('10ELDGUL')
    pnpc.save(current_file)

daemon = produce_ar.ProduceDaemon(exported_dir, "AR1000")
daemon.load_template(out_daemon_file)
daemon.load_npc_classes(out_npcs_file)
daemon.produce_npcs("place_npcs")
daemon.save(out_daemon_file)