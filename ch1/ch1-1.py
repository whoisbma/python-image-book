from PIL import Image

pil_im = Image.open('images/a.png')

# return value is a PIL image object.

# color conversions are done using the convert() method.
# to convert an image to greyscale, add argument 'L'

pil_im = Image.open('images/a.png').convert('L')