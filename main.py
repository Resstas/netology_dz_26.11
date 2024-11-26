import time

def formula_1(x):
    return x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x

def formula_2(x):
    return x + x

def compute_results(iterations):
    results_1 = []
    results_2 = []

    start_time = time.time()
    for x in range(iterations):
        result = formula_1(x)
        results_1.append(result)
    time_formula_1 = time.time() - start_time

    start_time = time.time()
    for x in range(iterations):
        result = formula_2(x)
        results_2.append(result)
    time_formula_2 = time.time() - start_time

    start_time = time.time()
    results_3 = []
    for i in range(iterations):
        result = results_1[i] + results_2[i]
        results_3.append(result)
    time_formula_3 = time.time() - start_time

    return time_formula_1, time_formula_2, time_formula_3

for iterations in [10000, 100000]:
    print("\nIterations:", iterations)
    time_1, time_2, time_3 = compute_results(iterations)
    print("Time for formula 1:", time_1, "seconds")
    print("Time for formula 2:", time_2, "seconds")
    print("Time for formula 3:", time_3, "seconds")