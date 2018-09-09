#!/home/jack/anaconda2/bin/python
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
xx.save("junk/aa.png")
yy.save("junk/bb.png")
src1 = Image.open('junk/aa.png').convert('RGB')
dst1 = Image.open('junk/bb.png').convert('RGB')
src1.save("junk/aa.png")
dst1.save("junk/bb.png")
n = 5 #number of partitions per channel.
src_handle = Image.open("junk/bb.png")
dst_handle = Image.open("junk/aa.png")
src2 = src_handle.load()
dst2 = dst_handle.load()
assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"

def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l

lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)

def sortAndDivide(coordlist,pixelimage,channel): #core
    global src2,dst2,n
    retlist = []
    #sort
    coordlist.sort(key=lambda t: pixelimage[t][channel])
    #divide
    partitionLength = int(len(coordlist)/n)
    if partitionLength <= 0:
        partitionLength = 1
    if channel < 2:
        for i in range(0,len(coordlist),partitionLength):
            retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
    else:
        retlist += coordlist
    

    print(src[lsrc[0]])
    lsrc = sortAndDivide(lsrc,src2,0)
    ldst = sortAndDivide(ldst,dst2,0)

    for i in range(len(ldst)):
        dst2[ldst[i]] = src2[lsrc[i]]
        
def resize640(src):
    Bp=Image.open(src)
    width, height = Bp.size
    w1=int((width-height)/2)
    w2 = int(width-w1)
    h1=height-height
    h2=height
    Cc=Bp.crop((w1,h1,w2,h2))
    result = Cc.resize((640,640), Image.NEAREST)
    return result


dst_handle.save(options.output)
print options.output