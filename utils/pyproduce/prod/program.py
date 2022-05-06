import sys
import producer_doc

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
temple_src_path = r'../../../TemplePlus'

def main():
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
    are_prod = doc.acquire_are_producer('AR1000')
    are_prod.produce()

    return 0

if __name__ == "__main__":
    sys.exit(main())