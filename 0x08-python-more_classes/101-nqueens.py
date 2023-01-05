#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """Check if it is safe to place a queen at board[row][col]"""

    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper digonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queen(board, col, N, solutions):
    """Base case: If all queens are placed, return True"""
    if col >= N:
        # Add the current board configuration to the list of solutions
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queen(board, col + 1, N, solutions)
            # If placing queen in board[i][col] doesn't lead to a solution,
            # remove queen from board[i][col]
            board[i][col] = 0


def main():
    """Check if the number of arguments is correct"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    # Check if the argument is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        exit(1)

    # Create an empty board
    board = [[0 for x in range(N)] for x in range(N)]

    # Create a list to store the solutions
    solutions = []

    # Solve the N queens problem
    solve_n_queen(board, 0, N, solutions)

    # Print the solution
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
