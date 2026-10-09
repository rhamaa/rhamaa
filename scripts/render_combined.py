import cairo
import os
import re
from svgelements import SVG, Move, Line, QuadraticBezier, CubicBezier, Close, Path

landscape_dir = 'src/components/landscape'
# Render all natural terrain files
terrain_files = [
    'MountainLeft.astro', 'MountainRight.astro', 'MountainFarRight.astro',
    'HillsLeft.astro', 'ButteLeft.astro', 'Meadow.astro',
    'TreeOakShadow.astro', 'TreeTwinShadow.astro', 'TreePineShadow.astro',
    'TreeOak.astro', 'TreeTwin.astro', 'TreePine.astro'
]

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1024, 409)
ctx = cairo.Context(surface)
ctx.set_source_rgb(242/255, 238/255, 230/255)
ctx.paint()
ctx.set_source_rgb(0x17/255, 0x27/255, 0x24/255)

for f in terrain_files:
    content = open(os.path.join(landscape_dir, f), 'r', encoding='utf-8').read()
    svg_match = re.search(r'<svg[^>]*>([\s\S]*?)</svg>', content)
    if svg_match:
        svg_xml = f'<svg width="1024" height="409" xmlns="http://www.w3.org/2000/svg">{svg_match.group(1)}</svg>'
        svg = SVG.parse(svg_xml)
        for element in svg:
            if isinstance(element, Path):
                for seg in element:
                    if isinstance(seg, Move):
                        ctx.move_to(seg.end.x, seg.end.y)
                    elif isinstance(seg, Line):
                        ctx.line_to(seg.end.x, seg.end.y)
                    elif isinstance(seg, CubicBezier):
                        ctx.curve_to(seg.control1.x, seg.control1.y, seg.control2.x, seg.control2.y, seg.end.x, seg.end.y)
                    elif isinstance(seg, QuadraticBezier):
                        c1x = seg.start.x + 2/3 * (seg.control.x - seg.start.x)
                        c1y = seg.start.y + 2/3 * (seg.control.y - seg.start.y)
                        c2x = seg.end.x + 2/3 * (seg.control.x - seg.end.x)
                        c2y = seg.end.y + 2/3 * (seg.control.y - seg.end.y)
                        ctx.curve_to(c1x, c1y, c2x, c2y, seg.end.x, seg.end.y)
                    elif isinstance(seg, Close):
                        ctx.close_path()
                ctx.fill()

surface.write_to_png('scripts/rendered_combined_components.png')
print("Rendered scripts/rendered_combined_components.png")
