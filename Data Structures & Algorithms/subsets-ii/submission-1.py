class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = []
        res = []
        
        def helper(i): 
            
            if i >= len(nums): 
                ans.append(res.copy())
                return 

            
            # incl i
            res.append(nums[i])
            helper(i+1)
            res.pop()

            # not incl i

            # Not consider duplicates 
            while i<len(nums)-1 and nums[i] == nums[i+1]: 
                i+=1

            helper(i+1)
        helper(0)
        return ans
            