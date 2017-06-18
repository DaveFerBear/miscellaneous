def answer(l):
	c = [0]
	nbTriples = 0
	for k in range(len(l)-1):
		for j in range(k-1):
			if (l[k] % l[j] == 0):
				c[k] += 1
				nbTriples += c[j]
	return nbTriples

A = [1,2,3,4,5,6]
print(answer(A))