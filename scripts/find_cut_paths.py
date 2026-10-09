import re

with open('public/art/landscape-full-pure-vector.svg', 'r') as f:
    content = f.read()

ink_match = re.search(r'<g class="svg-ink-layer"[^>]*>([\s\S]*?)</g>', content)
if ink_match:
    paths = re.findall(r'<path[^>]*d="([^"]*)"[^>]*transform="([^"]*)"', ink_match.group(1))
    print(f"Found {len(paths)} paths with transform")
    for idx, (d, t) in enumerate(paths):
        # find if d has long straight segments or cuts
        if '118' in d or '330' in d or '115' in d:
            print(f"Path {idx} at {t} contains coordinate 115/118")
