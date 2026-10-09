import vtracer
import os

configs = [
    {"name": "speckle2", "filter_speckle": 2, "length_threshold": 3.0},
    {"name": "speckle1", "filter_speckle": 1, "length_threshold": 2.5},
    {"name": "speckle4", "filter_speckle": 4, "length_threshold": 4.0},
]

for cfg in configs:
    out = f"scripts/trace_{cfg['name']}.svg"
    vtracer.convert_image_to_svg_py(
        'public/art/landscape-art.png',
        out,
        colormode='binary',
        mode='spline',
        filter_speckle=cfg['filter_speckle'],
        color_precision=7,
        layer_difference=12,
        corner_threshold=60,
        length_threshold=cfg['length_threshold'],
        max_iterations=10,
        splice_threshold=45,
        path_precision=2
    )
    print(f"{cfg['name']}: size = {os.path.getsize(out)} bytes")
