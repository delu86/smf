import json


def scan(element):
    if(element.get("type")):
        return element["Name"]+" "+" is  a subsection"
    else :
        return element["Name"]+" "+" is  an element"


SUFFIX = "./smf"

header_file = open(SUFFIX+"030/header.json")
header_obj = json.load(header_file)
names = list(map(scan ,header_obj))
print(names)





