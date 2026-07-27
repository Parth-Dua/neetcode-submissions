from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if len(nums) == 0: 
            return True

        if len(nums) == 1: 
            return True if nums[0] == 0 else False 

        @cache
        def helper(i , grp1, grp2) : 

            # Processed all 
            if i >= len(nums) : 
                # Subset sum is same
                if  grp1 == grp2: 
                    return True
                else: 
                    return False 

            
            return helper(i+1, grp1+nums[i], grp2) or helper(i+1, grp1, grp2+nums[i])

        
        return helper(0, 0, 0)
