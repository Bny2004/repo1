import cv2 as cv

img = cv.imread('images/download.jfif')

def rescaleFrame(frame, scale=0.75):
    width =int(frame.shape[1] * scale)
    height =int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img, scale=4)

cv.imshow('taj mahal',img)
cv.imshow('resized taj mahal',resized_img)

cv.waitKey(0)