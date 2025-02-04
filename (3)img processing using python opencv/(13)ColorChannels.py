import cv2 as cv
import numpy as np

img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
cv.imshow("tree",img)

b,g,r =cv.split(img)
cv.imshow("treeB",b)
cv.imshow("treeG",g)
cv.imshow("treeR",r)



print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

mergedImg = cv.merge([b,g,r])
cv.imshow("mergedImg",mergedImg)

blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("BImg",blue)
cv.imshow("GImg",green)
cv.imshow("RImg",red)

cv.waitKey(0)