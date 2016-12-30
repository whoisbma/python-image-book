import cv2
from pylab import *

# setup video capture
cap = cv2.VideoCapture(0)

frames = []
# get frame, store in array

while True:
	ret,im = cap.read()
	cv2.imshow('video', im)
	frames.append(im)
	if cv2.waitKey(10) == 27:
		break

frames = array(frames)

# check the sizes
print im.shape
print frames.shape

# each frame array is added to the end of a list until the capturing is stopped. the resulting array will have size (number of frames, height, width, 3).