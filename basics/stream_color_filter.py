import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = (20, 100, 120)
    upper_yellow = (40, 255, 255)

    filtered = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    kernel = np.ones((3,3), np.uint8)
    eroded_mask = cv2.erode(filtered, kernel)
    mask = cv2.dilate(eroded_mask, kernel)
    masked_image = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("filtered", filtered)
    cv2.imshow("mask", mask)
    cv2.imshow("masked_image", masked_image)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.detroyAllWindows()
cap.release()
