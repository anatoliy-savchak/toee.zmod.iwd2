import pyproduce
import produce_npc

exported_dir = pyproduce.InfinityExportedDir('../../resources/iwd2_exp')
#exported_dir.read_cre('10HEDRON')

pnpc = produce_npc.ProduceNPC(exported_dir)
pnpc.load_template('data/py06616_template.py')
pnpc.produce_npc('10HEDRON')
pnpc.save('data/py06616_auto.py')