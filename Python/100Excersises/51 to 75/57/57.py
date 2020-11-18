import json
from pprint import pprint
myFile=open("company.json",'r')
pprint(json.load(myFile))