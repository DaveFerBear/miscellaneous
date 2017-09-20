class Node:

  def __init__(self, value):
    self.value = value
    self.left  = None
    self.right = None

  def insert_left(self, value):
    self.left = Node(value)
    return self.left

  def insert_right(self, value):
    self.right = Node(value)
    return self.right

def BST_checker(root):
  node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

  while len(node_and_bounds_stack):
    node,lower_bound, upper_bound = node_and_bounds_stack.pop()
    if node.value < lower_bound or node.value > upper_bound:
      return False

    if node.left:
      node_and_bounds_stack.append(node.left, lower_bound, node.value)
    if node.right:
      node_and_bounds_stack.append(node.right, node.value, upper_bound)

  return True
