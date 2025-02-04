import cv2  as cv
import numpy as np


img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
cv.imshow("tree",img)


imgGray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('imgGRAY',imgGray)

#Laplacian
lap = cv.Laplacian(imgGray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

# Soble
sobelx = cv.Sobel(imgGray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(imgGray, cv.CV_64F, 0, 1)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('combine_sobel',combine_sobel)

# Canny
imgCanny = cv.Canny(imgGray,150,175)
cv.imshow('imgCanny',imgCanny)

cv.waitKey(0)