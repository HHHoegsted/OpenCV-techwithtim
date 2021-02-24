import numpy as np
import cv2

cap = cv2.VideoCapture('assets/sample-mp4-file.mp4')

while True:
	ret, frame = cap.read()
	width, height = int(cap.get(3)), int(cap.get(4))

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([90,50,50])
	upperblue = np.array([130,255,255])

	mask = cv2.inRange(hsv, lower_blue, upperblue)
	result = cv2.bitwise_and(frame, frame, mask = mask)

	cv2.imshow('Video', result)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

cv2.cvtColor([[[255,0,0]]], cv2.COLOR_BGR2HSV)