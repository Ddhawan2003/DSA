# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        leng=0
        while current:
            leng+=1
            current=current.next
        i=0
        if leng == n:
            return head.next
        current=head
        while i < (leng-n)-1:
            i+=1
            print(i)
            current=current.next
        if current.next:
            current.next = current.next.next
        return head
        