import cv2 as  cv

capture = cv.VideoCapture('(3)img processing using python opencv/images_videos/video.mp4')

while True:
    isTrue, frame = capture.read()
    d =cv.resize(frame,(600,600),fx=0,fy=0,interpolation=cv.INTER_CUBIC)
    #                    H  W    


    #                     from     to
    videoCroped = frame[50:200 , 200:400]


    cv.imshow('video', d)
    cv.imshow('video cropped', videoCroped)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()