# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        elif k == 0:
            return head
        
        len_list = 0
        head_iter = head
        while head_iter != None:
            head_iter = head_iter.next
            len_list += 1
            
        k = k%len_list
        if k == 0:
            return head
        
        head_iter = head
        for i in range(len_list - k - 1):
            head_iter = head_iter.next
            
        if head_iter.next != None:
            head2 = head_iter.next
        else:
            head2 = head_iter
        head_iter.next = None
        tail = head2
        while tail.next != None:
            tail = tail.next
            
        tail.next = head
        return head2
