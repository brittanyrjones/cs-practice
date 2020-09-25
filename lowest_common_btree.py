# O(n) solution to find LCS of two given values node_1 and node_2 

# A binary tree node 
class Node: 
	# Constructor to create a new binary node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path 
# exists otherwise false 
def find_root_node_path( root, path, j): 

	# Baes Case 
	if root is None: 
		return False

	# Store this node is path vector. The node will be 
	# removed if not in path from root to j 
	path.append(root.data) 

	# See if the j is same as root's data 
	if root.data == j : 
		return True

	# Check if j is found in left or right sub-tree 
	if ((root.left != None and find_root_node_path(root.left, path, j)) or
			(root.right!= None and find_root_node_path(root.right, path, j))): 
		return True

	# If not present in subtree rooted with root, remove 
	# root from path and return False 
	
	path.pop() 
	return False

# Returns LCA if node node_1 , node_2 are present in the given 
# binary tre otherwise return -1 
def get_lowest_common(root, node_1, node_2): 

	# To store paths to node_1 and node_2 fromthe root 
	path1 = [] 
	path2 = [] 

	# Find paths from root to node_1 and root to node_2. 
	# If either node_1 or node_2 is not present , return -1 
	if (not find_root_node_path(root, path1, node_1) or not find_root_node_path(root, path2, node_2)): 
		return -1

	# Compare the paths to get the first different value 
	i = 0
	while(i < len(path1) and i < len(path2)): 
		if path1[i] != path2[i]: 
			break
		i += 1
	return path1[i-1] 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 

print get_lowest_common(root, 4, 5,)
print get_lowest_common(root, 4, 6)
