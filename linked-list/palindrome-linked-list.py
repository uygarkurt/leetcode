# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
            
        if len(l) % 2 != 0:
            l.pop(len(l) // 2)
            
        mid = len(l)//2
        
        left = l[:mid]
        right = l[mid:]
        
        if left[::-1] == right:
            return True
        return False
