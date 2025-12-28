# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_sum = 0
            level_count = len(queue)  # Snapshot of how many nodes are in the current level

            # Iterate ONLY through the nodes of the current level
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate average for this level
            result.append(level_sum / level_count)

        return result


