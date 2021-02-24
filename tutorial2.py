import cv2
import random

img = cv2.imread('assets/gertrud.jpg', -1)

# INSERTING RANDOM PIXELS IN THE FIRST 100 LINES
# for i in range(100):
# 	for j in range(img.shape[1]):
# 		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# COPYING FROM ONE AREA OF THE IMAGE TO ANOTHER
# tag = img[200:300, 300:400]
# img[100:200, 200:300] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()