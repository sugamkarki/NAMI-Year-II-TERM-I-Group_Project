# myFile=open('check.txt','r')
# print(myFile.read())
lettersList=[]
for i in range(97,123):
    myFile=open("letters/"+str(chr(i))+".txt",'r')
    lettersList.append(myFile.read().strip('\n'))

print(lettersList)    