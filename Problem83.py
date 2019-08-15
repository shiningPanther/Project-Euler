import numpy as np
import time


def readMatrix():
	return np.loadtxt("p082_matrix.txt", dtype='i', delimiter=',')
	return np.array([[131, 673, 234, 103, 18],
		[201, 96, 342, 965, 150],
		[630, 803, 746, 422, 111],
		[537, 699, 497, 121, 956],
		[805, 732, 524, 37, 331]])

def updatePaths(matrix, paths, edgeNodes):
	resultFound = False
	matrixSize = len(matrix)
	minPath = 1e8
	row = -1
	column = -1

	# Find which is the edgeNode with the minimum path length so far
	for i in edgeNodes:
		a = paths[i[0]][i[1]]
		if a and a<minPath: 
			minPath = a
			row = i[0]
			column = i[1]

	edgeNodes.remove((row,column))
	a = paths[row][column]

	if row != 0:
		if paths[row-1][column] == 0:
			paths[row-1][column] = a + matrix[row-1][column]
			edgeNodes.insert(-1,(row-1,column))

	if row != matrixSize-1:
		if paths[row+1][column] == 0:
			paths[row+1][column] = a + matrix[row+1][column]
			edgeNodes.insert(-1,(row+1,column))

	if column != 0:
		if paths[row][column-1] == 0:
			paths[row][column-1] = a + matrix[row][column-1]
			edgeNodes.insert(-1,(row,column-1))

	if column != matrixSize-1:
		if paths[row][column+1] == 0:
			paths[row][column+1] = a + matrix[row][column+1]
			edgeNodes.insert(-1,(row,column+1))

	if (row == matrixSize-1 and column == matrixSize-2) or (row == matrixSize-2 and column == matrixSize-1):
		resultFound = True

	'''
	for i in edgeNodes:
		row = i[0]
		column = i[1]
		if row != 0:
			if paths[row-1][column] == 0:
				continue
		if row != matrixSize-1:
			if paths[row+1][column] == 0:
				continue
		if column != 0:
			if paths[row][column-1] == 0:
				continue
		if column != matrixSize-1:
			if paths[row][column+1] == 0:
				continue
		edgeNodes.remove((row,column))
	'''
	
	return resultFound
	


def getShortestPath(matrix):
	matrixSize = len(matrix)
	paths = np.zeros((matrixSize, matrixSize))
	paths[0][0] = matrix[0][0]
	edgeNodes = [(0,0)]

	while True:
		resultFound = updatePaths(matrix,paths,edgeNodes)
		if resultFound:
			break

	return paths[matrixSize-1][matrixSize-1]


if __name__ == '__main__':
	matrix = readMatrix()
	shortestPath = 1e8
	for i in range(len(matrix)):
		temp_shortestPath = getShortestPath(matrix)
		if temp_shortestPath < shortestPath: 
			shortestPath=temp_shortestPath
	print(shortestPath)
