class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        letter_to_letter = {}

        letters = set()
        if len(s) != len(t):
            return False

        for x1,x2 in zip(s,t):
            if x1 in letter_to_letter.keys():
                if letter_to_letter[x1] != x2:
                    return False
            else:
                if x2 in letters:
                    return False
                letter_to_letter[x1] = x2
                letters.add(x2)

        return True