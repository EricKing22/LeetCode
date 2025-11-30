# Definition for a binary tree node.
from functools import total_ordering
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = root.left
        right = root.right

        left_depth = self.maxDepth(left)
        right_depth = self.maxDepth(right)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.maxDepth(root)

        return self.diameter


