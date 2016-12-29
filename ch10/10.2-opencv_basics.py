import cv2
from numpy import *

# reading and writing images

# imread() returns the image as a standard numpy array
# use this as an alternative to the PIL image
im = cv2.imread('images/pug.jpg')
h,w = im.shape[:2]
print h, w

# imwrite() takes care of any conversion
cv2.imwrite('result.png', im)


# color spaces

# in openCV images are stored in BGR order (backwards)
# when reading an image the default is BGR but there are conversions available
# color space conversions are done using cvtColor()

# converting to greyscale:
im = cv2.imread('images/pug.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# cv2.COLOR_BGR2RGB
# cv2.COLOR_GRAY2BGR

cv2.imwrite('gray.png', gray)


# displaying images and results 

# create an integral image representation:
intim = cv2.integral(gray)

# normalize and save:
intim = (255.0*intim) / intim.max()
cv2.imwrite("intim.png", intim)

# after reading the image and converting to grayscale, integral() creates an image where the value at each pixel is the sum of the intensities above and to the left.
# this is a very useful trick for quickly evaluating features.
# integral images are used in openCV's cascadeClassifier, which is based on a framework introduced by Viola and Jones.
# before saving the resultimg image, we normalize the values to 0...255 by dividing with the largest value.


# flood fill starting from a seed pixel:
diff = (6,6,6)
mask = zeros((h+2,w+2), uint8)
cv2.floodFill(im, mask, (10,10), (255,255,0), diff, diff)

# show the result in an openCV window:
cv2.imshow('flood fill', im)
cv2.waitKey()

# save the result:
cv2.imwrite('floodfill.jpg', im)


# Extracting SURF features

im = cv2.imread('images/pug.jpg')

# downsample:
im_lowres = cv2.pyrDown(im)

# convert to grayscale:
gray = cv2.cvtColor(im_lowres, cv2.COLOR_RGB2GRAY)

# detect feature points
# s = cv2.SURF()
# mask = uint8(ones(gray.shape))
# keypoints = s.detect(gray, mask)

# # show image and points
# vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# for k in keypoints[::10]:
# 	cv2.circle(vis,(int(k.pt[0]), int(k.pt[1])),2,(0,255,0),-1)
# 	cv2.circle(vis,(int(k.pt[0]), int(k.pt[1])), int(k.size), (0,255,0), 2)
# cv2.imshow('local descriptors', vis)
# cv2.waitKey()
