'''
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate 
lies between 0 and 2 inclusive; that is, 0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
'''

import numpy as np

def initialize_coordinates(N):
	c = np.empty([(N+1)**2-1,2],dtype=int)
	n = 0
	for x in range(N+1):
		for y in range(N+1):
			if x==0 and y==0:
				continue
			c[n,:] = np.array([x,y])
			n += 1
	return c

def get_right_triangles(coordinates):
	n = 0
	for p in coordinates:
		px = p[0]
		py = p[1]
		# x==0 and y==0 are special cases where the right angle can also be formed at the origin
		if px == 0:
			n += N
		# We also treat the case separately where the right angle is formed on the x-axis
		if py == 0:
			n += N
		# Form a right angle at P
		for qy in range(py):
			if px == 0:
				n += N
				break
			qx = px - py/px*(qy-py)
			if qx <= N and qx.is_integer():
				n += 1
		# Form the right angle at Q (but not at y==0)
		for qy in range(1,py):
			s = np.sqrt(px**2 + 4*qy*(py-qy))
			qx = (px + s)/2
			if qx <= N and qx.is_integer():
				n += 1
	return n


N = 50
coordinates = initialize_coordinates(N)
right_triangles = get_right_triangles(coordinates)
print(right_triangles)