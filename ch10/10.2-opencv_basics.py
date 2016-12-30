# READING AND WRITING IMAGES

import cv2
from pylab import *

# read image
im = cv2.imread('images/pug.jpg')
h,w = im.shape[:2]
print h, w

# save image
cv2.imwrite('resulting pug.png',im)

# imread() returns the image as a standard NumPy array and can handle a wide range of image formats. You can use this function as an alternative to the PIL image reading.

# imwrite() automatically takes care of any conversion based on the file ending.



# COLOR SPACES

# in openCV images are not stored using RGB channels, they are stored in BGR order. When reading an image the default is BGR, however there are several conversions available. Color space conversions are done using cvtColor().

# converting to grayscale
grayPug = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('graypug.png', grayPug)

# others:
# cv2.COLOR_BGR2GRAY
# cv2.COLOR_BGR2RGB
# cv2.COLOR_GRAY2BGR

# the last version converts grayscale to BGR and is useul if you want to plot or overlay colored objects on the images.



# DISPLAYING IMAGES AND RESULTS

# compute integral image
intim = cv2.integral(grayPug)

# normalize and save
intim = (255.0 * intim) / intim.max()
cv2.imwrite('intim.png', intim)

# integral() creates an image where the value at each pixel is the sum of the intensities above and to the left. this is a very useful trick for quickly evaluating features. integral images are used in openCV's cascade classifier which is based on a framework introduced by Viola and Jones.

# before saving the resulting image, we normalize the values to 0...255 by dividing with the largest value.




# FLOOD FILL

diff = (6,6,6)
mask = zeros((h+2,w+2),uint8)
cv2.floodFill(im,mask,(10,10),(255,255,0),diff,diff)

# show the result in an openCV window
cv2.imshow('floodfill', im)
cv2.waitKey()

# save the result
cv2.imwrite('floodfill result.jpg', im)

# the example applies flood fill to the image and shows the result in an OpenCV window. waitKey() pauses until a key is pressed and the window is automatically closed. Here the function floodFill() takes the image (grayscale or color), a mask with non-zero pixels indicating areas not to be filled, a seed pixel, the new color value to replace the tflooded pixels together with lower and upper difference thresholds to accept new pixels. the difference thesholds are given as tuples (R,G,B).
