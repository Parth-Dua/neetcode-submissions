class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        if target == 0: 
            return [[]]

        def helper(i, target): 
            if target == 0: 
                # Found one list
                return [[]]

            # Processed all
            if i == len(nums): 
                return []

            ans = []
            if nums[i] <= target: 
                # Only then include it
                incl_i =  helper(i, target - nums[i])
                for comb in incl_i: 
                    ans.append([nums[i]] + comb)


            not_incl_i = helper(i+1, target)
            for comb in not_incl_i:
                ans.append(comb)


            return ans

        return helper(0, target)
        

        


