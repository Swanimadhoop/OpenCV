import cv2 as cv
import numpy as np

blank =  np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#paint image
blank[200:300,300:400]=0,0,255
cv.imshow('green',blank) 

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# Write text
cv.putText(blank, 'Hello, my name is swani!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
