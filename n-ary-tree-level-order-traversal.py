"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        level = [root]
        while root and level:
            res.append([node.val for node in level])
            new_level = []
            for node in level:
                for leaf in node.children:
                    if leaf:
                        new_level.append(leaf)
            level = new_level[:]
        return res
