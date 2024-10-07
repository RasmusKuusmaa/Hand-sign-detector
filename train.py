import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300
while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        
        if imgCrop.size > 0:  
            imgCrop = cv.resize(imgCrop, (imgSize, imgSize))
            imgWhite[0:imgCrop.shape[0], 0:imgCrop.shape[1]] = imgCrop
            
            cv.imshow("Image White", imgWhite)

    cv.imshow("Image", img)
    cv.waitKey(1)