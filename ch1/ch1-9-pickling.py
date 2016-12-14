# Using the Pickle module
# Saving results or data for later use.

# Pickle can take almost any Python object and convert it to a string representation, and back (unpickling)

from PIL import Image
from numpy import *
from pylab import *
import imtools
import pca
import pickle

imlist = imtools.get_imlist("data/fontimages/", "jpg")

im = array(Image.open(imlist[0])) # open one image to get size
m,n = im.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')

# perform PCA
V,S,immean = pca.pca(immatrix)

# show some images (mean and 7 first modes)
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
	subplot(2,4,i+2)
	imshow(V[i].reshape(m,n))

show()

# Suppose we want to save the image mean and principal components of the font images in the previous section.

# save mean and principal components
f = open('font_pca_modes.pk1', 'wb')
pickle.dump(immean, f)
pickle.dump(V, f)
f.close()

# several objects can be pickled to the same file.

# there are several different protocols available for the .pkl files, and if unsure, it is best to read and write binary files.

# To load the data in some other Python session, just use load():

# load mean and principal components
f = open('font_pca_modes.pk1', 'rb')
immean = pickle.load(f)
V = pickle.load(f)
f.close()

# to do this instead using "with":

# open file and save
with open('font_pca_modes.pk1', 'wb') as f:
	pickle.dump(immean,f)
	pickle.dump(V,f)

# open file and load
with open('font_pca_modes.pk1', 'rb') as f:
	immean = pickle.load(f)
	V = pickle.load(f)

# Alternative to using pickle: NumPy also has simple functions for reading and writing text files that can be useful if your data does not contain complicated structures, for example a list of points clicked in an image.

# to save array x to file:
x = [1,2,4]
savetxt('test.txt',x,'%i') # with integer format

# to read:
x = loadtxt('test.txt')

# NumPy also has dedicated functions for saving and loading arrays.