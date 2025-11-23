
def longestCommonPrefix(self, strs) -> str:
    substring = ""

    for i in range(len(strs[0])):
        substring += strs[0][i]
        for str in strs:
            if not str.startswith(substring):
                return substring[:-1]


    return substring
