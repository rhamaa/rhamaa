import re

with open('scripts/test_trace_binary.svg', 'r') as f:
    content = f.read()

# Sun center was at x=547, y=156
# Let's check transforms near 547, 156
transforms = re.findall(r'transform="translate\(([^)]*)\)"', content)
print("Transforms near sun (x: 480-600, y: 100-200):")
for t in transforms:
    parts = [float(x.strip()) for x in t.split(',')]
    if 480 <= parts[0] <= 600 and 100 <= parts[1] <= 200:
        print(" ", t)
