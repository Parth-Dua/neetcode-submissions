from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache      
        def dfs(i, amount): 
            #Base case

            if amount == 0: 
                return 1
            if amount<0 or i == len(coins): 
                return 0

            #Options 1 include first element of coins  
            incl = dfs(i, amount - coins[i])

            #Option 2: not include first element of coins 
            not_incl = dfs(i+1, amount)

            return incl+not_incl

        return dfs(0, amount )
