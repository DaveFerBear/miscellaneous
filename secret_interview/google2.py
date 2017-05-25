class Node(object):
    def __init__(self):
        self.nodes = []
        self.data = None

    def sortNodes(self):
		self.nodes.sort(key=lambda x: x.data, reverse=False)

    def addNodes(self, l):
    	if (len(l) == 0):
    		return
    	for n in self.nodes:
    		if (n.data == l[0]):
    			n.addNodes(l[1:])
    			return
    	n = Node()
    	n.data = l[0]
    	self.nodes.append(n)
    	n.addNodes(l[1:])

    def traversal(self):
    	print(self.data)
    	for x in self.nodes:
    		x.traversal()

    def addtoArray(self, main_arr, path):
    	path.append(self.data)
    	if (len(self.nodes) == 0): #leaf node
    		main_arr.append(path)
    	else:
	    	for n in self.nodes:
	    		n.addtoArray(main_arr, path)


def answer(l):
	l = [i.split(".") for i in l]
	root = Node()
	# Generate tree
	for x in l:
		root.addNodes(x)
	root.sortNodes() # recursively sorting nodes enables an in-order traversal
	root.traversal()
	arr = []
	root.addtoArray(arr, []) # in-order traversal with appending
	return arr

#L = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "2.0", "2"]
L = ["1.1.2","2"]
answer(L)
print(answer(L))

