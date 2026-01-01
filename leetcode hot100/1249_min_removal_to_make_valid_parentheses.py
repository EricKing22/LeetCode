class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        indices_to_remove = []
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            elif s[i] == ")":
                if len(stack) == 0:
                    indices_to_remove.append(i)
                else:
                    stack.pop()


        if len(stack) > 0:
            indices_to_remove += stack


        ans = ""
        for i in range(len(s)):
            if i in indices_to_remove:
                continue

            ans += s[i]
        return ans