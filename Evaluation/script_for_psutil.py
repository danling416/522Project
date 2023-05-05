import os
import psutil

sympy_dir = '/Users/danling/Desktop/sympy'

def analyze_file(filename):
    # Use psutil to analyze the file
    # For example:
    with open(filename, 'r') as f:
        lines = f.readlines()
    num_lines = len(lines)
    memory_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024  # in MB
    print(f"{filename}: {num_lines} lines, {memory_usage:.2f} MB")
def analyze_directory(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                full_path = os.path.join(dirpath, filename)
                analyze_file(full_path)

if __name__ == '__main__':
    analyze_directory(sympy_dir)