from SimpleCV import *
import time

cam=Camera()

Timer=time.clock()
while time.clock()<20:
	img=cam.getImage()

	blobs=img.findSkintoneBlobs(minsize=10, maxsize=0,dilate_iter=1)
	blobs.draw()
	d=img.show(type='window')
	

d.quit()	