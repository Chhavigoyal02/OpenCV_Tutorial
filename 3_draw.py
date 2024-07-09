import cv2 as cv
import numpy as np

# we can also create dummy image if we want like:(datatype of image is uint8)
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# 1.paint the image a certain colour(0,255,0 represents color)
# blank[:]=0,255,0  --> (by colon it mean we are referinf all the pixels in image)
# blank[200:300,300:400]=0,0,255
# cv.imshow('Colored ',blank)


# 2.draw a rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=4) --> hollow rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)

#3. draw a circle
# cv.circle(blank,(250,250),40,(0,0,255),thickness=cv.FILLED)
# cv.imshow('Circle',blank)

# 4. draw a line
# cv.line(blank,(0,0),(250,250),(0,0,255),thickness=4)
# cv.imshow('Line',blank)

# 5.write text on image
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,60,255),thickness=4)
cv.imshow('text',blank)

cv.waitKey(0)