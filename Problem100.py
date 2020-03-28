'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the box would contain.
'''

'''
This can be written as a Diophantine Equation:
2b^2 - 2b -n^2 + n = 0
According to this website:
https://www.alpertron.com.ar/QUAD.HTM
The recursive solution to the equation is
x_(n+1) = 3*x_n + 2*y_n - 2
y_(n+1) = 4*x_n + 3*y_n - 3
'''

b = 15
n = 21

while n<10**12:
	b,n = 3*b+2*n-2, 4*b+3*n-3
	print(b,n)