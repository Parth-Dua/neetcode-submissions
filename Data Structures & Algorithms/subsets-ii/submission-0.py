class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        def helper(i): 


            if i == len(nums): 
                return [[]]

            
            ans = []
            
            # Skipping duplicates
            next_i = i+1
            while next_i < len(nums) and nums[i] == nums[next_i]: 
                next_i+=1


            rec_subset = helper(next_i)

            # Number of times nums[i] appears
            repeated_count = next_i - i

            # Add 0, 1, 2, ... repeated_count copies
            for sub in rec_subset:
                for count in range(repeated_count + 1):
                    ans.append([nums[i]] * count + sub)

            return ans
        
        return helper(0)