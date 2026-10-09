from PIL import Image

im_contact = Image.open('public/art/contact-reference.webp')
# Crop using the box from ReferenceArt.astro: box: '815 573 857 311', width: 1672, height: 941
# Scaled by 2:
box = (815 * 2, 573 * 2, (815 + 857) * 2, (573 + 311) * 2)
cropped = im_contact.crop(box)
print("Cropped from contact-reference:", cropped.size)
cropped.save("scripts/cropped_from_contact.png")

# Now check landscape-art.png
im_land = Image.open('public/art/landscape-art.png')
print("Landscape-art.png:", im_land.size)
