import os, sys, glob
import argparse
from typing import List, Dict
from lib.convert import convert
from lib.load_json import load_json
from lib.write_notebook import write_notebook
from lib.config_mapper import config_mapper, extension_mapper, comment_mapper

def main(_files : List[str], 
         out_dir : str = None) -> None:
    """
    Main insertion function
    """

    # keep stats on files
    _processed_files = []
    _errored_files = []
    
    for _file in _files:
        """
        Loop for all found files
        """

        try:
            # load the notebook json file
            _json_load = load_json(_file)
            _json = _json_load['json']
            _name = _json_load['name']

            try:
                _lang = config_mapper['%'+_json_load['lang']]
            except:
                _lang = _language

            # convert the notebook
            _convert = convert(_json, _lang)
            _notebook = _convert['text']
            _user = _convert['user']
            _note_id = _convert['note_id']

            try:
                out_ext : str = extension_mapper[_lang]
            except Exception as err:
                raise ValueError(f"Failed to find extention for {_lang}, err : {err}")

            # set the new output file
            if out_dir == '':
                _new_file : str = _file.replace('.json', f"-magicked{out_ext}")
                _dir = '/'.join(_new_file.split("/")[:-1])
            else:
                # if output directory is specified, use format
                #   out_directory/user/notebook.py
                _dir : str = '/'.join([out_dir, _user])

                # check if path exists, create it if it doesn't
                if not os.path.isdir(_dir):
                    os.makedirs(_dir)
                
                _new_file : str = '/'.join([_dir,
                                            f"{_name}-magicked{out_ext}"])

                if _name == "":
                    _new_file : str = '/'.join([_dir,
                                                 f"{_note_id}-magicked{out_ext}"])
                else:
                    _new_file : str = '/'.join([_dir,
                                                f"{_name}-magicked{out_ext}"])

            # check if the file already exists
            if os.path.isfile(_new_file):
                _new_file : str = '/'.join([_dir,
                                            f"{_name}-{_note_id}-magicked{out_ext}"])

            # write out results
            write_notebook(_notebook, _new_file)

            # add file to written files
            _processed_files.append(_file)

        except Exception as err:
            _errored_files.append((_file, err))

    print(f"Processed Files : {_processed_files}\n\nErrored Files : {_errored_files}\n")

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
    if args.out_dir:
        main(_files, args.out_dir)
    else:
        main(_files, '')