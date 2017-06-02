import requests


url = "http://127.0.0.1:8001/Application/"
r = requests.post(url, data = {"value": "This is the request."})
if r.status_code == 200:
	print r.text