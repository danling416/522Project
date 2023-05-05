import random
import time
import cProfile
from memory_profiler import profile

def create_matrix(n):
    """
    Create a random n x n matrix of integers between 1 and 10.
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, 10))
        matrix.append(row)
    return matrix

def matrix_game(matrix):
    """
    Play a matrix game where each player chooses a row and a column,
    and the player with the highest value in their chosen cell wins.
    """
    n = len(matrix)
    player1_score = 0
    player2_score = 0
    for i in range(n):
        # Player 1 chooses a row and column
        row1 = i
        col1 = random.randint(0, n-1)
        # Player 2 chooses a row and column
        row2 = random.randint(0, n-1)
        col2 = random.randint(0, n-1)
        # Determine the winner of this round
        if matrix[row1][col1] > matrix[row2][col2]:
            player1_score += 1
        elif matrix[row1][col1] < matrix[row2][col2]:
            player2_score += 1
        # If the values are equal, no one wins
    if player1_score > player2_score:
        return 1
    elif player1_score < player2_score:
        return 2
    else:
        return 0

def main():
    n = 5000
    matrix = create_matrix(n)
    start_time = time.time()
    winner = matrix_game(matrix)
    end_time = time.time()

# Test the matrix game
if __name__ == '__main__':
    print("\n\n\n\n")
    cProfile.run('main()')
    print("\n Done with matrix.py")
        
