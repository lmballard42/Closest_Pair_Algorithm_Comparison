# -----------------------------------------------------------------
# Brute Force Algorithm
# Written by Sydney Frisbee
#
# Description: The algorithm figures out the distance between every 
#   possible pair and store the minimum distance found
# -----------------------------------------------------------------

import math

def distance(x, y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)

def brute_force(points):
    n = len(points)

    # If there is not enough points
    if n < 2:
        return None
    
    min_dist = float('inf')
    closest_points = None

    # Loop to compare each point
    for i in range (n-1):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])

            # To see if the distance is smaller than the current minimum distance
            if dist < min_dist:
                min_dist = dist
                closest_points = (points[i], points[j])
    
    return min_dist, closest_points
