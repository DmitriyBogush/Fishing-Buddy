import requests

water = "https://waterservices.usgs.gov/nwis/iv/?format=json&sites=12182500&siteStatus=all&parameterCd=00065"
site = "https://waterservices.usgs.gov/nwis/site/?format=rdb&bBox=-122.3464,48.4319,-122.3111,48.45555&siteStatus=all"

site_data = requests.get(site)
water_data = requests.get(water)


water_json = water_data.json()
site_rdb = site_data.content

print(water_json["value"]["timeSeries"][0]["values"][0]["value"][0]["value"])
print(site_rdb.decode("utf-8"))