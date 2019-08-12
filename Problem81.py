import numpy as np

def readMatrix():
	return np.loadtxt("p081_matrix.txt", dtype='i', delimiter=',')
	return np.array([[131, 673, 234, 103, 18],
		[201, 96, 342, 965, 150],
		[630, 803, 746, 422, 111],
		[537, 699, 497, 121, 956],
		[805, 732, 524, 37, 331]])

def getShortestPath(matrix, row, column, lookUp):
	if row == len(matrix)-1 and column == len(matrix)-1:
		return matrix[len(matrix)-1][len(matrix)-1]
	
	if lookUp[row][column]:
		return lookUp[row][column]

	if column == len(matrix)-1:
		a = getShortestPath(matrix, row+1, column, lookUp) + matrix[row][column]
	elif row == len(matrix)-1:
		a = getShortestPath(matrix, row, column+1, lookUp) + matrix[row][column]
	else:
		a = min(getShortestPath(matrix, row+1, column, lookUp), getShortestPath(matrix, row, column+1, lookUp)) + matrix[row][column]
	lookUp[row][column] = a
	return a


if __name__ == '__main__':
	matrix = readMatrix()
	lookUp = np.zeros((80,80))
	shortestPath = getShortestPath(matrix, row=0, column=0, lookUp=lookUp)
	print(shortestPath)
