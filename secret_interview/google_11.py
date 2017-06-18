#Dinic Algorithm

#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
        n = len(C)
        queue = []
        queue.append(s)
        global level
        level = n * [0]  # initialization
        level[s] = 1  
        while queue:
            k = queue.pop(0)
            for i in range(n):
                    if (F[k][i] < C[k][i]) and (level[i] == 0): # not visited
                            level[i] = level[k] + 1
                            queue.append(i)
        return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(C)):
            if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
                f = Dfs(C,F,i,min(tmp,C[k][i] - F[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp

#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)] # F is the flow matrix
        flow = 0
        while(Bfs(C,F,s,t)):
               flow = flow + Dfs(C,F,s,100000)
        return flow


def answer(entrances, exits, path):
    n = len(path)
    #Add dummy source and sink to matrix
    source_weights = [sum(path[row]) for row in entrances]
    sink_weights = [sum([row[x] for row in path]) for x in exits]

    #Enlarge path matrix
    path = [row+[0,0] for row in path]
    [path.append([0 for x in range(n+2)]) for y in range(2)]

    for i,e in enumerate(entrances):
        path[n][e] = 999999999
    for i,e in enumerate(exits):
        path[e][n+1] = sink_weights[i]

    return MaxFlow(path,n,n+1)

entrances = [0]
exits = [3]
path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
# entrances = [0, 1]
# exits = [4, 5]
# path = [[0, 0, 4, 6, 0, 0],
#       [0, 0, 5, 2, 0, 0],
#       [0, 0, 0, 0, 4, 4],
#       [0, 0, 0, 0, 6, 6],
#       [0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0]]
a = answer(entrances, exits, path)
print(a)