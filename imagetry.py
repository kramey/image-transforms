
from PIL import Image

im = Image.open('A.png')
print im.format, im.size, im.mode

out = im.rotate(45)
out.save('Amod.png')
