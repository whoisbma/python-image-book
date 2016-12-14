# Convert Images to Another Format
# pg. 1

# Using the save() method, PIL can save images in most image file formats.
# Here's an example that takes all image files in a list of filenames (filelist) and converts the images to JPEG files

from PIL import Image
import os

# os provides a portable way of using operating system dependent functionality (i.e. reading/writing a file)

filelist = ['images/0.png', 'images/1.png', 'images/2.png']

for infile in filelist:
		# splitext splits the pathname into a pair (root, ext) such that root + ext == path
		# and ext is empty or begins with a period and contains at least one period.
		# leading periods on the basename are ignored.
		# [0] returns the first of the pair
		outfile = os.path.splitext(infile)[0] + ".jpg"
		if infile != outfile:
			try:
				Image.open(infile).save(outfile)
			except IOError:
				print "cannot convert", infile