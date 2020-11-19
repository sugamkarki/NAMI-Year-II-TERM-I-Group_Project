import requests

rp = requests.get("http://www.pythonhow.com")
print(rp.text[:100])