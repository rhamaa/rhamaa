import cairo
from svgelements import SVG, Move, Line, QuadraticBezier, CubicBezier, Close, Path

def render_svg_to_png(svg_path, out_png):
    svg = SVG.parse(svg_path)
    width = 1024
    height = 409
    
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    
    # Fill background with cream
    ctx.set_source_rgb(242/255, 238/255, 230/255)
    ctx.paint()
    
    # Draw paths with ink color #172724
    ctx.set_source_rgb(0x17/255, 0x27/255, 0x24/255)
    
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
            
    surface.write_to_png(out_png)
    print(f"Rendered {out_png}")

render_svg_to_png('scripts/trace_speckle2.svg', 'scripts/rendered_trace_speckle2.png')
render_svg_to_png('scripts/trace_speckle1.svg', 'scripts/rendered_trace_speckle1.png')
