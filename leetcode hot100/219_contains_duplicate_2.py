from typing import List
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = {}

        for i in range(len(nums)):
            if nums[i] not in map.keys():
                map[nums[i]] = i
            else:
                if i - map[nums[i]] <= k:
                    return True
                else:
                    map[nums[i]] = i

        return False