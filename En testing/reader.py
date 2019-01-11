import requests
url = "https://google.com"
r = requests.get(url)
r.text
print(r)
