class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        l,r = 0, 1 

        max_profit = 0

        while r <n: 
            profit = prices[r] - prices[l]

            if profit < 0: 

                # We have found a new low, YAY!!
                # So all the future values will be impacted by this, and not the previous l 

                l = r
                r = l+1 
            
            else: 
                # New profit found - see if it is the max one
                max_profit = max(max_profit, profit)
                r+=1


        return max_profit


