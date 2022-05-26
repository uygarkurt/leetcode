"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        def get_node(head, index):
            counter = 0
            while counter != index:
                head = head.next
                counter += 1
            return head
        
        nodes_list = []
        marker = head
        start_node = head
        while head != None:
            if head.random != None:
                random_node = head.random
                curr_node = head
                counter = 0
                while start_node != random_node:
                    start_node = start_node.next
                    counter += 1
                start_node = marker
                nodes_list.append((curr_node.val, counter))
            else:
                nodes_list.append((head.val, None))              
            head = head.next
         
        curr = new_head = Node(nodes_list[0][0])
        for tup in nodes_list:
            curr.next = Node(tup[0])
            curr = curr.next
            
        new_head = new_head.next
        final_head = new_head
        counter = 0
        while new_head != None:
            if nodes_list[counter][1] != None:
                new_head.random = get_node(final_head, nodes_list[counter][1])
            else:
                new_head.random = None
            new_head = new_head.next
            counter += 1
                
        return final_head
