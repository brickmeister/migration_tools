# Introduction
This repo contains tools for migrating from various platforms to Databricks.
- [Introduction](#introduction)
- [Supported Platforms](#supported-platforms)
- [Qubole](#qubole)
  - [Zeppelin Notebook Migration](#zeppelin-notebook-migration)
    - [Convert a single json file](#convert-a-single-json-file)
    - [Convert json files in a directory](#convert-json-files-in-a-directory)
# Supported Platforms
|Platform|Status|
|--------|------|
|Qubole|33%|

# Qubole
Migrating over Qubole workloads consists of several steps outlined below.

|Feature|Description|Link|
|-------|-----------|----|
|Zeppelin Notebooks|Notebooks used for day to day workloads | [Zeppelin Notebook Migration](#zeppelin-notebook-migration)|
|Airflow|Scheduler used to orchestrate workloads|
|Hive Metastore|Database metadata needed for accessing data|

## Zeppelin Notebook Migration
Export your zeppelin notebooks as *json* format and download them to a folder.

Enter the directory : `src/zeppelin_migration/`

|Parameter|Description|
|---------|-----------|
|--language|Default language of the zeppelin notebook : spark, pyspark, sql, dep|
|--file|Location of zeppelin json to convert|
|--directory|Location of zeppelin json directory to convert|

### Convert a single json file
Run the following command below to convert a single Zeppelin json file. The notebooks will be located in the same directory with a suffix of *--magicked.py*

`python3 zeppelin_converter.py --file <path of file> --language <language>`

### Convert json files in a directory
Run the following command below to json notebooks in a directory. The notebooks will be located in the same directory with a suffix of *--magicked.py*

`python3 zeppelin_converter.py --dir <directory> --language <language>`