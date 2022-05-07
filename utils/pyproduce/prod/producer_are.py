import os
import producer_base
import producer_daemon
import producer_ctrl_auto
import produce_dialog
import producer_ctrl_manual
import produce_bcs_manager

class ProducerOfAre(producer_base.Producer):
    def __init__(self, doc, are_name: str, script_id: int, make_new: bool):
        src_path = os.path.join(doc.exp_dir, 'Areas', are_name, are_name + '_sec.json')
        self.src_sec_path = os.path.join(doc.exp_dir, 'Areas', are_name, are_name + '.json')

        super().__init__(doc, src_path=src_path)

        self.make_new = make_new
        self.are_name = are_name
        self.script_id = script_id
        self.bcs_counter = 0

        self.daemon = producer_daemon.ProducerOfDaemon(self.doc
            , self.are_name
            , self.script_id
            , self.make_new
            , self.src)
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

            if not self.doc.classesRegistry.get_class_tup('class_inst_auto', self.are_name + '_' + actor_name):
                self.produce_cre_class_inst_auto(actor_name, actor_cre_name)

            if not self.doc.classesRegistry.get_class_tup('class_inst_manual', self.are_name + '_' + actor_name):
                self.produce_cre_class_inst_manual(actor_name, actor_cre_name)

        self.daemon.produce()
        return

    def produce_start(self):
        producer_ctrl_auto.ProducerOfCtrlAuto.overwrite_by_template(self.doc, are_name=self.are_name, script_id=self.script_id+1)
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

    def produce_cre_class_inst_auto(self, actor_name: str, cre_name: str):
        return

    def produce_cre_class_inst_manual(self, actor_name: str, cre_name: str):
        return                

    def ensure_actor_bcses(self, actor_dict: dict):
        actor_name = actor_dict["Name"]
        cre_name = actor_dict["CREFile"]
        
        if bcs_name := actor_dict["ScriptGeneral"]:
            self.ensure_bcs(actor_name, bcs_name, 'script_general_auto', cre_name, "ScriptGeneral (Special 3)")
        
        if bcs_name := actor_dict["ScriptClass"]:
            self.ensure_bcs(actor_name, bcs_name, 'script_class_auto', cre_name, "ScriptClass (Special 2)")
        
        if bcs_name := actor_dict["ScriptRace"]:
            self.ensure_bcs(actor_name, bcs_name, 'script_combat_auto', cre_name, "ScriptRace (Combat Script)")
        
        if bcs_name := actor_dict["ScriptDefault"]:
            self.ensure_bcs(actor_name, bcs_name, 'script_movement_auto', cre_name, "ScriptDefault (Movement Script)")
        
        if bcs_name := actor_dict["ScriptSpecific"]:
            self.ensure_bcs(actor_name, bcs_name, 'script_team_auto', cre_name, "ScriptSpecific (Team Script)")
        
        if bcs_name := actor_dict["ScriptSpecial1"]:
            self.ensure_bcs(actor_name, bcs_name, 'script_special_one_auto', cre_name, "ScriptSpecial1 (Special1)")
        return

    def ensure_bcs(self, actor_name: str, bcs_name: str, def_name: str, cre_name: str, script_code: str):
        if not self.doc.bcsManager.get_bc(bcs_name):
            #file_path_out = self.doc.get_path_out_are_bcs_file(self.are_name)
            #self.doc.bcsManager.produce_bcs(bcs_name, file_path_out)
            make_new_bcs = False
            if self.bcs_counter == 0:
                make_new_bcs = True
            bcs_prod = produce_bcs_manager.ProduceBCSFile(self.doc, bcs_name, self.are_name, self.script_id + 5, make_new_bcs)
            bcs_prod.produce(def_name, cre_name, actor_name, script_code)
            bcs_prod.save()
            t = bcs_prod.get_ctrl_tuple()
            self.doc.bcsManager.set_bc(bcs_prod.bcs_name, t[1], t[0])
            self.bcs_counter += 1
            del bcs_prod
        return
