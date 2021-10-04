import os, sys
import argparse
from typing import List, Dict
from lib.convert import convert
from lib.load_json import load_json
from lib.write_notebook import write_notebook
from lib.config_mapper import config_mapper

def main(_files : List[str]) -> None:
    """
    Main insertion function
    """
    
    for _file in _files:
        """
        Loop for all found files
        """

        try:
            # load the notebook json file
            _json = load_json(_file)
            
            # set the new output file
            _new_file : str = _file.replace('.json', '-magicked.py')

            # convert the notebook
            _notebook = convert(_json, _language)

            # write out results
            write_notebook(_notebook, _new_file)

        except Exception as err:
            raise ValueError(str({"msg" : f"Failed to process {_file}",
                                  "err" : err}))

if __name__ == '__main__':
    """
    Execute from cmdline
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='Directory containing Zeppelin JSONs to convert to Databricks Notebooks')
    parser.add_argument('--file', help='Zeppelin JSON convert to a Databricks Notebook')
    parser.add_argument('--language', help='Default Zeppelin Notebook language (DEFAULT : spark)', default = 'spark')
    args = parser.parse_args()

    ## SETUP
    # check if using a directory or a file
    if args.dir:
        _files = os.listdir(args.dir)
        _files = ['/'.join([args.dir, _file]) for _file in _files if '.json' in _file]
    elif args.file:
        _files = [args.file]
    else:
        print("Missing valid zeppelin json. Couldn't find json files\n")
        parser.print_help()
        sys.exit(1)

    # set the default language
    try:
        _language = config_mapper['%'+args.language.lower()]
    except Exception as error:
        raise ValueError(f"Couldn't understand default language. This language is probably not supported")
    
    # Run the main insertion function
    main(_files)