letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for i in range(len(letters)-1):
    if(i%2!=0):
        continue;
    print(letters[i])