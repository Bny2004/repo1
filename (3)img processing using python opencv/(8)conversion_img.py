import cv2  as cv

#captures the  img in var
img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')


#shows the img 
cv.imshow("tree",img)

 
#shows the resized video
cv.imshow('img0',img)

#converts from RBG to Gray                          #box named imgGRAY
imgGray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('imgGRAY',imgGray)

#converts from RBG to BGR                           #box named imgBGR
imgBGR = cv.cvtColor(img,cv.COLOR_RGB2BGR)
cv.imshow('imgBGR',imgBGR)

#converts from RBG to HSV                           #box named imgHSV
imgGray = cv.cvtColor(img,cv.COLOR_RGB2HSV)
cv.imshow('imgHSV',imgGray)

#converts from RBG to LAB                           #box named imgLAB
imgGray = cv.cvtColor(img,cv.COLOR_RGB2LAB)
cv.imshow('imgLAB',imgGray)

#converts from RBG to Canny                         #box named imgCanny
imgCanny = cv.Canny(img,125,175)
cv.imshow('imgCanny',imgCanny)

#converts from Canny to Dialated                    #box named imgDialated
imgDialation =cv.dilate(imgCanny,(3,3),iterations=3)
cv.imshow('imgDialated',imgDialation)

#applies gaussianBlure                             #box named gaussian blure
imgBlur = cv.GaussianBlur(img,(9,9),0)
cv.imshow("gaussian img",imgBlur)

#converts from Dialated to Eroded                  #box named Erode img
imgErode = cv.erode(imgDialation,(3,3),iterations=3)
cv.imshow("Erode img",imgErode)


cv.waitKey(0)
