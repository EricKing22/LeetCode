class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        chars = []
        for c in s:
            if c not in chars:
                chars.append(c)
        for char in chars:
            nums = [1 if item == char else 0 for item in s]
            ans = max(ans, self.max_consecutive_ones(nums, k))

        return ans



    def max_consecutive_ones(self, nums, k):
        left, right = 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                    right += 1
                else:
                    if nums[left] == 0:
                        k += 1
                    left += 1
            else:
                right += 1

            ans = max(ans, right - left)

        return ans
