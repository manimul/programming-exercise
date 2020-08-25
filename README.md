# Programming Exercise

## Description
This is a programming exercise that simulates the movement of an object within a matrix based on a set of input commands.
It requires python3

## Input Commands
Start by entering 4 numbers, seperated by commas
- The first two number represent the width and height of the matrix, the second two are the x and y starting coordinates of the object
Follow this by entering a set of numbers, seperated by commas
- These numbers will command the movement are orientation of the object
0 = quit simulation and print results to stout
1 = move forward one step
2 = move backwards one step
3 = rotate clockwise 90 degrees (eg north to east)
4 = rotate counterclockwise 90 degrees (eg west to south)

## Output
The output will show the final coordinates of the object if on the matrix, or [-1,-1] if out of bounds.