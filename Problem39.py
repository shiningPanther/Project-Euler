'''

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

'''

For another (and probably more clever) way to do this look at:
https://www.youtube.com/watch?v=QJYmyhnaaek

'''


if __name__ == '__main__':
	count = {1:1}
	a = 1
	b = 1
	c = 1
	for b in range(2,500):
		for a in range(2,b):
			c = (a**2 + b**2)**0.5
			if c.is_integer():
				p = a + b + c
				if p > 1000:
					break
				if p in count:
					count[p] += 1
				else:
					count[p] = 1
	maxCount = 1
	maxP = 0
	for p, value in count.items():
		if value > maxCount:
			maxP = p
			maxCount = value
	print(maxP, maxCount)





