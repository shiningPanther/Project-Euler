import numpy as np


def calculateLength():
	words = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:8}
	characters = 0
	for i in range(1,1000):
		if i <= 20:
			characters += words[i]
			continue
		if i < 100:
			a = words[int(i//10*10)] + words[int(i%10)]
			characters += a
			words[i] = a
			continue
		if i % 100 == 0:
			characters += words[int(i//100)] + words[100]
			continue
		characters += words[int(i//100)] + words[100] + words[int(i%100)] + 3

	return characters + words[1] + words[1000]





if __name__ == '__main__':
	print(calculateLength())

	

