import requests

url = "https://waterservices.usgs.gov/nwis/iv/?format=json&sites=12182500&siteStatus=all&parameterCd=00065"

data = requests.get(url)

data_json = data.json()
print(data_json["value"]["timeSeries"][0]["values"][0]["value"][0]["value"])