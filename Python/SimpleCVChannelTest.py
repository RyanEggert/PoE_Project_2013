## SimpleCVChannelTest

from SimpleCV import *
import time
from numpy import mean


img=Image('C://Users//reggert//Documents//My Box Files//Olin//Year II//POE//Project//laser_dot.jpg')

(red, green, blue)=img.splitChannels(False)

mx,pts=red.maxValue(True)

(AvgX,AvgY)=tuple(map(mean, zip(*pts)))
print AvgX
print AvgY

AvgMax=(int(AvgX), int(AvgY))

red.drawPoints(pts, color=Color.BLUE, sz=10, width=-1)
red.drawPoints([AvgMax], color=Color.BLACK,sz=3,width=-1)

d=red.show(type='window')

time.sleep(6)

d.quit()