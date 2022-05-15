from math import fabs
import sys
import os
import producer_doc
import producer_strref

npc_template_file = 'data/py06616_template.py'
out_npcs_file = '../../src/zmod_iwd2_core/scr/py01001_targos_docks_encounters.py'
out_dialog_file = '../../src/zmod_iwd2_core/dlg/01001_targos_docks_encounters.dlg'
out_daemon_file = '../../src/zmod_iwd2_core/scr/py01000_targos_docks_daemon.py'
exp_dir = '../../resources/iwd2_exp'
src_dir = '../../resources/iwd2_src'
core_dir = '../../src/zmod_iwd2_core'
module_dir = '../../src/zmod_iwd2'
wav_dir = r'D:\IE\Resources\IWD2\WAV'
baf_dir = rf'{src_dir}/SCR'
bam_dir = r'D:\IE\Resources\IWD2\BAM'
protos_paths = fr'D:\Temple\Temple of Elemental Evil.template\data\rules\protos.tab;D:\Dev.Home\GitHub\anatoliy-savchak\TemplePlus\tpdatasrc\tpgamefiles\rules\protos;{core_dir}/rules/protos'
temple_src_path = r'../../../TemplePlus'

def main():
    for i in range(1, 20): print("")
    print("################### START")

    doc = producer_doc.ProducerDoc(exp_dir=exp_dir
        , core_dir=core_dir
        , wav_dir = wav_dir
        , src_dir = src_dir
        , module_dir = module_dir
        , baf_dir = baf_dir
        , bam_dir = bam_dir
        , protos_paths = protos_paths
        , temple_src_path = temple_src_path
    )
    doc.init(from_scratch=False)
    if False:
        are_prod = doc.acquire_are_producer('AR1000')
        are_prod.skip_script_general = True
        are_prod.skip_script_class = True
        are_prod.skip_script_race = True
        are_prod.skip_script_default = True
        are_prod.skip_script_specific = True
        are_prod.skip_script_special1 = True
        are_prod.skip_script_daemon = False
        if True:
            are_prod.produce()
        else:
            are_prod.produce_start()
            are_prod.produce_actor("Hedron")
            are_prod.produce_daemon(True)

    if True:
        are_prod = doc.acquire_are_producer('AR1201', False)
        are_prod.skip_script_general = True
        are_prod.skip_script_class = True
        are_prod.skip_script_race = True
        are_prod.skip_script_default = True
        are_prod.skip_script_specific = True
        are_prod.skip_script_special1 = True
        are_prod.skip_script_daemon = False
        are_prod.produce()
        if False:
            are_prod.produce_start()
            are_prod.produce_actor("Shawford_Crale")
            are_prod.produce_actor("Messenger_Hidden")
            
            are_prod.daemon.produce(False)
            are_prod.daemon.save()
            are_prod.produce_end()

    if False:
        doc.producerOfScripts.log_usage = True
        doc.producerOfScripts.log_statistics = True
        doc.producerOfScripts.log_strrefs = False
        #doc.scan_all_ares()
        merge_from_path = os.path.join(doc.core_dir, 'scr/inf_scripting_copy2.py')
        doc.producerOfScripts.produce_func_defs(merge_from_path=merge_from_path)
        #doc.producerOfScripts._save_index()
        for e in doc.producerOfScripts.error_messages:
            print(e)

    if False:
        doc.producerOfScripts.log_usage = False
        doc.producerOfScripts.log_strrefs = True
        doc.producerOfFloats = producer_strref.ProducerOfFloats(doc, True)
        doc.scan_all_ares()
        #doc.producerOfScripts.produce_func_defs()
        #doc.producerOfScripts._save_index()
        doc.producerOfFloats.save()
        for e in doc.producerOfScripts.error_messages:
            print(e)

    return 0

if __name__ == "__main__":
    sys.exit(main())
