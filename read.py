#read and resize image

import cv2 as cv


def rescaleFrame(frame, scale=0.25):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[1]*scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img= cv.imread('images\stone.png')

resized_image = rescaleFrame(img)
cv.imshow('pic', img)
cv.imshow('resize pic', resized_image)
cv.waitKey(0)


capture=cv.VideoCapture('video\VZYJ2576.MP4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Resize video',frame_resized)

    if cv.waitKey(2) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 
