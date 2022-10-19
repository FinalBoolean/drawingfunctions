from calendar import c
import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype='uint8')

cv2.line(img, (10, 20), (200, 405), (255, 1, 255), 20)

cv2.imshow('blank', img)

cv2.waitKey(0)
cv2.destroyAllWindows()