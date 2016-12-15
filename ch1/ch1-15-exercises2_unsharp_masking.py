# ch1-15-exercises2_unsharp_masking.py
# pp. 26
# blur an image and then subtract the blurred version from the original - giving a sharpening effect.
# try this on both grayscale and color images.

from PIL import Image
import numpy as numpy
import pylab as pylab
from scipy.ndimage import filters

c_im = pylab.array(Image.open('images/pug.jpg'))
g_im = pylab.array(Image.open('images/pug.jpg').convert('L'), 'f')

blurred_c_im = filters.gaussian_filter(c_im, 5)
blurred_g_im = filters.gaussian_filter(g_im, 5)

sharp_c_im = c_im + (c_im - blurred_c_im) * 1.0
sharp_g_im = g_im + (g_im - blurred_g_im) * 1.0

# pylab.gray()

pylab.imshow(c_im)
pylab.figure()
pylab.imshow(blurred_c_im)
pylab.figure()
pylab.imshow(sharp_c_im)



print g_im.dtype, blurred_g_im.dtype, sharp_g_im.dtype

pylab.show()
