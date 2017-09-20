
my_rectangle = {
	# coordinates of bottom‐left corner
	'left_x': 1,
	'bottom_y': 5,
	# width and height
	'width': 10,
	'height': 4,
}

def find_overlap(x1, w1, x2, w2):
	if x2<x1:
		x1,x2 = x2,x1
		w1,w2 = w2,w1
	a = max(x1, x1+w1-x2)
	b = min(x1+w1, x2+w2)
	return max(0, a-b)


