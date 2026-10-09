from PIL import Image

im = Image.open('public/art/contact-reference.webp')
# Save full preview of contact-reference.webp
im_small = im.resize((836, 470))
im_small.save('scripts/contact_ref_preview.png')
print("Saved contact_ref_preview.png")
