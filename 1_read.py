import cv2 as cv
# Reading images
# img=cv.imread('photos/cat_large.jpg')
# cv.imshow('Cat',img) --> image will be opened in new window
# cv.waitKey(0) --> new window will not close untill any key is pressed
# Reading videos
capture=cv.VideoCapture('videos/dog.mp4')
# capture=cv.VideoCapture(0) --> for web cam
while True:
    isTrue, frame=capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()