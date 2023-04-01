import cv2 as cv

capture = cv.VideoCapture(0)

def  changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

while True:
    isTrue, frame = capture.read()
    frame_rezo = changeRes(2,2)


    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)
    cv.imshow('rereso', frame_rezo)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()