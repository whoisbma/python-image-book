# OPTICAL FLOW

# the image motion of objects as the objects, scene, or camera moves between two consecutive images. it is a 2d vector field of within-image translation. its a classic and well studied field in computer vision with many successful applications in video compression, motion estimation, object tracking, and image segmentation.

# optical flow relies on three major assumptions:
# 1-	brightness constancy (pixel intensities of an object don't change between images)
# 2-	temporarl regularity (between-frame time is short enough to consider the motion change between images using differentials)
# 3-	spatial consistency (neighboring pixels have similar motion)

# OpenCV has several optical flow implementations.

import cv2
from numpy import *

def draw_flow(im, flow, step=16):
	""" Plot optical flow at sample points spaced step pixels apart. """

	h,w = im.shape[:2]
	y,x = mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
	fx,fy = flow[y,x].T

	# create line endpoints
	lines = vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
	lines = int32(lines)

	# create image and draw
	vis = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
	for (x1,y1), (x2,y2) in lines:
		cv2.line(vis, (x1,y1), (x2,y2), (0,255,0), 1)
		cv2.circle(vis, (x1,y1), 1, (0,255,0), -1)
	return vis


# set up video capture
cap = cv2.VideoCapture(0)
ret,im = cap.read()
prev_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

while True:
	# get grayscale image
	ret,im = cap.read()
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

	# compute flow
	flow = cv2.calcOpticalFlowFarneback(prev_gray,gray,0.5,1,3,15,3,5,1)
	prev_gray = gray

	# plot the flow vectors
	cv2.imshow('Optical Flow', draw_flow(gray, flow))
	if cv2.waitKey(10) == 27:
		break