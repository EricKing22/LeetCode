from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if not prerequisites:
            return list(range(numCourses))

        pre = defaultdict(list)

        for course, requirement in prerequisites:
            pre[course].append(requirement)

        ans = []

        for course in range(numCourses):
            if not pre[course]:
                ans.append(course)

        taken = set()

        def dfs(course): # can I take this course

            if not pre[course] or pre[course] == []:
                return True

            if course in taken: # cycle detected
                return False

            taken.add(course)

            for requirement in pre[course]:
                if not dfs(requirement):
                    return False

            ans.append(course)

            pre[course] = []

            return True

        for course, _ in prerequisites:
            if not dfs(course):
                return []

        return ans

