'''

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. 
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, 
for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; 
the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.

'''

def getCubes(M):
	cubes = {}

	def calculateSides(u,v):
		a = u*u - v*v
		b = 2*u*v
		if a > b:
			a,b = b,a
		c = u*u + v*v
		return a,b,c

	def updateCubes(x,l,n):
		'''
		Here x is the longest side of the cube - hence it corresponds to M
		l is the sum of the lengths of the remaining sides (all smaller than x)
		n is the number of combinations with length l of the remaining sides
		'''
		if x in cubes:
			if l not in cubes[x]:
				cubes[x][l] = n
		else:
			cubes[x] = {l:n}

	def getAllTriangles(a,b,c):
		y = b-a
		if a>=y:
			n = (a-y)//2+1
			updateCubes(a,b,n)

		if b<=M:
			n = a//2
			updateCubes(b,a,n)
			
		# We need to look for the one smaller solution
		if a%2 == 0 and b%2 == 0:
			a/=2
			b/=2
			y=b-a
			if a>=y:
				n = (a-y)//2+1
				updateCubes(a,b,n)

			if b<=M:
				n = a//2
				updateCubes(b,a,n)
			
			a*=2
			b*=2

		# And we need to look for all higher solutions
		n=2
		while n*a<=M:
			a*=n
			b*=n
			y=b-a
			if a>=y:
				m = (a-y)//2+1
				updateCubes(a,b,m)

			if b<=M:
				m = a//2
				updateCubes(b,a,m)
			a/=n
			b/=n
			n+=1

	u = 2
	v = 1
	l = 0

	while True:
		a,b,c = calculateSides(u,v)
		getAllTriangles(a,b,c)
		while (v+1)<u:
			v += 1
			a,b,c = calculateSides(u,v)
			getAllTriangles(a,b,c)
		u+=1
		v=1
		if a > M:
			break
	return cubes


def main():

	# Solution Number 1
	count = 0
	x=2
	while count<10**6:
		x+=1
		for wh in range(3,2*x+1):
			root = ((x*x)+wh*wh)**0.5
			if root.is_integer():
				if wh < x:
					count+=wh//2
				else:
					count+=1+(x-(wh+1)//2)
	print(x)

	# Solution Number 2
	'''
	M = 2000
	cubes = getCubes(M)
	count = 0
	for m in range(1,M+1):
		if m in cubes:
			print(m,cubes[m])
			for i in cubes[m]:
				count+=cubes[m][i]
			if count>10**6:
				print(m)
				break
	'''

if __name__ == '__main__':
	main()




