# LaserDectFunct.py


def FindLaser(image, BlueThreshold, GreenThreshold):
    """Returns (x,y) tuple corresp. to the avg. of all red pts."""
    from numpy import mean

    # Split into RGB channels. red, green, & blue are image classes
    (red, green, blue) = image.splitChannels(False)

    # Get matrices for each color channel. EX:  gmat[50][70] returns a
    # three-member 'vector' in the form [R,G,B], where R, G, & B are 0-255
    # color values
    gmat = green.getNumpy()
    bmat = blue.getNumpy()
    rmat = red.getNumpy()  # Not used

    # pts is a list of (x,y) tuples which correspond to points where the red
    # channel is at a maximum. mx gives this maximum value. We do not use it.
    mx, pts = red.maxValue(True)

    # Splits pts tuples into two lists, one of x-red max value points, and one
    # of y-red max value points
    rmvpx, rmvpy = zip(*pts)

    # Declares/clears two lists
    redx = []
    redy = []

    # The for-loop evaluates the blue and green value at each max red point.
    # This is because white (255,255,255), (255,255,0), and red(255,0,0) all
    # will appear to be a maximum on the red channel. By checking the B & G
    # values at each point, we can avoid identifying yellow or white areas as
    # lasers.
    for n in range(len(pts)):
        # Could theoretically use image matrix
        bv = bmat[rmvpx[n]][rmvpy[n]][2]
        #Then could be done in one line, 										grabbing two values
        gv = gmat[rmvpx[n]][rmvpy[n]][1]

        # If the blue AND the green value at a point are under their
        # appropriate threshold parameter, then they are confirmed to be
        # sufficiently red, and their coordinates are apppended to lists
        #if not much blue and green, then it is red
        if bv < BlueThreshold and gv < GreenThreshold:
            redx.append(rmvpx[n])
            redy.append(rmvpy[n])

    # Combine the redx and redy coordinates into a list of (x,y) tuples
    redPTS = zip(redx, redy)

    # Calculate the average X and Y value from all the points we confirmed to
    # be red. The try-except statement takes care of scenarios where the
    # function detects no red points. In this case, it passes out it's own
    # AvgX and AvgY values. These can be configured to make it easy for the
    # robot to detect and react to this error (e.g. if AvgMax==(-2,-2): STOP!)
    try:
        (AvgX, AvgY) = tuple(map(mean, zip(*redPTS)))
    except ValueError:
        AvgX = 0
        AvgY = 0

    # Converts the calculated average coordinates to integers (because decimal
    # pixels don't make sense) and saves them as an (x,y) tuple
    AvgMax = (int(AvgX), int(AvgY))

    # Draws all the confirmed red pixels with blue dots. Draws the average of
    #all these points with a larger black point. Displays the original image
    #with the points overlayed. (can be eliminated for RPi running)

    # image.drawPoints(redPTS, color=Color.BLUE, sz=1, width=-1)
    # image.drawPoints([AvgMax], color=Color.BLACK,sz=3,width=-1)
    # image.show(type='window')

    # Return the (x,y) tuple containing the average of all the confirmed red
    # points
    return AvgMax

from SimpleCV import *
import time

cam = Camera()

Timer = time.clock()
while time.clock() < 10:
    img = cam.getImage()
    Max = FindLaser(img, 150, 150)
    print Max
    img.drawPoints([Max], color=Color.BLACK, sz=4, width=-1)
    d = img.show(type='window')
# img=Image('C://Users//reggert//Documents//My Box Files//Olin//Year II//POE//Project//laser_dot.jpg')
d.quit()
