class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(s,e): 
            if s > e: 
                return -1

            mid = (s+e)//2
            if target == nums[mid]: 
                return mid

            # Left half sorted
            if nums[s] <= nums[mid]: 
                # B.S in left half
                if nums[s] <= target and target <= nums[mid]: 
                    return helper(s, mid-1)
                else: 
                    #B.S in right half
                    return helper(mid+1, e)
            # Right half sorted
            else: 
                # B.S in left half
                if nums[mid] <= target and target <= nums[e]: 
                    return helper(mid+1, e)
                else: 
                    #B.S in right half
                    return helper(s, mid-1)
            
        return helper(0, len(nums)-1)
                    
