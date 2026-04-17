# -----------------------------------------------------------------
# Line Sweep Algorithm
# Written by Sydney Frisbee
#
# Description: Initially, all points are sorted based on their x-coordinates. 
#   This allows the "sweep line" to move from left to right, processing points 
#   in an ordered manner. Then it starts iterating over all the points in 
#   increasing order of their x-coordinates.
# -----------------------------------------------------------------

import math

def distance(x, y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)

def line_sweep(points):
    # Have the points sorted by x-coordinate
    points.sort(key=lambda p: p[0])

    # Have all the points in the data set
    active_set = []

    min_dist = float('inf')
    closest_points = None

    # Left pointer for sweep window
    left = 0

    for i in range(len(points)):
        current = points[i]

        # Remove far points in the x-direction
        while left < i and (current[0] - points[left][0]) > min_dist:
            active_set.remove(points[left])
            left += 1

        # Check points in the y-range
        for p in active_set:
            if abs(p[1] - current[1]) < min_dist:
                dist = distance(p, current)
                if dist < min_dist:
                    min_dist = dist
                    closest_points = (p, current)
        
        # Add points to the active set
        active_set.append(current)

    return min_dist, closest_points
