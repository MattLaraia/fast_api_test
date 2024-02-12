import requests

url = "http://127.0.0.1:8000/tabs"

params = {
	'cigs':55
}

answer = requests.post(url, json = params)

print(answer.text)