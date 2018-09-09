#!/usr/bin/python
# Saves a file as a png with the date and time. Example: 20170621-151523.png
# usage:   img.save(datename())  or newim.save("mydirectory/"+datename()) 
import time
def date_name():
    timename = time.strftime("%Y%m%d-%H%M%S")
    filename = timename+".png"
    return filename