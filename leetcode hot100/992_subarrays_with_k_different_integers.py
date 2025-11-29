from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        ways = []

        def dfs(current_index, my_array):
            my_array.append(nums[current_index])

            if my_array.dis() == k:
                ways.append(my_array.array)

            if my_array.dis() > k:
                return

            if current_index + 1 <= len(nums) - 1:
                dfs(current_index + 1, my_array)

        for i in range(len(nums)-1):
            empty_array = my_array([])
            dfs(i, empty_array)

        print(ways)
        return len(ways)


class my_array:
    def __init__(self, array):
        self.array = array

    def append(self, item):
        self.array.append(item)

    def pop(self):
        self.array.pop()

    def length(self):
        return len(self.array)

    def dis(self):
        return len(set(self.array))

