import cv2 as cv

img=cv.imread('photos/group 2.jpg')
cv.imshow('Group',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade=cv.CascadeClassifier('15_haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)

print(f'Number of faces = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Images',img)

cv.waitKey(0)