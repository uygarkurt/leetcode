# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = [root]
        while root and level:
            res.append([node.val for node in level])
            level = [x for xs in [[node.left, node.right] for node in level] for x in xs if x]
        return res
