# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = set([root])
        dfs(root, to_delete, res)
        
        return list(res)

        
def dfs(root, to_delete, res):
    if not root:
        return None
    
    # if root.val not in to_delete, just simply recusively call left and right child
    if root.val not in to_delete:
        root.left = dfs(root.left, to_delete, res)
        root.right = dfs(root.right, to_delete, res)
        
        return root
        
    # if root.val in to_delete, we need to 
    # 1. remove it from res if present
    # 2. if left child is not None, add to res
    # 3. if right child is not None, add to res
    # 4 .recursively call left and right child
    # 5. return None as root should be deleted
    if root in res:
        res.remove(root)

    if root.left:
        res.add(root.left)

    if root.right:
        res.add(root.right)

    dfs(root.left, to_delete, res)
    dfs(root.right, to_delete, res)

    return None