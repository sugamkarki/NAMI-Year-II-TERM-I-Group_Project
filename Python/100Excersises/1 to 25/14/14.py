a = ["1", 1, "1", 2]
# for item in a:
a.reverse()
for i in a:
    occurance=0
    for j in a:
        if (i==j):
            occurance+=1
    if(occurance>1):
        a.remove(i)
a.reverse()
print(a)        