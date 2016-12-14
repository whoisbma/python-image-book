# Principal Component Analysis
# useful technique for dimensionality reduction
# optimal in the sense that it represents the variability of the training data with as few dimensions as possible.
# Even a tiny 100x100 pixel greyscale image has 10,000 dimensions, and can be a considered a point in 10,000 dimensional space.
# A megapixel image has dimensions in the millions.
# With such high dimensionality, its no surprise that dimensionality reduction comes in handy in many computer vision applications.
# The projection matrix resulting from PCA can be seen as a change of coordinates to a coordinate system where the coordinates are in descending order of importance.

# To apply PCA on image data, the images need to be converted to a 1D vector representation using, for example, numpy's flatten() method.

# The flattened images are collected in a single matrix by stacking them, one row for each image.
# The rows are then centered relative to the mean image before teh computation of the dominant directions.
# To find the principal components, singular value decomposition (SVD) is usually used, but if the dimensionality is high, there is a useful trick that can be used instead since the SVD computation will be very slow in that case.

from PIL import Image
from numpy import *

def pca(X):
	""" Principal Component Analysis
		input: X, matrix with training data stored as flattened arrays in rows
		return: projection matrix (with important dimensions first), variance and mean. """

	# get dimensions
	num_data, dim = X.shape

	# center data
	mean_X = X.mean(axis=0)
	X = X - mean_X

	if dim>num_data:
		# PCA - compact trick used
		M = dot(X, X.T) # covariance matrix
		e,EV = linalg.eigh(M) # eigenvalues and #eigenvectors
		tmp = dot(X.t, EV).T # this is the compact trick
		V = tmp[::-1] # reverse since last eigenvectors are the ones we want
		S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
		for i in range(V.shape[1]):
			V[:,i] /= S
	else:
		# PCA - SVD used
		U,S,V = linalg.svd(X)
		V = V[:num_data] # only makes sense to return the first num_data

	# return the projection matrix, the variance and the mean
	return V,S,mean_X