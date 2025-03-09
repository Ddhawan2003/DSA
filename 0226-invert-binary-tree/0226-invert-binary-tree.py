# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # ✅ Base case: Empty node
        root.left, root.right = root.right, root.left  # ✅ Swap children
        self.invertTree(root.left)  # ✅ Recursively invert left subtree
        self.invertTree(root.right)  # ✅ Recursively invert right subtree
        return root  # ✅ Return inverted tree
        