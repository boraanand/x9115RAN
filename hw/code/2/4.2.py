from swampy.TurtleWorld import *
import math

world = TurtleWorld()
t = Turtle()
t.delay = 0.0000001
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def shift(t,length):
    pu(t)
    fd(t,length)
    pd(t)

def draw_flower(n,length,deg):
    for i in range(n):
	for j in range(2):
	    arc(t,length,deg)
	    lt(t,180-deg)
    	lt(t,360.0/n)

draw_flower(7,100,60)

shift(t,200)

draw_flower(10,80,80)

shift(t,200)

draw_flower(25,400,14)
wait_for_user()
