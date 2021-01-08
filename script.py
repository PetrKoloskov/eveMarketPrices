#!/usr/bin/env python

import yaml
import pandas as pd

with open("typeIDs.yaml", 'r', encoding="utf-8") as stream:
    s = yaml.safe_load(stream)
colNames = [ 'NAME']
filteredDict = {}
for key, value in s.items():
    filteredDict[str(key)] = value['name']['en']
    print(str(key), value['name']['en'])
df = pd.DataFrame.from_dict(filteredDict, orient="index",columns=colNames)
df.to_excel("sample.xlsx")


