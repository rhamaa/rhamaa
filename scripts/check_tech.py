from PIL import Image

im_tech = Image.open('public/art/technology-standalone.webp')
print('tech size:', im_tech.size)
# Let's inspect what is inside technology-standalone.webp
# Is it the full-resolution artwork or a standalone page?
box = (0, 0, 3072, 2048)
# Let's save a reduced version to inspect
thumb = im_tech.resize((768, 512))
thumb.save('scripts/tech_preview.png')
print('Saved tech_preview.png')
