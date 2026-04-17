import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to find the minimum distance in the strip
def strip_closest(strip, d, best_pair):
    min_dist = d
    closest_points = best_pair

    # Sort points in the strip by their y-coordinate
    strip.sort(key=lambda point: point[1])

    # Compare each point in the strip
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) < min_dist:
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    closest_points = (strip[i], strip[j])
            else:
                break

    return min_dist, closest_points

# Divide and conquer function to find the minimum distance
def min_dist_util(points, left, right):
    closest_points = None
    
    # Base case brute force for 2 or fewer points
    if right - left <= 2:
        min_dist = float('inf')
        for i in range(left, right):
            for j in range(i + 1, right):
                d = distance(points[i], points[j])
                if d < min_dist:
                    min_dist = d
                    closest_points = (points[i], points[j])
                
        return min_dist, closest_points

    # Find the midpoint
    mid = (left + right) // 2
    mid_x = points[mid][0]

    left_dist, left_pair = min_dist_util(points, left, mid)
    right_dist, right_pair = min_dist_util(points, mid, right)

    # Choose smaller of two halves
    if left_dist < right_dist:
        min_dist = left_dist
        closest_points = left_pair
    else:
        min_dist = right_dist
        closest_points = right_pair

    # Build strip
    strip = [p for p in points if abs(p[0] - mid_x) < min_dist]

    strip_dist, strip_pair = strip_closest(strip, min_dist, closest_points)

    if strip_dist < min_dist:
        return strip_dist, strip_pair
    else:
        return min_dist, closest_points

# Function to find the closest pair of points
def divide_and_conquer(points):
    n = len(points)

    # Sort points by x-coordinate
    points.sort(key=lambda point: point[0])

    return min_dist_util(points, 0, n)

"""
It is returning the correct distance, but not the correct pair of points
"""