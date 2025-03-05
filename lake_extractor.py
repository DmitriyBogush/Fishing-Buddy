import re
import overpy
from pypdf import PdfReader


lakes = PdfReader("regs.pdf")

# Check number of pages should be 152 for 2024-2025
# print(len(lakes.pages))
lakestr = ""

# Extract the text from all pages about lakes 79-100
for i in range(85,86):
    lakestr += lakes.pages[i].extract_text()


# Extract all of the lake names using regex 
res = re.findall(r'\w*\W*[ ]LAKE\s\w*|(?<=\n)LAKE\s\w*', lakestr)

for lake in res:
    print(lake)

# Get the coordinates of a lake
api = overpy.Overpass()

# What are we looking for 
lake = "Banks Lake"

# Query Overpass API 
query = """<osm-script output="json" output-config="" timeout="25">
  <union into="_">
    <query into="_" type="way">
      <has-kv k="natural" modv="" v="water"/>
      <has-kv k="name" modv="" v="{lookingFor}"/>
      <bbox-query s="45.460130637921" w="-125.15625" n="49.095452162535" e="-116.6748046875"/>
    </query>
    <query into="_" type="relation">
      <has-kv k="natural" modv="" v="water"/>
      <has-kv k="name" modv="" v="{lookingFor}"/>
      <bbox-query s="45.460130637921" w="-125.15625" n="49.095452162535" e="-116.6748046875"/>
    </query>
  </union>
  <print e="" from="_" geometry="center" ids="yes" limit="" mode="body" n="" order="id" s="" w=""/>
</osm-script>""".format(lookingFor=lake)

coord = api.query(query)

# Extract the coordinates 
print(type(coord))