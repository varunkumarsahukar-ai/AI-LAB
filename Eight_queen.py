# Eight Queen Problem Solver using Backtracking

def is_safe(board, row, col):
    n = len(board)

    # Check this column in previous rows
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve_8queens(board, row):
    n = len(board)

    # Base case: All queens are placed
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = "Q"  # Place queen
            if solve_8queens(board, row + 1):
                return True
            board[row][col] = "."  # Backtrack
    return False

# Initialize 8x8 chessboard
board = [["." for _ in range(8)] for _ in range(8)]

if solve_8queens(board, 0):
    print("Solution for 8-Queens Problem:\n")
    for row in board:
        print(" ".join(row))
else:
    print("No solution exists.")