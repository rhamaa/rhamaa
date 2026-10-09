from PIL import Image
import numpy as np

im = Image.open('public/art/landscape-art.png').convert('RGB')
arr = np.array(im)
w, h = im.size
print(f"Image size: {w}x{h}")

# In landscape-art.png, let's analyze the ink colors:
# Foreground landscape ink is dark slate/charcoal/teal: #172724 or similar dark color
# Background is cream: ~ (242, 238, 230)
# Sun is golden: ~ (210-230, 160-190, 80-120)
# Circuit nodes are golden: ~ (230, 180, 70)
# Let's see color clusters or histogram

# Find dark ink pixels:
# brightness = (R + G + B) / 3
brightness = np.mean(arr, axis=2)
dark = brightness < 150
print("Pixels with brightness < 150:", np.sum(dark))
print("Pixels with brightness < 100:", np.sum(brightness < 100))
print("Pixels with brightness < 60:", np.sum(brightness < 60))
