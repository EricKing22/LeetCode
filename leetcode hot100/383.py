class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == "":
            return True

        for n in ransomNote:
            if magazine == "":
                return False
            index = magazine.find(n)
            if index == -1:
                return False

            magazine = magazine[0: index] + magazine[index + 1:]

