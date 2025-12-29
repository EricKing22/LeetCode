class Solution:
    def __init__(self):
        self.seen = set()

    def isHappy(self, n: int) -> bool:
        str_num = str(n)
        print(str_num)
        sqr_sum = 0
        for d in str_num:
            sqr_sum += int(d) ** 2


        if sqr_sum == 1:
            return True
        else:
            if sqr_sum in self.seen:
                return False
            self.seen.add(sqr_sum)
            return self.isHappy(sqr_sum)