#!/usr/bin/python
def rm_black(image_in ="20170622-071317.png", image_out = "XCXCXC.png"):
    import cv2    
    src = cv2.imread(image_in, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    cv2.imwrite(image_out, dst)
    return dst