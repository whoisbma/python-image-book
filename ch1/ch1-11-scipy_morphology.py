# Morphology
# Framework and collection of image processing methods for measuring and analyzing basic shapes.
# Morphology is usually applied to binary images but can be used with grayscale also.
# A binary image is an image in which each pixel takes only two values, usually 0 and 1.
# Binary images are often the result of thresholding an image, for example with the intention of counting objects or measuring their size.
# Morphological operations are included in the scipy.ndimage module morphology.
# Counting and measurement functions for binary images are in the scipy.ndimage module measurements.

from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import measurements,morphology

# load image and threshold to make sure it is binary
im = array(Image.open('data/houses.png').convert('L'))
im = 1*(im<128) # multiplying by 1 converts the boolean array to a binary one
gray()
imshow(im)
labels, nbr_objects = measurements.label(im)
print "Number of objects:", nbr_objects
im2 = Image.fromarray(labels)
figure()
imshow(im2)

# this results in some small connections between the objects.
# using an operation called binary opening, we can remove them.

im_open = morphology.binary_opening(im,ones((9,5)),iterations=2)
labels_open, nbr_objects_open = measurements.label(im_open)
print "Number of objects: ", nbr_objects_open

figure()
imshow(im_open)
figure()
imshow(labels_open)

# the second argument of binary_opening() specifies the Structuring Element, an array that indicates what neighbors to use when centered around a pixel.
# in this case we used 9 pixels (4 above, 4 below) in the Y direction and 5 in the x direction.
# you can specify any array as a structuring element - the non-zero elements will determine the neighbors.
# the parameter iterations determines how many times to apply the operation.
# binary_closing() does the reverse.


show()
