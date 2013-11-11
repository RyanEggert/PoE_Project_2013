## SimpleCVChannelTest

from SimpleCV import *
import time
from numpy import mean


img=Image('C://Users//reggert//Documents//My Box Files//Olin//Year II//POE//Project//testimage.jpg')
imgmat=img.getNumpy()

(red, green, blue)=img.splitChannels(False)

# gt=green.threshold(240)
# bt=blue.threshold(240)
gmat=green.getNumpy()
bmat=blue.getNumpy()
rmat=red.getNumpy()

mx,pts=red.maxValue(True)

rmvpx,rmvpy=zip(*pts)

redx=[]
redy=[]

for n in range(len(pts)):
	bv=bmat[rmvpx[n]][rmvpy[n]][2]
	gv=gmat[rmvpx[n]][rmvpy[n]][1]

	if bv<100 and gv<100:  #if not much blue and green, then it is red
		redx.append(rmvpx[n])
		redy.append(rmvpy[n])

redPTS=zip(redx,redy)

(AvgX,AvgY)=tuple(map(mean, zip(*redPTS)))
AvgMax=(int(AvgX), int(AvgY))

print redPTS
print AvgMax
xtt,ytt=AvgMax
print imgmat[xtt][ytt]

red.drawPoints(redPTS, color=Color.BLUE, sz=1, width=-1)
red.drawPoints([AvgMax], color=Color.BLACK,sz=3,width=-1)
	
d=red.show(type='window')

time.sleep(5)

d.quit()