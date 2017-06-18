import itertools

def answer(num_buns, num_required):
    L = []
    x = num_buns-num_required+1
    combos = itertools.combinations(range(0,num_buns),num_required)
    total = len(list(combos))*num_required 
    combos = list(itertools.combinations(range(0,num_buns),x))

    for bun in range(0,num_buns):
        L.append([])

    for i in range(total/x):
        for j in combos[i]:
            L[j].append(i)
    return L
