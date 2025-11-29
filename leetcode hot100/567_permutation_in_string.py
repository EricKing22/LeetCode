class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        if s1_count == s2_count:
            return True


        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)
            s2_count[s2[left]] = s2_count[s2[left]] - 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            if s1_count == s2_count:
                return True

            left += 1

        return False