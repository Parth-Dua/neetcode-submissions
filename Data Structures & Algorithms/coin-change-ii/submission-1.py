from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache      
        def dfs(coins, amount): 
            #Base case

            if amount == 0: 
                return 1
            if amount<0 or len(coins) == 0: 
                return 0

            #Options 1 include first element of coins  
            incl = dfs(tuple(coins), amount - coins[0])

            #Option 2: not include first element of coins 
            not_incl = dfs(tuple(coins[1:]), amount)

            return incl+not_incl

        return dfs(tuple(coins), amount )
