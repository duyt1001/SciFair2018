from PIL import Image

im = Image.open('/Users/anna/Desktop/sandwithseafish.jpg')
im_grey = im.convert('LA') # convert to grayscale
width,height = im.size

total=0
for i in range(0,width):
    for j in range(0,height):
        total += img.getpixel((i,j))[0]

mean = total / (width * height)