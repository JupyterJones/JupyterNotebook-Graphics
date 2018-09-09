#!/usr/bin/python
# randim(inpath = "images/") Finds random images in a directory 
#Default directory is: images/
import PIL
import time
from PIL import Image
import random, os
from random import randint
def rand_im(inpath = "images/"):
    random_filename2 = random.choice([
        x for x in os.listdir(inpath)
        if os.path.isfile(os.path.join(inpath, x))
    ])

    img1 = inpath+"/"+random_filename2
    im1=Image.open(img1)
    longer_side = max(im1.size)
    basewidth = longer_side
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img4 = img.crop(
        (
            half_the_width - 320,
            half_the_height - 320,
            half_the_width + 320,
            half_the_height + 320
        )
    )
    return img4
if __name__ == '__main__':
    rand_im()