puzzle = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def find_empty_cell(grid):
    """
    Finds the first empty position (0) in the Sudoku grid.
    Returns None if there are no empty positions.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_move_valid(grid, position, num, row_sets, col_sets, block_sets):
    """
    Checks if a number can be placed at a given position.
    Uses sets to track numbers already used in rows, columns, and subgrids.
    """
    row, col = position
    block_index = (row // 3) * 3 + (col // 3)
    
    if num in row_sets[row] or num in col_sets[col] or num in block_sets[block_index]:
        return False
    return True


def solve_sudoku(grid):
    """
    Solves the Sudoku puzzle using backtracking.
    Returns True if the board is solved, False if unsolvable.
    """
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    block_sets = [set() for _ in range(9)]
    
    # Initialize sets with existing numbers
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                row_sets[i].add(grid[i][j])
                col_sets[j].add(grid[i][j])
                block_sets[(i // 3) * 3 + (j // 3)].add(grid[i][j])

    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # No empty cells left
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_move_valid(grid, (row, col), num, row_sets, col_sets, block_sets):
            # Place the number
            grid[row][col] = num
            row_sets[row].add(num)
            col_sets[col].add(num)
            block_sets[(row // 3) * 3 + (col // 3)].add(num)
            
            # Recursively try to solve the board
            if solve_sudoku(grid):
                return True
            
            # Undo the move if it leads to no solution
            grid[row][col] = 0
            row_sets[row].remove(num)
            col_sets[col].remove(num)
            block_sets[(row // 3) * 3 + (col // 3)].remove(num)
    
    return False


def display_board(grid):
    """
    Prints the Sudoku board in a readable format.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j], end="\n")
            else:
                print(str(grid[i][j]) + " ", end="")

# Solve and print the solved board
print("Original Puzzle:")
display_board(puzzle)
if solve_sudoku(puzzle):
    print("\nSolved Puzzle:")
    display_board(puzzle)
else:
    print("\nNo solution exists.")
