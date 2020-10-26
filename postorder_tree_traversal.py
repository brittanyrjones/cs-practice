# A class that represents an individual node in a 
# Binary Tree 

"""
Postorder traversal is used to delete the tree. 
Please see the question for deletion of tree for details. 
Postorder traversal is also useful to get the postfix expression of an expression tree.
 Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for 
 the usage of postfix expression.
"""
class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
  
          
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val), 
  
  
# Driver code 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print "\nPostorder traversal of binary tree is"
printPostorder(root) 
