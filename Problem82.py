'''

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, 
and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

'''



import numpy as np
import time


def readMatrix():
	return np.loadtxt("p082_matrix.txt", dtype='i', delimiter=',')
	return np.array([[131, 673, 234, 103, 18],
		[201, 96, 342, 965, 150],
		[630, 803, 746, 422, 111],
		[537, 699, 497, 121, 956],
		[805, 732, 524, 37, 331]])

def updateTable(matrix, table, potentialPosition):
	minTable = 1e8
	row = -1
	column = -1
	for i in potentialPosition:
		a = table[i[0]][i[1]]
		if a and a<minTable: 
			minTable = a
			row = i[0]
			column = i[1]

	# Abort condition
	if column == 0:
		return False

	potentialPosition.remove((row,column))
	a = table[row][column]
	
	if table[row][column-1] == 0:
		table[row][column-1] = a+matrix[row][column-1]
		potentialPosition.insert(-1,(row,column-1))

	if row != len(matrix)-1 and table[row+1][column] == 0:
		table[row+1][column] = a + matrix[row+1][column]
		potentialPosition.insert(-1,(row+1,column))

	if row != 0 and table[row-1][column] == 0:
		table[row-1][column] = a + matrix[row-1][column]
		potentialPosition.insert(-1,(row-1,column))

	for i in potentialPosition:
		row = i[0]
		column = i[1]
		if row == 0:
			if table[row+1][column] and table[row][column-1]:
				potentialPosition.remove((row,column))
		elif row == len(matrix)-1:
			if table[row-1][column] and table[row][column-1]:
				potentialPosition.remove((row,column))
		elif table[row+1][column] and table[row-1][column] and table[row][column-1]:
			potentialPosition.remove((row,column))
	
	return True
	


def getShortestPath(matrix, row):
	table = np.zeros((len(matrix), len(matrix)))
	table[row][-1] = matrix[row][-1]
	potentialPosition = [(row,len(matrix)-1)]
	column=1
	while column:
		column = updateTable(matrix,table,potentialPosition)

	minPath=1e8
	for i in range(len(matrix)):
		if table[i][0] != 0 and table[i][0] < minPath: 
			minPath = table[i][0]
	return minPath


if __name__ == '__main__':
	matrix = readMatrix()
	shortestPath = 1e8
	for i in range(len(matrix)):
		temp_shortestPath = getShortestPath(matrix, i)
		if temp_shortestPath < shortestPath: 
			shortestPath=temp_shortestPath
	print(shortestPath)
