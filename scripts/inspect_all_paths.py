import re

with open('scripts/trace_speckle2.svg', 'r') as f:
    content = f.read()

paths = re.findall(r'<path[^>]*d="([^"]*)"[^>]*transform="translate\(([^)]*)\)"', content)
print(f"Total paths: {len(paths)}")

for idx, (d, t) in enumerate(paths):
    x, y = [float(v.strip()) for v in t.split(',')]
    print(f"Path {idx}: at ({x:.1f}, {y:.1f}) len={len(d)}")
