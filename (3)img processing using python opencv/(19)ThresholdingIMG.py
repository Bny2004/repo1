import cv2  as cv


img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
cv.imshow("tree",img)

imgGray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('imgGRAY',imgGray)

#simple Thersholding
threshold, thresh = cv.threshold(imgGray, 100, 255, cv.THRESH_BINARY)
cv.imshow("simple thresh", thresh)

threshold, thresh_inv = cv.threshold(imgGray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple thresh ", thresh_inv)


#adaptive thresholding
addaptive_thresh = cv.adaptiveThreshold(imgGray,                    
                                        255, 
                                        cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv.THRESH_BINARY_INV, 
                                        11, 
                                        9)
cv.imshow("Adaptive thresholding", addaptive_thresh)


cv.waitKey(0)

