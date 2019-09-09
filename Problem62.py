'''

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''

def cubeFound(number,lookUp):
	n = number**3
	a = sorted([int(x) for x in str(n)])
	s = ''.join([str(x) for x in a])
	if s in lookUp:
		lookUp[s][1]+=1
	else:
		lookUp[s]=[number,1]
	if lookUp[s][1]==5:
		print(lookUp[s][0]**3)
		return True
	else:
		return False


def main():
	n = 1
	lookUp = {}
	while not cubeFound(n,lookUp):
		n+=1

if __name__ == '__main__':
	main()

