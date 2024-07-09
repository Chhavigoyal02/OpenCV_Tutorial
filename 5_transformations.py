import cv2 as cv
import numpy as np

img=cv.imread('photos/park.jpg')
cv.imshow('Cat',img)


# Translation
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])  
#     dimensions=(img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)

# # -x -->left
# # -y --> up
# # x --> right
# # y --> down

# translated=translate(img,100,200)
# cv.imshow('translated',translated)

# -----------------------------------------------------------

# Rotation
# def rotate(img,angle,rotPoint=None):
#     (height,width)=img.shape[:2]
#     if rotPoint is None:
#         rotPoint=(width//2,height//2)
#     rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions=(width,height)

#     return cv.warpAffine(img,rotMat,dimensions)

# # anticlockwise(-45 --> clockwise)
# rotated=rotate(img,45) 
# cv.imshow('Rotated',rotated)

# -----------------------------------------------------------

# Resize (same as previous one)

# -----------------------------------------------------------

# Flipping(0 -> vertically,1 -> horizontally, -1 -> both)
flip=cv.flip(img,-1)
cv.imshow('Flipped',flip)

# -----------------------------------------------------------

# Cropping(same as previous one)

cv.waitKey(0)