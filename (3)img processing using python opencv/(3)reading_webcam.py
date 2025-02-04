import cv2 as cv


#when VideoCapture is passed with value of 0 it read the web cam 
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

