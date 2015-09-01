from __future__ import division, print_function
import math
from swampy.TurtleWorld import *

def main():
    world = TurtleWorld() 
    bob = Turtle()
    bob.delay = 0.0001
    
    #draw flowers
    draw_flower(bob, 7,100,60)
    shift(bob,200)
    draw_flower(bob, 10,80,80)
    shift(bob,200)
    draw_flower(bob, 25,400,14)

    pu(bob)
    rt(bob, 90)
    fd(bob, 200)
    rt(bob, 90)
    fd(bob, 400)
    rt(bob, 180)
    pd(bob)

    #draw polygons   
    polygon_with_radius_line(bob, 5, 80)  
    pu(bob)
    fd(bob, 200)
    pd(bob)
    polygon_with_radius_line(bob, 6, 80)
    pu(bob)
    fd(bob, 200)
    pd(bob)
    polygon_with_radius_line(bob, 7, 80) 
    wait_for_user()

def draw_flower(t, n,length,deg):
    for i in range(n):
        for j in range(2):
            arc(t,length,deg)
            lt(t,180-deg)
        lt(t,360.0/n)

def polygon_with_radius_line(t, n, radius):
    """ Draw a polygon and its radius line
    
    t: Turtle object
    n: number of sides
    radius: radius of polygon
    """
    s = 2 * radius * math.sin(math.pi/n)
    #sum_of_interior_angles = 180 * (n-2)
    angle = (180 - 360/n)/2

    for i in range(n):
        fd(t, radius)
        rt(t, 180 - angle)
        fd(t, s)
        rt(t, 180 - angle)
        fd(t, radius)
        rt(t, 180)

def shift(t, length):
    pu(t)
    fd(t,length)
    pd(t)

def polygon(t, n, radius):
    """ Draw a polygon
    
    t: Turtle object
    n: number of sides
    radius: radius of polygon
    """
    s = radius * 2 * math.sin(180/n)
    sum_of_interior_angles = 180 * (n-2)
    angle = 180 - sum_of_interior_angles / n

    for i in range(n):
        fd(t, s)
        lt(t, angle)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

if __name__ == '__main__':
    main()