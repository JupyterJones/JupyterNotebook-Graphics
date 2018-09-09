#!/usr/bin/python
import PIL
import time
from PIL import Image
import random, os
from random import randint
import random, os
# Randomly choose two images. The default directories are images/. The images may be two 
# different directories.
def blend_overlay(Opath="images/", Bpath="images/"):
    #path = r"bugs/advertisements/"

    random_filename1 = random.choice([
        x for x in os.listdir(Opath)
        if os.path.isfile(os.path.join(Opath, x))
    ])
  
    img1 = Opath+random_filename1
    im1 = Image.open(img1)
    longer_side = max(im1.size)
    basewidth = 800
    img = Image.open(img1)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    im = img.crop(
        (
            half_the_width - 320,
            half_the_height - 320,
            half_the_width + 320,
            half_the_height + 320
        )
    ) 
    
    im.save("output/"+"TEMP-img4.png") 
    #path2 = r"bugs/butterflies/"
    #path2 = r"bugs/advertisements1800/"
    random_filename2 = random.choice([
        y for y in os.listdir(Bpath)
        if os.path.isfile(os.path.join(Bpath, y))
    ])

    img1a = Bpath+"/"+random_filename2
    im1a=Image.open(img1a)
    basewidth = 640
    imga = Image.open(img1a)
    wpercent = (basewidth / float(imga.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    imga = imga.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    half_the_width = imga.size[0] / 2
    half_the_height = imga.size[1] / 2
    img4a = imga.crop(
        (
            half_the_width - 320,
            half_the_height - 320,
            half_the_width + 320,
            half_the_height + 320
        )
    )
    img4a.save("output/"+"TEMP-img4a.png")

    
    background = Image.open("output/"+"TEMP-img4.png").convert("RGBA")
    overlay = Image.open("output/"+"TEMP-img4a.png").convert("RGBA")
 
    background = background.resize((640, 640), PIL.Image.ANTIALIAS)
    overlay = overlay.resize((640, 640), PIL.Image.ANTIALIAS)


    Alpha=(randint(1, 9))*0.1
    new_img = Image.blend(background, overlay, 0.4)

    
    return new_img