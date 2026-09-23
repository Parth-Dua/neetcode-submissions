class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        '''
        Rows :text1, col: text2

        c ,r ,a ,b ,t
      c 1  1  1  1  1 
      a 1  1  2  2  2
      t 1  1  2  2. 3 

        dp[i][j] = lcs in text1[0:i+1] and text2[0:j+1]

        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) {+ 1 if text1[i] == text2[j]}

        return dp[n-1][m-1]

        '''
        n, m = len(text1), len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]