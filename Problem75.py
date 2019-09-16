'''

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; 
for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

'''

'''
We follow the generation of Pythogarem triplets as described here:
https://www.youtube.com/watch?v=QJYmyhnaaek

'''


def getTriangles(L=int(1.5*10**6)):

	def calculateSides(u,v):
		a = u*u - v*v
		b = 2*u*v
		if a > b:
			a,b = b,a
		c = u*u + v*v
		l = a+b+c
		return a,b,c,l

	def updateTriangle(l,a,b,c):
		if l in triangles:
			if (a,b,c) not in triangles[l]:
				triangles[l].append((a,b,c))
		else:
			triangles[l]=[(a,b,c)]

	def getAllTriangles(l,a,b,c):
		if l<=L:
			updateTriangle(l,a,b,c)
		
		# We need to look for the one smaller solution
		if a%2 == 0 and b%2 == 0:
			l_new = (a+b+c)/2
			if l_new <= L:
				updateTriangle(l_new,a/2,b/2,c/2)

		# And we need to look for all higher solutions
		n = 2
		while n*l<=L:
			if n*l<=L:
				updateTriangle(n*l,n*a,n*b,n*c)
			else:
				break
			n+=1

	triangles = {}
	u = 2
	v = 1
	l = 0
	while l<=2*L:
		a,b,c,l = calculateSides(u,v)
		getAllTriangles(l,a,b,c)
		while (v+1)<u:
			v += 1
			a,b,c,l = calculateSides(u,v)
			getAllTriangles(l,a,b,c)
		u+=1
		v=1
	return triangles


def main():
	triangles = getTriangles()
	count = 0
	for triangle in triangles.values():
		if len(triangle)==1:
			count += 1
	print(count)

if __name__ == '__main__':
	main()




