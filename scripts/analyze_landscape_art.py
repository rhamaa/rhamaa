from PIL import Image
import numpy as np

im = Image.open('public/art/landscape-art.png')
# Convert to grayscale
gray = im.convert('L')
arr = np.array(gray)
print("Min brightness:", np.min(arr), "Max brightness:", np.max(arr))

# Find the darkest ink pixels (threshold < 80)
ink = arr < 80
print("Ink pixel percentage:", np.mean(ink) * 100)

# Check vertical projection of ink pixels
v_proj = np.sum(ink, axis=1)
h_proj = np.sum(ink, axis=0)

print("Vertical ink rows with > 0 ink:", np.where(v_proj > 0)[0][[0, -1]])
print("Horizontal ink cols with > 0 ink:", np.where(h_proj > 0)[0][[0, -1]])

# Check color of the sun region (is there a gold/yellow circular region?)
im_rgb = im.convert('RGB')
arr_rgb = np.array(im_rgb)
# Sun is yellowish: R > 200, G in [150, 200], B < 120
yellow = (arr_rgb[:, :, 0] > 180) & (arr_rgb[:, :, 1] > 140) & (arr_rgb[:, :, 1] < 200) & (arr_rgb[:, :, 2] < 120)
print("Yellow pixels found:", np.sum(yellow))
if np.sum(yellow) > 0:
    y_coords, x_coords = np.where(yellow)
    print("Yellow bbox: x=[", np.min(x_coords), np.max(x_coords), "], y=[", np.min(y_coords), np.max(y_coords), "]")
    print("Sun center approx:", (np.mean(x_coords), np.mean(y_coords)))
