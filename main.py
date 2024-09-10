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

def solve(bo):
    find = get_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1 , 10):
        if valid(bo , i , (row , col)):
            bo[row][col] = i
        
            if solve(bo):
                return True
        
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    row = pos[0] // 3
    col = pos[1] // 3

    for i in range(row*3, row*3 + 3):
        for j in range(col * 3, col*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def get_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def print_board(bo):
    for i in range(len(bo)):

        if i % 3 == 0 and i != 0:
            print('-' * 24)
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(' | ' , end='')

            if j == 8:
                print(str(bo[i][j]))

            else : 
                print(str(bo[i][j])+" " , end='')

print_board(board)
print('\n', '#' * 30 , "\n")
solve(board)
print_board(board)