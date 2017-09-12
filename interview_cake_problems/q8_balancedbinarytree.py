class BinaryTreeNode:
       def __init__(self, value):
           self.value = value
           self.left  = None
           self.right = None


def is_balanced(root):
	max_depth = 0
	min_depth = 0


def is_balanced_helper(node, max_depth, min_depth):
	if 