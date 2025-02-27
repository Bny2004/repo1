import cv2  as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle  = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle     = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle",circle)

#bitwise AND
bitwiseAND = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise and", bitwiseAND)

#bitwise OR
bitwiseOR = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise or", bitwiseOR)

#bitwise EX-OR
bitwiseEXOR = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise EXOR", bitwiseEXOR)

#bitwise NOT
bitwiseNOT = cv.bitwise_not(rectangle)
cv.imshow("bitwise NOT", bitwiseNOT)
bitwiseNOT = cv.bitwise_not(circle)
cv.imshow("bitwise NOT 2", bitwiseNOT)


cv.waitKey(0)