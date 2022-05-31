"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        elif root.left == None and root.right == None:
            return root

        def populate(node):
            if node.left and node.right:
                node.left.next = node.right
                if node.next != None:
                    node.right.next = node.next.left
                return node
            else:
                return node
        
        def traverse(node):
            if node:
                populate(node)
                traverse(node.right)
                traverse(node.left)
            
        traverse(root)
        return root
