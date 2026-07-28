class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [([0] * (n) ) for _ in range(m)]

        dp[0] = [1] * n

        for i in range(1, m): 
            for j in range(n): 

                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]