import math
import time

def distance(x, y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)

def closest_pair(points):
    n = len(points)

    if n < 2:
        return None
    
    min_dist = float('inf')
    closest_points = None

    for i in range (n-1):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])

            if dist < min_dist:
                min_dist = dist
                closest_points = (points[i], points[j])
    
    return min_dist, closest_points

start = time.perf_counter()

result = closest_pair()

end = time.perf_counter()
