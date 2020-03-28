'''
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations 
(+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, 
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 
1 to n, can be obtained, giving your answer as a string: abcd.
'''

def get_combinations(digits):
	four_digits = set()

	def add_numbers(x,y):
		s = float(x*y)
		if s>0 and s.is_integer():
			four_digits.add(x*y)
		try:
			s = x/y
			if s>0 and s.is_integer():
				four_digits.add(s)
		except:
			pass
		try: 
			s = y/x
			if s>0 and s.is_integer():
				four_digits.add(s)
		except :
			pass
		s = float(x+y)
		if s>0 and s.is_integer():
			four_digits.add(s)
		s = float(x-y)
		if s>0 and s.is_integer():
			four_digits.add(s)
		s = float(y-x)
		if s>0 and s.is_integer():
			four_digits.add(s)


	two_digits = []
	for x in digits:
		for y in digits:
			if x==y:
				continue
			two_digits.append([x*y,[x,y]])
			two_digits.append([x/y,[x,y]])
			two_digits.append([x-y,[x,y]])
			two_digits.append([x+y,[x,y]])

	three_digits = []
	for x in digits:
		for y in two_digits:
			if x in y[1]:
				continue
			d = y[1]
			y = y[0]
			three_digits.append([x*y,d+[x]])
			three_digits.append([x/y,d+[x]])
			three_digits.append([y/x,d+[x]])
			three_digits.append([x+y,d+[x]])
			three_digits.append([x-y,d+[x]])
			three_digits.append([y-x,d+[x]])

	for x in digits:
		for y in three_digits:
			if x in y[1]:
				continue
			y = y[0]
			add_numbers(x,y)

	for x_ in two_digits:
		for y in two_digits:
			if x_[1][0] in y[1] or x_[1][1] in y[1]:
				continue
			x = x_[0]
			y = y[0]
			add_numbers(x,y)

	return four_digits

x_max = 0
for i in range(1,7):
	for j in range(i+1,8):
		for k in range(j+1,9):
			for l in range(k+1,10):
				digits = set([i,j,k,l])
				if len(digits) != 4:
					continue
				comb = get_combinations(digits)
				x = 1
				while x in comb:
					x += 1
				if x > x_max:
					x_max = x
					digits_max = digits
					comb_max = comb

print(digits_max,comb_max)



