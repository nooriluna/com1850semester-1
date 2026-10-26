# Week 1.5, Session 1: Task 3

import math


class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Add distance() method here

    def distance(self):

        return math.hypot(self.x, self.y)
    

    # Add distance_to() method here
    # (This will need a parameter representing another point)

def distance_to(self, point):
    """
    Return distance from this point to specified point
    """
    return math.hypot(self.x - point.x,
                      self.y - point.y)


# Finally, add code here to demonstrate use of Point



p = Point(1.5, 4.2)
q = Point(3.7, 2.6)

print(p.distance_to(q))