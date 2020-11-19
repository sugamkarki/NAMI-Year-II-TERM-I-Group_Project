# str="hi i m adon"
# 
myFile=open("c.txt","r")
countriesRaw=myFile.read()
countriesNeat=''
countriesRaw= countriesRaw.split(" ")
for country in countriesRaw:
    # print(country)
    if(len(country)>1):
        countriesNeat =countriesNeat+'\n'+