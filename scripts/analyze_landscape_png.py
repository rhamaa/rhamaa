from PIL import Image
import numpy as np

im = Image.open('public/art/landscape-art.png')
arr = np.array(im)
print('Shape:', arr.shape)
# Count transparent pixels
alpha = arr[:, :, 3]
print('Transparent pixels (%):', np.mean(alpha == 0) * 100)
# Look at unique colors where alpha > 0
non_trans = arr[alpha > 0]
print('Mean RGB non-trans:', np.mean(non_trans[:, :3], axis=0))
