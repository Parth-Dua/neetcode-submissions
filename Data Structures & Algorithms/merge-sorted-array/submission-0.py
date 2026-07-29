class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        def helper(i, j) : 
            # i is pointer in nums1 and j is pointer in nums2 

            if i == len(nums1): 
                # all elements of nums1 is smaller
                nums1.extend(nums2[j:])
                return
            
            if j == n: 
                # nums2 is finished
                return 
            
            if nums1[i] <= nums2[j]: 
                return helper(i+1, j)
            else: 
                
                nums1.insert( i, nums2[j])
                return helper(i,j+1)
        
        return helper(0,0)


