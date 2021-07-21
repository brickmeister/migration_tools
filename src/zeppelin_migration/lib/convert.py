from typing import Dict, List
from .config_mapper import config_mapper

def convert(_json : List[Dict],
            _language : str) -> List[str]:
    """
    Convert zeppelin json to databricks .py files
    """

    # Create a string array
    _string = []
        
    # Write databricks title
    _string.append('# Databricks notebook source\n')
    # loop for all cells
    for _cell in _json:
        try:
            _string.append(f"# DBTITLE 1,{_cell['title']}\n")
        except:
            pass
        
        _string.append('# COMMAND ----------\n')
        _string.append('\n')

        try:
            _str = _cell['text'].split('\n')

            # deal with new line white space
            if len(_str) > 1:
                _index = next(i for i,v in enumerate(_str) if v != '')
                # add in the white space in the string to preserve structure
                _string.extend(['' for a in range(_index)])
                _str = _str[_index:]

            # Add the magic cell command
            if _str[0].lower() in config_mapper.keys():
                _string.append(f'# MAGIC {config_mapper[_str[0]]}\n')
                _str = _str[1:]
            else:
                # use the default language if not specified
                _string.append(f'# MAGIC {_language}\n')
                _string.append('# MAGIC\n')

            for _cmd in _str:
                _string.append(f"# MAGIC {_cmd}\n")
            _string.append('\n')

        except Exception as err:
            raise ValueError(err)
    return _string