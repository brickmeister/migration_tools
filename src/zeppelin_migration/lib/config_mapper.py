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
                                  '%md'      : '%md'}