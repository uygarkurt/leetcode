# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return None
        result = []
        def get_sum(node, sm):
            sm += node.val
            if node.left:
                get_sum(node.left, sm)
            if node.right:
                get_sum(node.right, sm)
            if node.right == None and node.left == None:
                result.append(sm)
                
        get_sum(root, 0)
        if targetSum in result:
            return True
        return False
