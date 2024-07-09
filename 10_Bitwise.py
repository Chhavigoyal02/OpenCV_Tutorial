import cv2 as cv
import numpy as np
# (operate in binary manner)
# turn on if its value is 1 and turn off if its value is 0

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#Bitwise AND (return the common or intersecting parts of two images)
bitwise_And=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise And',bitwise_And)

#Bitwise OR (return the both intersecting and non intersecting parts of two images)
bitwise_Or=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise Or',bitwise_Or)

#Bitwise XOR (return the non intersecting parts of two images)
bitwise_XOR=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bitwise_XOR)

# OR-XOR=AND
# OR-AND=XOR

#Bitwise NOT (just invert the binary columns)
rectangle_NOT=cv.bitwise_not(rectangle)
cv.imshow('rectangle NOT',rectangle_NOT)

circle_NOT=cv.bitwise_not(circle)
cv.imshow('circle NOT',circle_NOT)

cv.waitKey(0)