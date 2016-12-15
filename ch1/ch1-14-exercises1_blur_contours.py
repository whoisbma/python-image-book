# ch1-14-exercises.py
# pp. 26

from PIL import Image
import numpy as numpy
import pylab as pylab
from scipy.ndimage import filters

# 1: Take an image and apply Gaussian blur. Plot the image contours for increasing blur values.

im = pylab.array(Image.open('images/pug.jpg').convert('L'))

pylab.gray()
pylab.subplot(2,2,1)
pylab.axis('equal')
pylab.contour(im, origin='image')

im2 = filters.gaussian_filter(im,2)
pylab.subplot(2,2,2)
pylab.axis('equal')
pylab.contour(im2, origin='image')

im3 = filters.gaussian_filter(im,5)
pylab.subplot(2,2,3)
pylab.axis('equal')
pylab.contour(im3, origin='image')

im4 = filters.gaussian_filter(im, 8)
pylab.subplot(2,2,4)
pylab.axis('equal')
pylab.contour(im4, origin='image')

# pylab.axis('off')

pylab.show()