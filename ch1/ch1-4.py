# Image Contours and Histograms

# an image histogram is a plot showing the distribution of pixel values.
# a number of bins is specified for the span of values and each bin gets a count of how many pixels have values in the bin's range. 
# the visualization of the graylevel image histogram is done using the hist() function.

from PIL import Image
from pylab import *

# read image to array and convert to greyscale
im = array(Image.open('images/pug.jpg').convert('L'))

# create a new figure
figure()

# don't use colors
gray()

# show contours with origin upper left corner
contour(im, origin='image')
# imshow(im)

axis('equal')
axis('off')

figure()

# the second argument specifies the number of bins to use
# note that the image needs to be flattened first because hist() takes a 1D array as input.
# the method flatten() converts any array to a 1D array with values taken row-wise.
hist(im.flatten(), 128)
show()