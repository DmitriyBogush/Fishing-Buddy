import re
import overpass
import geojson
from pypdf import PdfReader

### Extract River Names and Regulations from WDFW Regulations PDF###

rivers = PdfReader("regs.pdf")

# Check number of pages should be 152 for 2024-2025
# print(len(lakes.pages))
riversStr = ""

# Extract the text from all pages about lakes 79-100
for i in range(85,86):
    riversStrtr += rivers.pages[i].extract_text()


# Extract all of the lake names using regex 
res = re.findall(r'\w*\W*[ ]LAKE\s\w*|(?<=\n)LAKE\s\w*', riversStr)
rivers = []

# Convert to lover case and remove commas and extra space at end 
for river in res:
    rivers.append(river.lower().replace(',','').title().rstrip())


### Get Coordinates of all rivers in Washington State through Overpass ###
