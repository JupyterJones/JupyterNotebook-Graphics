#!/usr/bin/python
import PIL
import time
from PIL import Image
import random, os
from random import randint
# rand_size(imp_path='STUFF/new/', minS=150, maxS=300, output="STUFF/Temp.jpg")
# Picks a ranom image in a directory, and distorts it  
# Default path images/ default minimum width random(250-400), height random(250-400) intentionally\
# distorting the aspect.
def rand_size(imp_path='images/', minS=250, maxS=500, output="output/Temp.jpg"):
    path3 = imp_path
    random_filename3 = random.choice([
        x for x in os.listdir(path3)
        if os.path.isfile(os.path.join(path3, x))
    ])
    sidea=(randint(minS, maxS))
    
    sideb=(randint(minS, maxS))
    img1 = path3+"/"+random_filename3
    im1=Image.open(img1)
    img = im1.resize((sidea,sideb), PIL.Image.ANTIALIAS)
    img.save(output)
    return img 
 