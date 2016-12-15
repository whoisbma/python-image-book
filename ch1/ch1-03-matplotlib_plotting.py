# Matplotlib

# matplotlib is a  graphics library with more powerful features than the plotting available in PIL.


#		Plotting Images, Points, and Lines
# Only a few commands are needed for most computer vision purposes.
# We want to be able to show things like interest points, correspondences, and detected objects using points and lines.

# Plotting an image with a few points and a line:

from PIL import Image
from pylab import *

# read image to array
im = array(Image.open("images/0.png"))

# plot the image
imshow(im)

# some points
x = [100,100,400,400]
y = [200,500,200,500]

# plot the points with red star-markers
plot(x,y, 'r*')

# line plot connecting the first two points
plot(x[:2], y[:2])

# line w green circle markers
plot(x[1:3], y[1:3], 'go-')

# dotted line w square markers
plot(x[2:], y[2:], 'ks:')


# add title and show the plot
title('Plotting: "0.png"')

# pylab uses a coordinate origin at the top left corner.
# turn off axes with:
axis('off')

# show() starts the figure GUI and raises the figure windows.
# the GUI loop blocks your scripts and they are paused until the last figure window is closed.
# call show() only once per script, usually at the end
show()