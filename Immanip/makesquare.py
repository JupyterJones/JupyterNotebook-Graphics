#!/usr/bin/python
import PIL
import time
from PIL import Image
import random, os
from random import randint
# make_square(imp_path = "images/", side=300) Picks a ranom image in a directory, squares it \
# reguardless of aspect. The default directory is images/ the default size is 300
# usage for default directory and size just use: make_square()
# For your own directory or size: make_square(imp_path = "My-directory/", side=500)
def make_square(imp_path = "images/", side=300):
    random_filename = random.choice([
        x for x in os.listdir(imp_path)
        if os.path.isfile(os.path.join(imp_path, x))
    ])
    img2 = imp_path+"/"+random_filename
    im2=Image.open(img2)
    img5 = im2.resize((side,side), PIL.Image.ANTIALIAS)
    return img5
   