def luckyTriple(x,y,z):
	if x%y==0 and y%z==0:
		return True
	return False

def bruteAnswer(l):
	l.sort()
	count = 0
	x = len(l)-1
	y = len(l)-2
	z = len(l)-3
	while x >= 2:
		y = x-1
		while y >= 1:
			z = y-1
			while z >= 0:
				if luckyTriple(l[x], l[y], l[z]):
					count+=1
				z-=1
			y-=1
		x-=1
	return count

def answer(l):
	cache = [0 for x in range(len(l))]
	count = 0
	for k in range(0,len(l)):
		for j in range(0,k):
			if l[k]%l[j] is 0:
				cache[k] += 1
				count += cache[j]
	return count

L = [1,2,3,4,5,6]
B = [1,1,1]
print(answer(L))