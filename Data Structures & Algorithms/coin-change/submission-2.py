class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom Up
        dp = [0] * (amount+1) # min coins to make amount i

        for i in range(1, amount+1):
            # i th val in the table is how many
            min_val = 10000 + 1 
            for j in coins: 
                # Will j be included? 
                if i>=j: 
                    if dp[i - j] != -1  and dp[i - j] <  min_val: 
                        min_val = dp[i - j]
                
            if min_val == 10000 + 1  :
                dp[i] = -1
            else: 
                dp[i] = 1 + min_val 
        
        return dp[amount]