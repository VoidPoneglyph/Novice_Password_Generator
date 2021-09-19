import numpy as np
grid = [[0,0,0,0,0,0,8,0,0],
        [3,9,0,0,0,2,0,4,5],
        [0,8,0,0,0,7,0,0,6],
        [0,6,3,0,8,0,4,0,0],
        [0,0,8,4,0,0,0,6,0],
        [0,1,0,2,0,9,3,7,0],
        [0,0,0,7,0,0,0,0,0],
        [0,0,1,9,4,0,0,0,0],
        [0,7,2,0,3,5,0,8,0]]

# I'll have to define a set of rules that adhere to Sudoku's game rules. These conditions check whether the number
# can be put in the blank spaces.

def possible(row, column, number):
    global grid      # have to globalise the variable since the grid variable lies outside the function
    for i in range(0,9):  # looping through the columns for a single row(which will be specified later in the program)
        if grid[row][i] == number: # check whether the number is unique in that specific row.
            return False
    for i in range(0,9): # looping through the rows for a single column
        if grid[i][column] == number: # check whether the number is unique in that given column. If not, it returns a
            # a boolean False.
            return False
    # Next. I'll have to check whether the number already exists in a section or not, for this, I need to define section boundaries.

    x0 = (row//3) * 3 # Starting point of the section. Suppose the number is in row 5. (5//3)*3 = 1*3 = 3. This
    # says that the starting row of the section that contains row 5 is 3. The same is applied to columns below
    # this then defines the boundaries of a section
    y0 = (column//3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if grid[x0 + i][y0 + j] == number: # When checking a number, the program gets the specific row and column. From here
                # we can calculate x0 and y0 a.k.a the starting points of rows and columns respectively. From the starting
                # point, it increments by the values of i and j. This basically sweeps the entire section where the number
                # originated and then checks whether the number is unique. If not, returns False.
                return False

    return True # After checking through all those conditions, and if none of them passes as False, then it ultimately
# returns a true value

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(0,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print(np.matrix(grid))

solve()