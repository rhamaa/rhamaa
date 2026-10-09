import re

with open('scripts/test_trace_binary.svg', 'r') as f:
    content = f.read()

paths = re.findall(r'<path[^>]*>', content)
print("Paths count:", len(paths))
for p in paths[:5]:
    print(p[:150])
