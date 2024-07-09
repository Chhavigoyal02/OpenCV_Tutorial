import cv2 as cv

img=cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)


# converting to greyscale
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# -----------------------------------------------------------

# blur an image
# blurred=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blurred)

# -----------------------------------------------------------

# Edge Cascade
# canny=cv.Canny(blurred,125,175)
# cv.imshow('Canny',canny)

# -----------------------------------------------------------

# Dilating the image
# dilated=cv.dilate(canny,(5,5),iterations=3)
# cv.imshow('Dilated',dilated)

# -----------------------------------------------------------

# Eroding
# eroded=cv.erode(dilated,(3,3),iterations=1)
# cv.imshow('Eroded',eroded)

# -----------------------------------------------------------

# Resize
resized=cv.resize(img,(300,300))
cv.imshow('Resize',resized)

# -----------------------------------------------------------

# Cropping
cropped=img[50:200,200:400]
cv.imshow('Crop',cropped)

cv.waitKey(0)