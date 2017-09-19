import math

def factor(n):
	step = 2 if n%2 else 1
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))

count = 0
amicables = {}
for i in range(1,10001):
	s = factor(i)
	s.remove(i) #definition of factor(n) does not include n
	amicables[i] = sum(s)

for i in range(1,10001):
	a = amicables[i]
	if a in amicables:
		if a == amicables[a]:
			count+=a
			count+=i

count/=2

print(count)