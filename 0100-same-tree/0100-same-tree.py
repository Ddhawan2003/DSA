# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # while p.left and q.left:
        #     if p.val != q.val:
        #         return False
        #     p = p.left
        #     q = q.left
        if not p and not q:
            return True  # Both are None, so they are the same
        if not p or not q:
            return False  # One is None, the other isn't → Not the same
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)