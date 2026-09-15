class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l<=r: 

            mid = (l+r) //2 
            if nums[mid] == target: 
                return mid
            
            # SORTED ARRAY
            if nums[l] <= nums[mid] <= nums[r]: 
                # Regular binary search 
                if target < nums[mid] : 
                    r = mid -1 
                else: 
                    l = mid +1 

            # Only Left sorted
            elif nums[l] <= nums[mid-1] :
                if target in range(nums[l], nums[mid-1] + 1) : 
                    # Search here
                    r = mid - 1 
                else: 
                    l = mid + 1 
            
            # Only right is sorted
            else: 
                if target in range(nums[mid+1], nums[r] + 1) : 
                    # Search here
                    l = mid + 1
                else: 
                    r = mid - 1

        return -1 



        # # Recursive
        # def helper(s,e): 
        #     if s > e: 
        #         return -1

        #     mid = (s+e)//2
        #     if target == nums[mid]: 
        #         return mid

        #     # Left half sorted
        #     if nums[s] <= nums[mid]: 
        #         # B.S in left half
        #         if nums[s] <= target and target <= nums[mid]: 
        #             return helper(s, mid-1)
        #         else: 
        #             #B.S in right half
        #             return helper(mid+1, e)
        #     # Right half sorted
        #     else: 
        #         # B.S in left half
        #         if nums[mid] <= target and target <= nums[e]: 
        #             return helper(mid+1, e)
        #         else: 
        #             #B.S in right half
        #             return helper(s, mid-1)
            
        # return helper(0, len(nums)-1)
                    
