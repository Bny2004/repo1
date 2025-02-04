import cv2  as cv
import numpy as np


img = cv.imread('(3sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss)img processing using python opencv/images_videos/tree.jpg')
imgBlur = cv.GaussianBlur(img,(9,9),0)
imgCanny = cv.Canny(img,125,155)
cv.imshow('imgCanny without blur',imgCanny)


imgCanny = cv.Canny(imgBlur,125,155)
cv.imshow('imgCanny with blur',imgCanny)
contours , hierarchies = cv.findContours(imgCanny, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
#RETR_LIST        //returns all contours
#RETR_EXTERNAL    //returns external contours
#RETR_TREE        //returns hierarchical contours

#   approxcimaton method
#cv.CHAIN_APPROX_NONE       //returns all counters
#cv.CHAIN_APPROX_SIMPLE     //returns compressed counters whitch make most sence

print(f'{len(contours)} contour(s) found')

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("contourimg",blank)

###     Non-Blure Contours     ###

# imgCanny = cv.Canny(img,125,155)
# contours , hierarchies = cv.findContours(imgCanny, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found')
# blank = np.zeros(img.shape, dtype='uint8')
# cv.drawContours(blank,contours,-1,(0,0,255),2)
# cv.imshow("contourimg2",blank)

cv.waitKey(0)