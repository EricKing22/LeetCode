# bfs build tree use queue
# dfs to do inorder traversal


values = input().split()
values = [-1 if x == "#" else int(x) for x in values]

t, k = list(map(int, input().split()))
class TreeNode():
    def __init__(self, value, fa = None):
        self.left = None
        self.right = None
        self.value = value
        self.fa = fa


def build_tree():
    i = 1
    rt = TreeNode(values[0])
    q = [rt]

    while len(q) != 0 and i < len(values):
        u = q.pop(0)

        if i < len(values) and values[i] != -1:
            left = TreeNode(values[i], u)
            q.append(left)
            u.left = left

        i += 1

        if i < len(values) and values[i] != -1:
            right = TreeNode(values[i], u)
            q.append(right)
            u.right = right
        i += 1

    return rt

rt = build_tree()

in_order = []
def dfs(u):
    left = u.left
    right = u.right
    value = u.value

    if left:
        dfs(left)

    in_order.append(u)
    if value == t:
        return

    if right:
        dfs(right)

dfs(rt)
for u in in_order:
    if u.value == t:
        target = u

fathers = [target]

while target.fa:
    fathers.append(target.fa)
    target = target.fa

target_index = None
for i in range(len(in_order)):
    if in_order[i].value == t:
        target_index = i

ans = None

for i in range(len(in_order)):
    if in_order[i] in fathers:
        k -= 1
        if k == 0:
            ans = i
            break

if ans is not None and ans < target_index:
    print(in_order[ans].value)
else:
    print(-1)

