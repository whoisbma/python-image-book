import cv2
from pylab import *
from numpy import *

im = cv2.imread('images/pug.jpg')

# downsample by 50%
im_lowres = cv2.pyrDown(im)

# convert to grayscale
gray = cv2.cvtColor(im_lowres, cv2.COLOR_RGB2GRAY)

# detect feature points
s = cv2.SURF()
mask = uint8(ones(gray.shape))

# the mask determines what areas to apply the keypoint detector.

keypoints = s.detect(gray, mask)

# show image and points
vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# loop over every 10th keypoint and plot a circle at the center and a circle showing the scale of the keypoint.

#circle takes an image, a tuple with integer coordinates, a radius, a tuple with plot color, and the line thickness.
for k in keypoints[::10]:
	cv2.circle(vis, (int(k.pt[0]), int(k.pt[1])), 2, (0,255,0), -1)
	cv2.circle(vis, (int(k.pt[0]), int(k.pt[1])), int(k.size), (0,255,0), 2)

cv2.imshow('local descriptors', vis)
cv2.waitKey()