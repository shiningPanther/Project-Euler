'''

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''

class Powers():

	def __init__(self, n):
		self.base = n
		self.number = [n]

	def multiplication(self, index, transfer):
		self.number[index]*=self.base
		self.number[index]+=transfer
		if self.number[index] >= 10:
			product = self.number[index]
			self.number[index] = product % 10
			return product // 10
		return 0

	def __pow__(self, n):
		while(n-1):
			n-=1
			transfer=0
			for index in range(len(self.number)):
				transfer = self.multiplication(index, transfer)
				if transfer > 0 and index == len(self.number)-1:
					self.number.append(transfer)
			
		return(self.number)


print(sum(Powers(2)**1000))