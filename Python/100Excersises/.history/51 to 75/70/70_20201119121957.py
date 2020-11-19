import requests
resto = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
print(text)