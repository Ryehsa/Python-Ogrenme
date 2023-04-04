import requests
import json

url = "https://api.covid19api.com/summary"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

result = json.loads(response.text)


print(result["Global"])


"""""
r = requests.get("https://apiogrenme.free.beeceptor.com/users", stream=True)

print(r.elapsed)

with open("Result.txt", "wb") as fd:
    fd.write(r.content)
    fd.close()


print(r.status_code)
print(r.content)
print(r.headers)
headers = r.headers.decode("utf-8")

with open("ResultHeaders.txt", "wb") as fd:
    fd.write(headers)
    fd.close()
""" ""
