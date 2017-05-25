def answer(l):
	l = [i.split(".") for i in l]
	l = sorted(l, key=lambda x: x[0]) #sort by major number
	return sortSubList(l,0)

def sortSubList(l, i):
	a = 0
	b = 1
	if (len(l[0]) == i+1):
		return sorted(l, key=lambda x: x[i]) #sort by major number
	
	while (b < len(l)):
		while (len(l[a]) > i+1): #numbers without minor digits don't require sorting
			a+=1
			b+=1
		while (l[a][i] == l[b][i]):
			b+=1
		if ((b-a) > 1):
			l[a:b] = sortSubList(l[a:b], i+1) # sort section of list in place
		a = b+1
		b += 2
	return l

l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "2.0"]
print(answer(l))
