from functools import cache
class Solution:
    def tribonacci(self, n: int) -> int:

        @cache
        def helper(n): 
            # Base cases
            if n ==0: return 0
            if n == 1 or n == 2: return 1

            return helper(n-1)+ helper(n-2) + helper(n-3)

        return helper(n)