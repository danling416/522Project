import random
import time
import cProfile
import multiprocessing
import numpy as np
from memory_profiler import profile

def create_matrix(n):
    """
    Create a random n x n matrix of integers between 1 and 10.
    """
    return np.random.randint(1, 11, size=(n, n))

def matrix_game(matrix):
    """
    Play a matrix game where each player chooses a row and a column,
    and the player with the highest value in their chosen cell wins.
    """
    n = matrix.shape[0]
    # Player 1 chooses a row and column
    row1 = np.arange(n)
    col1 = np.random.randint(n, size=n)
    # Player 2 chooses a row and column
    row2 = np.random.randint(n, size=n)
    col2 = np.random.randint(n, size=n)
    # Determine the winner of each round
    player1_score = np.sum(matrix[row1, col1] > matrix[row2, col2])
    player2_score = np.sum(matrix[row1, col1] < matrix[row2, col2])
    # If the values are equal, no one wins
    if player1_score > player2_score:
        return 1
    elif player1_score < player2_score:
        return 2
    else:
        return 0


def main():
    #print("x")
    n = 5000
    matrix = create_matrix(n)
    start_time = time.time()
    winner = matrix_game(matrix)
    end_time = time.time()

# Test the matrix game
if __name__ == '__main__':
    print("\n\n\n\n")
    #main()
    cProfile.run('main()')
    print("\n Done with op_matrix.py")