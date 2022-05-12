import producer_base
import common
import os

class ProducerOfCoords(producer_base.ProducerOfFile):
    def __init__(self, doc
        , are_name: str
    ):
        out_path = doc.get_path_out_are_coords_todo_file(are_name)
        template_path = doc.get_path_empty_json()
        index_path = doc.get_path_out_are_coords_file(are_name)
        super().__init__(doc, out_path, template_path, make_new=False, index_path=index_path)
        self.are_name = are_name
        self.coords_todo=dict()
        if os.path.exists(self.out_path):
            self.coords_todo = common.read_file_json(self.out_path)
        return

    def translate_coords(self, pair: str):
        pair = pair.replace(' ', '')
        coords = self.index_file.get(pair)
        if not coords:
            self.coords_todo[pair]=pair
            self.save()
            coords = '(?,?)'
            print(f'Are {self.are_name} coords {pair} not found!')
        else:
            coords = f'({coords})'
        return coords

    def save(self):
        common.write_json(self.out_path, self.coords_todo)
        return