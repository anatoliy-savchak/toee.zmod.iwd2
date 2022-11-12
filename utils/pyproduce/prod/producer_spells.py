import os
import producer_base
import common
import json

class ProducerOfSpells(producer_base.ProducerOfFile):
    def __init__(self, doc, make_new: bool):
        out_path = os.path.join(doc.src_dir, 'HELPERS', 'spells.tab')
        src_path = os.path.join(doc.exp_dir, 'Spells', 'spell_files.json')
        super().__init__(doc, out_path, None, make_new, src_path)
        self.spells = []
        self.parse_spells()
        self.spell_codes = []
        self.spell_codes_out_path = os.path.join(self.doc.exp_dir, 'Spells', 'spell_codes.json')
        with open(self.spell_codes_out_path, encoding='utf-8', mode='r') as f:
            self.spell_codes = json.load(f)
        return

    def produce(self):
        fn = self.doc.get_path_2da('LISTSPLL.2DA')
        if fn:
            listspells = common.parse_2da_file(fn, make_key_int=1)
            for spell_index, columns in listspells.items():
                spell_file = columns[-1]
                f = (r for r in self.spells if isinstance(r, dict) and r["SpellFile"] == spell_file)
                rec = next(f, None)
                if rec: continue
                rec = {
                    "SpellRef": -1,
                    "SpellFile": spell_file,
                    "SpellIndex": spell_index,
                    "SpellName": None,
                    "SpellCode": None,
                    "SpellCode2": None
                }
                self.spells.append(rec)

        spell_ids = self.doc.ids.get('SPELL.IDS')
        fn = self.doc.get_path_2da('SPELDESC.2DA')
        spell_desc = common.parse_2da_file(fn, make_key_int=0)
        if spell_desc:
            for rec in self.spells:
                spell_file = rec["SpellFile"]
                spell_desc_rec = spell_desc.get(spell_file)
                if spell_desc_rec:
                    spell_ref = spell_desc_rec[-1]
                    rec["SpellRef"] = spell_ref

                if ((spell_name_rec := self.src.get(spell_file)) and (spell_name := spell_name_rec.get("name"))):
                    rec["SpellName"] = spell_name

        if spell_ids:
            for ref, code in spell_ids.items():
                if next((r for r in self.spell_codes if r["ref"] == ref), None) is None:
                    self.spell_codes.append({"ref": ref, "code": code, "name": None})

            for rec in self.spells:
                spell_code = rec["SpellCode"]
                if spell_code: continue

                spell_name = str(rec["SpellName"])
                if not spell_name: continue
                #if spell_name == "Inflict Critical Wounds": breakpoint()

                spell_file = rec["SpellFile"]
                #if spell_file == 'SPPR102': breakpoint()

                spell_name_u = spell_name.upper()
                spl = spell_name_u.split(' ')
                keyword = self._fix_keyword(spl[0])
                p = f'_{keyword}'
                f = [(k, v) for k, v in spell_ids.items() if v and p in str(v)]
                found = False
                i = 0
                while (f and not found):
                    found = False
                    if len(f) == 1:
                        found = True
                    else:                
                        if len(spl) == 1 + i:
                            found = True
                        else:
                            keyword = self._fix_keyword(spl[1 + i])
                            f2 = [(k, v) for k, v in f if f'_{keyword}' in v]
                            f = f2
                            i += 1

                if found:
                    f = sorted(f, key=lambda t: len(t[1]), reverse=False)
                    rec["SpellRef"] = f[0][0]
                    rec["SpellCode"] = f[0][1]
                    if len(f) > 1:
                        #rec["SpellRef"] = f[0][0]
                        rec["SpellCode2"] = f[1][1]
                    #if len(f) > 2: breakpoint()
                    print(f'spell_name: {spell_name}, codes: {f}')
                    self.assign_spell_code(f, rec)
                
        return

    def _fix_keyword(self, keyword):
        keyword = keyword.replace("'", '')
        if keyword == 'I': keyword = '1'
        elif keyword == 'II': keyword = '2'
        elif keyword == 'III': keyword = '3'
        elif keyword == 'III': keyword = '3'
        elif keyword == 'IV': keyword = '4'
        elif keyword == 'V': keyword = '5'
        elif keyword == 'VI': keyword = '6'
        elif keyword == 'VII': keyword = '7'
        elif keyword == 'VIII': keyword = '8'
        elif keyword == 'IX': keyword = '9'

        elif keyword.lower() == 'inflict': keyword = 'CAUSE'
        return keyword

    def _fix_keyword_back(self, keyword):
        if keyword == 'CAUSE': keyword = 'INFLICT'
        return keyword

    def save(self):
        self.save_spell_codes()
        self.lines.clear()
        for rec in self.spells:
            self.writeline(f'{rec["SpellIndex"]}\t{rec["SpellFile"]}\t{rec["SpellName"]}\t{rec["SpellRef"]}\t{rec["SpellCode"]}\t{rec["SpellCode2"]}')
        return super().save()

    def parse_spells(self):
        for line in self.lines:
            if not line: continue
            tabbed = line.split('\t')
            SpellCode = tabbed[4].replace('\n', '')
            if SpellCode == 'None': SpellCode = None
            SpellCode2 = tabbed[5].replace('\n', '')
            if SpellCode2 == 'None': SpellCode2 = None
            rec = {
                "SpellRef": tabbed[3],
                "SpellFile": tabbed[1],
                "SpellIndex": tabbed[0],
                "SpellName": tabbed[2],
                "SpellCode": SpellCode,
                "SpellCode2": SpellCode2,
            }
            self.spells.append(rec)
        return

    def assign_spell_code(self, codes, spell_rec):
        spell_name0 =  spell_rec["SpellName"]
        spell_name = spell_name0.upper().replace("'", '')
        # ensure that codes and spell coincide exept first part: WIZARD_ACID_FOG=ACID FOG and 'ANIMATE DEAD' != 'WIZARD_ANIMATE_DEAD_LICH'
        spl = spell_name.split(' ')
        codes2 = []
        for ref, code in codes:
            csplitted = code.split('_')
            coincide = True
            j = 0
            for i, c in enumerate(csplitted):
                if i == 0: 
                    continue
                if len(spl) <= j:
                    coincide = False
                    break
                spl_val = spl[j]
                spl_val = self._fix_keyword(spl[j])
                cc = self._fix_keyword(c)
                if spl_val != cc:
                    coincide = False
                    break
                j += 1

            if coincide:
                codes2.append((ref, code))

        if not codes2:
            return

        for ref, code in codes2:
            found = [(r, i) for i, r in enumerate(self.spell_codes) if r["ref"] == ref]
            if not found:
                self.spell_codes.append({"ref": ref, "code": code, "name": spell_name})
            else:
                if len(found) > 1:
                    breakpoint()
                    print('')
                else:
                    if found[0][0]["name"] != spell_name:
                        self.spell_codes[found[0][1]]["name"] = spell_name0
                        #found[0]["name"] != spell_name
                        #breakpoint()
                        #print('')
        return

    def save_spell_codes(self):
        with open(self.spell_codes_out_path, 'w') as f:
            json.dump(self.spell_codes, f, indent=4)
        return

    def get_spell_name(self, spell_code: str):
        rec = next((rec for rec in self.spell_codes if rec["code"] == spell_code), None)
        if rec:
            return rec["name"]
        return