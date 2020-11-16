
myFile=open('alphabets.txt','w')

for i in range(97,123):
    myFile.write(str(chr(i))+str(chr(i+1))+'\n')
    i+=2
myFile.close()        