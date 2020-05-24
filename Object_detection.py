import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while(True):
    #frame = cv2.imread('smarties.png')
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerHue = cv2.getTrackbarPos('LH', 'Tracking')
    lowerSaturation = cv2.getTrackbarPos('LS', 'Tracking')
    lowerValue = cv2.getTrackbarPos('LV', 'Tracking')
    upperHue = cv2.getTrackbarPos('UH', 'Tracking')
    upperSaturation = cv2.getTrackbarPos('US', 'Tracking')
    upperValue = cv2.getTrackbarPos('UV', 'Tracking')

    #lowerBoundBlue = np.array([110, 50, 50])
    #upperBoundBlue = np.array([130, 255, 255])

    lowerBound = np.array([lowerHue, lowerSaturation, lowerValue])
    upperBound = np.array([upperHue, upperSaturation, upperValue])

    mask = cv2.inRange(hsv, lowerBound, upperBound)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
