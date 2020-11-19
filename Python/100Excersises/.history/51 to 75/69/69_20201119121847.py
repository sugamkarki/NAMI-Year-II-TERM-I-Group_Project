import requests

sugam = requests.get("http://www.pythonhow.com")
print(sugam.text[:100])
