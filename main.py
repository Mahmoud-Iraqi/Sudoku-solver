# The game board. Zeros represent empty cells.
board = [
    [0, 0, 0, 0, 0, 0, 6, 4, 0],
    [5, 4, 0, 0, 0, 0, 8, 0, 7],
    [0, 0, 0, 0, 8, 0, 0, 0, 1],
    [9, 0, 0, 0, 6, 0, 0, 7, 0],
    [0, 6, 3, 4, 0, 0, 1, 0, 5],
    [0, 0, 0, 0, 7, 8, 0, 0, 0],
    [0, 0, 4, 1, 0, 0, 0, 0, 0],
    [3, 0, 6, 0, 0, 5, 0, 1, 8],
    [1, 0, 0, 0, 0, 2, 0, 9, 0]
]

def solve(board):
    '''
    Solves the Sudoku board using backtracking.
    
    It first picks an empty cell and attempts to fill it with a valid number (1-9).
    The process repeats until the board is filled. If it gets stuck (i.e., no valid number 
    can be placed), it backtracks by resetting the cell and trying a different number.
    
    Parameters:
        board (list): A 2D list representing the Sudoku board.
    
    Returns:
        bool: True if the board is solved, False otherwise.
    '''
    find = get_empty(board)
    if not find:
        return True  # No empty spaces left, solution found
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True  # Solved

            board[row][col] = 0  # Backtrack

    return False  # Trigger backtracking


def valid(board, num, pos):
    '''
    Checks if placing a number on the board is valid.
    
    It checks the row, column, and 3x3 box to ensure the number doesn't already exist.
    
    Parameters:
        board (list): A 2D list representing the Sudoku board.
        num (int): The number to be placed.
        pos (tuple): The (row, col) position of the cell to be filled.
    
    Returns:
        bool: True if the number is valid, False otherwise.
    '''
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def get_empty(board):
    '''
    Finds the first empty cell on the board (represented by 0).
    
    Parameters:
        board (list): A 2D list representing the Sudoku board.
    
    Returns:
        tuple: A tuple (row, col) representing the position of the first empty cell.
        None: If no empty cells are found.
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Return the first empty cell (row, col)
    return None  # No empty cells found


def print_board(board):
    '''
    Prints the Sudoku board in a readable format with 3x3 grid separators.
    
    Parameters:
        board (list): A 2D list representing the Sudoku board.
    '''
    for i in range(len(board)):

        if i % 3 == 0 and i != 0:
            print('-' * 24)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end='')


# Print the initial board
print_board(board)
print('\n', '#' * 30, "\n")

# Solve the Sudoku and print the solution
solve(board)
print_board(board)
