import requests, json
import urllib3
urllib3.disable_warnings()

url = "https://api.covid19tracking.narrativa.com/api/countries/spain/regions"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

regions =[]
print("SPAIN REGIONS")
print("================")
for elem in data["countries"][0]["spain"]:
    regions[elem] = elem["name"]

regions.sort

for elem in region:
    print(regions[elem])