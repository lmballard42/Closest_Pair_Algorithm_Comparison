# -----------------------------------------------------------------
# Closest Pair Problem Algorithm Comparison
#   Authors: Lydia Ballard and Sydney Frisbee
#   Featured Algorithms: 
#       Brute Force
#       Divide and Conquer
#       Line Sweep
#       Bee Colony Optimization (BCO)
#
#   This project explores the different run times of different algorithms 
#   solving the closest pair problem. This is a problem that finds the two 
#   closest points in a metric space, typically using Euclidean distance, 
#   for a set of n points.
#
#   How to Run from command line: 
#       python main.py
#
#   This script runs the 4 algorithms multiple times and writes the output to: 
#       closest_pair_results.csv
#   in the "Results" folder
# -----------------------------------------------------------------


import random
import time
from line_sweep import line_sweep
from brute_force import brute_force
from divide_and_conquer import divide_and_conquer
from bco import bee_colony_optimization
import csv


def generate_dataset(n):
    points = []
    for _ in range(n):
        x = random.uniform(0, 10000)
        y = random.uniform(0, 10000)
        points.append((x, y))
    return points


line_sweep_times = []
brute_force_times = []
divide_and_conquer_times = []
bco_times = []

i = 2


# Loop generates new dataset of n points and then runs each algorithm once
while i <= 4096:
    print(f"\nDataset size: {i} points")
    line_sweep_5_runs = []
    brute_force_5_runs = []
    divide_and_conquer_5_runs = []
    bco_5_runs = []

    for j in range(5):
        print(f"\nDataset {j+1} of 5")
        dataset = generate_dataset(i)

        # Timer to see how long the Brute Algorithm takes
        start = time.perf_counter()
        result = brute_force(dataset)
        end = time.perf_counter()
        print(result)
        print(f"Brute Force: Took {(end - start):0.5f} seconds")
        brute_force_5_runs.append(end-start)

        # Timer to see how long the Divide and Conquer Algorithm takes
        start = time.perf_counter()
        result = divide_and_conquer(dataset)
        end = time.perf_counter()
        print(result)
        print(f"Divide and Conquer: Took {(end - start):0.5f} seconds")
        divide_and_conquer_5_runs.append(end-start)

        # Timer to see how long the Line Sweep Algorithm takes
        start = time.perf_counter()
        result = line_sweep(dataset)
        end = time.perf_counter()
        print(result)
        print(f"Line Sweep: Took {(end - start):0.5f} seconds")
        line_sweep_5_runs.append(end-start)

        # Timer to see how long the Bee Colony Optimzation Algorithm takes
        start = time.perf_counter()
        result = bee_colony_optimization(dataset)
        end = time.perf_counter()
        print(result)
        print(f"Bee Colony Optimization: Took {(end - start):0.5f} seconds")
        bco_5_runs.append(end-start)


    line_sweep_times.append(line_sweep_5_runs)
    brute_force_times.append(brute_force_5_runs)
    divide_and_conquer_times.append(divide_and_conquer_5_runs)
    bco_times.append(bco_5_runs)

    i = i*2



with open("../results/closest_pair_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow([
        "Dataset Size",
        "Trial",
        "Brute Force Times",
        "Divide and Conquer Times",
        "Line Sweep Times",
        "Bee Colony Optimization Times"
    ])

    i = 2
    index = 0

    while i <= 4096:
        for trial in range(5):
            writer.writerow([
                i,
                trial + 1,
                brute_force_times[index][trial],
                divide_and_conquer_times[index][trial],
                line_sweep_times[index][trial],
                bco_times[index][trial]
            ])
        i *= 2
        index += 1


