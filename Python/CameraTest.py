# CameraTest.py

import SimpleCV as scv
import numpy as np

cam = scv.Camera(0)

img = cam.getImage()

(Red, Green, Blue) = img.splitChannels(grayscale=False)
rmat = Red.getNumpy()
Sliced = rmat[:, :, 0]
MaxVal = np.max(Sliced)
x, y = np.where(Sliced == MaxVal)
print zip(x.tolist(), y.tolist())

print img.size()