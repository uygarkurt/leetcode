# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if node != None:
                traverse(node.left)
                res.append(node.val)
                traverse(node.right)
                
        res = []
        traverse(root)
        return res
