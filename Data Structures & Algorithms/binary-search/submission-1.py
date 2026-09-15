class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # iterative way

        n = len(nums)
        

        l,r = 0, n-1

        while l<=r: 
            
            mid = (l+r) // 2 
            if nums[mid] == target: 
                return mid

            elif nums[mid] > target: 
                # Go left
                r = mid - 1

            else: 
                # Go right 
                l = mid + 1 

        return -1 

        # # recursive way
        
        # def helper(start, end) :

        #     if start > end: 
        #         return -1 
            
        #     mid = (start + end) //2
        #     if target == nums[mid] : 
        #         return mid
        #     elif target > nums[mid] : 
        #         # Search right
        #         return helper(mid+1, end)
        #     else:
        #         # Search left
        #         return helper(start, mid-1)

        # return helper(0,len(nums)-1)
