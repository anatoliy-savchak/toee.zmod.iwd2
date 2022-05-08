import os
import producer_base
import producer_daemon
import producer_ctrl_auto
import produce_dialog
import producer_ctrl_manual
import produce_bcs_manager
import producer_ctrl_inst_auto
import producer_ctrl_inst_manual
import common

class ProducerOfAre(producer_base.Producer):
    def __init__(self, doc, are_name: str, script_id: int, make_new: bool):
        self.src_sec_path = os.path.join(doc.exp_dir, 'Areas', are_name, are_name + '_sec.json')
        src_path = os.path.join(doc.exp_dir, 'Areas', are_name, are_name + '.json')

        super().__init__(doc, src_path=src_path)

        self.make_new = make_new
        self.are_name = are_name
        self.script_id = script_id
        self.bcs_counter_auto = 0
        self.src_sec = None
        if os.path.exists(self.src_sec_path):
            self.src_sec = common.read_file_json(self.src_sec_path)

        self.daemon = producer_daemon.ProducerOfDaemon(self.doc
            , self.are_name
            , self.script_id
            , self.make_new
            , self.src
            , self.src_sec
            )
        self.dialog = produce_dialog.DialogFile(self.doc.get_path_out_npcs_dialog_file(self.are_name, self.script_id + 1))
        return

    def produce(self):
        self.produce_start()
        for actor in self.daemon.get_eligible_actor_recs():
            actor_name = actor['Name']
            actor_cre_name = actor['CREFile']
            self.ensure_actor_bcses(actor)

            if not self.doc.classesRegistry.get_class_tup('class_auto', actor_cre_name):
                self.produce_cre_class_auto(actor_cre_name)

            if not self.doc.classesRegistry.get_class_tup('class_manual', actor_cre_name):
                self.produce_cre_class_manual(actor_cre_name)

            if not self.doc.classesRegistry.get_class_tup('class_inst_auto', f'{self.are_name}.{actor_cre_name}.{actor_name}'):
                self.produce_cre_class_inst_auto(actor_name, actor_cre_name, actor)

            if not self.doc.classesRegistry.get_class_tup('class_inst_manual', f'{self.are_name}.{actor_cre_name}.{actor_name}'):
                self.produce_cre_class_inst_manual(actor_name, actor_cre_name)

        self.daemon.produce()
        self.daemon.save()
        return

    def scan(self):
        area_script = self.src["AreaScript"]
        if area_script and area_script != "None":
            bcs_prod = produce_bcs_manager.ProduceBCSFileAuto(self.doc, area_script, self.are_name, self.script_id + 5, False)
            bcs_prod.scan()
            del bcs_prod

        cres_to_scan = list()
        for actor in self.daemon.get_eligible_actor_recs():
            actor_name = actor['Name']
            actor_cre_name = actor['CREFile']
            if not actor_cre_name in cres_to_scan:
                cres_to_scan.append(actor_cre_name)
            self.scan_actor_bcses(actor)
        for cre_name in cres_to_scan:
            src_path = self.doc.get_path_cre(cre_name)
            cre = common.read_file_json(src_path)
            dialog_name = cre["DialogFile"]
            dialog_name = dialog_name.strip()
            producer_ctrl_auto.ProducerOfCtrlAuto.scan_dialog(self.doc, dialog_name, self.are_name, cre_name)
        return

    def produce_start(self):
        producer_ctrl_auto.ProducerOfCtrlAuto.overwrite_by_template(self.doc, are_name=self.are_name, script_id=self.script_id+1)
        producer_ctrl_inst_auto.ProducerOfCtrlInstAuto.overwrite_by_template(self.doc, are_name=self.are_name, script_id=self.script_id+3)
        return

    def produce_cre_class_auto(self, cre_name: str):
        prod = producer_ctrl_auto.ProducerOfCtrlAuto(self.doc
            , cre_name=cre_name
            , are_name=self.are_name
            , script_id=self.script_id + 1
            , make_new=False
            , dialog_file = self.dialog
        )
        prod.produce()
        prod.save()
        ctrl_name, ctrl_file_name = prod.get_ctrl_tuple()
        self.doc.classesRegistry.set_class_tup('class_auto', cre_name, ctrl_file_name, ctrl_name)
        return

    def produce_cre_class_manual(self, cre_name: str):
        class_auto = self.doc.classesRegistry.get_class_tup('class_auto', cre_name)
        prod = producer_ctrl_manual.ProducerOfCtrlManual(self.doc
            , cre_name=cre_name
            , are_name=self.are_name
            , script_id=self.script_id + 2
            , make_new=False
            , base_class=class_auto
        )
        prod.produce()
        prod.save()
        ctrl_name, ctrl_file_name = prod.get_ctrl_tuple()
        self.doc.classesRegistry.set_class_tup('class_manual', cre_name, ctrl_file_name, ctrl_name)
        return

    def produce_cre_class_inst_auto(self, actor_name: str, cre_name: str, actor_dict: dict):
        class_manual = self.doc.classesRegistry.get_class_tup('class_manual', cre_name)
        prod = producer_ctrl_inst_auto.ProducerOfCtrlInstAuto(self.doc
            , cre_name=cre_name
            , are_name=self.are_name
            , script_id=self.script_id + 3
            , make_new=False
            , base_class=class_manual
            , actor_name = actor_name
            , actor_dict = actor_dict
        )
        prod.produce()
        prod.save()
        ctrl_name, ctrl_file_name = prod.get_ctrl_tuple()
        reg_name = f'{self.are_name}.{cre_name}.{actor_name}'
        self.doc.classesRegistry.set_class_tup('class_inst_auto', reg_name, ctrl_file_name, ctrl_name)
        return

    def produce_cre_class_inst_manual(self, actor_name: str, cre_name: str):
        reg_name = f'{self.are_name}.{cre_name}.{actor_name}'
        class_auto = self.doc.classesRegistry.get_class_tup('class_inst_auto', reg_name)
        prod = producer_ctrl_inst_manual.ProducerOfCtrlInstManual(self.doc
            , cre_name=cre_name
            , are_name=self.are_name
            , script_id=self.script_id + 4
            , make_new=False
            , base_class=class_auto
            , actor_name = actor_name
        )
        prod.produce()
        prod.save()
        ctrl_name, ctrl_file_name = prod.get_ctrl_tuple()
        self.doc.classesRegistry.set_class_tup('class_inst_manual', reg_name, ctrl_file_name, ctrl_name)
        return                

    def ensure_actor_bcses(self, actor_dict: dict):
        actor_name = actor_dict["Name"]
        cre_name = actor_dict["CREFile"]
        
        if bcs_name := actor_dict["ScriptGeneral"]:
            self.ensure_bcs(actor_name, bcs_name, cre_name, "ScriptGeneral (Special 3)")
        
        if bcs_name := actor_dict["ScriptClass"]:
            self.ensure_bcs(actor_name, bcs_name, cre_name, "ScriptClass (Special 2)")
        
        if bcs_name := actor_dict["ScriptRace"]:
            self.ensure_bcs(actor_name, bcs_name, cre_name, "ScriptRace (Combat Script)")
        
        if bcs_name := actor_dict["ScriptDefault"]:
            self.ensure_bcs(actor_name, bcs_name, cre_name, "ScriptDefault (Movement Script)")
        
        if bcs_name := actor_dict["ScriptSpecific"]:
            self.ensure_bcs(actor_name, bcs_name, cre_name, "ScriptSpecific (Team Script)")
        
        if bcs_name := actor_dict["ScriptSpecial1"]:
            self.ensure_bcs(actor_name, bcs_name, cre_name, "ScriptSpecial1 (Special1)")
        return

    def ensure_bcs(self, actor_name: str, bcs_name: str, cre_name: str, script_code: str):
        if not self.doc.bcsManager.get_bc(bcs_name + '_AUTO'):
            #file_path_out = self.doc.get_path_out_are_bcs_file(self.are_name)
            #self.doc.bcsManager.produce_bcs(bcs_name, file_path_out)
            make_new_bcs = False
            if self.bcs_counter_auto == 0:
                make_new_bcs = True
            bcs_prod = produce_bcs_manager.ProduceBCSFileAuto(self.doc, bcs_name, self.are_name, self.script_id + 5, make_new_bcs)
            bcs_prod.produce(cre_name, actor_name, script_code)
            bcs_prod.save()
            ctrl_name, file_name = bcs_prod.get_ctrl_tuple()
            self.doc.bcsManager.set_bc(bcs_prod.bcs_name + '_AUTO', file_name, ctrl_name)
            self.bcs_counter_auto += 1
            del bcs_prod

            if not self.doc.bcsManager.get_bc(bcs_name):
                bcs_prod_manual = produce_bcs_manager.ProduceBCSFileManual(self.doc
                    , bcs_name, self.are_name, self.script_id + 6, file_name, ctrl_name, False)
                if bcs_prod_manual.produce(cre_name, actor_name, script_code):
                    bcs_prod_manual.save()
                ctrl_name, file_name = bcs_prod_manual.get_ctrl_tuple()
                self.doc.bcsManager.set_bc(bcs_prod_manual.bcs_name, file_name, ctrl_name)
                del bcs_prod_manual
        return

    def scan_actor_bcses(self, actor_dict: dict):
        actor_name = actor_dict["Name"]
        cre_name = actor_dict["CREFile"]
        
        if bcs_name := actor_dict["ScriptGeneral"]:
            self.scan_bcs(actor_name, bcs_name, 'script_general_auto', cre_name, "ScriptGeneral (Special 3)")
        
        if bcs_name := actor_dict["ScriptClass"]:
            self.scan_bcs(actor_name, bcs_name, 'script_class_auto', cre_name, "ScriptClass (Special 2)")
        
        if bcs_name := actor_dict["ScriptRace"]:
            self.scan_bcs(actor_name, bcs_name, 'script_combat_auto', cre_name, "ScriptRace (Combat Script)")
        
        if bcs_name := actor_dict["ScriptDefault"]:
            self.scan_bcs(actor_name, bcs_name, 'script_movement_auto', cre_name, "ScriptDefault (Movement Script)")
        
        if bcs_name := actor_dict["ScriptSpecific"]:
            self.scan_bcs(actor_name, bcs_name, 'script_team_auto', cre_name, "ScriptSpecific (Team Script)")
        
        if bcs_name := actor_dict["ScriptSpecial1"]:
            self.scan_bcs(actor_name, bcs_name, 'script_special_one_auto', cre_name, "ScriptSpecial1 (Special1)")
        return

    def scan_bcs(self, actor_name: str, bcs_name: str, def_name: str, cre_name: str, script_code: str):
        if not self.doc.bcsManager.get_bc(bcs_name + '_AUTO'):
            bcs_prod = produce_bcs_manager.ProduceBCSFileAuto(self.doc, bcs_name, self.are_name, self.script_id + 5, False)
            bcs_prod.scan(cre_name, actor_name)
            del bcs_prod
        return
