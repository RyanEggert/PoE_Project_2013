##OpenCV Test

import cv2
import numpy as np
import time


cv2.namedWindow("Default")
img=cv2.cv.LoadImage('C://Users//reggert//Documents//My Box Files//Olin//Year II//POE//Project//laser_dot.jpg')

cv2.imshow("Default",img)

cv2.waitkey(0)

cv2.destroyAllWindows

