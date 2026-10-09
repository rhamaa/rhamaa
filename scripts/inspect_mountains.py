from PIL import Image
import numpy as np

im = Image.open('public/art/landscape-art.png').convert('RGB')
arr = np.array(im)

# Mountains are around x=300..700, y=140..250
# Let's inspect brightness in that region
# Let's check a patch on the mountain ridge
patch = arr[180:220, 400:450]
gray_patch = np.mean(patch, axis=2)
print("Mountain patch min brightness:", np.min(gray_patch))
print("Mountain patch mean brightness:", np.mean(gray_patch))
print("Mountain patch max brightness (paper):", np.max(gray_patch))
