class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        letter_to_word = {}
        words = set()
        s = s.split()

        if len(pattern) != len(s):
            return False

        for idx, word in enumerate(s):
            if pattern[idx] in letter_to_word.keys():
                if letter_to_word[pattern[idx]] != word:
                    return False
            else:
                letter_to_word[pattern[idx]] = word
                if word in words:
                    return False
                else:
                    words.add(word)

        return True

