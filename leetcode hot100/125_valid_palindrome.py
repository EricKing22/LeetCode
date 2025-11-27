class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while (not s[left].isalnum() and left < right):
                left += 1
            left_char = s[left].lower()
            left += 1
            while (not s[right].isalnum() and left < right):
                right -= 1
            right_char = s[right].lower()
            right -= 1
            if left_char != right_char:
                return False

        return True