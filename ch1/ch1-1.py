# Basic PIL Operations

from PIL import Image

pil_im = Image.open('images/0.png')

# return value is a PIL image object.


# 		Color Conversions

# color conversions are done using the convert() method.
# to convert an image to greyscale, add argument 'L'

pil_im = Image.open('images/0.png').convert('L')


# 		Creating Thumbnails

# the thumbnail() method takes a tuple specifying the new size and converts the image to a thumbnail image with size that fits within the tuple.

# create a thumbnail with longest side 128 pixels: 
pil_thumbnail = pil_im.thumbnail((128,128))


#		Copy and Paste Regions

# create a 4-tuple, where coords are left, upper, right, lower
box = (100,100,400,400)
region = pil_im.crop(box)

# rotate then put back using the paste() method:
region = region.transpose(Image.ROTATE_180)
pi_im.paste(region, box)


# 		Resizing and Rotating

# resize() takes a tuple giving the new size:
pil_resized = pil_im.resize((128,128))

# rotate() takes a counterclockwise angle:
pil_rotated = pil_im.rotate(45)