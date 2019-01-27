'''
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

products = []

# x is the large number of the product
x = 999
xlimit = 950
# y is the small number of the product
ylimit = 900


# first get a list of all the products
while x > xlimit:
	y = x
	while y > ylimit:
		products.append(x*y)
		y -= 1
	x -= 1

def isPalindromicNumber(x):
	if str(x)[:3] == str(x)[:-4:-1]:
		print(x)

print('Products, unsorted:', products)
products.sort(reverse = True)
for x in products:
	isPalindromicNumber(x)
