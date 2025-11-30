# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = root.left
        right = root.right

        new_left = self.invertTree(left)
        new_right = self.invertTree(right)

        root.left = new_right
        root.right = new_left
        return root
