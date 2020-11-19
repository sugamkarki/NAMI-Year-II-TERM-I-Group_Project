import requests
resto = requests.get("http://www.pythonhow.com/data/universe.txt")
text = rest.text
print(text)