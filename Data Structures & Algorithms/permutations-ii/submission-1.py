class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        curr = []
        used = [False] * len(nums) # What indices are already occupied in some position in the permutation 

        def helper(pos): 
            if pos == len(nums): 
                res.append(curr.copy())
                return

            for j in range(len(nums)): 
                
                if used[j]: 
                    continue
                
                # nums[pos] is available to be added

                # skip duplicates for specific position
                if (j>0 and nums[j] == nums[j-1] and not used[j-1]) :
                    continue
                
                curr.append(nums[j])
                used[j] = True
                helper(pos+1)
                used[j] = False
                curr.pop()
        helper(0)
        return res




                    
            
