from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        start, end = intervals[0][0], intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] > end:
                ans.append((start, end))
                start, end = interval[0], interval[1]
            else:
                end = max(end, interval[1])
        ans.append((start,end))
        return ans
