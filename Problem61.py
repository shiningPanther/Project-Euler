'''

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 		P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

- The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
- Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
- This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
is represented by a different number in the set.

'''

def update(candidates):
	c = candidates[-1]
	candidates.remove(c)

	if all([x in c[1] for x in ['tri','square','penta','hexa','hepta']]):
		if c[0][-1]%100 == c[0][0]//100:
			print(c)
			print(sum(c[0]))
			candidates.clear()

	if 'tri' not in c[1]:
		minTri = c[0][-1]%100*100+1
		maxTri = minTri+98
		for i in range(200):
			tri = triangle(i)
			if tri < minTri:
				continue
			elif tri > maxTri:
				break
			elif tri > 1000:
				temp1 = c[0].copy()
				temp1.append(tri)
				temp2 = c[1].copy()
				temp2.append('tri')			
				candidates.append([temp1,temp2])

	if 'square' not in c[1]:
		minSquare = c[0][-1]%100*100+1
		maxSquare = minSquare + 98
		for i in range(200):
			sq = square(i)
			if sq < minSquare:
				continue
			elif sq > maxSquare:
				break
			elif sq > 1000:
				temp1 = c[0].copy()
				temp1.append(sq)
				temp2 = c[1].copy()
				temp2.append('square')			
				candidates.append([temp1,temp2])

	if 'penta' not in c[1]:
		minPenta = c[0][-1]%100*100+1
		maxPenta = minPenta + 98
		for i in range(200):
			penta = pentagonal(i)
			if penta < minPenta:
				continue
			elif penta > maxPenta:
				break
			elif penta > 1000:
				temp1 = c[0].copy()
				temp1.append(penta)
				temp2 = c[1].copy()
				temp2.append('penta')			
				candidates.append([temp1,temp2])

	if 'hepta' not in c[1]:
		minHepta = c[0][-1]%100*100+1
		maxHepta = minHepta + 98
		for i in range(200):
			hepta = heptagonal(i)
			if hepta < minHepta:
				continue
			elif hepta > maxHepta:
				break
			elif hepta > 1000:
				temp1 = c[0].copy()
				temp1.append(hepta)
				temp2 = c[1].copy()
				temp2.append('hepta')			
				candidates.append([temp1,temp2])

	if 'hexa' not in c[1]:
		minHexa = c[0][-1]%100*100+1
		maxHexa = minHexa + 98
		for i in range(200):
			hexa = hexagonal(i)
			if hexa < minHexa:
				continue
			elif hexa > maxHexa:
				break
			elif hexa > 1000:
				temp1 = c[0].copy()
				temp1.append(hexa)
				temp2 = c[1].copy()
				temp2.append('hexa')			
				candidates.append([temp1,temp2])

	if 'hepta' not in c[1]:
		minHepta = c[0][-1]%100*100+1
		maxHepta = minHepta + 98
		for i in range(200):
			hepta = heptagonal(i)
			if hepta < minHepta:
				continue
			elif hepta > maxHepta:
				break
			elif hepta > 1000:
				temp1 = c[0].copy()
				temp1.append(hepta)
				temp2 = c[1].copy()
				temp2.append('hepta')			
				candidates.append([temp1,temp2])

	#print(candidates[-1])


def main():

	candidates = []
	for i in range(19,59):
		candidates.append([[octagonal(i)],['octa']])

	while candidates:
		update(candidates)


if __name__ == '__main__':
	triangle = lambda x: x*(x+1)/2
	square = lambda x: x**2
	pentagonal = lambda x: x*(3*x-1)/2
	hexagonal = lambda x: x*(2*x-1)
	heptagonal = lambda x: x*(5*x-3)/2
	octagonal = lambda x: x*(3*x-2)
	main()
