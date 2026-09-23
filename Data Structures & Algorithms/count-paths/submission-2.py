from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ''' 

        helper(i,j) = helper(i+1,j) + helper(i-1,j)

        '''
        @cache
        def helper(i,j):    

            if i == m-1 and j == n-1: 
                return 1 

            if i < 0 or i>=m or j < 0 or j>=n: 
                return 0 

            return helper(i+1,j) + helper(i, j+1)
            
        
        return helper(0,0)