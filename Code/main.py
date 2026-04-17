import random
import time
from line_sweep import line_sweep
from brute_force import brute_force
from openpyxl import Workbook



def generate_dataset(n):
    points = []
    for _ in range(n):
        x = random.uniform(0, 10000)
        y = random.uniform(0, 10000)
        points.append((x, y))
    return points



line_sweep_times = []
brute_force_times = []
i = 2


# Loop generates new dataset of n points and then runs each algorithm once
while i <= 4096:
    print(f"\nDataset size: {i} points")
    line_sweep_5_runs = []
    brute_force_5_runs = []

    for j in range(5):
        print(f"\nDataset {j+1} of 5")
        dataset = generate_dataset(i)

        # Timer to see how long the Line Sweep Algorithm takes
        start = time.perf_counter()
        result = line_sweep(dataset)
        end = time.perf_counter()
        print(f"Line Sweep: Took {(end - start):0.5f} seconds")
        line_sweep_5_runs.append(end-start)

        # Timer to see how long the Brute Algorithm takes
        start = time.perf_counter()
        result = brute_force(dataset)
        end = time.perf_counter()
        print(f"Brute Force: Took {(end - start):0.5f} seconds")
        brute_force_5_runs.append(end-start)

    line_sweep_times.append(line_sweep_5_runs)
    brute_force_times.append(brute_force_5_runs)

    i = i*2


"""
Add code that would write the "line_sweep_times" and "brute force_times" arrays to a new Exel file 

"""
# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Results"

# Headers
ws.append([
    "Dataset Size",
    "Trial",
    "Line Sweep Time (s)",
    "Brute Force Time (s)"
])

i = 2
index = 0  # tracks dataset size index

while i <= 4096:
    for trial in range(5):
        ws.append([
            i,
            trial + 1,
            line_sweep_times[index][trial],
            brute_force_times[index][trial]
        ])
    i *= 2
    index += 1

# Save file
wb.save("../results/closest_pair_results.xlsx")


