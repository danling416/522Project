import random
import cProfile
import resource

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Choose a pivot element
    pivot = arr[random.randint(0, len(arr)-1)]
    # Partition the input data around the pivot element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort the left and right partitions
    return quick_sort(left) + middle + quick_sort(right)


# Generate a random list of integers to sort
arr = [random.randint(0, 99) for _ in range(1000000)]
# Use cProfile to measure the runtime and memory usage of quick_sort
print("Quick Sort:")
cProfile.run("quick_sort(arr)")
# Get the maximum resident set size used by the program
max_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print("Maximum resident set size:", max_rss, "bytes")