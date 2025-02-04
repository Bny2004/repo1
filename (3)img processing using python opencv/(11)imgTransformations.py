import cv2  as cv
import numpy as np

#captures the  img in var
img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')

#translation
def translate (img , x, y) :
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1],img.shape[0])

    return cv.warpAffine(img,transMat,dimentions)
#  -x --> shift to left
#  +x --> shift to right
#  -y --> shift to down
#  +y --> shift to up

#Rotation
def rotate (img , angle , rotPoint= None):
    (height , width) = img.shape[:2]

    if rotPoint is None:
        rotPoint= (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimentions = (width,height)

    return cv.warpAffine(img,rotMat,dimentions)
#Rotates counterclockwise


#fliping
flip = cv.flip(img,0)
# 0 -->  flips vertically
# 1 -->  flips horizontally
#-1 --> flips vertically and horizontally

#shows the img 
cv.imshow("tree",img)   
cv.imshow("imgTranslate", translate(img , 100,100))
cv.imshow("imgRotated", rotate(img,-90))
cv.imshow("imgRotatedRotated",rotate(rotate(img,-45),-45))
cv.imshow("flip",flip)   


cv.waitKey(0)
