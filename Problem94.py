'''
It is easily proved that no equilateral triangle exists with integral length sides and integral area. 
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs 
by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths 
and area and whose perimeters do not exceed one billion (1,000,000,000).
'''


# It can be shown that all triangles can be found by finding the solutions to Pell's equation:
# x^2 - n*y^2 = 1 with n = 3
# Here, x = (3a+-1)/2 (for the two cases b = a+-1) and y = h.
# According to Wikipedia, all solutoins to Pell's equation are found by:
# x_k+1 = x_1x_k + ny_1y_k
# y_k+1 = x_1y_k + y_1x_k
# and the first solution to Pell's equation with n=3 is x1=2, y1=1

x1 = 2
y1 = 1
x = x1
y = y1
n = 3
total_perimeter = 0
while x < 10**9:
	x, y = x1*x + n*y1*y, x1*y + y1*x
	a1 = (2*x + 1)/3
	if a1.is_integer():
		A = 0.5*(a1+1)*y
		if A.is_integer():
			per = 2*a1+(a1+1)
			if per <= 10**9:
				total_perimeter += per
	a2 = (2*x - 1)/3
	if a2.is_integer():
		A = 0.5*(a2-1)*y
		if A.is_integer():
			per = 2*a2+(a2-1)
			if per <= 10**9:
				total_perimeter += per

print(total_perimeter)

