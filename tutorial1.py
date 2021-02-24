import cv2

img = cv2.imread('assets/gertrud.jpg', -1)

# img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite('gertrud90.jpg', img)

cv2.imshow('Gertrud', img)
cv2.waitKey(0)
cv2.destroyAllWindows()