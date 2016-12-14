import os

def get_imlist(path, file_ext):
	""" Returns a list of filenames for all jpg images in a directory. """
	return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(file_ext)]



# in order to resize an image with numpy arrays:
# use the PIL object conversion to make a simple image resizing fucntion.
def imresize(im,sz):
	""" Resize an image array using PIL. """
	pil_im = Image.fromarray(uint8(im))
	return array(pil_im.resize(sz))
