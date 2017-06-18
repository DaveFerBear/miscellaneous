class Edge(object):
	def __init__(self, u, v, w):
		self.source = u
		self.target = v
		self.capacity = w


class FlowNetwork(object):
	def  __init__(self):
		self.adj = {}
		self.flow = {}

	def AddVertex(self, vertex):
		self.adj[vertex] = []

	def GetEdges(self, v):
		return self.adj[v]

	def AddEdge(self, u, v, w = 0):
		if u == v:
			raise ValueError("u == v")
		edge = Edge(u, v, w)
		redge = Edge(v, u, 0)
		edge.redge = redge
		redge.redge = edge
		self.adj[u].append(edge)
		self.adj[v].append(redge)
		# Intialize all flows to zero
		self.flow[edge] = 0
		self.flow[redge] = 0

	def FindPath(self, source, target, path):
		if source == target:
			return path
		for edge in self.GetEdges(source):
			residual = edge.capacity - self.flow[edge]
			if residual > 0 and not (edge, residual) in path:
				result = self.FindPath(edge.target, target, path + [(edge, residual)])
				if result != None:
					return result

	def MaxFlow(self, source, target):
		path = self.FindPath(source, target, [])
		while path != None:
			flow = min(res for edge, res in path)
			for edge, res in path:
				self.flow[edge] += flow
				self.flow[edge.redge] -= flow
			path = self.FindPath(source, target, [])
		return sum(self.flow[edge] for edge in self.GetEdges(source))

def answer(entrances, exits, path):
	#Edmonds-Karp Maximum Flow Implementation
	#https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm#Python_implementation_of_Edmonds-Karp_algorithm

	# #Construct graph
	# num_rooms = len(path)
	# G = {a:{b:path[a][b] for b in range(num_rooms) if (path[a][b]!=0 and a!=b)} for a in range(num_rooms)}
	
	# #Add dummy source and sink
	# source_weights = [sum([row[x] for row in path]) for x in entrances]
	# sink_weights = [sum([row[x] for row in path]) for x in exits]
	# G['s'] = {entrances[i]:source_weights[i] for i in range(len(entrances))} #source
	# G['t'] = {exits[i]:sink_weights[i] for i in range(len(entrances))} #sink

	n = len(path)

	#Add dummy source and sink to matrix
	source_weights = [sum(path[row]) for row in entrances]
	sink_weights = [sum([row[x] for row in path]) for x in exits]
	path = [row+[0,0] for row in path]
	[path.append([0 for x in range(n+2)]) for y in range(2)]
	for i,e in enumerate(exits):
		path[e][n+1] = sink_weights[i]
	for i,e in enumerate(entrances):
		path[n][i] = source_weights[i]

	for x in path:
		print(x)
	g = FlowNetwork()
	[g.AddVertex(x) for x in range(n+2)]
	for i,row in enumerate(path):
		for j,item in enumerate(row):
			if i!=j:
				g.AddEdge(i, j, w=row[j])
	
	return g.MaxFlow(n, n+1)


entrances = [0]
exits = [3]
path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
# entrances = [0, 1]
# exits = [4, 5]
# path = [[0, 0, 4, 6, 0, 0],
# 		[0, 0, 5, 2, 0, 0],
# 		[0, 0, 0, 0, 4, 4],
# 		[0, 0, 0, 0, 6, 6],
# 		[0, 0, 0, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 0]]
a = answer(entrances, exits, path)
print(a)


