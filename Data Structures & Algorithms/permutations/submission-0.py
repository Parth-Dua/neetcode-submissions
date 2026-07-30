class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i): 

            if i == len(nums): 
                return [[]]

            
            rec_permute = helper(i+1)
            new = []
            for perm in rec_permute: 
                if len(perm) == 0: 
                    new.append([nums[i]])
                else: 
                    for j in range (len(perm) +  1):
                        new.append(perm[:j]+ [nums[i]] + perm[j:])

            return new

        return helper(0)