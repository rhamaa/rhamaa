import os
import re

landscape_dir = 'src/components/landscape'
files = [f for f in os.listdir(landscape_dir) if f.endswith('.astro')]

total_paths = 0
for f in files:
    content = open(os.path.join(landscape_dir, f), 'r', encoding='utf-8').read()
    paths = re.findall(r'<path[^>]*d="([^"]*)"[^>]*transform="([^"]*)"', content)
    total_paths += len(paths)
    print(f"{f:22s}: {len(paths)} paths, size={len(content)} bytes")

print(f"Total paths across all files: {total_paths}")
