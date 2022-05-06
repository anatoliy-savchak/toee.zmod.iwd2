import os
import common
import producer_base

class ClassesRegistry(producer_base.Producer):
    def __init__(self, doc
        , index_path: str = None
    ):
        if not index_path:
            index_path = os.path.join(doc.get_path_registry_dir(), 'classes.json')
        super().__init__(doc, index_path = index_path)
        return

    def get_class_tup(self, category: str, name: str):
        if (cat := self.index_file.get(category)):
            return cat.get(name)
        return

    def set_class_tup(self, category: str, name: str, file_name: str, class_name: str):
        if not (cat := self.index_file.get(category)):
            cat = dict()
            self.index_file[category] = cat
        cat[name] = common.tDict(file_name=file_name, class_name=class_name)
        return