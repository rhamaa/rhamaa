import re

with open('scripts/trace_speckle2.svg', 'r') as f:
    content = f.read()

paths = re.findall(r'<path[^>]*d="([^"]*)"[^>]*transform="translate\(([^)]*)\)"', content)

for idx, (d, t) in enumerate(paths):
    if len(d) > 10000:
        print(f"Main path {idx} at {t}: len={len(d)}")
        # Check coordinates in d
        # Find min and max x, y offsets
        nums = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', d)]
        print(f"Total numbers in path {idx}: {len(nums)}")
