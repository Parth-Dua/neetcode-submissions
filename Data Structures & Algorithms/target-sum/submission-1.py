from functools import cache 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        '''
        add or subtract, 
        target = 0 

        helper(i,target) = helper(i+1, target - nums[i]) + helper(i+1, target + nums[i])

        valid way = reached end and target = 0 

        base cases: 
        reached the end but not target 0 
        
        
        '''

        # Brute force = 2^n 

        @cache 
        def helper(i, target) :

            if i == len(nums):
                if target == 0 : 
                    return 1 
                return 0 

            return helper(i+1, target - nums[i])+ helper(i+1, target + nums[i])


        return helper(0, target)