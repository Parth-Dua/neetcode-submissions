class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        '''

        For rotated array
        mid value - either left of the mid is sorted or right of the mid is sorted. whichever one is sorted -> check the other one 


        For sorted array -> first element

        '''

        l,r = 0, len(nums)-1 

        while l<=r: 

            mid = l+ (r-l)//2

            # Sorted array
            if nums[l] <= nums[mid] <= nums[r]: 
                return nums[l]

            # Rotated array
            if nums[l]<= nums[mid]: 
                # Left sorted
                l = mid + 1 
            else: 
                # Right sorted
                r = mid 

        return -1 