import cv2 as cv
import numpy as np

#                  H   W  No of colour channelsS
blank = np.zeros((500,500,3),dtype='uint8')

cv.imshow('blank',blank)


# changes colour of img
#         B  G  R               
blank[:]= 255,0,0
cv.imshow('Blue',blank)

# blank[:]= 0,255,0                                                           #uncomment to use 
# cv.imshow('Green',blank)

# blank[:]= 0,0,255       
# cv.imshow('Red',blank)

blank[250:300 , 300:400]= 0,0,0
cv.imshow('Blue2',blank)


blank[:]= 0,0,0
#             imgname    coordinates colour
cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=1)                    #rectangle
cv.circle(blank,(250,250),50,(255,0,0), thickness=1)                          #circle
cv.line(blank,(125,50),(300,300),(255,255,255),thickness=1)                   #slant linge eg
cv.line(blank,(125,50),(300,50),(255,255,255),thickness=1)                    #horizontal line eg
cv.line(blank,(300,50),(300,300),(255,255,255),thickness=1)                   #vertical line eg
cv.putText(blank,'hello',(225,225),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Blank2',blank)

blank[:]= 0,0,0


cv.waitKey(0)