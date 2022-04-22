import pyproduce
import produce_npc

out_file = '../../src/zmod_iwd2_core/scr/py01001_targos_docks_encounters.py'
exported_dir = pyproduce.InfinityExportedDir('../../resources/iwd2_exp')
#exported_dir.read_cre('10HEDRON')

current_file = 'data/py06616_template.py'
pnpc = produce_npc.ProduceNPC(exported_dir)
#pnpc.elements["base_class"] = 
pnpc.load_template(current_file)
pnpc.produce_npc('10HEDRON')
current_file = out_file
pnpc.save(current_file)

pnpc = produce_npc.ProduceNPC(exported_dir)
pnpc.load_template(current_file)
pnpc.produce_npc('10ELDGUL')
pnpc.save(current_file)