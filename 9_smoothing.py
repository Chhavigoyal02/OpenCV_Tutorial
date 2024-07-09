import cv2 as cv

img=cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

#Averaging --> here(3,3) shows kernel or filter size
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

#Gaussian Blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gausssian Blur',gauss)

#Median Blur --> here kernel size will not like 7,7 its just int 7
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

#Bilateral
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral Filter',bilateral)

cv.waitKey(0)