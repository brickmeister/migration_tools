from typing import Dict, List
from .config_mapper import config_mapper, comment_mapper

def convert(_json : List[Dict],
            _language : str) -> Dict[str, List[str]]:
    """
    Convert zeppelin json to databricks .py files
    """

    # Create a string array
    _string = []

    # Grab user credentials
    _user = ""

    # Grab the notebook id
    _note_id = ""

    # get the comment marker for the langauge
    _comment : str = comment_mapper[_language]
        
    # Write databricks title
    _string.append(f"{_comment} Databricks notebook source\n")

    # loop for all cells
    for _cell in _json:
        try:
            _string.append(f"{_comment} DBTITLE 1,{_cell['title']}\n")
        except:
            pass
        
        _string.append(f"{_comment} COMMAND ----------\n")
        _string.append('\n')

        if not _user:
            try:
                ## get the user email from the user object
                _user = _cell['user']
            except:
                pass

        if not _note_id:
            try:
                ## get the notebook id from the id object
                _note_id = _cell['id'].split("_")[-1]
            except:
                pass

        try:
            if 'text' in _cell:
                _str = _cell['text'].split('\n')

                # deal with new line white space
                if len(_str) > 1:
                    try:
                        _index = next(i for i,v in enumerate(_str) if v != '')
                    except:
                        _index = 0
                    # add in the white space in the string to preserve structure
                    _string.extend(['' for a in range(_index)])
                    _str = _str[_index:]

                # Add the magic cell command
                if _str[0].lower() in config_mapper.keys():
                    _string.append(f"{_comment} MAGIC {config_mapper[_str[0]]}\n")
                    _str = _str[1:]
                else:
                    # use the default language if not specified
                    _string.append(f"{_comment} MAGIC {_language}\n")
                    _string.append(f"{_comment} MAGIC\n")

                for _cmd in _str:
                    _string.append(f"{_comment} MAGIC {_cmd}\n")
                _string.append('\n')

        except Exception as err:
            raise ValueError(err)
    
    ## if we still don't have a user, label it as unknown
    if _user == "":
        _user = "unknown"

    return {'user' : _user, 
            'text' : _string,
            'note_id' : _note_id}