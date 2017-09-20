def is_single_riffle(h1,h2,cards):
	i = 0
	j = 0
	max_i = len(h1)
	max_j = len(h2)
	for card in cards:
		if i < max_i and card == h1[i]:
			i+=1
		elif j < max_j and card == h2[j]:
			j+=1
		else: return False
	return True

print is_single_riffle([1,2,3,4,5],[6,7,8,9,10],[1,2,6,3,7,8,9,4,10,5])