'''

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. 
For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

'''

def threeGonRing():
	solutions = range(9,13)
	for sol in solutions:
		# First group
		for a1 in range(1,5):
			for a2 in range(1,7):
				if a1 == a2:
					continue
				firstGroup = []
				for a3 in range(1,7):
					if a3 == a2 or a3 == a1:
						continue
					if a1 + a2 + a3 == sol:
						firstGroup = [a1,a2,a3]
						break

				# Second group
				if firstGroup != []:
					for b1 in range(a1+1,7):
						if b1 in firstGroup:
							continue
						secondGroup = []
						for b3 in range(1,7):
							if b3 == b1 or b3 in firstGroup:
								continue
							if b1 + a3 + b3 == sol:
								secondGroup = [b1,a3,b3]
								break

						# Third group
						if secondGroup != []:
							for c1 in range(a1+1,7):
								if c1 in firstGroup or c1 in secondGroup:
									continue
								if c1 + b3 + a2 == sol:
									thirdGroup = [c1,b3,a2]
									print(sol,firstGroup,secondGroup,thirdGroup)
									break


def fiveGonRing():
	solutions = range(13,21)
	r = []
	for sol in solutions:
		# First group
		for a1 in range(1,7):
			for a2 in range(1,11):
				if a1 == a2:
					continue
				firstGroup = []
				for a3 in range(1,11):
					if a3 == a2 or a3 == a1:
						continue
					if a1 + a2 + a3 == sol:
						firstGroup = [a1,a2,a3]
						break

				# Second group
				if firstGroup != []:
					for b1 in range(a1+1,11):
						if b1 in firstGroup:
							continue
						secondGroup = []
						for b3 in range(1,11):
							if b3 == b1 or b3 in firstGroup:
								continue
							if b1 + a3 + b3 == sol:
								secondGroup = [b1,a3,b3]
								break

						# Third group
						if secondGroup != []:
							for c1 in range(a1+1,11):
								if c1 in firstGroup or c1 in secondGroup:
									continue
								thirdGroup = []
								for c3 in range(1,11):
									if c3 == c1 or c3 in secondGroup or c3 in firstGroup:
										continue
									if c1 + b3 + c3 == sol:
										thirdGroup = [c1,b3,c3]
										break

								# Fourth group
								if thirdGroup != []:
									for d1 in range(a1+1,11):
										if d1 in firstGroup or d1 in secondGroup or d1 in thirdGroup:
											continue
										fourthGroup = []
										for d3 in range(1,11):
											if d3 == d1 or d3 in thirdGroup or d3 in secondGroup or d3 in firstGroup:
												continue
											if d1 + c3 + d3 == sol:
												fourthGroup = [d1,c3,d3]
												break

										# Fourth group
										if fourthGroup != []:
											for e1 in range(a1+1,11):
												if e1 in firstGroup or e1 in secondGroup or e1 in thirdGroup or e1 in fourthGroup:
													continue
												if e1 + d3 + a2 == sol:
													finalGroup = [e1,d3,a2]
													r.append(firstGroup + secondGroup + thirdGroup + fourthGroup + finalGroup)
													break
	return r





def main():
	#threeGonRing()
	solutions = fiveGonRing()
	maxSol = '0'
	for sol in solutions:
		s = [str(x) for x in sol]
		s = ''.join(s)
		if len(s) == 16 and s > maxSol:
			maxSol = s
	print(maxSol)


if __name__ == '__main__':
	main()




