class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []

        curr = []
        
        def helper(i, target): 
                      
            if target == 0: 
                ans.append(curr.copy())
                return 

            if i == len(nums) or target< 0: 
                return

            
            # Incl i 
            curr.append(nums[i])
            helper(i, target - nums[i])
            curr.pop()

            # Not include i 
            helper(i+1, target)

        helper(0,target)

        return ans
