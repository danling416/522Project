import time

def search_word(words, target):
    """
    Search for a word in a list of strings.
    """
    matches = []
    for word in words:
        if target in word:
            matches.append(word)
    return matches

words = ["apple", "banana", "orange", "peach", "plum", "grape"]
target = "pe"
print("Searching for words containing '", target, "' in", words)
start_time = time.time()
matches = search_word(words, target)
end_time = time.time()
print("Result:", matches)
print("Time taken:", end_time - start_time, "seconds")
