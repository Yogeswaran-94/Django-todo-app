from PIL import Image

img = Image.new('RGBA', (16, 16), (255, 0, 0, 255))
img.save('favicon.ico')
print("favicon.ico generated!")
