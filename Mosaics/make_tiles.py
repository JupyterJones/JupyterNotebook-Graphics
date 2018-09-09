#!/usr/local/bin/python
#GOOD DO NOT TOUCH
def maketiles(quantity):
    from PIL import Image
    from PIL import ImageDraw
    from random import randint
    from Mosaics import datename
    from time import sleep
    counter = 0
    while counter <= quantity:
        #Bcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
        Bcolor = (randint(10, 155), randint(11, 155), randint(1, 155))
        im = Image.new('RGB', (50,50), (Bcolor))
        transparent_area = (randint(0, 50), randint(0, 50), randint(5, 50), randint(5, 50))

        mask=Image.new('1', im.size, color=255)
        draw=ImageDraw.Draw(mask) 
        draw.rectangle(transparent_area, fill=0)
        im.putalpha(mask)

        color2 = (randint(0, 155), randint(0, 155), randint(0, 155))
        overlay = Image.new('RGB', (50,50), (color2))

        sav = Image.composite(im, overlay, im)
        sleep(1)
        filename = "mosaic/"+datename.date_name()
        sav.save(filename)

        h = randint(15, 20)
        v = randint(25, 50)
        color = (randint(10, 155), randint(0, 155), randint(10, 155))

        im = Image.new('RGB', (50,50), (color))
        x, y =  im.size
        eX, eY = h, v #Size of Bounding Box for ellipse
        bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
        draw = ImageDraw.Draw(im)
        color2 = (randint(2, 155), randint(2, 155), randint(2, 155))
        draw.ellipse(bbox, fill=color2)
        sleep(1)
        filename = "mosaic/"+datename.date_name()
        im.save(filename)

        counter = counter +1
        