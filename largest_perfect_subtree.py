class Node(object):
    def __init__(self, l,r,x):
        self.x = x
        self.l = l
        self.r = r

def solution(T):
    
    current_max = 1
    
    def is_perfect_node(node):
        return node.l is not None and node.r is not None
    
    def maximum_depth_of_perfect_nodes(node, depth):
        if not is_perfect_node(node):
            return depth
        return min(maximum_depth_of_perfect_nodes(node.l, depth+1),
                    maximum_depth_of_perfect_nodes(node.r, depth+1))
    
    def traverse(node):
        if not node:
            return 0
        max_d = maximum_depth_of_perfect_nodes(node, 1)
        current_max = max(current_max, max_d)
        traverse(node.l)
        traverse(node.r)
    
    traverse(T)
    
    return current_max

if __name__=='__main__':
	t = Node(None, None, 5)
	solution(t)