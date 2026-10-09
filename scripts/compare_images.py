from PIL import Image
import numpy as np

im_land = Image.open('public/art/landscape-art.png')
im_contact = Image.open('scripts/cropped_from_contact.png')

print("im_land size:", im_land.size)
print("im_contact size:", im_contact.size)

# If we resize im_contact to width 1024, height is 1024 * 622 / 1714 = 371.4
# Or maybe landscape-art was cropped with a different box or resized?
# Let's inspect subregions of both images
print("im_land top-left 10x10 RGB:", np.array(im_land)[:5, :5, :3])
print("im_contact top-left 10x10 RGB:", np.array(im_contact)[:5, :5, :3])
