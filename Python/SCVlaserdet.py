#SCVlaserdet.py


from SimpleCV import *
import time
from numpy import mean

cam=Camera()

Timer=time.clock()
while time.clock()<20:
	img=cam.getImage()

	(red, green, blue)=img.splitChannels(False)

	mx,pts=red.maxValue(True)

	(AvgX,AvgY)=tuple(map(mean, zip(*pts)))

	AvgMax=(int(AvgX), int(AvgY))

	red.drawPoints(pts, color=Color.BLUE, sz=1, width=-1)
	red.drawPoints([AvgMax], color=Color.BLACK,sz=3,width=-1)

	d=red.show(type='window')

d.quit()