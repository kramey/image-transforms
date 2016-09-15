
from PIL import Image

im = Image.open('A.png')
print im.format, im.size, im.mode

im.rotate(45)
im.save('Amod.png')
