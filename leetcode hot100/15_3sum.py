
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        solutions = []
        left = 0
        mid = 1
        right = 2

        while 0 <= left <= len(nums) - 3:
            while 1 <= mid <= len(nums) - 2:
                while 2 <= right <= len(nums) - 1:

                    if nums[left] + nums[mid] + nums[right] == 0:
                        a = set()
                        a.add(nums[left])
                        a.add(nums[mid])
                        a.add(nums[right])

                        if a not in solutions and ([nums[left], nums[mid], nums[right]] not in ans):
                            ans.append([nums[left], nums[mid], nums[right]])
                            solutions.append(a)
                    right += 1

                mid += 1
                right = mid + 1

            left += 1
            mid = left + 1
            right = mid + 1

        return ans



        return ans
