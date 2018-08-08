def euclidean_distance(x1,y1,x2,y2):
	return euclidean_distance_squared(*args)**.5

def euclidean_distance_squared(x1,y1,x2,y2, epsilon=0.000001):
	if abs(x2-x1) < epsilon or abs(y2-y1) < epsilon:
		return 0.
	return (x2-x1)**2 + (y2-y1)**2