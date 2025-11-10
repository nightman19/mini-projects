import copy
import time

# --- 1. The Sudoku Board (0 represents an empty cell) ---
# NOTE: Using the same board. Since this is a known unique puzzle, 
# it will still only find 1 solution, but the code is now ready for 
# puzzles with multiple solutions.
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# ----------------------------------------------------------------------
# Modified Core Function
# ----------------------------------------------------------------------

def solve_all(bo, solutions):
    """
    Modified recursive backtracking function that finds all solutions 
    and stores them in the 'solutions' list.
    """
    find = find_empty(bo)

    # Base case: If no empty spot is found, we found a solution!
    if not find:
        # Crucial step: Store a deep copy of the solved board.
        solutions.append(copy.deepcopy(bo))
        # DO NOT RETURN TRUE. Allow the function to continue and backtrack 
        # to find other solutions.
        return 

    row, col = find

    # Trial and Error (Decision Point)
    for num in range(1, 10):
        if is_valid(bo, num, (row, col)):
            # 1. Place the number (Make a Decision)
            bo[row][col] = num

            # 2. Recursively try to solve the rest of the board
            solve_all(bo, solutions)

            # 3. BACKTRACK: If the recursive call returns (regardless of success), 
            #    reset the cell to 0 to explore the next number in the loop.
            bo[row][col] = 0
            
    # The function implicitly returns None here, allowing the recursion to unwind.


# --- (The rest of the helper functions: is_valid, find_empty, print_board are the same) ---
# Paste the unchanged functions below the solve_all function:

def is_valid(bo, num, pos):
    """
    Checks if a placement is valid according to Sudoku rules.
    """
    row, col = pos
    
    # Check row
    if num in bo[row]:
        return False
        
    # Check column
    for i in range(len(bo)):
        if bo[i][col] == num:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num:
                return False

    return True


def find_empty(bo):
    """
    Finds the next empty spot (represented by 0) on the board.
    Returns (row, col) or None if no empty spots are left.
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def print_board(bo):
    """
    Helper function to print the board in a readable Sudoku format.
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# ----------------------------------------------------------------------
# Modified Execution
# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    all_solutions = [] # List to store all unique solutions
    
    print("Unsolved Board:")
    print_board(board)
    print("\nSolving for ALL possible solutions...\n")
    
    start_time = time.time()
    solve_all(board, all_solutions)
    end_time = time.time()
    
    
    if all_solutions:
        print(f"Found {len(all_solutions)} total solution(s).")
        print("\n--- FIRST Solution Found ---")
        print_board(all_solutions[0])
        
    else:
        print("This Sudoku puzzle is unsolvable.")
    
    print(f"\nTime taken to find all solutions: {end_time - start_time:.4f} seconds")