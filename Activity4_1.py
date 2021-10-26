import requests, json
import urllib3
urllib3.disable_warnings()

url = "https://api.covid19tracking.narrativa.com/api/countries"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

print("LIST OF COUNTRIES")
print("=================")
for elem in data["countries"]:
    print(elem["name"])