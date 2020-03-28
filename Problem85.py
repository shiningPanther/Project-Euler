'''

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

'''

def rectangles(x,y):
	n = 0
	for lx in range(1,x+1):
		tempx=1+x-lx

		for ly in range(1,y+1):
			tempy = tempx
			tempy = (1+y-ly)*tempx
			n+=tempy

	return n


def main():
	dif = 10**4
	x = 1
	while rectangles(x,1)<2*10**6:
		x+=1
		for y in range(1,x+1):
			n = rectangles(x,y)
			if abs(2*10**6 - n) < dif:
				dif=abs(2*10**6-n)
				print(x,y,n,dif)
			if n>2*10**6:
				break



if __name__ == '__main__':
	main()




