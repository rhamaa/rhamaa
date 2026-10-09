from PIL import Image
import numpy as np

im = Image.open('public/art/landscape-art.png').convert('RGB')
arr = np.array(im)

# Let's inspect where the sun circle is:
# Search for circular patch with gold color
# Let's check center ~ (547, 156) as in landscape-full-pure-vector.svg
print("Pixel at (547, 156):", arr[156, 547])
print("Pixel at (547, 120):", arr[120, 547])
print("Pixel at (547, 100):", arr[100, 547])
print("Pixel at (547, 200):", arr[200, 547])
print("Pixel at (547, 220):", arr[220, 547])
