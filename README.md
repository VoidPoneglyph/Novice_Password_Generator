# Sudoku_solver
This is a program made to solve a 9X9 grid of Sudoku using its rules. I've implemented a function called "Possibility", that checks the three most important conditions assoicated
with sudoku.
1. Every row has numbers from 1 to 9 and no number should be repeating in a given row.
2. Every column has numbers from 1 to 9 and no number should be repeating in a single given row.
3. This 9X9 grid is further divided into 6 3X3 grids that are called sections. Each section consists of numbers from 1 to 9 but just like in the first 2 steps, no number should
repeat in a single section.

Lastly, we defined a function called "solve" which uses the above function as a filter and finds possible solutions in every space not inherited by another number other than zero.
