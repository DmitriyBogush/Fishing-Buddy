import re
import overpass
import json
from pypdf import PdfReader

lakes = PdfReader("regs.pdf")

# Check number of pages should be 152 for 2024-2025
# print(len(lakes.pages))
lakestr = ""

# Extract the regulations from all pages about lakes 79-100
for i in range(85,86):
    lakestr += lakes.pages[i].extract_text()


# Extract all of the lake names using regex 
res = re.findall(r'\w*\W*[ ]LAKE\s\w*|(?<=\n)LAKE\s\w*', lakestr)

# Convert to lover case and remove commas and extra space at end 
# for lake in res:
#     lakes.append(lake.lower().replace(',','').title().rstrip())

# Get the coordinates of a lake using overpass API 
api = overpass.API()

# What are we looking for 
lakescoord = []

# Query Overpass API KML Format  
# query = """<osm-script output="json" output-config="" timeout="25">
#   <union into="_">
#     <query into="_" type="way">
#       <has-kv k="natural" modv="" v="water"/>
#       <has-kv k="name" modv="" v="{lookingFor}"/>
#       <bbox-query s="45.460130637921" w="-125.15625" n="49.095452162535" e="-116.6748046875"/>
#     </query>
#     <query into="_" type="relation">
#       <has-kv k="natural" modv="" v="water"/>
#       <has-kv k="name" modv="" v="{lookingFor}"/>
#       <bbox-query s="45.460130637921" w="-125.15625" n="49.095452162535" e="-116.6748046875"/>
#     </query>
#   </union>
#   <print e="" from="_" geometry="center" ids="yes" limit="" mode="body" n="" order="id" s="" w=""/>
# </osm-script>""".format(lookingFor=lake)

# # Find certain lakes 
# for lake in lakes:
#   query = """
#   (
#     way["natural"="water"]["name"="{LookingFor}"](45.460130637921,125.15625,49.095452162535,-116.6748046875);
#     relation["natural"="water"]["name"="{LookingFor}"](45.460130637921,125.15625,49.095452162535,-116.6748046875);
#   );out center;
#   """.format(LookingFor=lake)

# Find all lakes 
query = """
(
  way["natural"="water"]["name"~"Lake"](45.460130637921,125.15625,49.095452162535,-116.6748046875);
  relation["natural"="water"]["name"~"Lake"](45.460130637921,125.15625,49.095452162535,-116.6748046875);
);out center;
"""

# Query the api 
# CSV Format
coord = api.get(query, responseformat="csv(name,::lon,::lat)")
# JSON Format 
# coord = api.get(query, responseformat="json")


# Extract the coordinates print if we didnt find the lake 
#   if len(coord) == 1:
#     print("Did not find", lake)
#     # Try again with lake name reversed FOLLOWING CODE IS UGLY FIX LATER
#     lakefirst = ' '.join(lake.split()[::-1])
#     query = """
#     (
#       way["natural"="water"]["name"="{LookingFor}"](45.460130637921,125.15625,49.095452162535,-116.6748046875);
#       relation["natural"="water"]["name"="{LookingFor}"](45.460130637921,125.15625,49.095452162535,-116.6748046875);
#     );out center;
#     """.format(LookingFor=lakefirst)

#     # Query the api 
#     coord = api.get(query, responseformat="csv(name,::lon,::lat)")

#     # Extract the coordinates print if we didnt find the lake 
#     if len(coord) == 1:
#       print("Did not find", lakefirst)
#     else:  
#       lakescoord += [coord[1]]
#   else:  
#     lakescoord += [coord[1]]

# print(lakescoord)

# Remove duplicate blanks 
coord[:] = [x for x in coord if x[1]]
del coord[0]

# Convert the lon and lat to ints 
for lake in coord:
  lake[1] = float(lake[1])
  lake[2] = float(lake[2])

# Store all of the lakes in a json for ease of use 
with open("lakes.json", 'w') as f:
  json.dump(coord, f, indent=2)
