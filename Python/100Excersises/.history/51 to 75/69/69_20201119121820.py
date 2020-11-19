import requests

rp = requests.get("http://www.pythonhow.com")
print(r.text[:100])