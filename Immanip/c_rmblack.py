#!/usr/bin/python
# Works Great makes black transparent
import cv2

image_in = "T-20170621-152227.png"
image_out = "NB-T-20170621-152227.png"

src = cv2.imread(image_in, 1)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
b, g, r = cv2.split(src)
rgba = [b, g, r, alpha]
dst = cv2.merge(rgba, 4)
cv2.imwrite(image_out, dst)
