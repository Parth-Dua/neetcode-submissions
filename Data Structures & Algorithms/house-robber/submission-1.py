class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp array which stores the max amount I can rob uptil ith house

        dp = [0] * (len(nums)+1)

        dp[0] = nums[0]

        for i in range(1, len(nums)): 
            # Include house i
            incl = 0 
            if i-2 >=-1: 
                incl = nums[i] + dp[i-2]
            not_incl = dp[i-1] # not include house i
            dp[i] = max(not_incl , incl)
        
        return dp[len(nums)-1]