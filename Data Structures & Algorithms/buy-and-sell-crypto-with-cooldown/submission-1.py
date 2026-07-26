from collections import defaultdict
from functools import cache
class Solution:


    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def helper(i, alreadyBought): 
            if i >= len(prices):
                return 0

            # already bought is True/ False
            if alreadyBought == True: 
                #Option1: Don't sell
                notSell = helper(i+1, True)

                # Option2: Sell
                sell =  prices[i]  + helper(i+2, False)

                return max(sell, notSell)
            
            else: 
                # Option1: Buy
                buy = helper(i+1, True) - prices[i]
                # Option2: Not Buy
                notBuy = helper(i+1, False)

                return max(buy, notBuy)
                

        # Top down 
        return helper(0, False)



            

