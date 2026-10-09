with open('src/components/landscape/Meadow.astro', 'r') as f:
    meadow = f.read()

import re
transforms = re.findall(r'transform="([^"]*)"', meadow)
print("Meadow transforms count:", len(transforms))
for t in transforms:
    if '722' in t or '330' in t:
        print("Transform in meadow:", t)
