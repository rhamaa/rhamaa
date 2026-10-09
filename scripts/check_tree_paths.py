import re

with open('scripts/test_trace_binary.svg', 'r') as f:
    content = f.read()

# Let's search for paths near x=650..750, y=200..350
transforms = re.findall(r'<path[^>]*d="([^"]*)"[^>]*transform="translate\(([^)]*)\)"', content)
print(f"Total paths in test_trace_binary.svg: {len(transforms)}")

for d, t in transforms:
    parts = [float(x.strip()) for x in t.split(',')]
    if 650 <= parts[0] <= 750:
        print(f"Path at translate({t}): length of d = {len(d)}")
        # Check if it has 118 or straight lines
        if '118' in d or '330' in d:
            print("  Contains 118 or 330!")
        else:
            print("  Does NOT contain 118 or 330 cut!")
