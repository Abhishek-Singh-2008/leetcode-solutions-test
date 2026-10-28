# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        while root:
            if (root.left.val is None):
                return (root.right.val > root.val)
            if (root.right.val is None):
                return (root.left.val < root.val)
            else:
                return (root.left.val < root.val and root.right.val > root.val)
        return None