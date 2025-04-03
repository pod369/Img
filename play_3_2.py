# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('river.jpg')
h=cv.calcHist([img], [2], None, [256], [0,256])
plt.plot(h,color='r',linewidth=1)