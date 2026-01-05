import collections
from typing import List


class Solution:
    def __init__(self):
        self.ans = False
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        group = collections.defaultdict(list)
        visited = set()

        for u,v in edges:
            group[u].append(v)
            group[v].append(u)

        def dfs(current, memory, visited):
            if current in visited or self.ans:
                return
            memory.append(current)
            visited.add(current)
            if current == destination:
                self.ans = True
                return

            for neighbour in group[current]:
                dfs(neighbour, memory, visited)

            memory.pop()

        dfs(source, [], visited)
        return self.ans


