
n = int(input())

class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.group = None

    def __str__(self):
        return self.name

nodes = {}
for _ in range(n):
    node, weight = input().split()
    nodes[node] = Node(node, weight)

m = int(input())
current_group = 0

for _ in range(m):
    a,b = input().split()
    if nodes[a].group is None:
        if nodes[b].group is None:
            nodes[a].group = current_group
            nodes[b].group = current_group
            current_group += 1
        else:
            nodes[a].group = nodes[b].group

    else:
        if nodes[b].group is None:
            nodes[b].group = nodes[a].group
        else:
            change_group = nodes[b].group
            for node in nodes.values():
                if node.group == change_group:
                    node.group = nodes[a].group

dict_group_weight = {}
for node in nodes.values():
    if node.group in dict_group_weight.keys():
        new_weight = dict_group_weight[node.group][0] + node.weight
        old_node = dict_group_weight[node.group][1]
        new_node = node if node.weight > old_node.weight else old_node

        dict_group_weight[node.group] = (new_weight, new_node)
    else:
        if node.group is not None:
            dict_group_weight[node.group] = (node.weight, node)



max_group = None
max_node = None
max_group_weight = 0
for group, (group_weight, group_node) in dict_group_weight.items():
    if group_weight > max_group_weight:
        max_group_weight = group_weight
        max_node = group_node

print(max_node.name, max_group_weight)