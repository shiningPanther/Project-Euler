'''

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''

def combinations(amount,coin,lookUp):
	if coin == len(coins)-1:
		return 1
	if (amount,coin) in lookUp:
		return lookUp[(amount,coin)]
	
	comb = 0
	a = amount
	while amount >= 0:
		comb += combinations(amount,coin+1,lookUp)
		amount -= coins[coin]
	lookUp[(a,coin)] = comb
	return comb

if __name__ == '__main__':
	lookUp = {}
	coins = [200, 100, 50, 20, 10, 5, 2, 1]
	print(combinations(200,0,lookUp))

