from typing import Dict

"""
This code creates the mapper for 
zeppelin interpreters to databricks interpreters
"""

# valid language conversions from Zeppelin
config_mapper : Dict[str, str] = {'%pyspark' : '%python',
                                  '%sh'      : '%sh',
                                  '%spark'   : '%scala',
                                  '%sql'     : '%sql',
                                  '%md'      : '%md',
                                  '%sparkpy3.sql' : '%sql',
                                  'scala' : '%scala',
                                  'python' : '%python',
                                  'sql' : '%sql'}



# valid extensions
extension_mapper : Dict[str, str] = {'%python' : '.py',
                                     '%scala' : '.scala',
                                     '%sql' : '.sql'}

# comment mapper
comment_mapper : Dict[str,str] = {'%python' : '#',
                                  '%sql' : '--',
                                  '%scala' : '//'}