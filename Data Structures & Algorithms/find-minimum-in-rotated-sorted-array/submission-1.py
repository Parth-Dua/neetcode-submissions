class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l, r = 0, len(nums) - 1 
        
        res = nums[0]

        while l<=r: 
            mid = (l+r)// 2
            
            # if mid >=1 and nums[mid - 1] > nums[mid] : 
            #     return nums[mid]

            if nums[l]<=nums[mid] and nums[mid]<=nums[r]: 
                # Array is sorted
                res = min(nums[l], res)
                break

            res = nums[mid]
            # Rotated array cases
            if nums[mid] >= nums[l]: 
                # Left half is sorted
                # Search in right
                l = mid + 1 
        
            else: 
                # Search in left
                r = mid - 1

        
        return res

            