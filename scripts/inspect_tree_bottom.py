from PIL import Image
import numpy as np

im = Image.open('public/art/landscape-art.png').convert('RGB')
arr = np.array(im)

# Look at region around x=650..750, y=310..350
region = arr[310:350, 650:750]
# Is there a cut seam or smooth engraving lines?
# Let's save a crop of this region magnified 4x
crop = Image.fromarray(region).resize((400, 160), Image.Resampling.NEAREST)
crop.save('scripts/zoom_tree_bottom.png')
print("Saved zoom_tree_bottom.png")
