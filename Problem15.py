'''

Project Euler Problem 52:

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

'''

import numpy as np
import sys


print('Script started')


def recursive(i,j):
	if i==0 or j==0:
		return 1
	return recursive(i-1,j) + recursive(i,j-1)

def recursiveArray(i,j,array):
	if i==0 or j==0:
		return 1
	if array[i][j] != 0:
		return array[i][j]
	array[i][j] = recursiveArray(i-1,j,array) + recursiveArray(i,j-1,array)
	return array[i][j]

def bottomUp(i,j):
	paths = np.zeros((i+1,j+1))
	for k in range(i+1):
		for l in range(j+1):
			if k==0 or l==0:
				paths[k][l] = 1
				continue
			paths[k][l]=paths[k-1][l] + paths[k][l-1]
	return paths[i][j]

def binomial(size):
	return factorial(2*size, size)/factorial(size)

def factorial(n, cutoff=0):
	fac = 1
	while n > cutoff:
		fac *= n
		n -= 1
	return fac


def problem15():
	size = 20

	# SOLUTION 1 (too time consuming)
	# return recursive(size,size)

	# SOLUTION 2
	recArray = np.zeros((size+1,size+1))
	#return recursiveArray(size,size,recArray)
	print('RecursiveArray: {}'.format(recursiveArray(size,size,recArray)))

	# SOLUTION 3
	# return bottomUp(size,size)
	print('Bottom Up: {}'.format(bottomUp(size,size)))

	# SOLUTION 4
	solution = binomial(size)
	print('Binomial: {}'.format(binomial(size)))

	return solution


print('Solution is: {}'.format(problem15()))

print('Script ended')
