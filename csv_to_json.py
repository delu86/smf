import pandas as pd
import json 

def  convert(filename):
    csv = pd.read_csv(filename,delimiter=";")
    keys = csv.columns
    values = csv.values
    fields = [dict(
                    list(
                        zip(keys,values[i]
                        )
                            )
                                )   for i in range(len(values))]
    return fields

fields =  convert("test.csv")
to_json = json.dumps(fields)
json_file = open('counter_data.json','w')
json_file.write(to_json)