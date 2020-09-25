# A class that represents an individual node in a 
# Binary Tree 
class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.value = key 
  
  
# in order tree traversal 
def order_tree(root): 
    if root: 
        # left child 
        order_tree(root.left) 
        print(root.value)
        # right child 
        order_tree(root.right) 
          
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
order_tree(root) 