# Python program to construct tree using inorder and 
# preorder traversals 

# A binary tree node 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


class Solution:
    def build_tree_1(self, preorder, inorder):
        if len(preorder)==0: return
        if len(preorder)==1: return Node(preorder[0])
        root=Node(preorder[0])
        div=inorder.index(preorder[0])
        root.left=self.build_tree_1(preorder[1:(div+1)],inorder[0:div])
        root.right=self.build_tree_1(preorder[(div+1):],inorder[(div+1):])
        return root
 
    def build_tree_2(self, preorder, inorder):
        if len(preorder)==0: return
        if len(preorder)==1: return Node(preorder[0])
        return self.build_from_pre_in(preorder, inorder, 0, 0, len(preorder))
 
    def build_from_pre_in(self,preorder,inorder,P,I,element):
        if element==0:
            return None
        root = Node(preorder[P])
        div = 0
        for i in range(I, I+element):
            if inorder[i] == preorder[P]:
                break
            div += 1
        root.left = self.build_from_pre_in(preorder, inorder, P+1, I, div)
        root.right = self.build_from_pre_in(preorder, inorder, P+div+1, I+div+1, element-1-div)
        return root

preorder=[1,2,4,5,6,7,3,8,9,10]
inorder=[4,5,6,7,2,1,8,9,3,10]
test=Solution()
res=test.build_tree_1(preorder,inorder)
print(res.data)
print(res.left.data)
print(res.right.data)
