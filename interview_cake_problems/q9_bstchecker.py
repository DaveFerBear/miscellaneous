class BinaryTreeNode:
	 def __init__(self, data):
			 self.data = data
			 self.left  = None
			 self.right = None
	 def insert_left(self, value):
			 self.left = BinaryTreeNode(data)
			 return self.left
	 def insert_right(self, value):
			 self.right = BinaryTreeNode(data)
			 return self.right


MAX_INT = 4294967296
MIN_INT = -4294967296

def bst_checker(root):
	return bst_util(root, MIN_INT, MAX_INT)

def bst_util(node, mini, maxi):
	if node is None:
		return True

	if node.data < maxi and node.data >= mini:
		return bst_util(node.left, mini, node.data) and bst_util(node.right, node.data, maxi)

	return False


root = BinaryTreeNode(4)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(5)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(3)
 
if (bst_checker(root)):
    print "Is BST"
else:
    print "Not a BST"