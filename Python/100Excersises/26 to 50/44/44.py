myFile=open("three.txt","w")
for i in range(97,121):
    myFile.write(str(chr(i))+str(chr(i+1))+str(chr(i+2))+"\n")
    i+=3