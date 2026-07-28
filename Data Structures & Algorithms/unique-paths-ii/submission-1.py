class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1: 
            return 0 

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [([0] * (n) ) for _ in range(m)]


        dp[0][0] = 1 

        for i in range(m): 
            for j in range(n): 
                if i+j == 0: 
                    continue
                
                paths = 0 
                # paths from left if not blocked
                if obstacleGrid[i][j-1] == 0: 
                    paths+= dp[i][j-1]
                
                # paths from up if not blocked
                if obstacleGrid[i-1][j] == 0: 
                    paths+=  dp[i-1][j]

                dp[i][j] = paths

        return dp[m-1][n-1]


