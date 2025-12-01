# Definition for a binary tree node.
import math
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        def dfs(current_node, min_val, max_val):
            if not current_node:
                return True

            if not min_val < current_node.val < max_val:
                return False

            return dfs(current_node.left, min_val, current_node.val) and dfs(current_node.right, current_node.val, max_val)


        return dfs(root, -math.inf, math.inf)
