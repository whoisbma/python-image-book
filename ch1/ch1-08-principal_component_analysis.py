# using PCA on font images

# fontimages.zip contains small thumbnail images of the character "a" printed in different fonts and then scanned. Assuming that the filenames of these images are stored in a list, imlist, the principal components can be computed and shown like this: 

from PIL import Image
from numpy import *
from pylab import *
import imtools
import pca

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