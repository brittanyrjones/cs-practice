# inorder traversal iteratice solution 

class Node: 
	
	def __init__(self, key): 
		self.left = None
		self.right = None
        self.value = key 


# Iterative function for inorder tree traversal 
def order_tree(root): 
	# Set current to root 
	current = root 
	stack = [] 
	done = 0
	
	while True: 
		
		# Reach the left most Node of the current Node 
		if current is not None: 
			
			# Place pointer to a tree node on the stack 
			# before traversing the node's left subtree 
			stack.append(current) 
		
			current = current.left 

		
		# BackTrack from the empty subtree and visit the Node 
		# at the top of the stack; however, if the stack is 
		# empty you are done 
		elif(stack): 
			current = stack.pop() 
			print(current.value, end=" ") # Python 3 printing 
		
			# We have visited the node and its left 
			# subtree. Now, it's right subtree's turn 
			current = current.right 

		else: 
			break
	
	print() 


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

order_tree(root) 

