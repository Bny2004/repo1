import cv2  as cv
import numpy as np

img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
cv.imshow("tree",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("blank",blank)

Mask = cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2), 100, 255, -1)
cv.imshow("mask", Mask)

maskedIMG = cv.bitwise_and(img, img, mask=Mask)
cv.imshow("maskedIMG", maskedIMG)

cv.waitKey(0)
