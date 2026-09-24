class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r: 

            mid = (l+r) //2 

            if nums[mid] == target: 
                return mid
            
            # Full sorted
            if nums[l] <= nums[mid] <= nums[r]: 
                if target < nums[mid]: 
                    r = mid - 1
                else: 
                    l = mid + 1 

                
            # Rotated sorted

            elif nums[l] <= nums[mid]: 
                # Left sorted
                if nums[l] <= target <= nums[mid]: 
                    r = mid -1 
                else: 
                    l = mid + 1 

            else: 
                # Right sorted
                if nums[mid] <= target <= nums[r]: 
                    l = mid + 1
                else: 
                    r = mid - 1

        return -1