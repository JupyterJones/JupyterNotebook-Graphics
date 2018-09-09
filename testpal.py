from PIL import Image
import time
import os
import sys
from optparse import OptionParser
n=5
# Parse options from the command line
parser = OptionParser()
parser.add_option("-d", "--dst", dest="dst",
                      help="transfer palette palette to ..", metavar="FILE")
parser.add_option("-s", "--src", dest="src", metavar="FILE",
                      help="transfer palette palette from ..")
parser.add_option("-o", "--out", dest="output", metavar="FILE",
                      help="save output to FILE", default="output.png")
(options, args) = parser.parse_args()
if not options.dst or not options.src:
        raise Exception("Missing arguments. See help for more info.")
#dst = "/home/jack/Documents/MechanicalChaos3.png"
#src ="outBorgPalette.jpg"

aa = Image.open(options.dst).convert("RGB")
#bb = Image.open("/home/jack/Documents/GG.jpg").convert("RGB")
bb = Image.open(options.src).convert("RGB")
xx=aa.resize((640,640), Image.NEAREST)
yy=bb.resize((640,640), Image.NEAREST)
xx.save("junk/Pala.png")
yy.save("junk/Palb.png")
src = Image.open('junk/Pala.png').convert('RGB')
dst = Image.open('junk/Palb.png').convert('RGB')
src.save("junk/aa.png")
dst.save("junk/bb.png")
n = 5 #number of partitions per channel.
src_handle = Image.open("junk/bb.png")
dst_handle = Image.open("junk/aa.png")
src = src_handle.load()
dst = dst_handle.load()
assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"

def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l

lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)
print ldst