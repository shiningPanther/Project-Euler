'''

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, 
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

'''

import numpy as np

def readFile():
	with open('p099_base_exp.txt','r') as f:
		for line in f:
			yield [int(x) for x in line.strip().split(',')]

def main():
	maxVal = 0
	maxLine = -1
	for i,element in enumerate(readFile()):
		val = np.log(element[0])*element[1]
		if val > maxVal:
			maxVal = val
			maxLine = i
	print(maxLine+1)


if __name__ == '__main__':
	main()

