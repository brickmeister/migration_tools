import json
from typing import Dict

def load_json(_file : str) -> Dict:
    """
    Load json file
    """

    with open(_file) as f:
        try:
            _json = json.load(f)['paragraphs']
            return _json
        except Exception as err:
            raise ValueError(f"Failed to load {_file}")


