# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def get_tree_right(node, l):
            if node != None:
                l.append(node.val)
                get_tree_right(node.left, l)
                get_tree_right(node.right, l)
            else:
                l.append(None)
                
        def get_tree_left(node, l):
            if node != None:
                l.append(node.val)
                get_tree_left(node.right, l)
                get_tree_left(node.left, l)  
            else:
                l.append(None)
                
        right = []
        left = []
        get_tree_right(root.right, right)
        get_tree_left(root.left, left)
        
        if left == right:
            return True
        return False
