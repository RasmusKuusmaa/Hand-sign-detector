import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        imgCrop = img[y - offset:y+h + offset, x - offset:x+w+offset]
        if imgCrop.size > 0:
            cv.imshow('Cropped Image', imgCrop)
    cv.imshow("image", img)
    cv.waitKey(1)