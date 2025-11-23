from typing import List
class Solution:
    def __init__(self):
        self.memory = []
        self.result = [0, 0]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = 0

        global result

        if len(self.memory) == 2:
            a = self.memory[0]
            b = self.memory[1]

            if a + b == target:
                self.result[0] = numbers.index(a)
                self.result[1] = numbers.index(b)
                return self.result

        for i in range(len(numbers)):
            self.memory.append(numbers[i])
            self.twoSum(numbers[i + 1:], target)
            self.memory.pop()

        return self.result

