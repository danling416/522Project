import string as str
import timeit
import os
import psutil

def count_words(str_func):
    my_dic = {}
    # creating the dictionary:
    for letter in str_func.split():
        my_dic[letter] = 0

    # Counting the words:
    for word in str_func.split():
        my_dic[word] += 1
    return my_dic


if __name__ == '__main__':
    str_input = input("Enter a word, phrase or sentence: ")

    # Get the process ID of the current Python process
    pid = os.getpid()
    # Create a Process object for the current process
    process = psutil.Process(pid)
    # Get the memory usage before calling count_words
    before_memory_info = process.memory_info()
    
    # run the function 100 time and calculate the average runtime
    runtime = timeit.timeit(lambda: count_words(str_input), number=100)
    print(f"Average runtime: {runtime/100} seconds")

    words_dic = count_words(str_input)

    # Get the memory usage after calling count_words
    after_memory_info = process.memory_info()
    # Calculate the memory usage difference
    memory_usage = after_memory_info.rss - before_memory_info.rss
    print("Memory usage:", memory_usage, "bytes")

    print("The number of words:")
    print(words_dic)
    total_words = sum(words_dic.values())
    print(f"The total number of words is: {total_words}")