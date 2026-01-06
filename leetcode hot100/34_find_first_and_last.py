from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums, target, check_left) -> int:
            left  = 0
            right = len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    if check_left:
                        temp = binary_search(nums[:mid], target, True)
                        if temp == -1:
                            return mid
                        else:
                            return temp

                    else:
                        return max(mid, mid + binary_search(nums[mid+1:],target,False) + 1)

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid

            return -1

        first = binary_search(nums, target, True)
        last = binary_search(nums, target, False)

        return [first, last]