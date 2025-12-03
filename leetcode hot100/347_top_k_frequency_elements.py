from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        results = [(key,length) for key,length in num_dict.items()]

        results.sort(key=lambda x : x[1], reverse=True)

        results = results[:k]
        return [key for key,length in results]