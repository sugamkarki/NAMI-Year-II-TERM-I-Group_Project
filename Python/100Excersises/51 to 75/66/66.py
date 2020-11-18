d = dict(weather = "clima", earth = "terra", rain = "chuva") 
userInput=input("enter a word to be translated: \n")
for key,value in d.items():
    if(key==userInput):
        print(value)
