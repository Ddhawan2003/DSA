# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = list1
        head2 = list2
        temp = None
    
        # List1 is empty then return List2
        if head1 is None:
            return head2
    
        # if List2 is empty then return List1
        if head2 is None:
            return head1
    
        # If List1's data is smaller or
        # equal to List2's data
        if head1.val <= head2.val:
    
            # assign temp to List1's data
            temp = head1
    
            # Again check List1's data is smaller or equal List2's
            # data and call mergeLists function.
            temp.next = self.mergeTwoLists(head1.next, head2)
    
        else:
            # If List2's data is greater than or equal List1's
            # data assign temp to head2
            temp = head2
    
            # Again check List2's data is greater or equal List's
            # data and call mergeLists function.
            temp.next = self.mergeTwoLists(head1, head2.next)
    
        # return the temp list.
        return temp
            
        