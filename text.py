import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype='uint8')

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Nathan Hathaway", (50, 50), font, 1, (255, 0, 0), 5, cv2.LINE_AA)

cv2.imshow("blank", img)

cv2.waitKey(0)
cv2.destroyAllWindows()