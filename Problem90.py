'''
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. 
By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 
01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} 
allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set 
{1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
'''

import numpy as np
from timeit import default_timer as timer

def initialize_cubes():
	cubes = np.empty([210,6],dtype=int)
	cube = np.empty(6,dtype=int)
	cube_number = 0
	for d1 in range(0,5):
		cube[0] = d1
		for d2 in range(d1+1,6):
			cube[1] = d2
			for d3 in range(d2+1,7):
				cube[2] = d3
				for d4 in range(d3+1,8):
					cube[3] = d4
					for d5 in range(d4+1,9):
						cube[4] = d5
						for d6 in range(d5+1,10):
							cube[5] = d6
							cubes[cube_number,:] = cube
							cube_number+=1
	return cubes

def check_combinations(cubes):
	squares = [[0,1],[0,4],[0,6],[1,6],[2,5],[3,6],[4,6],[6,4],[8,1]]
	number_solutions = 0
	for i1 in range(len(cubes)):
		cube1 = cubes[i1,:]
		cube1[np.where(cube1==9)] = 6
		for i2 in range(i1,len(cubes)):
			cube2 = cubes[i2,:]
			cube2[np.where(cube2==9)] = 6
			for square in squares:
				if not (square[0] in cube1 and square[1] in cube2) and not (square[0] in cube2 and square[1] in cube1):
					break
				if square == [8,1]:
					number_solutions += 1
	return number_solutions

start = timer()
cubes = initialize_cubes()
print(check_combinations(cubes))
end = timer()
print(end-start)

