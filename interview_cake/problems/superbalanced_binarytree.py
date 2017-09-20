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

def is_superbalanced(root):
  if not root:
    return True

  depths = []

  nodes = []

  nodes.append((root,0))

  while len(nodes):
    node, depth = nodes.pop()

    if not node.left and not node.right:
      if depth not in depths:
        depths.append(depth)
        if len(depths)>2 or len(depths)==2 and abs(depths[0]-depths[1] > 1):
          return False
    else:
      if node.left:
        nodes.append((node.left, depth+1))
      if node.right:
        nodes.append((node.right,depth+1))
  return True

root = Node(3).insert_left(4)
n1 = root.insert_left(4)
n1.insert_left(3)
n2 = n1.insert_right(2)
n3 = n2.insert_right(3)
n3.insert_left(420)

print is_superbalanced(root)