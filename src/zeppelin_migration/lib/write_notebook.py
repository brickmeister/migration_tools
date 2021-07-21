from typing import List

def write_notebook(_out : List[str],
                   _new_file : str) -> None:
    """
    Write Databricks Notebook
    """

    with open(_new_file, 'w') as w:
        try:
            w.write(''.join(_out))
        except Exception as err:
            raise ValueError(f"Failed to write {_new_file}")