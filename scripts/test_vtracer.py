import vtracer
import os

print("Testing vtracer...")
# Let's test binary/monochrome tracing on landscape-art.png
# Mode can be 'spline' or 'polygon' or 'none'
# colormode can be 'color' or 'binary'
vtracer.convert_image_to_svg_py(
    'public/art/landscape-art.png',
    'scripts/test_trace_binary.svg',
    colormode='binary',
    mode='spline',
    filter_speckle=4,
    color_precision=6,
    layer_difference=16,
    corner_threshold=60,
    length_threshold=4.0,
    max_iterations=10,
    splice_threshold=45,
    path_precision=2
)

print("Generated scripts/test_trace_binary.svg, size:", os.path.getsize('scripts/test_trace_binary.svg'))
