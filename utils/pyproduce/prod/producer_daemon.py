import producer_base

class ProducerOfDaemon(producer_base.ProducerOfFile):
    def __init__(self, doc
        , are_name: str
        , script_id: int
        , make_new: bool
        , src: dict
    ):
        template_path = doc.get_path_template_daemon_file()
        out_path = doc.get_path_out_daemon_file(are_name, script_id)
        super().__init__(doc, out_path=out_path, template_path=template_path, make_new=make_new, src=src)
        return

    def get_eligible_actor_recs(self):
        for rec in self.src['actors']:
            if not rec['DefaultHiddenCalc']:
                yield rec
        return

    def produce(self):
        return