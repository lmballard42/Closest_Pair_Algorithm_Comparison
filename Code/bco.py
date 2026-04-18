# -----------------------------------------------------------------
# Bee Colony Optimization Algorithm
# Written by Lydia Ballard with ChatGPT
#
# Description: A heuristic algorithm that is inspired by the foraging behavior of bees.
#   The algorithm is broken down into 3 separate stages:
#      - Employed Bees: Associated with specific food sources, they explore the neighborhood 
#           of their assigned source to find better, closer pairs.
#	   - Onlooker Bees: Wait in the hive and choose a food source to exploit based on the 
#           information shared by employed bees (waggle dance).
#	   - Scout Bees: If a solution cannot be improved over a set number of cycles ("limit"), 
#           the employed bee abandons it and becomes a scout, searching for a new random pair of points
# -----------------------------------------------------------------

import random
import math

# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate a random pair of indices
def random_pair(n):
    i, j = random.sample(range(n), 2)
    return (i, j)

# Fitness: higher is better (so inverse distance)
def fitness(pair, points):
    d = distance(points[pair[0]], points[pair[1]])
    return 1 / (d + 1e-9)  # avoid division by zero

# Generate neighbor by slightly modifying a pair
def neighbor(pair, n):
    i, j = pair

    if random.random() < 0.5:
        i = (i + random.choice([-1, 1])) % n
    else:
        j = (j + random.choice([-1, 1])) % n

    if i == j:
        j = (j + 1) % n

    return (i, j)

def bee_colony_optimization(points, num_bees=50, max_iter=500, limit=10):
    n = len(points)

    # Initialize food sources (pairs)
    food_sources = [random_pair(n) for _ in range(num_bees)]
    trials = [0] * num_bees

    min_distance = float('inf')
    closest_points = None

    for _ in range(max_iter):

        # --- Employed Bees Phase ---
        for i in range(num_bees):
            new_pair = neighbor(food_sources[i], n)

            if fitness(new_pair, points) > fitness(food_sources[i], points):
                food_sources[i] = new_pair
                trials[i] = 0
            else:
                trials[i] += 1

        # --- Onlooker Bees Phase ---
        fitness_values = [fitness(p, points) for p in food_sources]
        total_fit = sum(fitness_values)

        for _ in range(num_bees):
            probs = [f / total_fit for f in fitness_values]
            i = random.choices(range(num_bees), weights=probs)[0]

            new_pair = neighbor(food_sources[i], n)
            current_fit = fitness(food_sources[i], points)
            new_fit = fitness(new_pair, points)

            if new_fit > current_fit:
                food_sources[i] = new_pair
                trials[i] = 0
            else:
                trials[i] += 1

        # --- Scout Bees Phase ---
        for i in range(num_bees):
            if trials[i] > limit:
                food_sources[i] = random_pair(n)
                trials[i] = 0

        # Track best solution
        for pair in food_sources:
            d = distance(points[pair[0]], points[pair[1]])
            if d < min_distance:
                min_distance = d
                closest_points = pair

    if closest_points is not None:
        p1 = points[closest_points[0]]
        p2 = points[closest_points[1]]
        return min_distance, (p1, p2)
    else:
        return None, None
