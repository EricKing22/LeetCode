# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])
        ans = []

        def bfs():
            while queue:
                level_length = len(queue)
                temp = []
                for _ in range(level_length):

                    node = queue.popleft()

                    if not node:
                        continue

                    temp.append(node.val)

                    queue.append(node.left)
                    queue.append(node.right)

                if temp:
                    ans.append(temp[:])

        bfs()

        ans.reverse()
        return ans





