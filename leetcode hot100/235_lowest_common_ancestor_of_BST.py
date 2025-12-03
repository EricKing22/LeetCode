class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ancestors = []
        q_ancestors = []
        def dfs(current_node, memory, key, ancestors):

            if not current_node:
                return

            memory.append(current_node)

            if current_node == key:
                ancestors += memory[:]
                return

            dfs(current_node.left, memory, key, ancestors)
            dfs(current_node.right, memory, key, ancestors)

            memory.pop()

        dfs(root, [], p, p_ancestors)
        dfs(root, [], q, q_ancestors)

        print([item.val for item in p_ancestors])
        print([item.val for item in q_ancestors])

        ans = 0
        for i in range(min(len(p_ancestors), len(q_ancestors))):
            if p_ancestors[i] == q_ancestors[i]:
                ans = i
        return p_ancestors[ans]