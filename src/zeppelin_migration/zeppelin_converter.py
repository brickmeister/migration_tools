import os, sys, glob
import argparse
from typing import List, Dict
from lib.convert import convert
from lib.load_json import load_json
from lib.write_notebook import write_notebook
from lib.config_mapper import config_mapper

def main(_files : List[str], 
         out_dir : str = None) -> None:
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

            # convert the notebook
            _convert = convert(_json, _language)
            _notebook = _convert['text']
            _user = _convert['user']

            # set the new output file
            if out_dir == '':
                _new_file : str = _file.replace('.json', '-magicked.py')
            else:
                # if output directory is specified, use format
                #   out_directory/user/notebook.py
                _dir : str = '/'.join([out_dir, _user])

                # check if path exists, create it if it doesn't
                if not os.path.isdir(_dir):
                    os.mkdir(_dir)
                
                _new_file : str = '/'.join([_dir, 
                                            _file.replace('.json', '-magicked.py').split("/")[-1]])

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
    parser.add_argument('--out_dir', help='Specify output directory for the converted notebooks', default = '')
    args = parser.parse_args()

    ## SETUP
    # check if using a directory or a file
    if args.dir:
        # _files = os.listdir(args.dir)
        _files = glob.glob(args.dir+'/**/*.json', recursive = True)
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
    main(_files, args.out_dir)