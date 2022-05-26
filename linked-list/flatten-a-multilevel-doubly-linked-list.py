"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        def solver(first_node):
            while first_node != None:
                second_node = first_node.next
                if second_node == None:
                    tail_node = first_node
                    
                if first_node.child != None:
                    first_node.next = first_node.child
                    first_node.child.prev = first_node
                    first_node.child = None
                    child_tail = solver(first_node.next)
                    child_tail.next = second_node
                    if second_node != None:
                        second_node.prev = child_tail
                
                first_node = first_node.next
            return tail_node
        
        solver(head)
        return head
