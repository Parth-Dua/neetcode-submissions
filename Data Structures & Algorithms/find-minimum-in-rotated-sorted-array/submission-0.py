class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l, r = 0, len(nums) - 1 

        while l<=r: 
            mid = (l+r)// 2

            if mid >=1 and nums[mid - 1] > nums[mid] : 
                return nums[mid]

            if nums[l]<=nums[mid] and nums[mid]<=nums[r]: 
                # Array is sorted
                return nums[l]

            # Rotated array cases
            elif nums[mid] >= nums[l]: 
                # Left half is sorted
                # Search in right
                l = mid + 1 
        
            else: 
                # Search in left
                r = mid - 1

        
                

            