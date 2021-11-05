import json
from typing import Dict

def load_json(_file : str) -> Dict:
    """
    Load json file
    """

    with open(_file, encoding = 'utf-8-sig') as f:
        try:
            _json = json.load(f)
            _json_text = _json['paragraphs']
            _notebook_name = _json['name']
            try:
                _default_lang = _json['config']['defaultLang']
            except:
                _default_lang = ""

            return {'json' : _json_text,
                    'name' : _json['name'],
                    'lang' : _default_lang}
        except Exception as err:
            raise ValueError(f"Failed to load {_file} with {err}")


