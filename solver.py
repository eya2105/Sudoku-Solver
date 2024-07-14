board=[
       [7,8,0,4,0,0,1,2,0],
       [6,0,0,0,7,5,0,0,9],
       [0,0,0,6,0,1,0,7,8],
       [0,0,7,0,4,0,2,6,0],
       [0,0,1,0,5,0,9,3,0],
       [9,0,4,0,6,0,0,0,5],
       [0,7,0,3,0,0,0,1,2],
       [1,2,0,0,0,7,4,0,0],
       [0,4,9,2,0,6,0,0,7]
       ]
def is_empty(board):
    """
    

    Parameters
    ----------
    board :is list of lists 
        DESCRIPTION.
        representing the soduku grid

    Returns
    -------
    i : integer
        DESCRIPTION.
        the row of the empty position
    j : integer
        DESCRIPTION.
        the col of the empty position
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board,pos,num):
    """
    

    Parameters
    ----------
    board : list of lists
        DESCRIPTION.
        the Suduku grid
    pos : tulipe
        DESCRIPTION.
        representing two integers that represent the position
    num : integer
        DESCRIPTION.
        possible integer to fill into the empty position

    Returns
    -------
    bool
        DESCRIPTION.
        true if that num is possible in the pos position 
        false if it is not

    """
    for i in range(9):
        if board[pos[0]][i] == num and pos[0] != i:
            return False
    for i in range(9):
        if board[i][pos[1]] == num and pos[1] != i:
            return False
    for i in range(pos[0]//3*3, pos[0]//3*3+3):
        for j in range(pos[1]//3*3, pos[1]//3*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(board):
    """
    Parameters
    ----------
    board : list of lists
        DESCRIPTION.
        the sudoku board 
    Returns
    -------
    bool
        DESCRIPTION.
        true if the board is solved 
        false if there are empty position

    """
    empty = is_empty(board)
    if empty:
        row, col = empty
    else:
        return True
    for k in range(1, 10):
        if is_valid(board, (row, col), k):
            board[row][col] = k
            if solve(board):
                return True
            board[row][col] = 0
    return False
    
        
def print_board(board):
    """

    Parameters
    ----------
    board : list of lists
        DESCRIPTION.
        board of the sudoku
    Returns
    -------
    None.
    it prints the sudoku board

    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")


            
    
    
    

print_board(board)
solve(board)   
print('\n')
print("solved board")
print_board(board)
