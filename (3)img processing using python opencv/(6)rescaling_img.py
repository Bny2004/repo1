import cv2 as cv

import cv2  as cv

#captures the  img in var
img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')



#rescales the img maintaing the aspect ratio
def reScale(  img,scale=0.75):
    width  = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    dimention = (width,height)

    return cv.resize(img,dimention,interpolation=cv.INTER_AREA)



#shows the img 
cv.imshow("tree",reScale(img))


cv.waitKey(0)
