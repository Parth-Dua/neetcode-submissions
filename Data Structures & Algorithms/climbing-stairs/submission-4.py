
class Solution:

    
    def climbStairs(self, n: int) -> int:

        d = {}

        def helper(n): 

            if n <= 1: 
                return 1
            
            if n in d: 
                return d[n]
            
            d[n] = helper(n-1) + helper(n-2) 
            return d[n]

        return helper(n)