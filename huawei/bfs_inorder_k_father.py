values = input().split()
values = [int(value) if value != "#" else -1 for value in values]

u, k = list(map(int, input().split()))

class TreeNode:
    def __init__(self, value, fa = None):
        self.value = value
        self.fa = fa
        self.left = None
        self.right = None

q = []
i = 1
rt_value = values[0]
rt = TreeNode(rt_value)
q.append(rt)
# build tree with bfs

while len(q) > 0:
    fa = q.pop(0)
    value = values[i]
    if value != -1:
        node = TreeNode(value, fa)
        fa.left = node
        q.append(node)
    i += 1

    if i == len(values):
        break

    value = values[i]
    if value != -1:
        node = TreeNode(value,fa)
        fa.right = node
        q.append(node)
    i += 1

    if i == len(values):
        break

# dps for in order traversal
path = []
memory = [rt]

def dfs(node):
    left = node.left
    right = node.right
    value = node.value

    if left:
        dfs(left)

    path.append(node)
    if value == u:
        return

    if right:
        dfs(right)

dfs(rt)


target = None
for node in path:
    if node.value == u:
        target = node

fathers = [target]
while target is not None and target.fa is not None:
    fathers.append(target.fa)
    target = target.fa

ans = -1


for node in path:
    if node.value == u and k != 0:
        break

    if node in fathers:
        k -= 1
    if k == 0:
        ans = node.value
        break

print(ans)


