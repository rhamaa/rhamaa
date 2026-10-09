from PIL import Image
import numpy as np

im = Image.open('public/art/landscape-art.png').convert('RGB')
arr = np.array(im, dtype=np.float32)

# Background color in the sky is approx (242, 238, 230)
# Let's compute darkness relative to local/paper background
# Gray level = 0.299*R + 0.587*G + 0.114*B
gray = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
print("Min gray:", np.min(gray), "Max gray:", np.max(gray))

# Let's inspect percentiles of gray
for p in [1, 2, 5, 8, 10, 15, 20]:
    print(f"Percentile {p}%: {np.percentile(gray, p):.1f}")
