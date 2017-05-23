def answer(l):
	l.sort()
	D = {} #directed graph (child nodes indicate factors of parent node)
	for a in l:
		D[a] = []
	for i,a in enumerate(l):
		for j,b in enumerate(l):
			if a%b is 0 and i is not j and a >= b:
				D[a].append(b)
	print(D)
	count = 0
	for key in D:
		count += countPaths(D, key, 0)
	return count

def countPaths(dict, curNode, pathCount):
	if pathCount is 2:
		return 1
	count = 0
	for child in dict[curNode]:
		count += countPaths(dict,child,pathCount+1)
	return count

L = [1,2,3,4,5,6]
B = [1,1,1]
print(answer(L))
print(answer(B))