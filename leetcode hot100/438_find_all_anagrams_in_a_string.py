from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p = sorted(p)

        if not p or len(s) < len(p):
            return []
        ans = []

        for i in range(len(s)-len(p)+1):
            if "".join(sorted(s[i:i+len(p)])) == p:
                ans.append(i)

        return ans

