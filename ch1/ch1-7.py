# Greylevel Transforms

# after reading images to numpy arrays, we can perform any mathematical operation we like on them
# a simple example of this is to transform the graylevels of an image
# take any function f that maps the interval 0...255 to itself

from PIL import Image
from numpy import *

im = array(Image.open('pug.jpg').convert('L'))

im2 = 255 - im 						# invert image

im3 = (100.0/255) * im + 100 		# clamp to interval 100...200

im4 = 255.0 * (im/255.0) ** 2		# squared (lower the darkness values)

# check the minimum and maximum values of each image using:
print int(im.min()), int(im.max())

figure()
imshow(im)

print int(im2.min()), int(im2.max())

figure()
imshow(im2)

print int(im3.min()), int(im3.max())

figure()
imshow(im3)

print int(im4.min()), int(im4.max())

figure()
imshow(im4)