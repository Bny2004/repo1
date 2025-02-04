import cv2  as cv
import matplotlib.pyplot as plt

img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
cv.imshow("tree",gray)
grayHIST = cv.calcHist([gray], [0] ,None ,[256] ,[0, 256] )
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixcle')
plt.plot(grayHIST)
plt.xlim(0, 256)
plt.show()







