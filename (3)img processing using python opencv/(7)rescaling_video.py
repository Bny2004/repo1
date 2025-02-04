import cv2 as  cv

capture = cv.VideoCapture('(3)img processing using python opencv/images_videos/video.mp4')


#rescales the img maintaing the aspect ratio
def reScale(  img,scale=0.1):
    width  = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    dimention = (width,height)

    return cv.resize(img,dimention,interpolation=cv.INTER_AREA)


while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    cv.imshow('video2', reScale(frame))
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



