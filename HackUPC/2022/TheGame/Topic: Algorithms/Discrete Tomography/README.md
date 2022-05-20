## [Topic: Algorithms] Discrete Tomography

### Description
This problem is inspired by this Path Puzzles: Discrete Tomography with a Path Constraint is Hard by Erik Demaine. It is also an attempt to start using Prolog more frequently and getting used to it.
The problem can be considered as a puzzle consists of a (rectangular) grid of cells with two exits (or “doors”) on the boundary and numerical constraints on some subset of the rows and columns. A solution consists of a single non-intersecting path which starts and ends at two boundary doors and which passes through a number of cells in each constrained row and column equal to the given numerical clue.

For example, look at the example below:
This would be the input:

6 # size of a side of the square
3 4 4 3 4 3 # input of the X axis
6 2 3 2 2 6 # inputs of the Y axis
0 0 # starting point
6 6 # goal


The solution:

(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (5,1), (4,1), (4,2), (3,2), (2,2), (2,3), (1,3), (1,4), (0,4), (0,5), (1,5), (2,5), (3,5), (4,5), (5,5)


Can you solve this one? Moreover, to make it more interesting, we have added cells that we can not use.

8
6 4 2 4 8 5 7 7
6 7 8 7 5 5 4 1
0 5
4 7
# cells to be avoided (x,y)
3 1 
5 5 
0 6
1 6 
0 7
2 6 
2 7
7 7 
6 7
1 5
2 5
1 7
2 6
