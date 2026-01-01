from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter = Counter()

        for c in list(s):
            counter[c] += 1

        for c in list(t):

            if counter[c] == 0:
                return False

            counter[c] -= 1

            if counter[c] == 0:
                del counter[c]

        print(counter)
        return len(counter) == 0
