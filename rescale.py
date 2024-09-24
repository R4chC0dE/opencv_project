import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow("Cat", img)

def rescaleFrame(frame, scale=0.75):
    # works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


def changeRes(capture, width, height):
    # only works for live videos
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture("Videos/dog.mp4")

while capture.isOpened():
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
