a = [-10, -10, 1, 3, 2]

def highest_product_of_3(list_of_ints):
	if len(list_of_ints) < 3:
		return None

	highest_3 = set(i: list_of_ints[:3].count(i) for i in list_of_ints[:3])
	lowest_2 = set(i: list_of_ints[:2].count(i) for i in list_of_ints[:2])

	for n in list_of_ints[2:]:
		#check for highest
		if n not in highest_3:
			if n>min(highest_3):
				highest_3.remove(min(highest_3))
				highest_3.add(n)

		#check for lowest
		if n not in lowest_2:
			if n<max(lowest_2):
				lowest_2.remove(min(highest_3))
				lowest_2.add(n)
	a = 1
	for h in highest_3:
		a*=h
	b = 1
	for b in lowest_2:
		b*=h
	b*=max(highest_3)
	return max(a,b)

print(highest_product_of_3(a))