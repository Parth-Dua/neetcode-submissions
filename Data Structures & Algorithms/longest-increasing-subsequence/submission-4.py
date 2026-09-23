class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Bottom up
        if len(nums) <= 1: 
            return 1 

        lis = [1]* len(nums)

        lis[-1] = 1

        for i in range(len(nums)-2,-1,-1): 
            for j in range(i+1, len(nums)): 

                if nums[i] < nums[j]: 
                    lis[i] = max(lis[i], 1+lis[j])

        return max(lis)