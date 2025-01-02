# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        cnt = 0

        # Convert l1 to a number
        while l1:
            num1 += l1.val * pow(10, cnt)
            cnt += 1
            l1 = l1.next

        cnt = 0
        # Convert l2 to a number
        while l2:
            num2 += l2.val * pow(10, cnt)
            cnt += 1
            l2 = l2.next

        # Sum the two numbers
        sum = num1 + num2
        dummy = ListNode()
        current = dummy
        if sum == 0:
            return ListNode(0)
        while sum > 0:
            dig = sum%10
            current.next = ListNode(dig)
            current=current.next
            sum//=10
        return dummy.next