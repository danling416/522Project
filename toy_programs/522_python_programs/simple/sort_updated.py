import random
import cProfile
import resource

def counting_sort(arr):
    # Find the range of the input data
    k = max(arr) + 1

    # Create an array to count the frequency of each input value
    count = [0] * k
    for x in arr:
        count[x] += 1

    # Modify the count array to contain the cumulative sum of the frequencies
    for i in range(1, k):
        count[i] += count[i-1]

    # Create a new output array, and fill it with the sorted input values
    output = [0] * len(arr)
    for x in arr:
        output[count[x]-1] = x
        count[x] -= 1

    return output


# Generate a random list of integers to sort
arr = [random.randint(0, 99) for _ in range(1000000)]

# Use cProfile to measure the runtime and memory usage of counting_sort
print("Counting Sort:")
cProfile.run("counting_sort(arr)")# Run your function with cProfile
# Get the maximum resident set size used by the program
max_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print("Maximum resident set size:", max_rss, "bytes")