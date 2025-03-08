# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        while a and b:
            if a==b:
                return a
            a=a.next
            b=b.next
            if not a:
                a=headB
            elif not b:
                b=headA
        return None
        