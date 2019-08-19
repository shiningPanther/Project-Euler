'''

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''


if __name__ == '__main__':
	total = 0
	counter = 0
	skipSize = 1
	skip = 1
	for n in range(1,1001*1001+1):
		if n == 1:
			total+=1
			continue
		if skip >= 1:
			skip-=1
			continue
		total += n
		counter += 1
		if counter == 4:
			counter = 0
			skipSize += 2
		skip = skipSize
	print(total)


	








