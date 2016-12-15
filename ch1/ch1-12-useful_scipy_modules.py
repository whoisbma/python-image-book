# ch1-12-useful_scipy_modules.py

from pylab import *
from numpy import *
from PIL import Image

# Reading and Writing .mat Files
# If you have data stored in Matlab's .mat file format, it is possible to read this using the scipy.io module.

data = scipy.io.loadmat('test.mat')

# The object data now contains a dictionary with keys corresponding to the variable names stored in the original .mat file.
# The variables are in array format.

# Saving .mat Files
# Create a dictionary with all variables you want to save and call savemat():

data = {}
data['x'] = x
scipy.io.savemat('test.mat', data)


# Saving Arrays as Images
# The imsave() function is available through the scipy.misc module. 
# To save an array im to file:

from scipy.misc import imsave
imsave('test.jpg', im)


# Lena Test Image
# Included in scipy.misc

lena = scipy.misc.lena()

# This will give you a 512x512 grayscale array version of the image.