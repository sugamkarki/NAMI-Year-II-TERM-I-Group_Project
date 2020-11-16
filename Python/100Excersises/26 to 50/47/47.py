checkText = 'python'
lettersList = []
for i in range(97, 123):
    matched = False
    myFile = open("letters/"+str(chr(i))+'.txt', 'r')
    letter = (myFile.readline().strip('\n'))
    for letterCheck in checkText:
        if(letter == letterCheck):
            matched = True
            break
    if(matched):
        lettersList.append(letter)
print(lettersList)
