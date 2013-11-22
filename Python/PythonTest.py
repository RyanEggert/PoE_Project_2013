#!/usr/bin/python
foo1 = "Hello world"
foo2 = "bar"
foo3 = {"1": "a",
        "2": "b"}
foo4 = "1+1"

for name in dir():
    myvalue = eval(name)
    print name, "is", type(name), "and is equal to ", myvalue


# AvgSpeed=100
# steering=.1

# RightWheel = (2 * AvgSpeed) / (1 + steering)
# LeftWheel = steering * RightWheel

# print "Right = " + str(RightWheel)
# print "Left = " + str(LeftWheel)
# print (RightWheel+LeftWheel)/2

# if LeftWheel<30:
#     LeftWheel = 30
#     RightWheel = (steering**-1) * LeftWheel

# print "Right = " + str(RightWheel)
# print "Left = " + str(LeftWheel)
# print (RightWheel+LeftWheel)/2



