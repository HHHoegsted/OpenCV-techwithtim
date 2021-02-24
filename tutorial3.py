import numpy as np
import cv2

cap = cv2.VideoCapture('assets/sample-mp4-file.mp4')

while True:
	ret, frame = cap.read()
	width, height = int(cap.get(3)), int(cap.get(4))
	smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)

	img = np.zeros(frame.shape,np.uint8)
	img[:height//2, :width//2] = smaller_frame
	img[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
	img[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
	img[height//2:, width//2:] = smaller_frame


	cv2.imshow('Video', img)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()