class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i): 

            if i == len(nums): 
                return [[]]
            
            rec_lst = helper(i+1)

            # add single element
            ans = rec_lst.copy()

            #join single element to every existing element
            for lst in rec_lst: 
                ans.append([nums[i]] + lst)
            
            return ans
        
        return helper(0)
