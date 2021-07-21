from typing import Dict

# valid language conversions from Zeppelin
config_mapper : Dict[str, str] = {'%pyspark' : '%python',
                                  '%sh'      : '%sh',
                                  '%spark'   : '%scala',
                                  '%sql'     : '%sql',
                                  '%md'      : '%md'}