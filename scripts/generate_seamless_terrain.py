import cv2
import numpy as np
import vtracer
import re
import os

img = cv2.imread('public/art/landscape-art.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = gray.shape

# Threshold for ink (foreground lines)
# Background is ~240. Ink starts at <= 228
ink = np.zeros_like(gray)
ink[gray <= 228] = 255

# Mask out the sun
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
sun_mask = cv2.inRange(hsv, np.array([15, 60, 150]), np.array([40, 255, 255]))
ink[sun_mask > 0] = 0

# Mask out the sky circuits:
# 1. Left sky circuit: x in [0, 420], y in [0, 240] where lines/dots are in the sky
# 2. Right sky circuit: x in [600, 1024], y in [0, 160]
# Let's inspect connected components of ink to cleanly isolate sky circuit elements:
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(ink)

circuit_mask = np.zeros_like(gray)
organic_terrain_mask = np.zeros_like(gray)

for label in range(1, num_labels):
    x, y, bw, bh, area = stats[label]
    cx, cy = centroids[label]
    
    # Check if this component is sky circuit:
    # Sky circuits are either straight vertical/horizontal lines or dots in the sky
    is_left_circuit = (x < 420 and y < 240 and (x < 360 or y < 180) and (y + bh) < 260)
    is_right_circuit = (x > 620 and y < 140)
    
    # Check if it touches or is part of mountains:
    # Mountain contours start around y=130-180 and connect horizontally across the entire width
    if (is_left_circuit or is_right_circuit) and area < 400 and bh < 150:
        circuit_mask[labels == label] = 255
    else:
        organic_terrain_mask[labels == label] = 255

os.makedirs('public/art/seamless', exist_ok=True)
cv2.imwrite('public/art/seamless/terrain_organic.png', 255 - organic_terrain_mask)
cv2.imwrite('public/art/seamless/circuits.png', 255 - circuit_mask)

print("Organic terrain pixels:", cv2.countNonZero(organic_terrain_mask))
print("Circuit pixels:", cv2.countNonZero(circuit_mask))

# Vectorize organic terrain with high precision
vtracer.convert_image_to_svg_py(
    'public/art/seamless/terrain_organic.png',
    'public/art/seamless/terrain_organic.svg',
    colormode='binary',
    mode='spline',
    filter_speckle=1,
    corner_threshold=30,
    length_threshold=1.5,
    max_iterations=10,
    splice_threshold=30,
    path_precision=2
)

# Vectorize circuits
vtracer.convert_image_to_svg_py(
    'public/art/seamless/circuits.png',
    'public/art/seamless/circuits.svg',
    colormode='binary',
    mode='spline',
    filter_speckle=1,
    corner_threshold=20,
    length_threshold=1.5,
    max_iterations=10,
    splice_threshold=20,
    path_precision=2
)

with open('public/art/seamless/terrain_organic.svg', 'r') as f:
    t_svg = f.read()
t_paths = [p for p in re.findall(r'<path[^>]+/>', t_svg) if not ('d="M0 0 C337.92 0' in p and '1024 409' in p)]

with open('public/art/seamless/circuits.svg', 'r') as f:
    c_svg = f.read()
c_paths = [p for p in re.findall(r'<path[^>]+/>', c_svg) if not ('d="M0 0 C337.92 0' in p and '1024 409' in p)]

print(f"Terrain organic paths: {len(t_paths)}")
print(f"Circuits paths: {len(c_paths)}")
