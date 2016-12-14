import os

def get_imlist(path, file_ext):
		""" Returns a list of filenames for all jpg images in a directory. """
		return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(file_ext)]