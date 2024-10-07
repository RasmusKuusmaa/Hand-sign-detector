import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    cv.imshow("image", img)
    cv.waitKey(1)