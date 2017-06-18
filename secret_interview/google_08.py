import collections
 
# This class represents a directed graph using adjacency matrix representation
class Graph:
  
    def __init__(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
  
    def BFS(self,s, t, parent):
        '''Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path '''

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)
         
        # Create a queue for BFS
        queue = collections.deque()
         
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
         
        # Standard BFS Loop
        while queue:
            u = queue.popleft()
         
            # Get all adjacent vertices's of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]
             
    # Returns the maximum flow from s to t in the given graph
    def EdmondsKarp(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s !=  source:
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v !=  source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow


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

	g = Graph(path)
	return g.EdmondsKarp(n,n+1)


entrances = [0]
exits = [3]
path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

entrances = [0, 1]
exits = [4, 5]
path = [[0, 0, 4, 6, 0, 0],
		[0, 0, 5, 2, 0, 0],
		[0, 0, 0, 0, 4, 4],
		[0, 0, 0, 0, 6, 6],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0]]
a = answer(entrances, exits, path)
print(a)


