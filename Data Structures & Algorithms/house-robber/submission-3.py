from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Top down
        @cache
        def helper(i) : 
            # Base cases
            if i >= len(nums) : #empty list
                return 0 
            if i == len(nums) - 1: # one element
                return nums[i]

            # Option 1: Rob i
            rob_i =  nums[i] + helper(i+2)

            # Option 2: Not rob i
            not_rob_i = helper(i+1)

            max_money_rob = max(rob_i, not_rob_i)
            return max_money_rob

        return helper(0)



        # # dp array which stores the max amount I can rob uptil ith house

        # dp = [0] * (len(nums)+1)

        # dp[0] = nums[0]

        # for i in range(1, len(nums)): 
        #     # Include house i
        #     incl = 0 
        #     if i-2 >=-1: 
        #         incl = nums[i] + dp[i-2]
        #     not_incl = dp[i-1] # not include house i
        #     dp[i] = max(not_incl , incl)
        
        # return dp[len(nums)-1]