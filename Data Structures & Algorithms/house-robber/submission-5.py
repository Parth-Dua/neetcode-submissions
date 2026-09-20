class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        nums = [1,1,3,3]
        Rob 0 + Rob 2 or Rob 1 + Rob 3 
        Bottom up 
        dp = [1, 1, 4, 4] # Each element is the max (curr + i-2 , i-1)

        [2,1] -> [2, 1]
        Edge cases: 
        1. No elements
        2. Single element 
        '''     

        if len(nums) == 1 :
            return nums[0]

        dp = [nums[0]]

        for i in range(1, len(nums)): 
            
            dp_i_2 = dp[i-2] if i>=2 else 0 
            dp.append(max(dp[i-1], dp_i_2 + nums[i]))

        return dp[-1]

        