# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        t1=root.left
        t2=root.right
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True  # ✅ Both null → Symmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False  # ❌ Mismatch
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(t1,t2) if root else True

        # def traverse_left(temp):
        #     if not temp:
        #         return ["#"]  # ✅ Use a marker for NULL nodes
        #     return [temp.val] + traverse_left(temp.left) + traverse_left(temp.right)

        # def traverse_right(temp):
        #     if not temp:
        #         return ["#"]  # ✅ Use a marker for NULL nodes
        #     return [temp.val] + traverse_right(temp.right) + traverse_right(temp.left)

        # return traverse_left(root.left) == traverse_right(root.right) if root else True