import cv2  as cv
import matplotlib.pyplot as plt

img = cv.imread('(3)img processing using python opencv/images_videos/tree.jpg')
cv.imshow("img", img)

plt.figure()
plt.title('RGBscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixcle')


color = ('b', 'g', 'r')
for i,col in enumerate(color):
    HIST = cv.calcHist([img], [i] ,None ,[256] ,[0, 256] )
    plt.plot(HIST, color= col)
    plt.xlim(0, 256)

plt.show()

