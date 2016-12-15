# SciPy
# SciPy is an open-source package for mathematics that builds on NumPy and provides efficient routines for operations like numerical integration, optimization, statistics, signal processing, and most importantly for us, image processing.


# Blurring Images

# A classic and very useful example of image convolution is Gaussian blurring.
# Gaussian blurring is used to define an image scale to work in, for interpolation, for computing interest points, and many more applications.
# SciPy comes with a module for filtering called scipy.ndimage.filters that can be used to compute these convolutions using a fast 1D separation.

from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('data/empire.jpg'))
im2 = zeros(im.shape)
for i in range(3):
	im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = uint8(im2)

# the last conversion to uint8 is not always needed but forces the pixel values to be in an 8-bit representation
# also could have used im2 = array(im2, 'uint8')

imshow(im2)

# Image Derivatives

# How the image intensity changes over the image is important information and is used for many applications.

# applying derivative filters using the standard convolution available in the scipy.ndimage.filters module.

im3 = array(Image.open('data/empire.jpg').convert('L'))

# sobol derivative filters
imx = zeros(im3.shape)
filters.sobel(im3,1,imx)

imy = zeros(im3.shape)
filters.sobel(im3,0,imy)

magnitude = sqrt(imx**2+imy**2)

gray()

figure()
imshow(imx)

figure()
imshow(imy)

figure()
imshow(magnitude)

# Using this approach has the drawback that derivatives are taken on the scale determined by the image resolution. To be more robust to image noise and to compute derivatives at any scale, Gaussian Derivative Filters can be used.

# The filters.gaussian_filter() function we used for blurring earlier
sigma = 5 # standard deviation
imx2 = zeros(im3.shape)
filters.gaussian_filter(im3, (sigma,sigma), (0,1), imx2)
imy2 = zeros(im3.shape)
filters.gaussian_filter(im3, (sigma,sigma), (1,0), imy2)

figure()
imshow(imx2)
figure()
imshow(imy2)

show()