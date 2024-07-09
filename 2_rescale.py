import cv2 as cv

img=cv.imread('photos/cat_large.jpg')
# --> image will be opened in new window
# cv.imshow('Cat',img) 
# cv.waitKey(0)


# frame.shape[1] refers to width and frame.shape[0] refers to height and this function works for videos images and live videos
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# resized_image=rescaleFrame(img,scale=0.2)
# cv.imshow('image',resized_image)
# cv.waitKey(0)


capture=cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame=capture.read()
    resized_frame=rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('video resized',resized_frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()



# this function works for live videos only
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)