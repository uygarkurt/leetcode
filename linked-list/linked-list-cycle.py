# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        slow_pointer = head
        fast_pointer = head
        
        while True:
            if fast_pointer == None or fast_pointer.next == None or fast_pointer.next.next==None:
                return False
            
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
            if slow_pointer == fast_pointer:
                return True
