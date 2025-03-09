# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse_left(temp):
            if not temp:
                return ["#"]  # ✅ Use a marker for NULL nodes
            return [temp.val] + traverse_left(temp.left) + traverse_left(temp.right)

        def traverse_right(temp):
            if not temp:
                return ["#"]  # ✅ Use a marker for NULL nodes
            return [temp.val] + traverse_right(temp.right) + traverse_right(temp.left)

        return traverse_left(root.left) == traverse_right(root.right) if root else True