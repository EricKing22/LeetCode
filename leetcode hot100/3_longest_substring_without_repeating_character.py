
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans = 0
        right = 0
        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            ans = max(ans, len(window))
        window.add(s[right])


        return ans
