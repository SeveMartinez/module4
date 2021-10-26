import requests, json, locale, urllib3

from requests.api import get

locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')

def getCountryName():
    return spain_data["name"]

def getConfirmed():
    return locale.format_string("%d", spain_data["today_confirmed"], True)

def getTodayConfirmed():
    return locale.format_string("%d", spain_data["today_new_confirmed", True])

def getDeaths():
    return locale.format_string("%d", spain_data["today_deaths", True])

def getTodayDeaths():
    return locale.format_string("%d", spain_data["today_new_deaths", True])

urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/2021-1015/country/spain"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

print("Global Data")
print("-----------")
print("Country", "Confirmed", "Today Confirmed", "Deaths", "Today Deaths", sep="\t")
print(getCountryName(), getConfirmed(), getTodayConfirmed(), getDeaths(), getTodayDeaths(), sep="\t")

