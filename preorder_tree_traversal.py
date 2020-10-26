# Python program to for tree traversals 
"""
Preorder traversal is used to 
create a copy of the tree. Preorder traversal is 
also used to get prefix expression on of an expression tree. 
Please see http://en.wikipedia.org/wiki/Polish_notation to 
know why prefix expressions are useful.
"""
# A class that represents an individual node in a 
# Binary Tree 
class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 
  
  
# Driver code 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print "Preorder traversal of binary tree is"
printPreorder(root) 
