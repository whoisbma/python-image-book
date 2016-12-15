# NumPy
# numpy is used for scientific computing.
# contains array objects (for vectors, matrices, images, more) and linear algebra functions
# the array object lets you do important operations like matrix multiplication, transposition, solving equation systems, vector multiplication, normalization - needed for things like aligning images, warping images, modeling variations, classifying images, grouping images, etc.

# Array Image Representation

# When we loaded images in the previous examples, 
# we converted them to numpy array objects using the array() call

# arrays in numpy are multidimensional and can represent vectors, matrices, and images
# an array is much like a list or list of lists but is restricted to having all elements the same type
# unless specified on creation, the type will automatically be set depending on the data

# pylab contains components of numpy.

from PIL import Image
from pylab import *

im = array(Image.open('images/pug.jpg'))

print im.shape, im.dtype

im = array(Image.open('images/pug.jpg').convert('L'), 'f')
print im.shape, im.dtype

# the first tuple on each line is the shape of the image array (rows, columns, color channels), 
# and the following string is the datatype of the array elements

# images are usually encoded with unsigned 8-bit integers (uint8)
# but adding the 'f' argument converts it to 32-bit floating point.

# note that the grayscale image has only two values in the shape tuple - it has no color info.

# elements in the array are accessed with indexes.
# the value at coordinates i, j, and color channel k are accessed like:
# value = im[i,j,k]

print(im[10,10])

# multiple elements can be accessed using array slicing.
# slicing returns a view into the array specified by intervals.
# some examples:


# im[i,:] = im[j,:]			# set the values of row i with the values from row j
# im[:,i] = 100				# set all values in column i to 100
# im[:100,:50].sum()		# the sum of all values of the first 100 rows and 50 columns
# im[50:100,50:100]			# rows 50-100, columns 50-100 (not including 100)
# im[i].mean()				# average of row i
# im[:,-1]						# last column
# im[-2,:] # or im[-2]		# second to last row

