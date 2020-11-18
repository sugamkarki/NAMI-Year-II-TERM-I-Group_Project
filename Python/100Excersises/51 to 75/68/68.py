d = dict(weather = "clima", earth = "terra", rain = "chuva") 
userWord=input("enter the word\n")
wordExist=False
for key,value in d.items():
    if(str(key).lower()==userWord.lower()):
        print(value)
        wordExist=True
        break
if(wordExist==False):
    print("the word doesn't exist")    