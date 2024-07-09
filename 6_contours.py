import cv2 as cv
import numpy as np

img=cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blurres=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blurres)

# canny=cv.Canny(blurres,125,175)
# cv.imshow('Canny Edges',canny)

# contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contours found!')

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

# here -1 is for all countours
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank) 

cv.waitKey(0)