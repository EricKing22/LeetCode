# Definition for a binary tree node.
from functools import total_ordering
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = root.left
        right = root.right
        return max(1 + self.maxDepth(left), 1 + self.maxDepth(right))


