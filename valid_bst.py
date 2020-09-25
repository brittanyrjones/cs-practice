INT_MAX = 4294967296
INT_MIN = -4294967296
# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


# Returns true if the given tree is a binary search tree 
# (efficient version) 
def is_valid(node): 
	return (binary_node_compare(node, INT_MIN, INT_MAX)) 

# Retusn true if the given tree is a BST and its values 
# >= minimum and <= max 
def binary_node_compare(node, minimum, maximum): 
	
	# An empty tree is BST 
	if node is None: 
		return True

	# False if this node not minimum/max
	if node.data < minimum or node.data > maximum: 
		return False

	# Otherwise check the subtrees recursively 
	# tightening the minimum or max constraint 
	return (binary_node_compare(node.left, minimum, node.data -1) and
		binary_node_compare(node.right, node.data+1, maximum)) 

# Driver program to test above function 
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 

if (is_valid(root)): 
	print("Is BST")
else: 
	print("Not a BST")

