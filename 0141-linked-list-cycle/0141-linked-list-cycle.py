# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen = set()
        # curr = head
        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr=curr.next
        # return False
        left = head
        right = head
        while right and right.next:
            left = left.next
            right = right.next.next
            if left == right:
                return True
        return False
        