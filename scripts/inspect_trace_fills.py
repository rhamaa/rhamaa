import xml.etree.ElementTree as ET
from collections import Counter

tree = ET.parse('public/art/test_color_trace.svg')
root = tree.getroot()
print("Root tag:", root.tag, "attrib:", root.attrib)

fills = Counter()
for elem in root.iter():
    if 'fill' in elem.attrib:
        fills[elem.attrib['fill']] += 1

print("Top fills in test_color_trace.svg:")
for fill, count in fills.most_common(20):
    print(f"  {fill}: {count}")
