# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        while True:
            if head.val == "VISITED":
                return head
            head.val = "VISITED"
            head = head.next
            if head == None:
                return None
