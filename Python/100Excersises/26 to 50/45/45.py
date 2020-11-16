# no.c
for i in range(97,123):
    myFile=open(str(chr(i))+'.txt','w')
    myFile.write(chr(i))