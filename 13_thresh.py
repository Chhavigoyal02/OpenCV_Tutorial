import cv2 as cv
# thresholding means binarizing the images
img=cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple thresholding(here if above above 159 convert it to 255(1) otheriwse 0)
# threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
# cv.imshow('Simple Thresholded',thresh)

# threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
# cv.imshow('Simple Thresholded Inverse',thresh_inv)

# ---------------------------------------------------------------------
# Adapted Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('Adaptive thresholding',adaptive_thresh)

cv.waitKey(0)