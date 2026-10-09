from PIL import Image

im_contact = Image.open('public/art/contact-reference.webp').convert('RGB')
crop_contact = im_contact.crop((1630, 1146, 1630 + 1714, 1146 + 622))
crop_contact.save('scripts/full_crop_contact.png')
print("Saved full_crop_contact.png, size:", crop_contact.size)
