import numpy as np

def isLeapYear(year):
	if year % 4 != 0:
		return False
	if year % 100 == 0 and year % 400 != 0:
		return False
	return True

def countSundays():
	sundays = 0
	daysOfMonth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	nextSunday = 7
	for year in range(1900,2001):
		if isLeapYear(year):
			daysOfMonth[2] = 29
		else:
			daysOfMonth[2] = 28

		for month in range(1,13):
			while nextSunday <= daysOfMonth[month]:
				nextSunday += 7
			nextSunday -= daysOfMonth[month]
			if nextSunday == 1 and year > 1900:
				sundays += 1
				if year == 2000 and month == 12:
					print('The first of January 2001 was a Sunday')
					sundays -= 1

	return(sundays)

if __name__ == '__main__':
	print(countSundays())

	

