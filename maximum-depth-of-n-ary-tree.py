"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        level = []
        def traverse(root, count):
            if root:
                level.append(count)
                for node in root.children:
                    traverse(node, count+1)
        traverse(root, 1)
        return max(level)
