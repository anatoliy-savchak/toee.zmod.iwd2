import pyproduce

exported_dir = pyproduce.InfinityExportedDir('../../resources/iwd2_exp')
#exported_dir.read_cre('10HEDRON')
exported_dir.produce_npc('10HEDRON')
exported_dir.save('../npcs.py')