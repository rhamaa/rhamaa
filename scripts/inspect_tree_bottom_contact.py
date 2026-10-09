from PIL import Image

im_contact = Image.open('public/art/contact-reference.webp').convert('RGB')
# box: '815 573 857 311', width: 1672, height: 941
# Scaled by 2:
# (1630, 1146, 1630 + 1714, 1146 + 622)
# Let's crop the landscape area from contact-reference.webp
crop_contact = im_contact.crop((1630, 1146, 1630 + 1714, 1146 + 622))
# Resize to 1024x409 or 1024x371
# In 1024x409 coords:
# x=650..750 in 1024 is x = 650/1024 * 1714 = 1088 .. 1255 in crop_contact
# y=310..350 in 409 is y = 310/409 * 622 = 471 .. 532 in crop_contact
region_contact = crop_contact.crop((1088, 471, 1255, 532))
region_contact.save('scripts/zoom_tree_bottom_contact.png')
print("Saved zoom_tree_bottom_contact.png")
