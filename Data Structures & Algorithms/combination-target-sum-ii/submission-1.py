class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)

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
                incl_i =  helper(i+1, target - nums[i])
                for comb in incl_i: 
                    ans.append([nums[i]] + comb)

            # Find the next i to not include
            next_i = i+1 # next_i is the next i which is not the same as nums[i]
            while next_i < len(nums) and nums[i] == nums[next_i]: 
                next_i+=1

            not_incl_i = helper(next_i, target)
            for comb in not_incl_i:
                ans.append(comb)


            return ans

        return helper(0, target)
        

        


