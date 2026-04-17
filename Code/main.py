import random
import time
from line_sweep import line_sweep
from brute_force import brute_force
from divide_and_conquer import divide_and_conquer
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
i = 2


# Loop generates new dataset of n points and then runs each algorithm once
while i <= 4096:
    print(f"\nDataset size: {i} points")
    line_sweep_5_runs = []
    brute_force_5_runs = []
    divide_and_conquer_5_runs = []

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


    line_sweep_times.append(line_sweep_5_runs)
    brute_force_times.append(brute_force_5_runs)
    divide_and_conquer_times.append(divide_and_conquer_5_runs)

    i = i*2




with open("../results/closest_pair_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow([
        "Dataset Size",
        "Trial",
        "Brute Force Times",
        "Divide and Conquer Times",
        "Line Sweep Times"
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
                line_sweep_times[index][trial]
            ])
        i *= 2
        index += 1


