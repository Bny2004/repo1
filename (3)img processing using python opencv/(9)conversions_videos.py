import cv2 as  cv

capture = cv.VideoCapture('(3)img processing using python opencv/images_videos/video.mp4')

while True:
    isTrue, frame = capture.read()
    d =cv.resize(frame,(600,600),fx=0,fy=0,interpolation=cv.INTER_CUBIC)
    #                    H  W     
    cv.imshow('video', d)

    #converts from RBG to Gray                          #box named imgGRAY
    imgGray = cv.cvtColor(d,cv.COLOR_RGB2GRAY)
    cv.imshow('imgGRAY',imgGray)
    
    #converts from RBG to BGR                           #box named imgBGR
    imgBGR = cv.cvtColor(d,cv.COLOR_RGB2BGR)
    cv.imshow('imgBGR',imgBGR)

    #converts from RBG to HSV                           #box named imgHSV
    imgGray = cv.cvtColor(d,cv.COLOR_RGB2HSV)
    cv.imshow('imgHSV',imgGray)

    #converts from RBG to LAB                           #box named imgLAB
    imgGray = cv.cvtColor(d,cv.COLOR_RGB2LAB)
    cv.imshow('imgLAB',imgGray)

    #converts from RBG to Canny                         #box named imgCanny
    imgCanny = cv.Canny(d,500,500)
    cv.imshow('imgCanny',imgCanny)
    
    #converts from Canny to Dialated                    #box named imgDialated
    imgDialation =cv.dilate(imgCanny,(3,3),iterations=1)
    cv.imshow('imgDialated',imgDialation)
    
    #applies gaussianBlure                             #box named gaussian blure
    imgBlur = cv.GaussianBlur(d,(9,9),0)
    cv.imshow("gaussian img",imgBlur)
    
    #converts from Dialated to Eroded                  #box named Erode img
    imgErode = cv.erode(imgDialation,(3,3),iterations=1)
    cv.imshow("Erode img",imgErode)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()