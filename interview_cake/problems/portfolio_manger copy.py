from Queue import Queue

class Node:
    def __init__(self, data, left=None, right=None):
    self.data = data
    self.left  = left
    self.right = right

def deserialize(data):
    data = data.split()
        if data[0] == '#' or len(data) == 0:
            return None
        q = Queue()
        root = Node(int(data[0]))
        q.put(root)
        index = 1
        while index < len(data):
            node = q.get()
                if node == None:
                    break
                        if data[index] != '#':
                            node.left = Node(int(data[index]))
                                q.put(node.left)
                                    if index+1<len(data) and data[index+1] != '#':
                                        node.right = Node(int(data[index+1]))
                                            q.put(node.right)
                                                
                                                index += 2
                                            
    return root

def find_max(node):
    if node == None:
        return [0,0]
        left_max = find_max(node.left) 	# [max_without_root, max_with_root]
        right_max = find_max(node.right)
        return [max(left_max[0],left_max[1]) + max(right_max[0],right_max[1]), left_max[0]+right_max[0]+node.data]

def post_order(node):
    if node == None:
    return
        post_order(node.left)
            post_order(node.right)
                print node.data

def find_max_investment(n, data):
    root = deserialize(data)
        options = find_max(root)
        post_order(root)
        return max(options[0], options[1])

print find_max_investment(5, "1 2 # # 3 # 4 5")
