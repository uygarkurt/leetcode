# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            if head.val == val:
                return None
            return head
        
        fast = head.next
        slow = head
        
        while fast != None:
            if slow.val == val:
                head = fast
                fast = fast.next
                slow = slow.next
            elif fast.val == val:
                slow.next = fast.next
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        if slow.val == val:
            return None
                
        return head
