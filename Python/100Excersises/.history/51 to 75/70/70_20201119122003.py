import requests
resto = requests.get("http://www.pythonhow.com/data/universe.txt")
text = resto.text
print(text)