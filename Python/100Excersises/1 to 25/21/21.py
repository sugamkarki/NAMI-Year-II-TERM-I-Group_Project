d = {"a": 1, "b": 2, "c": 3}
newDict={}
for (key,value) in d.items():
    if(value<=1):
        newDict[key]=value
# for key,values in d.items():
#     if values>1:
#         d.pop[key]
print(newDict)
