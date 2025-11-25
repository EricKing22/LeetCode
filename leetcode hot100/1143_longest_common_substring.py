class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0] * len(text2) for _ in range(len(text1))]
        fill = 0
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                fill = 1
            dp[i][0] = fill
        fill = 0
        for j in range(len(text2)):
            if text2[j] == text1[0]:
                fill = 1
            dp[0][j] = fill

        def solve(t1, t2, m, n):
            if t1[m] == t2[n]:
                dp[m][n] = dp[m - 1][n - 1] + 1
            else:
                dp[m][n] = max(dp[m - 1][n], dp[m][n - 1])

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                solve(text1, text2, i, j)

        ans = 0
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                ans = max(ans, dp[i][j])

        return ans