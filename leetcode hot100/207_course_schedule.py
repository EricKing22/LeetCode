from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        taken = set()

        pre = defaultdict(list)

        for course, reqs in prerequisites:
            pre[course].append(reqs)

        def dfs(course): # Can I take this course

            if not pre[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for p in pre[course]:
                if not dfs(p):
                    return False

            pre[course] = []

            return True

        for course, _ in prerequisites:
            if not dfs(course):
                return False

        return True
