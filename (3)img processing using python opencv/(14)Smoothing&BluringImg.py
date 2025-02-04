import cv2  as cv

img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
cv.imshow("tree",img)

#Averaging
avg = cv.blur(img,(7,7))
cv.imshow("avg",avg)

#gaussianBlure                       
gus= cv.GaussianBlur(img,(7,7),0)
cv.imshow("gaussian img",gus)

#median
med = cv.medianBlur(img, 7 )
cv.imshow("median img",med)

#bilateral
biL = cv.bilateralFilter(img ,10 ,35 ,25)
cv.imshow("bilateral img",biL)

cv.waitKey(0)
