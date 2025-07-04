class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest_substring = " "
        if substring == "": return 0
        for i in s:
            if i not in substring:
                substring += i
            else:
                if len(substring) > len(longest_substring):
                    longest_substring = substring
                substring = substring[substring.index(i)+1:] + i
        return max(len(substring),len(longest_substring))