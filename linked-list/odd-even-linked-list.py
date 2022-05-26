# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        
        head_odd = ListNode(head.val)
        head_even = ListNode(head.next.val)
        head_even_r = head_even
        
        return_head = head_odd
        
        head_iter = head.next.next
        counter = 1
        while head_iter != None:
            if counter % 2 == 0:
                head_even.next = ListNode(head_iter.val)
                head_even = head_even.next
            elif counter % 2 != 0:
                head_odd.next = ListNode(head_iter.val)
                head_odd = head_odd.next
                
            head_iter = head_iter.next
            counter += 1
            
        head_odd.next = head_even_r
            
        return return_head
