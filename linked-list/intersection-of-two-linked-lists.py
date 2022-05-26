# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        counterx = 0
        headA_temp = headA
        while headA_temp != None:
            headA_temp = headA_temp.next
            counterx += 1
            
        countery = 0
        headB_temp = headB
        while headB_temp != None:
            headB_temp = headB_temp.next
            countery += 1
            
        if counterx > countery:
            for i in range(counterx - countery):
                headA = headA.next
            while headA != None:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None
        
        if counterx <= countery:
            for i in range(countery - counterx):
                headB = headB.next
            while headA != None:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None
