import cv2 as cv
import numpy as np
# EDGE DETECTION
#gradients are edges are different thingsin maths but you can think these are the same things in the programming persepctive only
img=cv.imread('photos/park.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

# Sobel gradient magnitude representation 
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined Sobel',combined_sobel)

# Canny(multi step process it uses sobel in its one of the steps)
# (cleaner version)
canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.waitKey(0)