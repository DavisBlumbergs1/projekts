import requests

url = "https://nodarbibas.rtu.lv/"
info = requests.get(url)
print(info)