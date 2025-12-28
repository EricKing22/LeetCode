# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_ancestors = []
        q_ancestors = []

        def dfs(current, memory, key, ancestors):
            if not current:
                return

            memory.append(current)

            if current.val == key.val:
                ancestors += memory[:]
                return

            dfs(current.left, memory, key, ancestors)
            dfs(current.right, memory, key, ancestors)

            memory.pop()


        dfs(root, [], p, p_ancestors)
        dfs(root, [], q, q_ancestors)

        for i in range(min(len(p_ancestors), len(q_ancestors))):
            if p_ancestors[i] == q_ancestors[i]:
                ans = i

        return p_ancestors[ans]