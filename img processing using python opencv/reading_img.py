import cv2  as cv

img = cv.imread('images/tree.jpg')

cv.imshow('tree',img)

cv.waitKey(0)