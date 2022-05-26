# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_values(head):
            if head == None:
                return None
            r = get_values(head.next)
            if r != None:
                return r + str(head.val)
            else:
                return str(head.val)
            
        l1_s = get_values(l1)
        l2_s = get_values(l2)
        
        sm = int(l1_s) + int(l2_s)
        sm_s = str(sm)[::-1]
        
        head = ListNode(sm_s[0])
        iterator = head
        for i in range(1, len(sm_s)):
            iterator.next = ListNode(sm_s[i])
            iterator = iterator.next
            
        return head
