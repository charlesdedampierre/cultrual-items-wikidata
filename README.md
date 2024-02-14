# Database of Works in Wikidata

Pipeline:

1) Extract all works that are instance of sub-instance of work of art (Q838948) (extraction/extract_seed.py)
2) Extract related meta-data (extraction/extract_raw.py)
3) Insert the data into a SQL Database (data_pipeline.ipynb)

Data related to infrastructures and archaeological sites have been extracted buit not their meta-data. They are available as a json in the OST Forum.

## Content

The main table is SubjectLabel that contains all the piece of works in Wikidata. A table if made of a wikidata identifier, the label and often linked to another wikidata property.

In this table, the count_all means that the instance (for instance 'Hitsugi no Chaika') has 6 different instance. An instance means the type of work it is. In order to see the different instances, please go to the table subject_instance:

You will find this result:

subject     subjectLabel        instance
Q10855446 Hitsugi no Chaika Q220898
Q10855446 Hitsugi no Chaika Q747381
Q10855446 Hitsugi no Chaika Q1667921
Q10855446 Hitsugi no Chaika Q2635894
Q10855446 Hitsugi no Chaika Q21198342
Q10855446 Hitsugi no Chaika Q63952888

In order to access the instance name, please go to the table instanceLabel. For instance, Q220898 means 'original video animation'

## Access the data with python

In order to read the table using python, here is an example:

```python

import sqlite3
import pandas as pd

conn = sqlite3.connect('works.db')

# Chose a table to extract
table_name = 'SubjectLabel'

# Load the table as a pandas DataFrame
df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

```

### ntities that are in the database

- Time period (P2348)
- Inception (P571)
- culture (P2596)
- architectural style (P149)
- architect (P84)
- founded by (P112)
- creator (P170)
- genre (P136)
- movement (P135)

### Location Entities

- country (P17)
- located in the administrative territorial entity (P131)

## Count Entities in Wikidata (02/05/2024) OPTIONAL

Count is from item and sub-items (wdt:P279*)

- 'architectural structure' (Q811979): 5,133,991 (include gardens) - (inception before 1900)
- 'work of art' (Q838948): 3,629,404 (include sculptures, paintings etc)
- 'tool' (Q39546): 9,297,105 (include scientific instruments)
- 'archaeological site' (Q839954): 248,550
- 'infrastructure' (Q121359): 1,400,027

'human'(Q5): 10,632,484
