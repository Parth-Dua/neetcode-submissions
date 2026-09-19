class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod_no_zeroes = 1 
        num_zeroes = 0
        for i in nums: 
            if i == 0: 
                num_zeroes+=1
            else: 
                prod_no_zeroes*=i
            
        ans = [0]*len(nums)

        for i in range(len(nums)): 

            if nums[i] != 0: 
                if num_zeroes >= 1: 
                    ans[i] = 0 
                else: 
                    ans[i] = prod_no_zeroes//nums[i]

            else: 
                if num_zeroes <= 1: 
                    ans[i] = prod_no_zeroes
                else: 
                    ans[i] = 0
                
        return ans

