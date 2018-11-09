def is_prime(n):
        if n < 2: 
            return False;
        if n % 2 == 0:             
            return n == 2  # return False
        k = 3
        while k*k <= n:
            if n % k == 0:
                return False
            k += 2
        return True

def primeQuery(n, first, second, values, queries):
    n = len(values)
    m = len(first)

    # Create an array of bools indicating primality.
    prime_arr = [False]*n
    prime_map = {} # Storing already calculated primes
    for i in xrange(n):
        v = values[i]
        if v not in prime_map:
            prime_map[v] = is_prime(v)
        prime_arr[i] = prime_map[v]

    # Hash the edges for fast access. Store both ways (undirected).
    edges = {}
    for i in xrange(m):
        if first[i] not in edges:
            edges[first[i]] = set()
        edges[first[i]].add(second[i])
        if second[i] not in edges:
            edges[second[i]] = set()
        edges[second[i]].add(first[i])

    # Only need to store the distance from node 1 (the depth).
    # If a node is closer than the queried root,
    # it isn't part of the subgraph.
    depth = [0]*n
    visited = [False]*n
    def calculate_depth(i, cur_depth):
        if visited[i-1]:
            return
        visited[i-1] = True
        depth[i-1] = cur_depth
        for ni in edges[i]: # Named edges are 1 greater than indeces.
            calculate_depth(ni, cur_depth+1)

    calculate_depth(1, 0)
    
    # Helper function to calculate primes in subgraph.
    primes_below = [-1]*n # Number of primes including and below a given node.
    def count_primes_in_subgraph(i):
        if primes_below[i-1] != -1: # node visited in another query.
            return primes_below[i-1]
        prime_count = 0
        if prime_arr[i-1]: # The current node is prime.
            prime_count +=1
        for ei in edges[i]:
            if depth[ei-1] > depth[i-1]:
                prime_count += count_primes_in_subgraph(ei)
        primes_below[i-1] = prime_count
        return prime_count

    return [count_primes_in_subgraph(query) for query in queries]
    
