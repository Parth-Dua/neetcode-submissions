from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        prices = [1,3,4,0,4]

        at i = 0 -> buy or not buy

        if alreadyBought, at i = 1 -> sell or not sell

        for sell -> recurse on i+2
        for not sell -> recurse on i+1

        at each i -> eitiher buy or not buy

        if buy -> curr Profit -= prices[i]

        if not buy -> 

        [4,3,2,1]
        '''

        @cache
        def helper(i, canBuy): 
            
            # Termination condition
            if i >= len(prices): 
                return 0

            ans = 0
            
            # Either buy it or not buy it
            if canBuy: 
                buy_i = helper(i+1, False) - prices[i]
                not_buy_i = helper(i+1, True)

                ans = max(buy_i, not_buy_i)

            # Already bought something
            else:   
                sell_i = helper(i+2, True) + prices[i]
                not_sell_i = helper(i+1, False)
                ans = max(sell_i, not_sell_i)

            return ans
        
        return helper(0, True)
        # prices = [1,3,4,0,4]
        # Time complexity = O(2n) = O(n)
        # Space complxty = O(n)
        


            
