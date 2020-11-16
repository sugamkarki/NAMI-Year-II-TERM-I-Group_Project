myFile=open("alphabets.txt",'w')
for i in range(97, 123):
    myFile.write(chr(i))
    myFile.write('\n')
