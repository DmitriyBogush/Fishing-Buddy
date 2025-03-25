import json 
from math import radians, cos, sin, asin, sqrt

# Calulate the distance between two points on earth
def haversine(long, lat, long1, lat1): 
  long, lat, long1, lat1 = map(radians, [long, lat, long1, lat1])
  difflon = long1 - long
  difflat = lat1  - lat
  a = sin(difflat/2)**2+cos(lat) * cos(lat1) * sin(difflon/2)**2
  c = 2 * asin(sqrt(a))
  return 6371 * c

# Open lakes coordinates json 
with open("lakes.json", 'r') as f: 
  lakes = json.load(f)

fishing = [-119.328858, 47.165648]

#Iterate through each lake and find the closest MIGHT NOT BE EFFICIENT FIX LATER 
closestLake = ''
closestDist = float('inf')
for lake in lakes: 
  dist = haversine(lake[1], lake[2], fishing[0], fishing[1])
  if dist < closestDist:
    closestDist = dist
    closestLake = lake[0]
    
print(closestLake)