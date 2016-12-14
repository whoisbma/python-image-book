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
print int(in.min()), int(im.max())

