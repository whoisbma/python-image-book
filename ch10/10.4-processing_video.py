# VIDEO INPUT
# capture frames and show them in an openCV window

import cv2

cap = cv2.VideoCapture(0)

# VideoCapture captures video from cameras or files. Here we pass it an integer at initialization - the ID of the video device. with a single camera connected this is 0.

# the method read() decodes and returns the next video frame - the first value is a success flag and the second is the actual image array.

while True:
	ret, im = cap.read()
	# cv2.imshow('video test', im)
	blur = cv2.GaussianBlur(im, (0,0), 5)
	cv2.imshow('camera blur', blur)

	key = cv2.waitKey(10)
	if key == 27:
		break
	if key == ord(' '):
		cv2.imwrite('vid_result.jpg', im)

# each frame is passed to the function GaussianBlur() which applies a filter to the image. in this case we're passing a color image so each color channel is blurred separately. the function takes a tuple for filter size and the standard deviation for the gaussian function.


# READING VIDEO

# works the same way but the call to VideoCapture() takes the video filename as input.

# capture = cv2.VideoCapture('filename')