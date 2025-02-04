import cv2 as cv
import numpy as np

img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
print(img.shape)


#resizes the img with the provided parameters
imgResize = cv.resize(img,(240,240), interpolation= cv.INTER_CUBIC)
#interpotion =  cv.INTER_AREA      //for changing big to small
#            =  cv.INTER_LINEAR    //for changing small to big
#            =  cv.INTER_CUBIC     //slow but better quality

#                from     to
imgCroped = img[50:200 , 200:400]

cv.imshow('tree',img)
cv.imshow('img resize',imgResize)
cv.imshow('cropped',imgCroped)



cv.waitKey(0)

#480, 771, 3