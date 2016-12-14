# Interactive Annotation

# sometimes users need to interact with an application, for example by marking points on an image
# pylab comes with ginput()

from PIL import Image
from pylab import *

im = array(Image.open('images/pug.jpg'))
imshow(im)

print('Please click 3 points')

x = ginput(3)

print('You clicked: ', x)

show()